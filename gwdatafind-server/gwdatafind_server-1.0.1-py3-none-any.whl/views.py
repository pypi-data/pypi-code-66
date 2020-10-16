#!/usr/bin/env python
# Copyright (2019) Cardiff University
# Licensed under GPLv3+ - see LICENSE

"""Data views for GWDataFindServer
"""

import json
import operator
import re
import socket
from collections import defaultdict
from functools import (reduce, wraps)
from math import inf as INF
from urllib.parse import urlparse, unquote

from flask import (Blueprint, current_app, jsonify, request)

from ligo.segments import (segmentlist, segment)

from . import authentication

# we expect to be configured to /LDR in Apache
_PREFIX = '/services/data/v1'

blueprint = Blueprint(
    "data",
    __name__,
    url_prefix=_PREFIX,
)

_DEFAULT_GSIFTP_HOST = socket.gethostbyaddr(socket.gethostname())[0]
_DEFAULT_GSIFTP_PORT = 15000

# -- utilities ----------------------------------------------------------------


def as_json(func):
    """Dump a function's return to JSON
    """
    @wraps(func)
    def decorated(*args, **kwargs):
        return jsonify(func(*args, **kwargs))
    return decorated


def _file_url(path):
    config = current_app.config['LDRDataFindServer']
    host = config.get('filehost', 'localhost')
    return 'file://{0}{1}'.format(host, path)


def _gsiftp_url(path):
    config = current_app.config['LDRDataFindServer']
    host = config.get('gsiftphost', _DEFAULT_GSIFTP_HOST)
    port = config.get('gsiftpport', _DEFAULT_GSIFTP_PORT)
    return 'gsiftp://{0}:{1}{2}'.format(host, port, path)


# -- routes -------------------------------------------------------------------

@blueprint.route('/', methods=['GET', 'POST'])
@authentication.validate()
def show_my_urls():
    ret = '<h3>gwdatafind_server URLs</h3>\n'
    for rule in current_app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        line = unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        ret += '<p>{0}</p>\n'.format(line)

    return ret


@blueprint.route('/<ext>.json', methods=['GET', 'POST'])
@authentication.validate()
@as_json
def find_observatories(ext):
    """List all observatories
    """
    current_app.logger.info('find_observatories: ext: {0}'.format(ext))
    return list(current_app.get_cache_data(ext).keys())


@blueprint.route('<ext>/<site>.json', methods=['GET', 'POST'])
@authentication.validate()
@as_json
def find_types(ext, site):
    """List all data tags 'frametypes'
    """
    current_app.logger.info('find_observatories: ext: {0}, site: {1}'.
                            format(ext, site))
    ecache = current_app.cache_manager.cache.get(ext, {})
    if site == 'all':
        sites = list(ecache.keys())
    else:
        sites = [site]
    return [tag for site in sites for
            tag in current_app.get_cache_data(ext, site)]


@blueprint.route('<ext>/<site>/<tag>/segments.json', methods=['GET', 'POST'])
@authentication.validate()
@as_json
def find_all_times(ext, site, tag):
    """List segments known for a given tag
    """
    span = segmentlist([segment(0., INF)])
    return reduce(
        operator.or_,
        (segs & span for
         segs in current_app.get_cache_data(ext, site, tag).values()),
        segmentlist(),
    )


@blueprint.route('<ext>/<site>/<tag>/segments/<int:start>,<int:end>.json',
                 methods=['GET', 'POST'])
@authentication.validate()
@as_json
def find_times(ext, site, tag, start, end):
    """List segments known for a given tag
    """
    span = segmentlist([segment(float(start), float(end))])
    return reduce(
        operator.or_,
        (segs & span for segs in
         current_app.get_cache_data(ext, site, tag).values()),
        segmentlist(),
    )


@blueprint.route('<ext>/<site>/<tag>/<filename>.json', methods=['GET', 'POST'])
@authentication.validate()
@as_json
def find_url(ext, site, tag, filename):
    """Return URL(s) for a given filename
    """
    # parse GPS information from filename
    _, _, start, dur = filename.split('-')
    dur = dur[:-len(ext)].rstrip('.')
    # find urls
    return list(_find_urls(
        ext,
        site,
        tag,
        int(start),
        int(start + dur),
    ))


@blueprint.route('<ext>/<site>/<tag>/<int:start>,<int:end>.json',
                 methods=['GET', 'POST'])
@blueprint.route('<ext>/<site>/<tag>/<int:start>,<int:end>/<urltype>.json',
                 methods=['GET', 'POST'])
@authentication.validate()
@as_json
def find_urls(ext, site, tag, start, end, urltype=None):
    """Find all URLs in a given GPS time interval
    """
    return list(_find_urls(
        ext,
        site,
        tag,
        start,
        end,
        urltype=urltype,
        **request.args,
    ))


@blueprint.route('<ext>/<site>/<tag>/latest.json', methods=['GET', 'POST'])
@blueprint.route('<ext>/<site>/<tag>/latest/<urltype>.json',
                 methods=['GET', 'POST'])
@authentication.validate()
@as_json
def find_latest_url(ext, site, tag, urltype=None):
    """Find the latest URL(s) for a given tag
    """
    return list(_find_urls(
        ext,
        site,
        tag,
        0,
        INF,
        urltype=urltype,
        latest=True,
    ))


# -- URL matcher --------------------------------------------------------------


def _get_latest_segment(seglist, duration):
    """Get segment for latest file of the given duration in a segment list
    """
    end = seglist[-1][1]
    return segment(end-duration, end)


def _find_urls(ext, site, tag, start, end, urltype=None, match=None,
               latest=False):
    """Find all URLs for the given GPS interval
    """
    # parse file paths
    search = segment(start, end)
    lfns = defaultdict(list)
    maxgps = -1e9  # something absurdly old
    for (path, cdur), seglist in current_app.get_cache_data(
            ext,
            site,
            tag,
    ).items():
        # if running a 'latest' URL search, restrict the search to
        # the most recent available segment for this frametype
        if latest and seglist:  # 'if seglist' to prevent IndexError
            # get latest segment for this path
            latest = _get_latest_segment(seglist, cdur)
            if latest[1] <= maxgps:  # if this is not an improvement, move on
                continue
            # only keep the segment of the last file
            maxgps = latest[1]
            seglist = [latest]
            # empty matches to keep only this one
            lfns = defaultdict(list)

        # loop over segments and construct file URLs
        for seg in seglist:
            if not seg.intersects(search):
                continue
            gps = seg[0]
            while gps < seg[1]:
                if segment(gps, gps+cdur).intersects(search):
                    lfn = '{site}-{tag}-{start}-{dur}.{ext}'.format(
                        site=site, tag=tag, start=gps, dur=cdur, ext=ext)
                    lfns[lfn].append('{0}/{1}'.format(path, lfn))
                gps += cdur

    # convert paths to URLs for various schemes
    allurls = {}
    for lfn in lfns:
        allurls[lfn] = []
        for path in lfns[lfn]:
            # build file:// and gsiftp:// URL for each LFN
            allurls[lfn].extend((
                _file_url(path),
                _gsiftp_url(path),
            ))

    # filter URLs for each LFN and return
    urls = []
    for lfn in allurls:
        urls.extend(_filter_urls(allurls[lfn], urltype=urltype, regex=match))
    return urls


# -- URL filtering ------------------------------------------------------------

def _filter_urls(urls, urltype=None, regex=None):
    """Filter a list of URLs that all represent the same LFN.
    """
    if regex:
        regex = re.compile(regex)

    def _filter(url):
        return (
            (not urltype or urlparse(url).scheme == urltype) and
            (not regex or regex.search(url))
        )

    return _filter_preference(filter(_filter, urls))


def _filter_preference(urls):
    """Preferencially downselect a list of URLs representing a single LFN.

    If ``filter_preference`` is empty, this will just return the input list
    unfiltered.
    """
    # parse filter preference as a dict of regex keys
    # each with a list of regexs as value
    filter_preference = {
        re.compile(key): list(map(re.compile, value)) for (key, value) in
        json.loads(current_app.config["LDRDataFindServer"].get(
            'filter_preference',
            '{}',
        ).replace('\'', '"')).items()
    }

    matches = defaultdict(list)
    unmatched = []  # list of all URLs that didn't match any pattern
    for url in urls:
        matched = False
        for pattern in filter_preference:
            if pattern.match(url):
                matches[pattern].append(url)
                matched = True
        if not matched:
            unmatched.append(url)

    keep = []

    for pattern, murls in matches.items():
        if len(murls) == 1:  # one match, just keep
            keep.extend(murls)
            continue
        # multiple matches, so we pick the one that matches highest in
        # the filter_preference list set by the server admin
        keep.extend(_rank_select_urls(murls, filter_preference[pattern]))

    # return ranked, selected list of URLs, plus everything else that
    # didn't match a preference pattern
    return keep + unmatched


def _rank_select_urls(urls, patterns):
    """Filter multiple matches of a given pattern using admin preference

    Parameters
    ----------
    urls : `list` of `str`
        the list of URLs that all represent the same LFN, and all matched
        a given master pattern (usually just a URL type scheme)

    patterns : `list` of `re.Pattern`
        the ordered list of regular expressions against which to
        preferentially match URLs

    Returns
    -------
    matches : `list` of `str`
        a list containing a single URL that first matched one of the patterns,
        or the full input list of nothing matched
    """
    for pattern in patterns:
        for url in urls:
            if pattern.search(url):
                return [url]
    return urls  # we should never get to here
