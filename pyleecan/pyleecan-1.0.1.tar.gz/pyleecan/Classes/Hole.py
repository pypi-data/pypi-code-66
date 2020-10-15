# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/Hole.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/Hole
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.Hole.comp_radius import comp_radius
except ImportError as error:
    comp_radius = error

try:
    from ..Methods.Slot.Hole.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.Hole.get_is_stator import get_is_stator
except ImportError as error:
    get_is_stator = error

try:
    from ..Methods.Slot.Hole.get_Rbo import get_Rbo
except ImportError as error:
    get_Rbo = error

try:
    from ..Methods.Slot.Hole.has_magnet import has_magnet
except ImportError as error:
    has_magnet = error

try:
    from ..Methods.Slot.Hole.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Slot.Hole.comp_height import comp_height
except ImportError as error:
    comp_height = error


from ._check import InitUnKnowClassError
from .Material import Material


class Hole(FrozenClass):
    """Holes for lamination (abstract)"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.Hole.comp_radius
    if isinstance(comp_radius, ImportError):
        comp_radius = property(
            fget=lambda x: raise_(
                ImportError("Can't use Hole method comp_radius: " + str(comp_radius))
            )
        )
    else:
        comp_radius = comp_radius
    # cf Methods.Slot.Hole.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError("Can't use Hole method comp_surface: " + str(comp_surface))
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.Hole.get_is_stator
    if isinstance(get_is_stator, ImportError):
        get_is_stator = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Hole method get_is_stator: " + str(get_is_stator)
                )
            )
        )
    else:
        get_is_stator = get_is_stator
    # cf Methods.Slot.Hole.get_Rbo
    if isinstance(get_Rbo, ImportError):
        get_Rbo = property(
            fget=lambda x: raise_(
                ImportError("Can't use Hole method get_Rbo: " + str(get_Rbo))
            )
        )
    else:
        get_Rbo = get_Rbo
    # cf Methods.Slot.Hole.has_magnet
    if isinstance(has_magnet, ImportError):
        has_magnet = property(
            fget=lambda x: raise_(
                ImportError("Can't use Hole method has_magnet: " + str(has_magnet))
            )
        )
    else:
        has_magnet = has_magnet
    # cf Methods.Slot.Hole.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use Hole method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Slot.Hole.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError("Can't use Hole method comp_height: " + str(comp_height))
            )
        )
    else:
        comp_height = comp_height
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, Zh=36, mat_void=-1, init_dict=None, init_str=None):
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
            if "Zh" in list(init_dict.keys()):
                Zh = init_dict["Zh"]
            if "mat_void" in list(init_dict.keys()):
                mat_void = init_dict["mat_void"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.Zh = Zh
        self.mat_void = mat_void

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Hole_str = ""
        if self.parent is None:
            Hole_str += "parent = None " + linesep
        else:
            Hole_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Hole_str += "Zh = " + str(self.Zh) + linesep
        if self.mat_void is not None:
            tmp = self.mat_void.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Hole_str += "mat_void = " + tmp
        else:
            Hole_str += "mat_void = None" + linesep + linesep
        return Hole_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.Zh != self.Zh:
            return False
        if other.mat_void != self.mat_void:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        Hole_dict = dict()
        Hole_dict["Zh"] = self.Zh
        if self.mat_void is None:
            Hole_dict["mat_void"] = None
        else:
            Hole_dict["mat_void"] = self.mat_void.as_dict()
        # The class name is added to the dict for deserialisation purpose
        Hole_dict["__class__"] = "Hole"
        return Hole_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Zh = None
        if self.mat_void is not None:
            self.mat_void._set_None()

    def _get_Zh(self):
        """getter of Zh"""
        return self._Zh

    def _set_Zh(self, value):
        """setter of Zh"""
        check_var("Zh", value, "int", Vmin=0, Vmax=1000)
        self._Zh = value

    Zh = property(
        fget=_get_Zh,
        fset=_set_Zh,
        doc=u"""Number of Hole around the circumference

        :Type: int
        :min: 0
        :max: 1000
        """,
    )

    def _get_mat_void(self):
        """getter of mat_void"""
        return self._mat_void

    def _set_mat_void(self, value):
        """setter of mat_void"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "mat_void"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Material()
        check_var("mat_void", value, "Material")
        self._mat_void = value

        if self._mat_void is not None:
            self._mat_void.parent = self

    mat_void = property(
        fget=_get_mat_void,
        fset=_set_mat_void,
        doc=u"""Material of the void part of the hole (Air in general)

        :Type: Material
        """,
    )
