# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/HoleUD.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/HoleUD
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .HoleMag import HoleMag

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.HoleUD.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.HoleUD.comp_surface_magnet_id import comp_surface_magnet_id
except ImportError as error:
    comp_surface_magnet_id = error

try:
    from ..Methods.Slot.HoleUD.has_magnet import has_magnet
except ImportError as error:
    has_magnet = error

try:
    from ..Methods.Slot.HoleUD.remove_magnet import remove_magnet
except ImportError as error:
    remove_magnet = error


from ._check import InitUnKnowClassError
from .Surface import Surface
from .Material import Material


class HoleUD(HoleMag):
    """User defined hole from list of surface"""

    VERSION = 1
    IS_SYMMETRICAL = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.HoleUD.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleUD method build_geometry: " + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.HoleUD.comp_surface_magnet_id
    if isinstance(comp_surface_magnet_id, ImportError):
        comp_surface_magnet_id = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleUD method comp_surface_magnet_id: "
                    + str(comp_surface_magnet_id)
                )
            )
        )
    else:
        comp_surface_magnet_id = comp_surface_magnet_id
    # cf Methods.Slot.HoleUD.has_magnet
    if isinstance(has_magnet, ImportError):
        has_magnet = property(
            fget=lambda x: raise_(
                ImportError("Can't use HoleUD method has_magnet: " + str(has_magnet))
            )
        )
    else:
        has_magnet = has_magnet
    # cf Methods.Slot.HoleUD.remove_magnet
    if isinstance(remove_magnet, ImportError):
        remove_magnet = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use HoleUD method remove_magnet: " + str(remove_magnet)
                )
            )
        )
    else:
        remove_magnet = remove_magnet
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        surf_list=-1,
        magnet_dict=-1,
        Zh=36,
        mat_void=-1,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "surf_list" in list(init_dict.keys()):
                surf_list = init_dict["surf_list"]
            if "magnet_dict" in list(init_dict.keys()):
                magnet_dict = init_dict["magnet_dict"]
            if "Zh" in list(init_dict.keys()):
                Zh = init_dict["Zh"]
            if "mat_void" in list(init_dict.keys()):
                mat_void = init_dict["mat_void"]
        # Set the properties (value check and convertion are done in setter)
        self.surf_list = surf_list
        self.magnet_dict = magnet_dict
        # Call HoleMag init
        super(HoleUD, self).__init__(Zh=Zh, mat_void=mat_void)
        # The class is frozen (in HoleMag init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        HoleUD_str = ""
        # Get the properties inherited from HoleMag
        HoleUD_str += super(HoleUD, self).__str__()
        if len(self.surf_list) == 0:
            HoleUD_str += "surf_list = []" + linesep
        for ii in range(len(self.surf_list)):
            tmp = (
                self.surf_list[ii].__str__().replace(linesep, linesep + "\t") + linesep
            )
            HoleUD_str += "surf_list[" + str(ii) + "] =" + tmp + linesep + linesep
        HoleUD_str += "magnet_dict = " + str(self.magnet_dict) + linesep
        return HoleUD_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from HoleMag
        if not super(HoleUD, self).__eq__(other):
            return False
        if other.surf_list != self.surf_list:
            return False
        if other.magnet_dict != self.magnet_dict:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from HoleMag
        HoleUD_dict = super(HoleUD, self).as_dict()
        if self.surf_list is None:
            HoleUD_dict["surf_list"] = None
        else:
            HoleUD_dict["surf_list"] = list()
            for obj in self.surf_list:
                HoleUD_dict["surf_list"].append(obj.as_dict())
        HoleUD_dict["magnet_dict"] = (
            self.magnet_dict.copy() if self.magnet_dict is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        HoleUD_dict["__class__"] = "HoleUD"
        return HoleUD_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        for obj in self.surf_list:
            obj._set_None()
        self.magnet_dict = None
        # Set to None the properties inherited from HoleMag
        super(HoleUD, self)._set_None()

    def _get_surf_list(self):
        """getter of surf_list"""
        if self._surf_list is not None:
            for obj in self._surf_list:
                if obj is not None:
                    obj.parent = self
        return self._surf_list

    def _set_surf_list(self, value):
        """setter of surf_list"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "surf_list"
                    )
                    value[ii] = class_obj(init_dict=obj)
        if value == -1:
            value = list()
        check_var("surf_list", value, "[Surface]")
        self._surf_list = value

    surf_list = property(
        fget=_get_surf_list,
        fset=_set_surf_list,
        doc=u"""List of surface to draw the Hole. Surfaces must be ordered in trigo order, label must contain HoleMagnet for Magnet and Hole for holes

        :Type: [Surface]
        """,
    )

    def _get_magnet_dict(self):
        """getter of magnet_dict"""
        return self._magnet_dict

    def _set_magnet_dict(self, value):
        """setter of magnet_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("magnet_dict", value, "dict")
        self._magnet_dict = value

    magnet_dict = property(
        fget=_get_magnet_dict,
        fset=_set_magnet_dict,
        doc=u"""dictionnary with the magnet for the Hole (None to remove magnet, key should be magnet_X)

        :Type: dict
        """,
    )
