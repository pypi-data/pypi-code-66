'''_2312.py

FlexiblePinAssemblySystemDeflection
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2040
from mastapy.system_model.analyses_and_results.static_loads import _6168
from mastapy.system_model.analyses_and_results.power_flows import _3315
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2355, _2299, _2300, _2301,
    _2352, _2337, _2332, _2302,
    _2259, _2357
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'FlexiblePinAssemblySystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAssemblySystemDeflection',)


class FlexiblePinAssemblySystemDeflection(_2357.SpecialisedAssemblySystemDeflection):
    '''FlexiblePinAssemblySystemDeflection

    This is a mastapy class.
    '''

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FlexiblePinAssemblySystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pin_tangential_oscillation_amplitude(self) -> 'float':
        '''float: 'PinTangentialOscillationAmplitude' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PinTangentialOscillationAmplitude

    @property
    def pin_tangential_oscillation_frequency(self) -> 'float':
        '''float: 'PinTangentialOscillationFrequency' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PinTangentialOscillationFrequency

    @property
    def assembly_design(self) -> '_2040.FlexiblePinAssembly':
        '''FlexiblePinAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2040.FlexiblePinAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6168.FlexiblePinAssemblyLoadCase':
        '''FlexiblePinAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6168.FlexiblePinAssemblyLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def power_flow_results(self) -> '_3315.FlexiblePinAssemblyPowerFlow':
        '''FlexiblePinAssemblyPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3315.FlexiblePinAssemblyPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None

    @property
    def pin_analysis(self) -> '_2355.ShaftSystemDeflection':
        '''ShaftSystemDeflection: 'PinAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2355.ShaftSystemDeflection)(self.wrapped.PinAnalysis) if self.wrapped.PinAnalysis else None

    @property
    def spindle_analyses(self) -> '_2355.ShaftSystemDeflection':
        '''ShaftSystemDeflection: 'SpindleAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2355.ShaftSystemDeflection)(self.wrapped.SpindleAnalyses) if self.wrapped.SpindleAnalyses else None

    @property
    def separate_gear_set_details(self) -> '_2299.CylindricalGearSetSystemDeflection':
        '''CylindricalGearSetSystemDeflection: 'SeparateGearSetDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2299.CylindricalGearSetSystemDeflection.TYPE not in self.wrapped.SeparateGearSetDetails.__class__.__mro__:
            raise CastException('Failed to cast separate_gear_set_details to CylindricalGearSetSystemDeflection. Expected: {}.'.format(self.wrapped.SeparateGearSetDetails.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SeparateGearSetDetails.__class__)(self.wrapped.SeparateGearSetDetails) if self.wrapped.SeparateGearSetDetails else None

    @property
    def separate_gear_set_details_of_type_cylindrical_gear_set_system_deflection_timestep(self) -> '_2300.CylindricalGearSetSystemDeflectionTimestep':
        '''CylindricalGearSetSystemDeflectionTimestep: 'SeparateGearSetDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2300.CylindricalGearSetSystemDeflectionTimestep.TYPE not in self.wrapped.SeparateGearSetDetails.__class__.__mro__:
            raise CastException('Failed to cast separate_gear_set_details to CylindricalGearSetSystemDeflectionTimestep. Expected: {}.'.format(self.wrapped.SeparateGearSetDetails.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SeparateGearSetDetails.__class__)(self.wrapped.SeparateGearSetDetails) if self.wrapped.SeparateGearSetDetails else None

    @property
    def separate_gear_set_details_of_type_cylindrical_gear_set_system_deflection_with_ltca_results(self) -> '_2301.CylindricalGearSetSystemDeflectionWithLTCAResults':
        '''CylindricalGearSetSystemDeflectionWithLTCAResults: 'SeparateGearSetDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2301.CylindricalGearSetSystemDeflectionWithLTCAResults.TYPE not in self.wrapped.SeparateGearSetDetails.__class__.__mro__:
            raise CastException('Failed to cast separate_gear_set_details to CylindricalGearSetSystemDeflectionWithLTCAResults. Expected: {}.'.format(self.wrapped.SeparateGearSetDetails.__class__.__qualname__))

        return constructor.new_override(self.wrapped.SeparateGearSetDetails.__class__)(self.wrapped.SeparateGearSetDetails) if self.wrapped.SeparateGearSetDetails else None

    @property
    def flexible_pin_shaft_details(self) -> '_2355.ShaftSystemDeflection':
        '''ShaftSystemDeflection: 'FlexiblePinShaftDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2355.ShaftSystemDeflection)(self.wrapped.FlexiblePinShaftDetails) if self.wrapped.FlexiblePinShaftDetails else None

    @property
    def pin_spindle_fit_analyses(self) -> 'List[_2352.ShaftHubConnectionSystemDeflection]':
        '''List[ShaftHubConnectionSystemDeflection]: 'PinSpindleFitAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PinSpindleFitAnalyses, constructor.new(_2352.ShaftHubConnectionSystemDeflection))
        return value

    @property
    def observed_pin_stiffness_reporters(self) -> 'List[_2337.ObservedPinStiffnessReporter]':
        '''List[ObservedPinStiffnessReporter]: 'ObservedPinStiffnessReporters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ObservedPinStiffnessReporters, constructor.new(_2337.ObservedPinStiffnessReporter))
        return value

    @property
    def load_sharing_factor_reporters(self) -> 'List[_2332.LoadSharingFactorReporter]':
        '''List[LoadSharingFactorReporter]: 'LoadSharingFactorReporters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadSharingFactorReporters, constructor.new(_2332.LoadSharingFactorReporter))
        return value

    @property
    def planet_gear_system_deflections(self) -> 'List[_2302.CylindricalGearSystemDeflection]':
        '''List[CylindricalGearSystemDeflection]: 'PlanetGearSystemDeflections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetGearSystemDeflections, constructor.new(_2302.CylindricalGearSystemDeflection))
        return value

    @property
    def flexible_pin_fit_details(self) -> 'List[_2352.ShaftHubConnectionSystemDeflection]':
        '''List[ShaftHubConnectionSystemDeflection]: 'FlexiblePinFitDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinFitDetails, constructor.new(_2352.ShaftHubConnectionSystemDeflection))
        return value

    @property
    def bearing_static_analyses(self) -> 'List[_2259.BearingSystemDeflection]':
        '''List[BearingSystemDeflection]: 'BearingStaticAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BearingStaticAnalyses, constructor.new(_2259.BearingSystemDeflection))
        return value
