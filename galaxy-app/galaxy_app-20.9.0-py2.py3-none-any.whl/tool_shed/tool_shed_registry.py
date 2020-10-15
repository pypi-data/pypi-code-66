import logging
from collections import (
    namedtuple,
    OrderedDict,
)

from galaxy.util import parse_xml_string
from galaxy.util.tool_shed.common_util import remove_protocol_from_tool_shed_url
from galaxy.util.tool_shed.xml_util import parse_xml

log = logging.getLogger(__name__)

DEFAULT_TOOL_SHEDS_CONF_XML = """<?xml version="1.0"?>
<tool_sheds>
    <tool_shed name="Galaxy Main Tool Shed" url="https://toolshed.g2.bx.psu.edu/"/>
</tool_sheds>
"""

AUTH_TUPLE = namedtuple('AuthSetting', 'username password')


class Registry:

    def __init__(self, config=None):
        self.tool_sheds = OrderedDict()
        self.tool_sheds_auth = OrderedDict()
        if config:
            # Parse tool_sheds_conf.xml
            tree, error_message = parse_xml(config)
            if tree is None:
                log.warning("Unable to load references to tool sheds defined in file %s" % str(config))
                return
            root = tree.getroot()
        else:
            root = parse_xml_string(DEFAULT_TOOL_SHEDS_CONF_XML)
            config = "internal default config"
        log.debug('Loading references to tool sheds from %s' % config)
        for elem in root.findall('tool_shed'):
            try:
                name = elem.get('name', None)
                url = elem.get('url', None)
                username = elem.get('user', None)
                password = elem.get('pass', None)
                if name and url:
                    self.tool_sheds[name] = url
                    self.tool_sheds_auth[name] = None
                    log.debug('Loaded reference to tool shed: %s' % name)
                if name and url and username and password:
                    self.tool_sheds_auth[name] = AUTH_TUPLE(username, password)
            except Exception as e:
                log.warning('Error loading reference to tool shed "{}", problem: {}'.format(name, str(e)))

    def url_auth(self, url):
        """
        If the tool shed is using external auth, the client to the tool shed must authenticate to that
        as well.  This provides access to the six.moves.urllib.request.HTTPPasswordMgrWithdefaultRealm() object for the
        url passed in.

        Following more what galaxy.demo_sequencer.controllers.common does might be more appropriate at
        some stage...
        """
        url_sans_protocol = remove_protocol_from_tool_shed_url(url)
        for shed_name, shed_url in self.tool_sheds.items():
            shed_url_sans_protocol = remove_protocol_from_tool_shed_url(shed_url)
            if url_sans_protocol.startswith(shed_url_sans_protocol):
                return self.tool_sheds_auth[shed_name]
        log.debug("Invalid url '%s' received by tool shed registry's url_auth method." % str(url))
        return None
