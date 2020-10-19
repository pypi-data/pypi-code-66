'''_2515.py

TorqueConverterPumpCompoundSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2186
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2380
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2439
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'TorqueConverterPumpCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpCompoundSystemDeflection',)


class TorqueConverterPumpCompoundSystemDeflection(_2439.CouplingHalfCompoundSystemDeflection):
    '''TorqueConverterPumpCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_PUMP_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2186.TorqueConverterPump':
        '''TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2186.TorqueConverterPump)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_2380.TorqueConverterPumpSystemDeflection]':
        '''List[TorqueConverterPumpSystemDeflection]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_2380.TorqueConverterPumpSystemDeflection))
        return value

    @property
    def component_system_deflection_load_cases(self) -> 'List[_2380.TorqueConverterPumpSystemDeflection]':
        '''List[TorqueConverterPumpSystemDeflection]: 'ComponentSystemDeflectionLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionLoadCases, constructor.new(_2380.TorqueConverterPumpSystemDeflection))
        return value
