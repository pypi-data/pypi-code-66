import os
import json
import copy
import re
import logging
import traceback
import importlib
import subprocess
from datetime import datetime
from colored import fg, bg, attr

from .exceptions import *
from .context import *
from .resources import *

logger = logging.getLogger('app')

def greenbg(txt):
    return "{} \u2713 {} {}".format(bg('light_green'), txt, attr(0))

def redbg(txt):
    return "{} \u274C {} {}".format(bg('indian_red_1a'), txt, attr(0))

def orangebg(txt):
    return "{} \u0023 {} {}".format(bg('dark_orange_3a'), txt, attr(0))

def read_siteconf_json(filename, app={}, context={}):

    try:
        # Try the sitelib first.
        import sitelib

        nature, siteconf = sitelib.read_siteconf(filename, app)
        if siteconf is None:
            raise Exception("Failed to read siteconf")
        if nature == 'open':
            logger.warning("Successfully read siteconf but it is insecure")
        else:
            logger.warning("Successfully read secure siteconf")
    except:
        # sitelib may not be installed
        logger.debug("Could not read secure siteconf. Falling back")
        try:
            # If this is a jsonx file, then try the json version of
            # the file.
            if filename.endswith('jsonx'):
                filename = filename.replace('jsonx', 'json')
            siteconf = json.load(open(filename))
        except:
            traceback.print_exc()
            siteconf = None

    if siteconf is None:
        raise Exception("Could not read siteconf")

    if not isinstance(siteconf, dict):
        raise Exception("Invalid siteconf found. Expecting 'dict' found '{}'".format(str(type(siteconf))))

    return siteconf

def read_siteconf(filename=None, app={}, context={}):


    # If context not available, then generate it.
    if len(context) == 0:
        context = Context().asdict()

    if filename is not None:
        return read_siteconf_json(filename, app)

    tries = []
    try:
        tries.extend([
            "%(ENRICH_ETC)s/siteconf.jsonx" % context,
            "%(ENRICH_ETC)s/siteconf.json" % context,
        ])
    except:
        pass

    tries.extend([
        os.path.expandvars("${ENRICH_ETC}/siteconf.jsonx"),
        os.path.expandvars("${ENRICH_ETC}/siteconf.json"),
    ])

    siteconf = None
    for filename in tries:
        if os.path.exists(filename):
            siteconf = read_siteconf_json(filename, app, context)
            if siteconf is None:
                continue
            else:
                break

    if siteconf is None:
        raise Exception("Could not find siteconf. Tried {} alternatives".format(len(tries)))

    return siteconf

def get_credentials(siteconf, name):
    """
    Look up the credentials file
    """

    if ((siteconf is None) or
        (not isinstance(siteconf, dict))):
        raise Exception("Invalid siteconf - None or has invalid datatype")

    if (('credentials' not in siteconf) or
        (name not in siteconf['credentials'])):
        raise Exception("missing credentials")

    return siteconf['credentials'][name]

def get_credentials_by_name(name, app={}, context={}):
    """
    Lookup credentials by name
    """

    siteconf = read_siteconf(app=app, context={})
    return get_credentials(siteconf, name)


def get_credentials_by_type(conditions,app={},context={}):
    """
    Lookup credentials by type
    """

    siteconf = read_siteconf(app=app, context={})

    if ((siteconf is None) or
        (not isinstance(siteconf, dict))):
        raise Exception("Invalid siteconf - None or has invalid datatype")

    if 'credentials' not in siteconf:
        raise Exception("missing credentials")

    if not isinstance(conditions, dict):
        raise Exception("Invalid condition specification")

    final = {}
    for name, detail in siteconf['credentials'].items():

        if not isinstance(detail, dict):
            continue

        if not detail.get('enable', True):
            continue

        match = True
        for var, choices in conditions.items():
            if var not in detail:
                match = False
                break
            if detail[var] not in choices:
                match = False
                break

        if not match:
            continue

        final[name] = copy.deepcopy(detail)

    return final

def update_from_git(detail, context):

    # Make a local version
    context = copy.copy(context)

    # Try the detail run root
    root = detail['git'] % context
    if not os.path.exists(root):

        # try one alternative path if possible
        if "ENRICH_RUN_ROOT" not in detail['git']:
            raise Exception("Expected ENRICH_RUN_ROOT: {}".format(detail['git']))

        # Fallback to the default run_root
        context['ENRICH_RUN_ROOT'] = context['ENRICH_ROOT']
        altroot = detail['git'] % context
        if not os.path.exists(root):
            raise Exception("Missing repo roots: {}, {}".format(root, altroot))
        root = altroot

    # Update in place
    detail['git'] = root

    # Collect all the notes
    cmd = "git -C {} log --pretty='%h--%ci--%N'".format(root)
    notes = subprocess.check_output(cmd, shell=True)
    notes = notes.decode('utf-8')
    notes = notes.split("\n")
    notes = [n.split("--") for n in notes if (n.count("--") == 2 and not n.endswith("--"))] # remove empty

    detail['notes']= [
        {
            'commit': n[0],
            'commit_date': n[1],
            'message': n[2]
        } for n in notes
    ]

    # => Collect branches..
    cmd = """git -C {} branch -l""".format(root)
    lines = subprocess.check_output(cmd, shell=True)
    lines = lines.decode('utf-8')
    lines = lines.split("\n")
    lines = [l[2:] for l in lines]
    detail['branches'] = lines

    # Collect the git commits
    head_tagged = False
    cmd = """git -C {} log --no-walk --tags --pretty="%h\t%D\t%ce\t%ci\t%s" --decorate=full --date=short""".format(root)
    lines = subprocess.check_output(cmd, shell=True)
    lines = lines.decode('utf-8')
    lines = lines.split("\n")
    lines = [l.strip() for l in lines]
    lines = [l.split("\t") for l in lines]
    lines = [l for l in lines if len(l) == 5]
    alltags = []
    for l in lines:
        refs = [x.strip() for x in l[1].split(",")]
        # Have we seed the head yet?
        head_tagged = head_tagged or any([ref.startswith('HEAD') for ref in refs])
        entry = {
            #['416366c', 'tag: refs/tags/v1.4.0, refs/heads/master', '2020-03-03', 'pingali@gmail.com', 'Bug']
            'commit': l[0],
            'refs':   refs,
            'author':   l[2],
            'date': l[3],
            'log':   l[4]
        }

        # Extract the tag for this commit
        for ref in refs:
            match = re.search("tag: refs/tags/(\S+)", ref)
            if match is not None:
                tag = match.group(1)
                entry['tag'] = tag
                break

        if 'tag' in entry:
            alltags.append(entry)

    if not head_tagged:
        # The head that is deployed does not correspond to any of the tags.
        #e1b93e1 HEAD -> refs/heads/master       pingali@gmail.com 2020-04-19 11:10:57 +0530  Updated documentation
        cmd = """git -C {} log --no-walk --pretty="%h\t%D\t%ce\t%ci\t%s" --decorate=full --date=short""".format(root)
        line = subprocess.check_output(cmd, shell=True)
        line = line.decode('utf-8')
        line = line.strip().split("\t")
        refs = [x.strip() for x in line[1].split(",")]
        alltags.append({
            'commit': line[0],
            'refs':   refs,
            'tag': 'HEAD',
            'author':   line[2],
            'date': line[3],
            'log':   line[4]
        })


    # Now sort by reverse commit date
    alltags = sorted(alltags,
                     key=lambda entry: entry['date'],
                     reverse=True)
    detail['alltags'] = alltags


    position='post'
    for entry in alltags:

        head = any([ref.startswith('HEAD') for ref in entry['refs']])
        # Where is this position...
        if head:
            entry['position'] = 'head'
            position = 'pre'
        else:
            entry['position'] = position

        if head:
            detail['release'] = entry['tag']
            detail['commit'] = entry['commit']
            detail['date'] = entry['date']

            # Insert the URL as well
            if 'url' in detail:
                urlparts = detail['url'].split("/")
                urlparts[-1] = detail['commit']
                url = "/".join(urlparts)
                detail['url'] = url

def update_from_package(detail, context):

    pkgname = detail['package']
    mod = importlib.import_module(pkgname)

    # v0.4.3+0.g659ce50.dirty
    if not hasattr(mod, '__version_detailed__'):
        return

    pkgdetails = mod.__version_detailed__
    release = pkgdetails['version']
    commit  = pkgdetails['full-revisionid']

    # Now overwrite the release information
    detail['release'] = release
    detail['commit'] = commit[:8]
    if 'url' in detail:
        urlparts = detail['url'].split("/")
        urlparts[-1] = detail['commit']
        url = "/".join(urlparts)
        detail['url'] = url
    else:
        detail['release'] += " (out of date; version missing)"
        logger.error("VersionMap: Cannot collect version information for {}".format(pkgname),
                     extra={
                         'data': json.dumps(detail, indent=4)
                     })

def read_versionmap(filename=None,
                    include_notes=False,
                    include_tags=False,
                    context={}):

    if isinstance(context, dict):
        if len(context) == 0:
            context = Context().asdict()
    elif isinstance(context, Context):
        context = context.asdict() 

    default = [
        {
            "repo": "error",
            "release": "v1xxx",
            "date": "2018-10-09 12:06:40 +0530",
            "commit": "5079404f12df939c138215ed1a02e4d0d8814e00",
            "description": "Error while reading the versionmap",
            "url": "https://github.com/pingali/error/commit/5079404f12df939c138215ed1a02e4d0d8814e00",
            "label": "error",
            "notes": [
                {
                    "commit": "6271dcae",
                    "commit_date": "2018-10-09 12:06:40 +0530",
                    "notes": "v0 of the release"
                }
            ]
        }
    ]

    if filename is None:
        if 'versionmap' in context:
            filename = context['versionmap']
        elif 'ENRICH_ETC' in context:
            filename = "%(ENRICH_ETC)s/versionmap.json" % context
        else:
            filename = os.path.expandvars("$ENRICH_ETC/versionmap.json")
    now = datetime.now().replace(microsecond=0).isoformat()
    if not os.path.exists(filename):
        error = "Missing versionmap: {}".format(filename)
        logger.error(error)
        default[0]['description'] = error
        return None, default

    try:
        versionmap = json.load(open(filename))
    except:
        error = "Invalid version file. Not a valid json file: {}".format(filename)
        logger.error(error)
        default[0]['description'] = error
        return default

    # => use the filename's timestamp as the default timestamp
    timestamp = datetime.fromtimestamp(os.path.getmtime(filename))
    timestamp = timestamp.isoformat()

    # => Newer dict format of the versionmap
    if isinstance(versionmap, dict):
        timestamp = versionmap.get('timestamp', timestamp)
        versionmap = versionmap.get('versionmap', None)

    if not isinstance(versionmap, list):
        error = "Invalid version map. Not a list: {}".format(filename)
        logger.error(error)
        default[0]['description'] = error
        return timestamp, default

    # Update the release and commit information if dynamic modules are
    # specified.
    for i in range(len(versionmap)):

        if versionmap[i].get('dynamic', False):
            try:
                if 'package' not in versionmap[i] and 'git' not in versionmap[i]:
                    versionmap[i]['release'] += " (out of date; config issue)"
                    logger.error("VersionMap: Missing package to be checked",
                                 extra={
                                     'data': json.dumps(versionmap[i], indent=4)
                                 })
                elif 'package' in versionmap[i]:
                    update_from_package(versionmap[i], context)
                elif 'git' in versionmap[i]:
                    update_from_git(versionmap[i], context)

            except:
                versionmap[i]['release'] += " (out of date; import issue)"
                logger.exception("Unable to import package/repository to update version",
                                 extra={
                                     'data': json.dumps(versionmap[i], indent=4)
                                 })

    # Cleanup of the output
    for i in range(len(versionmap)):

        # Drop the notes by default
        if not include_notes:
            versionmap[i].pop('notes',[])

        if not include_tags:
            versionmap[i].pop('alltags',[])


    return timestamp, versionmap
