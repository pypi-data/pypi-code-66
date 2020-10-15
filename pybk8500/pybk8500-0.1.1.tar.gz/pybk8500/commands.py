"""
Protocol can be found at https://bkpmedia.s3.amazonaws.com/downloads/manuals/en-us/85xx_manual.pdf
There is a section called Command details.
"""
from dynamicmethod import dynamicmethod

from pybk8500.field_types import Field, BytesField, StrField, \
    IntField, Int8Field, Int16Field, Int32Field, FloatField, ScalarFloatField, BitFlagField
from pybk8500.parser import Parser


__all__ = [
    'Message', 'CC_Commands', 'CV_Commands', 'CW_Commands', 'CR_Commands',
    'CommandStatus', 'SetRemoteOperation', 'LoadSwitch', 'SetMaxVoltage', 'ReadMaxVoltage', 'SetMaxCurrent',
    'ReadMaxCurrent', 'SetMaxPower', 'ReadMaxPower', 'SetMode', 'ReadMode', 'SetCCModeCurrent', 'ReadCCModeCurrent',
    'SetCVModeVoltage', 'ReadCVModeVoltage', 'SetCWModePower', 'ReadCWModePower', 'SetCRModeResistance',
    'ReadCRModeResistance', 'SetCCModeTransientCurrentAndTiming', 'ReadCCModeTransientParameters',
    'SetCVModeTransientVoltageAndTiming', 'ReadCVModeTransientParameters', 'SetCWModeTransientPowerAndTiming',
    'ReadCWModeTransientParameters', 'SetCRModeTransientResistanceAndTiming', 'ReadCRModeTransientParameters',
    'SelectListOperation', 'ReadListOperation', 'SetHowListsRepeat', 'ReadHowListsRepeat', 'SetNumberOfSteps',
    'ReadNumberOfSteps', 'SetOneStepCurrentAndTime', 'ReadOneStepCurrentAndTime', 'SetOneStepVoltageAndTime',
    'ReadOneStepVoltageAndTime', 'SetOneStepPowerAndTime', 'ReadOneStepPowerAndTime', 'SetOneStepResistanceAndTime',
    'ReadOneStepResistanceAndTime', 'SetListFileName', 'ReadListFileName', 'SetMemoryPartition', 'ReadMemoryPartition',
    'SaveListFile', 'RecallListFile', 'SetMinimumVoltage', 'ReadMinimumVoltage', 'SetTimerValueForLoadOn',
    'ReadTimerValueForLoadOn', 'SetTimerStateLoadOn', 'ReadTimerStateLoadOn', 'SetCommunicationAddress',
    'SetLocalControlState', 'SetRemoteSensingState', 'ReadRemoteSensingState', 'SelectTriggerSource',
    'ReadTriggerSource', 'TriggerElectronicLoad', 'SaveDCLoadSettings', 'RecallDCLoadSettings', 'SelectFunctionType',
    'GetFunctionType', 'ReadInputVoltageCurrentPowerState', 'GetProductInfo', 'ReadBarCode'
    ]


class Message(bytearray):
    """Message type object"""
    ID = 0
    NAME = 'Base Command'

    RESPONSE_TYPE = None

    MSG_LENGTH = 26

    # constant = Int8Field('constant', 0)  # Manually set and is not needed
    address = Int8Field('address', 1)
    command = Int8Field('command', 2)

    def get_checksum(self):
        """Return the checksum for the message."""
        if self.checksum_needs_updating:
            self.update_checksum()
        return self[25]

    def set_checksum(self, value):
        """Set the checksum for the message."""
        self[25] = value
        self.checksum_needs_updating = False

    checksum = Int8Field('checksum', 25, fget=get_checksum, fset=set_checksum)  # Last byte in message

    @staticmethod
    def calc_checksum(byts):
        """Calculate the checksum for the message."""
        byts = byts[:25]  # Do not use the checksum to calculate the checksum
        value = sum(byts)
        return value & 0xFF

    def update_checksum(self):
        """Update the checksum value with the new calculated value."""
        self.set_checksum(self.calc_checksum(self))
        self.checksum_needs_updating = False

    @dynamicmethod
    def fields(self):
        """Return a dictionary of {field names: values}."""
        fields = {}

        # Create get_value function for
        if isinstance(self, Message):
            # Is instance object with values
            get_value = lambda name: getattr(self, name, None)
        else:
            # Was called as a classmethod, so there are no values
            get_value = lambda name: None

        # Populate the fields
        for name in dir(self):
            f = getattr(self, name, None)
            if isinstance(f, Field) and f.name == name:
                fields[name] = get_value(name)

        return fields

    @classmethod
    def set_response_type(cls, msg_cls):
        cls.RESPONSE_TYPE = msg_cls
        return msg_cls

    def __init__(self, raw=None, address=None, **kwargs):
        self.checksum_needs_updating = False

        byts = raw
        if byts is None:
            # Create the base message
            byts = bytearray(b'\x00' * self.MSG_LENGTH)

            # Automatically set the constant and command
            try:
                byts[0] = 0xAA  # Constant
                byts[2] = self.ID  # Command
            except (ValueError, TypeError, Exception):
                pass

        # Check the message length
        length = len(byts)
        if length < self.MSG_LENGTH:
            byts = bytes(byts) + (b'\x00' * (self.MSG_LENGTH - length))

        super().__init__(byts[: self.MSG_LENGTH])

        # Set attributes with the given keyword arguments
        if address is not None:
            self.address = address

        for k, v in kwargs.items():
            setattr(self, k, v)

        # Only update the checksum if raw bytes were not given!
        if raw is None:
            self.update_checksum()

    def __setitem__(self, key, value):
        """Change set item to always flag `_update_checksum` to True.

        Every change will notify that the checksum needs to be recalculated.
        """
        ret = super().__setitem__(key, value)
        self.checksum_needs_updating = True
        return ret

    def __bytes__(self):
        if self.checksum_needs_updating:
            self.update_checksum()

        # bytearray has no super().__bytes___() I'm guessing most efficient is iter
        return bytes(iter(self))


@Parser.add_lookup
class CommandStatus(Message):
    """Indicates a return packet for a command sent to the DC Load"""
    ID = 0x12
    NAME = 'Command Status'

    # 3 Status byte (i.e., status of last command sent to DC Load).
    STATUS_NAMES = {'Checksum incorrect': 0x90,
                    'Parameter incorrect': 0xA0,
                    'Unrecognized command': 0xB0,
                    'Invalid command': 0xC0,
                    'Command was successful': 0x80}
    STATUS_VALUES = {v: k for k, v in STATUS_NAMES.items()}

    status = Int8Field('status', 3)
    status.get_converter = STATUS_VALUES.get
    status.set_converter = STATUS_NAMES.get
    value = status  # Alias so Message(value=1) can be used


@Parser.add_lookup
class SetRemoteOperation(Message):
    """Set the DC Load to remote operation"""
    ID = 0x20
    NAME = 'Set Remote Operation'

    OPERATION_NAMES = {'Front Panel': 0, 'Remote': 1}
    OPERATION_VALUES = {v: k for k, v in OPERATION_NAMES.items()}

    operation = Int8Field('operation', 3)
    operation.get_converter = OPERATION_VALUES.get
    operation.set_converter = OPERATION_NAMES.get
    value = operation  # Alias so Message(value=1) can be used


@Parser.add_lookup
class LoadSwitch(Message):
    """Load switch to turn the load on or off"""
    ID = 0x21
    NAME = 'Load Switch'

    SWITCH_NAMES = {'Off': 0, 'On': 1}
    SWITCH_VALUES = {v: k for k, v in SWITCH_NAMES.items()}

    operation = Int8Field('operation', 3)
    operation.get_converter = SWITCH_VALUES.get
    operation.set_converter = SWITCH_NAMES.get
    value = operation  # Alias so Message(value=1) can be used


@Parser.add_lookup
class SetMaxVoltage(Message):
    """Set the maximum voltage allowed"""
    ID = 0x22
    NAME = 'Set Max Voltage'

    voltage = ScalarFloatField('voltage', 3, length=4, scalar=1000)  # 1mV
    value = voltage  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SetMaxVoltage.set_response_type
class ReadMaxVoltage(SetMaxVoltage):
    """Read the maximum voltage allowed"""
    ID = 0x23
    NAME = 'Read Max Voltage'


@Parser.add_lookup
class SetMaxCurrent(Message):
    """Set the maximum current allowed"""
    ID = 0x24
    NAME = 'Set Max Current'

    current = ScalarFloatField('current', 3, length=4, scalar=10000)  # 0.1 mA
    value = current  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SetMaxVoltage.set_response_type
class ReadMaxCurrent(SetMaxCurrent):
    """Read the maximum current allowed"""
    ID = 0x25
    NAME = 'Read Max Current'


@Parser.add_lookup
class SetMaxPower(Message):
    """Set the maximum power allowed"""
    ID = 0x26
    NAME = 'Set Max Power'

    power = ScalarFloatField('power', 3, length=4, scalar=1000)  # 1 mW
    value = power  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SetMaxPower.set_response_type
class ReadMaxPower(SetMaxPower):
    """Read the maximum current allowed"""
    ID = 0x27
    NAME = 'Read Max Power'


@Parser.add_lookup
class SetMode(Message):
    """Set CC, CV, CW, or CR mode"""
    ID = 0x28
    NAME = 'Set Mode'

    MODE_NAMES = {'CC': 0,
                  'CV': 1,
                  'CW': 2,
                  'CR': 3}
    MODE_VALUES = {v: k for k, v in MODE_NAMES.items()}

    mode = Int8Field('mode', 3)
    mode.get_converter = MODE_NAMES.get
    mode.set_converter = MODE_VALUES.get
    value = mode  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SetMode.set_response_type
class ReadMode(SetMode):
    """Read the mode being used (CC, CV, CW, or CR)"""
    ID = 0x29
    NAME = 'Read Mode'


@Parser.add_lookup
class SetCCModeCurrent(Message):
    """Set CC mode current"""
    ID = 0x2A
    NAME = 'Set CC Mode Current'

    current = ScalarFloatField('current', 3, length=4, scalar=10000)
    value = current  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SetCCModeCurrent.set_response_type
class ReadCCModeCurrent(SetCCModeCurrent):
    """Read CC mode current"""
    ID = 0x2B
    NAME = 'Read CC Mode Current'


@Parser.add_lookup
class SetCVModeVoltage(Message):
    """Set CV mode voltage"""
    ID = 0x2C
    NAME = 'Set CV Mode Voltage'

    voltage = ScalarFloatField('voltage', 3, length=4, scalar=1000)
    value = voltage  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SetCVModeVoltage.set_response_type
class ReadCVModeVoltage(SetCVModeVoltage):
    """Read CV mode voltage"""
    ID = 0x2D
    NAME = 'Read CV Mode Voltage'


@Parser.add_lookup
class SetCWModePower(Message):
    """Set CW mode power"""
    ID = 0x2E
    NAME = 'Set CW Mode Power'

    power = ScalarFloatField('power', 3, length=4, scalar=1000)
    value = power  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SetCWModePower.set_response_type
class ReadCWModePower(SetCWModePower):
    """Read CW mode power"""
    ID = 0x2F
    NAME = 'Read CW Mode Power'


@Parser.add_lookup
class SetCRModeResistance(Message):
    """Set CR mode resistance"""
    ID = 0x30
    NAME = 'Set CR Mode Resistance'

    resistance = ScalarFloatField('resistance', 3, length=4, scalar=1000)
    value = resistance  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SetCRModeResistance.set_response_type
class ReadCRModeResistance(SetCRModeResistance):
    """Read CR mode resistance"""
    ID = 0x31
    NAME = 'Read CR Mode Resistance'


@Parser.add_lookup
class SetCCModeTransientCurrentAndTiming(Message):
    """Set CC mode transient current and timing

    Kwargs:
        current_a (float)[0]: Current as 0.1 mA
        time_a (float)[0]: Time as 0.1 ms
        current_b (float)[0]: Current as 0.1 mA
        time_b (float)[0]: Time as 0.1 ms
        operation (int/str)[0]: {'CONTINUOUS': 0, 'PULSE': 1, 'TOGGLED': 2}
    """
    ID = 0x32
    NAME = 'Set CC Mode Transient Current and Timing'

    # 3 to 6 Value A of current in units of 0.1 mA. Little-endian 4 byte number.
    current_a = ScalarFloatField('current_a', 3, length=4, scalar=10000)  # 0.1 mA
    value_a = current_a  # Alias so Message(value_a=1) can be used

    # 7 to 8 Time for A current in units of 0.1 ms. Little-endian 2 byte number.
    time_a = ScalarFloatField('time_a', 7, length=2, scalar=10000)  # 0.1 ms

    # 9 to 12 Value B of current in units of 0.1 mA. Little-endian 4 byte number.
    current_b = ScalarFloatField('current_b', 9, length=4, scalar=10000)  # 0.1 mA
    value_b = current_b  # Alias so Message(value_b=1) can be used

    # 13 to 14 Time for B current in units of 0.1 ms. Little-endian 2 byte number.
    time_b = ScalarFloatField('time_b', 13, length=2, scalar=10000)  # 0.1 ms

    # 15 Transient operation: 0 is CONTINUOUS, 1 is PULSE, 2 is TOGGLED
    OPERATION_NAMES = {'CONTINUOUS': 0, 'PULSE': 1, 'TOGGLED': 2}
    OPERATION_VALUES = {v: k for k, v in OPERATION_NAMES.items()}

    operation = Int8Field('operation', 15)
    operation.get_converter = OPERATION_VALUES.get
    operation.set_converter = OPERATION_NAMES.get


@Parser.add_lookup
@SetCCModeTransientCurrentAndTiming.set_response_type
class ReadCCModeTransientParameters(SetCCModeTransientCurrentAndTiming):
    """Read CC mode transient parameters"""
    ID = 0x33
    NAME = 'Read CC Mode Transient Parameters'


@Parser.add_lookup
class SetCVModeTransientVoltageAndTiming(Message):
    """Set CV mode transient voltage and timing"""
    ID = 0x34
    NAME = 'Set CV Mode Transient Voltage and Timing'

    # 3 to 6 Value A of voltage in units of 1 mV. Little-endian 4 byte number.
    voltage_a = ScalarFloatField('voltage_a', 3, length=4, scalar=1000)  # 1 mV
    value_a = voltage_a  # Alias so Message(value_a=1) can be used

    # 7 to 8 Time for A voltage in units of 0.1 ms. Little-endian 2 byte number.
    time_a = ScalarFloatField('time_a', 7, length=2, scalar=10000)  # 0.1 ms

    # 9 to 12 Value B of voltage in units of 1 mV. Little-endian 4 byte number.
    voltage_b = ScalarFloatField('voltage_b', 9, length=4, scalar=1000)  # 1 mV
    value_b = voltage_b  # Alias so Message(value_b=1) can be used

    # 13 to 14 Time for B voltage in units of 0.1 ms. Little-endian 2 byte number.
    time_b = ScalarFloatField('time_b', 13, length=2, scalar=10000)  # 0.1 ms

    # 15 Transient operation: 0 is CONTINUOUS, 1 is PULSE, 2 is TOGGLED
    OPERATION_NAMES = {'CONTINUOUS': 0, 'PULSE': 1, 'TOGGLED': 2}
    OPERATION_VALUES = {v: k for k, v in OPERATION_NAMES.items()}

    operation = Int8Field('operation', 15)
    operation.get_converter = OPERATION_VALUES.get
    operation.set_converter = OPERATION_NAMES.get


@Parser.add_lookup
@SetCVModeTransientVoltageAndTiming.set_response_type
class ReadCVModeTransientParameters(SetCVModeTransientVoltageAndTiming):
    """Read CV mode transient parameters"""
    ID = 0x35
    NAME = 'Read CV Mode Transient Parameters'


@Parser.add_lookup
class SetCWModeTransientPowerAndTiming(Message):
    """Set CW mode transient power and timing"""
    ID = 0x36
    NAME = 'Set CW Mode Transient Power and Timing'

    # 3 to 6 Value A of power in units of 1 mW. Little-endian 4 byte number.
    power_a = ScalarFloatField('power_a', 3, length=4, scalar=1000)  # 1 mW
    value_a = power_a  # Alias so Message(value_a=1) can be used

    # 7 to 8 Time for A power in units of 0.1 ms. Little-endian 2 byte number.
    time_a = ScalarFloatField('time_a', 7, length=2, scalar=10000)  # 0.1 ms

    # 9 to 12 Value B of power in units of 1 mW. Little-endian 4 byte number.
    power_b = ScalarFloatField('power_b', 9, length=4, scalar=1000)  # 1 mW
    value_b = power_b  # Alias so Message(value_b=1) can be used

    # 13 to 14 Time for B power in units of 0.1 ms. Little-endian 2 byte number.
    time_b = ScalarFloatField('time_b', 13, length=2, scalar=10000)  # 0.1 ms

    # 15 Transient operation: 0 is CONTINUOUS, 1 is PULSE, 2 is TOGGLED
    OPERATION_NAMES = {'CONTINUOUS': 0, 'PULSE': 1, 'TOGGLED': 2}
    OPERATION_VALUES = {v: k for k, v in OPERATION_NAMES.items()}

    operation = Int8Field('operation', 15)
    operation.get_converter = OPERATION_VALUES.get
    operation.set_converter = OPERATION_NAMES.get


@Parser.add_lookup
@SetCWModeTransientPowerAndTiming.set_response_type
class ReadCWModeTransientParameters(SetCWModeTransientPowerAndTiming):
    """Read CW mode transient parameters"""
    ID = 0x37
    NAME = 'Read CW Mode Transient Parameters'


@Parser.add_lookup
class SetCRModeTransientResistanceAndTiming(Message):
    """Set CR mode transient resistance and timing"""
    ID = 0x38
    NAME = 'Set CR Mode Transient Resistance and Timing'

    # 3 to 6 Value A of resistance in units of 1 m. Little-endian 4 byte number.
    resistance_a = ScalarFloatField('resistance_a', 3, length=4, scalar=1000)  # 1 m Ohm
    value_a = resistance_a  # Alias so Message(value_a=1) can be used

    # 7 to 8 Time for A resistance in units of 0.1 ms. Little-endian 2 byte number.
    time_a = ScalarFloatField('time_a', 7, length=2, scalar=10000)  # 0.1 ms

    # 9 to 12 Value B of resistance in units of 1 m. Little-endian 4 byte number.
    resistance_b = ScalarFloatField('resistance_b', 9, length=4, scalar=1000)  # 1 m Ohm
    value_b = resistance_b  # Alias so Message(value_b=1) can be used

    # 13 to 14 Time for B resistance in units of 0.1 ms. Little-endian 2 byte number.
    time_b = ScalarFloatField('time_b', 13, length=2, scalar=10000)  # 0.1 ms

    # 15 Transient operation: 0 is CONTINUOUS, 1 is PULSE, 2 is TOGGLED
    OPERATION_NAMES = {'CONTINUOUS': 0, 'PULSE': 1, 'TOGGLED': 2}
    OPERATION_VALUES = {v: k for k, v in OPERATION_NAMES.items()}

    operation = Int8Field('operation', 15)
    operation.get_converter = OPERATION_VALUES.get
    operation.set_converter = OPERATION_NAMES.get


@Parser.add_lookup
@SetCRModeTransientResistanceAndTiming.set_response_type
class ReadCRModeTransientParameters(SetCRModeTransientResistanceAndTiming):
    """Read CR mode transient parameters"""
    ID = 0x39
    NAME = 'Read CR Mode Transient Parameters'


@Parser.add_lookup
class SelectListOperation(Message):
    """Select the list operation (CC/CV/CW/CR)"""
    ID = 0x3A
    NAME = 'Select List Operation'

    OPERATION_NAMES = {'Constant Current (CC)': 0, 'Constant Voltage (CV)': 1,
                       'Constant Power (CP)': 2, 'Constant Resistance (CR)': 3}
    OPERATION_VALUES = {v: k for k, v in OPERATION_NAMES.items()}

    operation = Int8Field('operation', 3)
    operation.get_converter = OPERATION_VALUES.get
    operation.set_converter = OPERATION_NAMES.get
    value = operation  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SelectListOperation.set_response_type
class ReadListOperation(SelectListOperation):
    """Read the list operation (CC/CV/CW/CR)"""
    ID = 0x3B
    NAME = 'Read List Operation'


@Parser.add_lookup
class SetHowListsRepeat(Message):
    """Set how lists repeat (ONCE or REPEAT)"""
    ID = 0x3C
    NAME = 'Set Lists Repeat'

    REPEAT_NAMES = {'Once': 0, 'Repeat': 1}
    REPEAT_VALUES = {v: k for k, v in REPEAT_NAMES.items()}

    repeat = Int8Field('repeat', 3)
    repeat.get_converter = REPEAT_VALUES.get
    repeat.set_converter = REPEAT_NAMES.get
    value = repeat  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SetHowListsRepeat.set_response_type
class ReadHowListsRepeat(SetHowListsRepeat):
    """Read how lists repeat (ONCE or REPEAT)"""
    ID = 0x3D
    NAME = 'Read Lists Repeat'


@Parser.add_lookup
class SetNumberOfSteps(Message):
    """Set the number of list steps"""
    ID = 0x3E
    NAME = 'Set Number Of Steps'

    # 3 to 4 2 byte little-endian integer for number of steps
    steps = Int16Field('steps', 3)
    value = steps  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SetNumberOfSteps.set_response_type
class ReadNumberOfSteps(SetNumberOfSteps):
    """Read the number of list steps"""
    ID = 0x3F
    NAME = 'Read Number Of Steps'


@Parser.add_lookup
class SetOneStepCurrentAndTime(Message):
    """Set one of the step's current and time values"""
    ID = 0x40
    NAME = 'Set One Of Steps Current And Time Values'

    # 3 to 4 2 byte little-endian integer specifying which step number in the list
    step = Int16Field('step', 3)

    # 5 to 8 4 byte little-endian integer specifying the current in units of 0.1 mA
    current = ScalarFloatField('current', 5, length=4, scalar=10000)  # 0.1 mA
    value = current  # Alias so Message(value=1) can be used

    # 9 to 10 2 byte little-endian integer specifying the step timing in units of 0.1 ms
    time = ScalarFloatField('time', 9, length=2, scalar=10000)  # 0.1 ms


@Parser.add_lookup
@SetOneStepCurrentAndTime.set_response_type
class ReadOneStepCurrentAndTime(SetOneStepCurrentAndTime):
    """Read one of the step's current and time values"""
    ID = 0x41
    NAME = 'Read One Step Current And Time'


@Parser.add_lookup
class SetOneStepVoltageAndTime(Message):
    """Set one of the step's voltage and time values"""
    ID = 0x42
    NAME = 'Set One Of Steps Voltage And Time Values'

    # 3 to 4 2 byte little-endian integer specifying which step number in the list
    step = Int16Field('step', 3)

    # 5 to 8 4 byte little-endian integer specifying the voltage in units of 1 mV
    voltage = ScalarFloatField('voltage', 5, length=4, scalar=1000)  # 1 mV
    value = voltage  # Alias so Message(value=1) can be used

    # 9 to 10 2 byte little-endian integer specifying the step timing in units of 0.1 ms
    time = ScalarFloatField('time', 9, length=2, scalar=10000)  # 0.1 ms


@Parser.add_lookup
@SetOneStepVoltageAndTime.set_response_type
class ReadOneStepVoltageAndTime(SetOneStepVoltageAndTime):
    """Read one of the step's voltage and time values"""
    ID = 0x43
    NAME = 'Read One Step Voltage And Time'


@Parser.add_lookup
class SetOneStepPowerAndTime(Message):
    """Set one of the step's power and time values"""
    ID = 0x44
    NAME = 'Set One Of Steps Power And Time Values'

    # 3 to 4 2 byte little-endian integer specifying which step number in the list
    step = Int16Field('step', 3)

    # 5 to 8 4 byte little-endian integer specifying the power in units of 1 mW
    power = ScalarFloatField('power', 5, length=4, scalar=1000)  # 1 mV
    value = power  # Alias so Message(value=1) can be used

    # 9 to 10 2 byte little-endian integer specifying the step timing in units of 0.1 ms
    time = ScalarFloatField('time', 9, length=2, scalar=10000)  # 0.1 ms


@Parser.add_lookup
@SetOneStepPowerAndTime.set_response_type
class ReadOneStepPowerAndTime(SetOneStepPowerAndTime):
    """Read one of the step's power and time values"""
    ID = 0x45
    NAME = 'Read One Step Power And Time'


@Parser.add_lookup
class SetOneStepResistanceAndTime(Message):
    """Set one of the step's resistance and time values"""
    ID = 0x46
    NAME = 'Set One Of Steps Resistance And Time Values'

    # 3 to 4 2 byte little-endian integer specifying which step number in the list
    step = Int16Field('step', 3)

    # 5 to 8 4 byte little-endian integer specifying the resistance in units of 1 m Ohm
    resistance = ScalarFloatField('resistance', 5, length=4, scalar=1000)  # 1 mV
    value = resistance  # Alias so Message(value=1) can be used

    # 9 to 10 2 byte little-endian integer specifying the step timing in units of 0.1 ms
    time = ScalarFloatField('time', 9, length=2, scalar=10000)  # 0.1 ms


@Parser.add_lookup
@SetOneStepResistanceAndTime.set_response_type
class ReadOneStepResistanceAndTime(SetOneStepResistanceAndTime):
    """Read one of the step's resistance and time values"""
    ID = 0x47
    NAME = 'Read One Step Resistance And Time'


@Parser.add_lookup
class SetListFileName(Message):
    """Set the list file name"""
    ID = 0x48
    NAME = 'Set List File Name'

    # 3 to 12 List file name (ASCII characters)
    filename = StrField('filename', 3, length=10)
    value = filename  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SetListFileName.set_response_type
class ReadListFileName(SetListFileName):
    """Read the list file name"""
    ID = 0x49
    NAME = 'Read List File Name'


@Parser.add_lookup
class SetMemoryPartition(Message):
    """Set the memory partitioning for storing lists"""
    ID = 0x4A
    NAME = 'Set Memory Partition'

    SCHEME_NAMES = {'1 file of 1000 list steps': 1,
                    '2 files of 500 list steps': 2,
                    '4 files of 250 list steps': 4,
                    '8 files of 120 list steps': 8}
    SCHEME_VALUES = {v: k for k, v in SCHEME_NAMES.items()}

    scheme = Int8Field('scheme', 3)
    scheme.get_converter = SCHEME_VALUES.get
    scheme.set_converter = SCHEME_NAMES.get
    value = scheme  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SetMemoryPartition.set_response_type
class ReadMemoryPartition(SetMemoryPartition):
    """Read the memory partitioning for storing list steps"""
    ID = 0x4B
    NAME = 'Read Memory Partition'


@Parser.add_lookup
class SaveListFile(Message):
    """Save the list file"""
    ID = 0x4C
    NAME = 'Save List File'

    # Storage location, a one byte integer from 1 to 8. This number must be
    # consistent with the number of list files allowed as set by the 0x4A command.
    location = Int8Field('location', 3)
    value = location  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SaveListFile.set_response_type
class RecallListFile(SaveListFile):
    """Recall the list file"""
    ID = 0x4D
    NAME = 'Recall List File'


@Parser.add_lookup
class SetMinimumVoltage(Message):
    """Set minimum voltage in battery testing"""
    ID = 0x4E
    NAME = 'Set Minimum Voltage'

    # 3 to 6 4 byte little-endian integer specifying the minimum voltage in units of 1 mV
    voltage = ScalarFloatField('voltage', 3, length=4, scalar=1000)  # 1 mV
    value = voltage  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SetMinimumVoltage.set_response_type
class ReadMinimumVoltage(SetMinimumVoltage):
    """Read minimum voltage in battery testing"""
    ID = 0x4F
    NAME = 'Read Minimum Voltage'


@Parser.add_lookup
class SetTimerValueForLoadOn(Message):
    """Set timer value of for LOAD ON"""
    ID = 0x50
    NAME = 'Set Timer Value For Load On'

    # 2 byte little-endian integer specifying the time in units of 1 second
    seconds = Int16Field('seconds', 3)
    value = seconds  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SetTimerValueForLoadOn.set_response_type
class ReadTimerValueForLoadOn(SetTimerValueForLoadOn):
    """Read timer value for LOAD ON"""
    ID = 0x51
    NAME = 'Read Timer Value For Load On'


@Parser.add_lookup
class SetTimerStateLoadOn(Message):
    """Disable/enable timer for LOAD ON"""
    ID = 0x52
    NAME = 'Set Timer State Load On'

    STATE_NAMES = {'disabled': 0,
                   'enabled': 1}
    STATE_VALUES = {v: k for k, v in STATE_NAMES.items()}

    state = Int8Field('state', 3)
    state.get_converter = STATE_VALUES.get
    state.set_converter = STATE_NAMES.get
    value = state  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SetTimerStateLoadOn.set_response_type
class ReadTimerStateLoadOn(SetTimerStateLoadOn):
    """Read timer state for LOAD ON"""
    ID = 0x53
    NAME = 'Read Timer State Load On'


@Parser.add_lookup
class SetCommunicationAddress(Message):
    """Set communication address"""
    ID = 0x54
    NAME = 'Set Communication Address'

    # 2 byte little-endian integer specifying the address. Must be between 0 and 0xFE, inclusive.
    com_address = Int8Field('com_address', 3)
    value = com_address  # Alias so Message(value=1) can be used


@Parser.add_lookup
class SetLocalControlState(Message):
    """Enable/disable LOCAL control"""
    ID = 0x55
    NAME = 'Set Local Control State'

    STATE_NAMES = {'disabled': 0,  # 0 means to disable the Local key on the front panel
                   'enabled': 1}   # 1 means to enable the Local key on the front panel
    STATE_VALUES = {v: k for k, v in STATE_NAMES.items()}

    state = Int8Field('state', 3)
    state.get_converter = STATE_VALUES.get
    state.set_converter = STATE_NAMES.get
    value = state  # Alias so Message(value=1) can be used


@Parser.add_lookup
class SetRemoteSensingState(Message):
    """Enable/disable remote sensing"""
    ID = 0x56
    NAME = 'Set Remote Sensing State'

    STATE_NAMES = {'disabled': 0,  # 0 means to disable remote sensing
                   'enabled': 1}   # 1 means to enable remote sensing
    STATE_VALUES = {v: k for k, v in STATE_NAMES.items()}

    state = Int8Field('state', 3)
    state.get_converter = STATE_VALUES.get
    state.set_converter = STATE_NAMES.get
    value = state  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SetRemoteSensingState.set_response_type
class ReadRemoteSensingState(SetRemoteSensingState):
    """Read the state of remote sensing"""
    ID = 0x57
    NAME = 'Set Remote Sensing State'


@Parser.add_lookup
class SelectTriggerSource(Message):
    """Select trigger source"""
    ID = 0x58
    NAME = 'Select Trigger Source'

    TRIGGER_NAMES = {'immediate trigger': 0,  # 0 means immediate trigger (i.e., triggered from the front panel)
                     'external trigger': 1,  # 1 means external trigger from the rear panel connector
                     'software trigger': 2,  # 2 means a bus (software) trigger (the 0x5A command)
                     }
    TRIGGER_VALUES = {v: k for k, v in TRIGGER_NAMES.items()}

    trigger = Int8Field('trigger', 3)
    trigger.get_converter = TRIGGER_VALUES.get
    trigger.set_converter = TRIGGER_NAMES.get
    value = trigger  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SelectTriggerSource.set_response_type
class ReadTriggerSource(SelectTriggerSource):
    """Read trigger source"""
    ID = 0x59
    NAME = 'Read Trigger Source'


@Parser.add_lookup
class TriggerElectronicLoad(Message):
    """Trigger the electronic load"""
    ID = 0x5A
    NAME = 'Select Trigger Source'


@Parser.add_lookup
class SaveDCLoadSettings(Message):
    """Save DC Load's settings"""
    ID = 0x5B
    NAME = 'Save DC Load Settings'

    # Storage register, a number between 1 and 25 inclusive
    storage_register = Int8Field('storage_register', 3)
    value = storage_register  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SaveDCLoadSettings.set_response_type
class RecallDCLoadSettings(SaveDCLoadSettings):
    """Recall DC Load's settings"""
    ID = 0x5C
    NAME = 'Recall DC Load Settings'


@Parser.add_lookup
class SelectFunctionType(Message):
    """Select FIXED/SHORT/TRAN/LIST/BATTERY function"""
    ID = 0x5D
    NAME = 'Select Function Type'

    FUNCTION_NAMES = {'Fixed': 0,
                      'Short': 1,
                      'Transient': 2,
                      'List': 3,
                      'Battery': 4,
                      }
    FUNCTION_VALUES = {v: k for k, v in FUNCTION_NAMES.items()}

    function = Int8Field('function', 3)
    function.get_converter = FUNCTION_VALUES.get
    function.set_converter = FUNCTION_NAMES.get
    value = function  # Alias so Message(value=1) can be used


@Parser.add_lookup
@SelectFunctionType.set_response_type
class GetFunctionType(SelectFunctionType):
    """Get function type (FIXED/SHORT/TRAN/LIST/BATTERY)"""
    ID = 0x5E
    NAME = 'Get Function Type'


@Parser.add_lookup
class ReadInputVoltageCurrentPowerState(Message):
    """Read input voltage, current, power and relative state"""
    ID = 0x5F
    NAME = 'Read Input Voltage Current Power State'

    # 3 to 6 4 byte little-endian integer for terminal voltage in units of 1 mV
    voltage = ScalarFloatField('voltage', 3, length=4, scalar=1000)  # 1 mV

    # 7 to 10 4 byte little-endian integer for terminal current in units of 0.1 mA
    current = ScalarFloatField('current', 7, length=4, scalar=10000)  # 0.1 mA

    # 11 to 14 4 byte little-endian integer for terminal power in units of 1 mW
    power = ScalarFloatField('power', 11, length=4, scalar=1000)  # 1 mV

    # 15 Operation state register (see bit list below)
    operation_register = BitFlagField('operation_register', 15,
                                      flags={
                                          'calc_new_demarcation_coeff': 0,  # 0 Calculate the new demarcation coefficient
                                          'waiting': 1,  # 1 Waiting for a trigger signal
                                          'remote_control_state': 2,  # 2 Remote control state (1 means enabled)
                                          'output_state': 3,  # 3 Output state (1 means ON)
                                          'local_key_state': 4,  # 4 Local key state (0 means not enabled, 1 means enabled)
                                          'remote_sensing_mode': 5,  # 5 Remote sensing mode (1 means enabled)
                                          'load_on_timer': 6,  # 6 LOAD ON timer is enabled
                                          'reserved': 7,  # 7 Reserved
                                          })

    # 16 to 17 2 byte little-endian integer for demand state register (see bit list below)
    demand_register = BitFlagField('operation_register', 16, length=2,
                                   flags={
                                       'reversed_voltage': 0,  # 0 Reversed voltage is at instrument's terminals (1 means yes)
                                       'over_voltage': 1,  # 1 Over voltage (1 means yes)
                                       'over_current': 2,  # 2 Over current (1 means yes)
                                       'over_power': 3,  # 3 Over power (1 means yes)
                                       'over_temperature': 4,  # 4 Over temperature (1 means yes)
                                       'connect_remote_terminal': 5,  # 5 Not connect remote terminal
                                       'constant_current': 6,  # 6 Constant current
                                       'constant_voltage': 7,  # 7 Constant voltage
                                       'constant_power': 8,  # 8 Constant power
                                       'constant_resistance': 9,  # 9 Constant resistance
                                       })


@Parser.add_lookup
class GetProductInfo(Message):
    """Get product's model, serial number, and firmware version"""
    ID = 0x6A
    NAME = 'Get Product Info'

    # 3 to 7 ASCII model information
    model = StrField('model', 3, length=5)

    # 8 Low byte of firmware version number
    # 9 High byte of firmware version number
    firmware_version = Int16Field('firmware_version', 8)

    # 10 to 19 Instrument's serial number in ASCII
    serial_number = StrField('serial_number', 10, length=10)


@Parser.add_lookup
class ReadBarCode(Message):
    """Read the bar code information"""
    ID = 0x6B
    NAME = 'Read Bar Code'

    # 3 to 5 Identity
    identity = StrField('identity', 3, length=3)

    # 6 to 7 Sub
    sub = StrField('sub', 6, length=2)

    # 7 to 9 Version
    version = StrField('version', 7, length=3)

    # 10 to 11 Year
    year = StrField('year', 10, length=2)


CC_Commands = {'value': SetCCModeCurrent,
               'transient': SetCCModeTransientCurrentAndTiming,
               'step': SetOneStepCurrentAndTime,}

CV_Commands = {'value': SetCVModeVoltage,
               'transient': SetCVModeTransientVoltageAndTiming,
               'step': SetOneStepVoltageAndTime,}

CW_Commands = {'value': SetCWModePower,
               'transient': SetCWModeTransientPowerAndTiming,
               'step': SetOneStepPowerAndTime,}

CR_Commands = {'value': SetCRModeResistance,
               'transient': SetCRModeTransientResistanceAndTiming,
               'step': SetOneStepResistanceAndTime,}
