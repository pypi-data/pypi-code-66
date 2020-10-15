# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/EEC_SCIM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/EEC_SCIM
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .EEC import EEC

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.EEC_SCIM.comp_parameters import comp_parameters
except ImportError as error:
    comp_parameters = error

try:
    from ..Methods.Simulation.EEC_SCIM.solve_EEC import solve_EEC
except ImportError as error:
    solve_EEC = error

try:
    from ..Methods.Simulation.EEC_SCIM.gen_drive import gen_drive
except ImportError as error:
    gen_drive = error

try:
    from ..Methods.Simulation.EEC_SCIM.comp_joule_losses import comp_joule_losses
except ImportError as error:
    comp_joule_losses = error


from ._check import InitUnKnowClassError
from .IndMag import IndMag
from .Drive import Drive


class EEC_SCIM(EEC):
    """Electric module: Electrical Equivalent Circuit for Squirrel Cage Induction Machine"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.EEC_SCIM.comp_parameters
    if isinstance(comp_parameters, ImportError):
        comp_parameters = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_SCIM method comp_parameters: " + str(comp_parameters)
                )
            )
        )
    else:
        comp_parameters = comp_parameters
    # cf Methods.Simulation.EEC_SCIM.solve_EEC
    if isinstance(solve_EEC, ImportError):
        solve_EEC = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_SCIM method solve_EEC: " + str(solve_EEC))
            )
        )
    else:
        solve_EEC = solve_EEC
    # cf Methods.Simulation.EEC_SCIM.gen_drive
    if isinstance(gen_drive, ImportError):
        gen_drive = property(
            fget=lambda x: raise_(
                ImportError("Can't use EEC_SCIM method gen_drive: " + str(gen_drive))
            )
        )
    else:
        gen_drive = gen_drive
    # cf Methods.Simulation.EEC_SCIM.comp_joule_losses
    if isinstance(comp_joule_losses, ImportError):
        comp_joule_losses = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use EEC_SCIM method comp_joule_losses: "
                    + str(comp_joule_losses)
                )
            )
        )
    else:
        comp_joule_losses = comp_joule_losses
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        indmag=None,
        parameters=-1,
        freq0=None,
        drive=None,
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
            if "indmag" in list(init_dict.keys()):
                indmag = init_dict["indmag"]
            if "parameters" in list(init_dict.keys()):
                parameters = init_dict["parameters"]
            if "freq0" in list(init_dict.keys()):
                freq0 = init_dict["freq0"]
            if "drive" in list(init_dict.keys()):
                drive = init_dict["drive"]
        # Set the properties (value check and convertion are done in setter)
        self.indmag = indmag
        self.parameters = parameters
        self.freq0 = freq0
        self.drive = drive
        # Call EEC init
        super(EEC_SCIM, self).__init__()
        # The class is frozen (in EEC init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        EEC_SCIM_str = ""
        # Get the properties inherited from EEC
        EEC_SCIM_str += super(EEC_SCIM, self).__str__()
        if self.indmag is not None:
            tmp = self.indmag.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            EEC_SCIM_str += "indmag = " + tmp
        else:
            EEC_SCIM_str += "indmag = None" + linesep + linesep
        EEC_SCIM_str += "parameters = " + str(self.parameters) + linesep
        EEC_SCIM_str += "freq0 = " + str(self.freq0) + linesep
        if self.drive is not None:
            tmp = self.drive.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            EEC_SCIM_str += "drive = " + tmp
        else:
            EEC_SCIM_str += "drive = None" + linesep + linesep
        return EEC_SCIM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from EEC
        if not super(EEC_SCIM, self).__eq__(other):
            return False
        if other.indmag != self.indmag:
            return False
        if other.parameters != self.parameters:
            return False
        if other.freq0 != self.freq0:
            return False
        if other.drive != self.drive:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from EEC
        EEC_SCIM_dict = super(EEC_SCIM, self).as_dict()
        if self.indmag is None:
            EEC_SCIM_dict["indmag"] = None
        else:
            EEC_SCIM_dict["indmag"] = self.indmag.as_dict()
        EEC_SCIM_dict["parameters"] = (
            self.parameters.copy() if self.parameters is not None else None
        )
        EEC_SCIM_dict["freq0"] = self.freq0
        if self.drive is None:
            EEC_SCIM_dict["drive"] = None
        else:
            EEC_SCIM_dict["drive"] = self.drive.as_dict()
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        EEC_SCIM_dict["__class__"] = "EEC_SCIM"
        return EEC_SCIM_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.indmag is not None:
            self.indmag._set_None()
        self.parameters = None
        self.freq0 = None
        if self.drive is not None:
            self.drive._set_None()
        # Set to None the properties inherited from EEC
        super(EEC_SCIM, self)._set_None()

    def _get_indmag(self):
        """getter of indmag"""
        return self._indmag

    def _set_indmag(self, value):
        """setter of indmag"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "indmag"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = IndMag()
        check_var("indmag", value, "IndMag")
        self._indmag = value

        if self._indmag is not None:
            self._indmag.parent = self

    indmag = property(
        fget=_get_indmag,
        fset=_set_indmag,
        doc=u"""Magnetic inductance

        :Type: IndMag
        """,
    )

    def _get_parameters(self):
        """getter of parameters"""
        return self._parameters

    def _set_parameters(self, value):
        """setter of parameters"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("parameters", value, "dict")
        self._parameters = value

    parameters = property(
        fget=_get_parameters,
        fset=_set_parameters,
        doc=u"""Parameters of the EEC: computed if empty, or enforced

        :Type: dict
        """,
    )

    def _get_freq0(self):
        """getter of freq0"""
        return self._freq0

    def _set_freq0(self, value):
        """setter of freq0"""
        check_var("freq0", value, "float")
        self._freq0 = value

    freq0 = property(
        fget=_get_freq0,
        fset=_set_freq0,
        doc=u"""Frequency

        :Type: float
        """,
    )

    def _get_drive(self):
        """getter of drive"""
        return self._drive

    def _set_drive(self, value):
        """setter of drive"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "drive"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Drive()
        check_var("drive", value, "Drive")
        self._drive = value

        if self._drive is not None:
            self._drive.parent = self

    drive = property(
        fget=_get_drive,
        fset=_set_drive,
        doc=u"""Drive

        :Type: Drive
        """,
    )
