"""
OvsPort class.

     Copyright (C) 2020  Fundació Privada I2CAT, Internet i Innovació digital a Catalunya

     This program is free software: you can redistribute it and/or modify
     it under the terms of the GNU Affero General Public License as published by
     the Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.

     This program is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     GNU Affero General Public License for more details.

     You should have received a copy of the GNU Affero General Public License
     along with this program.  If not, see <https://www.gnu.org/licenses/>.

     Authors: Ferran Cañellas <ferran.canellas@i2cat.net>
"""

from ovsdbmanager.tables.ovs import OpenVSwitch


class OvsPort(OpenVSwitch):
    """
    Class that represents an OvS port
    """
    def get_interface(self):
        """
        Gets the first interface associated with a port
        :return:
        """
        return self.api.get_interface(getattr(self, "interfaces"))
