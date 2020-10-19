'''_3483.py

SpringDamperCompoundPowerFlow
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2178
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _3363
from mastapy.system_model.analyses_and_results.power_flows.compound import _3424
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'SpringDamperCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperCompoundPowerFlow',)


class SpringDamperCompoundPowerFlow(_3424.CouplingCompoundPowerFlow):
    '''SpringDamperCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2178.SpringDamper':
        '''SpringDamper: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2178.SpringDamper)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2178.SpringDamper':
        '''SpringDamper: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2178.SpringDamper)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_3363.SpringDamperPowerFlow]':
        '''List[SpringDamperPowerFlow]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3363.SpringDamperPowerFlow))
        return value

    @property
    def assembly_power_flow_load_cases(self) -> 'List[_3363.SpringDamperPowerFlow]':
        '''List[SpringDamperPowerFlow]: 'AssemblyPowerFlowLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyPowerFlowLoadCases, constructor.new(_3363.SpringDamperPowerFlow))
        return value
