'''_1170.py

MeasurementSettings
'''


from typing import Callable

from mastapy._internal.implicit import list_with_selected_item, overridable
from mastapy.utility.units_and_measurements import _1169
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.utility.units_and_measurements.measurements import (
    _1176, _1177, _1178, _1179,
    _1180, _1181, _1182, _1183,
    _1184, _1185, _1186, _1187,
    _1188, _1189, _1190, _1191,
    _1192, _1193, _1194, _1195,
    _1196, _1197, _1198, _1199,
    _1200, _1201, _1202, _1203,
    _1204, _1205, _1206, _1207,
    _1208, _1209, _1210, _1211,
    _1212, _1213, _1214, _1215,
    _1216, _1217, _1218, _1219,
    _1220, _1221, _1222, _1223,
    _1224, _1225, _1226, _1227,
    _1228, _1229, _1230, _1231,
    _1232, _1233, _1234, _1235,
    _1236, _1237, _1238, _1239,
    _1240, _1241, _1242, _1243,
    _1244, _1245, _1246, _1247,
    _1248, _1249, _1250, _1251,
    _1252, _1253, _1254, _1255,
    _1256, _1257, _1258, _1259,
    _1260, _1261, _1262, _1263,
    _1264, _1265, _1266, _1267,
    _1268, _1269, _1270, _1271,
    _1272, _1273, _1274, _1275,
    _1276, _1277, _1278, _1279,
    _1280, _1281, _1282, _1283
)
from mastapy._internal.cast_exception import CastException
from mastapy.utility import _1158
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_SETTINGS = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements', 'MeasurementSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementSettings',)


class MeasurementSettings(_1158.PerMachineSettings):
    '''MeasurementSettings

    This is a mastapy class.
    '''

    TYPE = _MEASUREMENT_SETTINGS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MeasurementSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def selected_measurement(self) -> 'list_with_selected_item.ListWithSelectedItem_MeasurementBase':
        '''list_with_selected_item.ListWithSelectedItem_MeasurementBase: 'SelectedMeasurement' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_MeasurementBase)(self.wrapped.SelectedMeasurement) if self.wrapped.SelectedMeasurement else None

    @selected_measurement.setter
    def selected_measurement(self, value: 'list_with_selected_item.ListWithSelectedItem_MeasurementBase.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_MeasurementBase.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_MeasurementBase.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value else None)
        self.wrapped.SelectedMeasurement = value

    @property
    def sample_input(self) -> 'str':
        '''str: 'SampleInput' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SampleInput

    @property
    def sample_output(self) -> 'str':
        '''str: 'SampleOutput' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SampleOutput

    @property
    def number_decimal_separator(self) -> 'str':
        '''str: 'NumberDecimalSeparator' is the original name of this property.'''

        return self.wrapped.NumberDecimalSeparator

    @number_decimal_separator.setter
    def number_decimal_separator(self, value: 'str'):
        self.wrapped.NumberDecimalSeparator = str(value) if value else None

    @property
    def number_group_separator(self) -> 'str':
        '''str: 'NumberGroupSeparator' is the original name of this property.'''

        return self.wrapped.NumberGroupSeparator

    @number_group_separator.setter
    def number_group_separator(self, value: 'str'):
        self.wrapped.NumberGroupSeparator = str(value) if value else None

    @property
    def default_to_metric(self) -> 'Callable[..., None]':
        '''Callable[..., None]: 'DefaultToMetric' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DefaultToMetric

    @property
    def default_to_imperial(self) -> 'Callable[..., None]':
        '''Callable[..., None]: 'DefaultToImperial' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DefaultToImperial

    @property
    def small_number_cutoff(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'SmallNumberCutoff' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.SmallNumberCutoff) if self.wrapped.SmallNumberCutoff else None

    @small_number_cutoff.setter
    def small_number_cutoff(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0, is_overridden)
        self.wrapped.SmallNumberCutoff = value

    @property
    def show_trailing_zeros(self) -> 'bool':
        '''bool: 'ShowTrailingZeros' is the original name of this property.'''

        return self.wrapped.ShowTrailingZeros

    @show_trailing_zeros.setter
    def show_trailing_zeros(self, value: 'bool'):
        self.wrapped.ShowTrailingZeros = bool(value) if value else False

    @property
    def current_selected_measurement(self) -> '_1169.MeasurementBase':
        '''MeasurementBase: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1169.MeasurementBase.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MeasurementBase. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_acceleration(self) -> '_1176.Acceleration':
        '''Acceleration: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1176.Acceleration.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Acceleration. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_angle(self) -> '_1177.Angle':
        '''Angle: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1177.Angle.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Angle. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_angle_per_unit_temperature(self) -> '_1178.AnglePerUnitTemperature':
        '''AnglePerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1178.AnglePerUnitTemperature.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AnglePerUnitTemperature. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_angle_small(self) -> '_1179.AngleSmall':
        '''AngleSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1179.AngleSmall.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngleSmall. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_angle_very_small(self) -> '_1180.AngleVerySmall':
        '''AngleVerySmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1180.AngleVerySmall.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngleVerySmall. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_angular_acceleration(self) -> '_1181.AngularAcceleration':
        '''AngularAcceleration: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1181.AngularAcceleration.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularAcceleration. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_angular_compliance(self) -> '_1182.AngularCompliance':
        '''AngularCompliance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1182.AngularCompliance.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularCompliance. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_angular_jerk(self) -> '_1183.AngularJerk':
        '''AngularJerk: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1183.AngularJerk.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularJerk. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_angular_stiffness(self) -> '_1184.AngularStiffness':
        '''AngularStiffness: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1184.AngularStiffness.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularStiffness. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_angular_velocity(self) -> '_1185.AngularVelocity':
        '''AngularVelocity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1185.AngularVelocity.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularVelocity. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_area(self) -> '_1186.Area':
        '''Area: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1186.Area.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Area. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_area_small(self) -> '_1187.AreaSmall':
        '''AreaSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1187.AreaSmall.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AreaSmall. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_cycles(self) -> '_1188.Cycles':
        '''Cycles: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1188.Cycles.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Cycles. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_damage(self) -> '_1189.Damage':
        '''Damage: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1189.Damage.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Damage. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_damage_rate(self) -> '_1190.DamageRate':
        '''DamageRate: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1190.DamageRate.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to DamageRate. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_data_size(self) -> '_1191.DataSize':
        '''DataSize: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1191.DataSize.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to DataSize. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_decibel(self) -> '_1192.Decibel':
        '''Decibel: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1192.Decibel.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Decibel. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_density(self) -> '_1193.Density':
        '''Density: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1193.Density.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Density. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_energy(self) -> '_1194.Energy':
        '''Energy: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1194.Energy.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Energy. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_energy_per_unit_area(self) -> '_1195.EnergyPerUnitArea':
        '''EnergyPerUnitArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1195.EnergyPerUnitArea.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to EnergyPerUnitArea. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_energy_per_unit_area_small(self) -> '_1196.EnergyPerUnitAreaSmall':
        '''EnergyPerUnitAreaSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1196.EnergyPerUnitAreaSmall.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to EnergyPerUnitAreaSmall. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_energy_small(self) -> '_1197.EnergySmall':
        '''EnergySmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1197.EnergySmall.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to EnergySmall. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_enum(self) -> '_1198.Enum':
        '''Enum: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1198.Enum.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Enum. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_flow_rate(self) -> '_1199.FlowRate':
        '''FlowRate: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1199.FlowRate.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FlowRate. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_force(self) -> '_1200.Force':
        '''Force: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1200.Force.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Force. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_force_per_unit_length(self) -> '_1201.ForcePerUnitLength':
        '''ForcePerUnitLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1201.ForcePerUnitLength.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ForcePerUnitLength. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_force_per_unit_pressure(self) -> '_1202.ForcePerUnitPressure':
        '''ForcePerUnitPressure: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1202.ForcePerUnitPressure.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ForcePerUnitPressure. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_force_per_unit_temperature(self) -> '_1203.ForcePerUnitTemperature':
        '''ForcePerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1203.ForcePerUnitTemperature.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ForcePerUnitTemperature. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_fraction_measurement_base(self) -> '_1204.FractionMeasurementBase':
        '''FractionMeasurementBase: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1204.FractionMeasurementBase.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FractionMeasurementBase. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_frequency(self) -> '_1205.Frequency':
        '''Frequency: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1205.Frequency.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Frequency. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_fuel_consumption_engine(self) -> '_1206.FuelConsumptionEngine':
        '''FuelConsumptionEngine: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1206.FuelConsumptionEngine.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FuelConsumptionEngine. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_fuel_efficiency_vehicle(self) -> '_1207.FuelEfficiencyVehicle':
        '''FuelEfficiencyVehicle: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1207.FuelEfficiencyVehicle.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FuelEfficiencyVehicle. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_gradient(self) -> '_1208.Gradient':
        '''Gradient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1208.Gradient.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Gradient. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_heat_conductivity(self) -> '_1209.HeatConductivity':
        '''HeatConductivity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1209.HeatConductivity.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatConductivity. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_heat_transfer(self) -> '_1210.HeatTransfer':
        '''HeatTransfer: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1210.HeatTransfer.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatTransfer. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_heat_transfer_coefficient_for_plastic_gear_tooth(self) -> '_1211.HeatTransferCoefficientForPlasticGearTooth':
        '''HeatTransferCoefficientForPlasticGearTooth: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1211.HeatTransferCoefficientForPlasticGearTooth.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatTransferCoefficientForPlasticGearTooth. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_heat_transfer_resistance(self) -> '_1212.HeatTransferResistance':
        '''HeatTransferResistance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1212.HeatTransferResistance.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatTransferResistance. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_impulse(self) -> '_1213.Impulse':
        '''Impulse: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1213.Impulse.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Impulse. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_index(self) -> '_1214.Index':
        '''Index: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1214.Index.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Index. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_integer(self) -> '_1215.Integer':
        '''Integer: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1215.Integer.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Integer. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_inverse_short_length(self) -> '_1216.InverseShortLength':
        '''InverseShortLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1216.InverseShortLength.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to InverseShortLength. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_inverse_short_time(self) -> '_1217.InverseShortTime':
        '''InverseShortTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1217.InverseShortTime.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to InverseShortTime. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_jerk(self) -> '_1218.Jerk':
        '''Jerk: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1218.Jerk.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Jerk. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_kinematic_viscosity(self) -> '_1219.KinematicViscosity':
        '''KinematicViscosity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1219.KinematicViscosity.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to KinematicViscosity. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_length_long(self) -> '_1220.LengthLong':
        '''LengthLong: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1220.LengthLong.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthLong. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_length_medium(self) -> '_1221.LengthMedium':
        '''LengthMedium: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1221.LengthMedium.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthMedium. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_length_per_unit_temperature(self) -> '_1222.LengthPerUnitTemperature':
        '''LengthPerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1222.LengthPerUnitTemperature.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthPerUnitTemperature. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_length_short(self) -> '_1223.LengthShort':
        '''LengthShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1223.LengthShort.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthShort. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_length_to_the_fourth(self) -> '_1224.LengthToTheFourth':
        '''LengthToTheFourth: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1224.LengthToTheFourth.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthToTheFourth. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_length_very_long(self) -> '_1225.LengthVeryLong':
        '''LengthVeryLong: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1225.LengthVeryLong.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthVeryLong. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_length_very_short(self) -> '_1226.LengthVeryShort':
        '''LengthVeryShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1226.LengthVeryShort.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthVeryShort. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_length_very_short_per_length_short(self) -> '_1227.LengthVeryShortPerLengthShort':
        '''LengthVeryShortPerLengthShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1227.LengthVeryShortPerLengthShort.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthVeryShortPerLengthShort. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_linear_angular_damping(self) -> '_1228.LinearAngularDamping':
        '''LinearAngularDamping: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1228.LinearAngularDamping.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearAngularDamping. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_linear_angular_stiffness_cross_term(self) -> '_1229.LinearAngularStiffnessCrossTerm':
        '''LinearAngularStiffnessCrossTerm: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1229.LinearAngularStiffnessCrossTerm.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearAngularStiffnessCrossTerm. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_linear_damping(self) -> '_1230.LinearDamping':
        '''LinearDamping: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1230.LinearDamping.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearDamping. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_linear_flexibility(self) -> '_1231.LinearFlexibility':
        '''LinearFlexibility: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1231.LinearFlexibility.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearFlexibility. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_linear_stiffness(self) -> '_1232.LinearStiffness':
        '''LinearStiffness: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1232.LinearStiffness.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearStiffness. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_mass(self) -> '_1233.Mass':
        '''Mass: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1233.Mass.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Mass. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_mass_per_unit_length(self) -> '_1234.MassPerUnitLength':
        '''MassPerUnitLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1234.MassPerUnitLength.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MassPerUnitLength. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_mass_per_unit_time(self) -> '_1235.MassPerUnitTime':
        '''MassPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1235.MassPerUnitTime.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MassPerUnitTime. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_moment_of_inertia(self) -> '_1236.MomentOfInertia':
        '''MomentOfInertia: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1236.MomentOfInertia.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MomentOfInertia. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_moment_of_inertia_per_unit_length(self) -> '_1237.MomentOfInertiaPerUnitLength':
        '''MomentOfInertiaPerUnitLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1237.MomentOfInertiaPerUnitLength.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MomentOfInertiaPerUnitLength. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_moment_per_unit_pressure(self) -> '_1238.MomentPerUnitPressure':
        '''MomentPerUnitPressure: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1238.MomentPerUnitPressure.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MomentPerUnitPressure. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_number(self) -> '_1239.Number':
        '''Number: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1239.Number.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Number. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_percentage(self) -> '_1240.Percentage':
        '''Percentage: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1240.Percentage.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Percentage. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_power(self) -> '_1241.Power':
        '''Power: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1241.Power.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Power. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_power_per_small_area(self) -> '_1242.PowerPerSmallArea':
        '''PowerPerSmallArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1242.PowerPerSmallArea.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerPerSmallArea. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_power_per_unit_time(self) -> '_1243.PowerPerUnitTime':
        '''PowerPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1243.PowerPerUnitTime.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerPerUnitTime. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_power_small(self) -> '_1244.PowerSmall':
        '''PowerSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1244.PowerSmall.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmall. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_power_small_per_area(self) -> '_1245.PowerSmallPerArea':
        '''PowerSmallPerArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1245.PowerSmallPerArea.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerArea. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_power_small_per_unit_area_per_unit_time(self) -> '_1246.PowerSmallPerUnitAreaPerUnitTime':
        '''PowerSmallPerUnitAreaPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1246.PowerSmallPerUnitAreaPerUnitTime.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerUnitAreaPerUnitTime. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_power_small_per_unit_time(self) -> '_1247.PowerSmallPerUnitTime':
        '''PowerSmallPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1247.PowerSmallPerUnitTime.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerUnitTime. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_pressure(self) -> '_1248.Pressure':
        '''Pressure: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1248.Pressure.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Pressure. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_pressure_per_unit_time(self) -> '_1249.PressurePerUnitTime':
        '''PressurePerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1249.PressurePerUnitTime.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PressurePerUnitTime. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_pressure_velocity_product(self) -> '_1250.PressureVelocityProduct':
        '''PressureVelocityProduct: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1250.PressureVelocityProduct.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PressureVelocityProduct. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_pressure_viscosity_coefficient(self) -> '_1251.PressureViscosityCoefficient':
        '''PressureViscosityCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1251.PressureViscosityCoefficient.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PressureViscosityCoefficient. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_price(self) -> '_1252.Price':
        '''Price: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1252.Price.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Price. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_quadratic_angular_damping(self) -> '_1253.QuadraticAngularDamping':
        '''QuadraticAngularDamping: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1253.QuadraticAngularDamping.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to QuadraticAngularDamping. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_quadratic_drag(self) -> '_1254.QuadraticDrag':
        '''QuadraticDrag: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1254.QuadraticDrag.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to QuadraticDrag. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_rescaled_measurement(self) -> '_1255.RescaledMeasurement':
        '''RescaledMeasurement: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1255.RescaledMeasurement.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to RescaledMeasurement. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_rotatum(self) -> '_1256.Rotatum':
        '''Rotatum: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1256.Rotatum.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Rotatum. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_safety_factor(self) -> '_1257.SafetyFactor':
        '''SafetyFactor: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1257.SafetyFactor.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SafetyFactor. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_specific_acoustic_impedance(self) -> '_1258.SpecificAcousticImpedance':
        '''SpecificAcousticImpedance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1258.SpecificAcousticImpedance.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SpecificAcousticImpedance. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_specific_heat(self) -> '_1259.SpecificHeat':
        '''SpecificHeat: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1259.SpecificHeat.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SpecificHeat. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_square_root_of_unit_force_per_unit_area(self) -> '_1260.SquareRootOfUnitForcePerUnitArea':
        '''SquareRootOfUnitForcePerUnitArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1260.SquareRootOfUnitForcePerUnitArea.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SquareRootOfUnitForcePerUnitArea. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_stiffness_per_unit_face_width(self) -> '_1261.StiffnessPerUnitFaceWidth':
        '''StiffnessPerUnitFaceWidth: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1261.StiffnessPerUnitFaceWidth.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to StiffnessPerUnitFaceWidth. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_stress(self) -> '_1262.Stress':
        '''Stress: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1262.Stress.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Stress. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_temperature(self) -> '_1263.Temperature':
        '''Temperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1263.Temperature.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Temperature. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_temperature_difference(self) -> '_1264.TemperatureDifference':
        '''TemperatureDifference: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1264.TemperatureDifference.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TemperatureDifference. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_temperature_per_unit_time(self) -> '_1265.TemperaturePerUnitTime':
        '''TemperaturePerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1265.TemperaturePerUnitTime.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TemperaturePerUnitTime. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_text(self) -> '_1266.Text':
        '''Text: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1266.Text.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Text. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_thermal_contact_coefficient(self) -> '_1267.ThermalContactCoefficient':
        '''ThermalContactCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1267.ThermalContactCoefficient.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ThermalContactCoefficient. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_thermal_expansion_coefficient(self) -> '_1268.ThermalExpansionCoefficient':
        '''ThermalExpansionCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1268.ThermalExpansionCoefficient.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ThermalExpansionCoefficient. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_thermo_elastic_factor(self) -> '_1269.ThermoElasticFactor':
        '''ThermoElasticFactor: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1269.ThermoElasticFactor.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ThermoElasticFactor. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_time(self) -> '_1270.Time':
        '''Time: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1270.Time.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Time. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_time_short(self) -> '_1271.TimeShort':
        '''TimeShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1271.TimeShort.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TimeShort. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_time_very_short(self) -> '_1272.TimeVeryShort':
        '''TimeVeryShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1272.TimeVeryShort.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TimeVeryShort. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_torque(self) -> '_1273.Torque':
        '''Torque: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1273.Torque.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Torque. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_torque_converter_inverse_k(self) -> '_1274.TorqueConverterInverseK':
        '''TorqueConverterInverseK: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1274.TorqueConverterInverseK.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorqueConverterInverseK. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_torque_converter_k(self) -> '_1275.TorqueConverterK':
        '''TorqueConverterK: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1275.TorqueConverterK.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorqueConverterK. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_torque_per_unit_temperature(self) -> '_1276.TorquePerUnitTemperature':
        '''TorquePerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1276.TorquePerUnitTemperature.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorquePerUnitTemperature. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_velocity(self) -> '_1277.Velocity':
        '''Velocity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1277.Velocity.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Velocity. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_velocity_small(self) -> '_1278.VelocitySmall':
        '''VelocitySmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1278.VelocitySmall.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to VelocitySmall. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_viscosity(self) -> '_1279.Viscosity':
        '''Viscosity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1279.Viscosity.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Viscosity. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_voltage(self) -> '_1280.Voltage':
        '''Voltage: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1280.Voltage.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Voltage. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_volume(self) -> '_1281.Volume':
        '''Volume: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1281.Volume.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Volume. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_wear_coefficient(self) -> '_1282.WearCoefficient':
        '''WearCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1282.WearCoefficient.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to WearCoefficient. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None

    @property
    def current_selected_measurement_of_type_yank(self) -> '_1283.Yank':
        '''Yank: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1283.Yank.TYPE not in self.wrapped.CurrentSelectedMeasurement.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Yank. Expected: {}.'.format(self.wrapped.CurrentSelectedMeasurement.__class__.__qualname__))

        return constructor.new_override(self.wrapped.CurrentSelectedMeasurement.__class__)(self.wrapped.CurrentSelectedMeasurement) if self.wrapped.CurrentSelectedMeasurement else None
