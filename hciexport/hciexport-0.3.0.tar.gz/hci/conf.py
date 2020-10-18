# The MIT License (MIT)
#
# Copyright (c) 2020 Thorsten Simons (sw@snomis.eu)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
from argparse import ArgumentParser
from configparser import ConfigParser
from time import asctime

from .version import Gvars

def parseargs():
    """
    args - build the argument parser, parse the command line.
    """

    mainparser = ArgumentParser()
    mainparser.add_argument('--version', action='version',
                            version="%(prog)s: {0}\n"
                            .format(Gvars.Version))
    mainparser.add_argument('-c', dest='configfile',
                            required=True,
                            help='configuration file to be used')
    mainparser.add_argument('-t', dest='task',
                            required=True,
                            help='the task within the config file')
    mainparser.add_argument('-o', dest='outfile',
                            required=False,
                            default='',
                            help='the file to write the export to '
                                 '(set default in config file)')

    result = mainparser.parse_args()
    return __readconfig(result)

def __readconfig(result):
    """
    Read the specified task from the config file.
    """
    cnf = ConfigParser()
    cnf.read(result.configfile)

    try:
        result.hcifqdn = cnf['HCI']['HCIFQDN']
        result.hciadminapiport = cnf['HCI']['ADMINAPIPORT']
        result.hcisearchapiport = cnf['HCI']['SEARCHAPIPORT']
        result.hciworkflowapiport = cnf['HCI']['WORKFLOWAPIPORT']

        result.type = cnf[result.task]['TYPE']
        result.user = cnf[result.task]['USER']
        result.password = cnf[result.task]['PASSWORD']
        result.realm = cnf[result.task]['REALM']
        result.granttype = cnf[result.task]['GRANTTYPE']
        result.clientsecret = cnf[result.task]['CLIENTSECRET']
        result.clientid = cnf[result.task]['CLIENTID']
        if not result.outfile:
            result.outfile = cnf[result.task]['OUTPUTFILE']
    except KeyError as e:
        sys.exit(f'fatal: invalid configuration file - missing entry {e}')

    result.pkgname = 'HCI config package'
    result.pkgdesc = f'<p>exported: {asctime()}<br>by {Gvars.s_description} {Gvars.Version}</p>'

    return result