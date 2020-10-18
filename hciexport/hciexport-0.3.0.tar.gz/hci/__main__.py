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
from collections import OrderedDict

from .conf import parseargs
from .comwf import ApiConWorkflows
from .comsys import ApiConSystem

def main():
    opts = parseargs()

    if opts.type not in ['workflows', 'system']:
        sys.exit(f'fatal: invalid TYPE {opts.type}')

    if opts.type == 'workflows':
        con = ApiConWorkflows(f'https://{opts.hcifqdn}:{opts.hciworkflowapiport}',
                              opts.granttype, opts.user, opts.password,
                              opts.clientsecret, opts.clientid, opts.realm)

        with open(opts.outfile, 'w') as outhdl:
            print(con.export_workflows(opts.outfile), file=outhdl)

    elif opts.type == 'system':
        con = ApiConSystem(f'https://{opts.hcifqdn}:{opts.hciadminapiport}',
                           opts.granttype, opts.user, opts.password,
                           opts.clientsecret, opts.clientid, opts.realm,
                           opts.pkgname, opts.pkgdesc)
        con.build()

        with open(opts.outfile, 'wb') as outhdl:
            outhdl.write(con.export_systemconfig(opts.outfile))

