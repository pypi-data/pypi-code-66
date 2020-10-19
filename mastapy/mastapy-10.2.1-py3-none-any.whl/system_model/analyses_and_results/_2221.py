'''_2221.py

SystemDeflectionAnalysis
'''


from mastapy.system_model.analyses_and_results.static_loads import (
    _6263, _6264, _6266, _6210,
    _6209, _6108, _6121, _6120,
    _6126, _6125, _6139, _6138,
    _6141, _6142, _6219, _6225,
    _6223, _6221, _6235, _6234,
    _6246, _6245, _6247, _6248,
    _6252, _6253, _6254, _6140,
    _6107, _6122, _6135, _6190,
    _6211, _6222, _6227, _6110,
    _6128, _6166, _6238, _6115,
    _6132, _6102, _6145, _6186,
    _6192, _6195, _6198, _6231,
    _6241, _6262, _6265, _6172,
    _6208, _6119, _6124, _6137,
    _6233, _6251, _6098, _6099,
    _6106, _6118, _6117, _6123,
    _6136, _6151, _6164, _6168,
    _6105, _6176, _6188, _6200,
    _6201, _6203, _6205, _6207,
    _6214, _6217, _6218, _6224,
    _6228, _6259, _6260, _6226,
    _6127, _6129, _6165, _6167,
    _6101, _6103, _6109, _6111,
    _6112, _6113, _6114, _6116,
    _6130, _6134, _6143, _6147,
    _6148, _6170, _6175, _6185,
    _6187, _6191, _6193, _6194,
    _6196, _6197, _6199, _6212,
    _6230, _6232, _6237, _6239,
    _6240, _6242, _6243, _6244,
    _6261
)
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2388, _2392, _2391, _2342,
    _2341, _2261, _2274, _2273,
    _2280, _2279, _2292, _2291,
    _2295, _2294, _2347, _2352,
    _2350, _2348, _2363, _2362,
    _2375, _2372, _2373, _2374,
    _2381, _2380, _2382, _2293,
    _2260, _2275, _2288, _2321,
    _2343, _2349, _2356, _2262,
    _2281, _2309, _2364, _2267,
    _2285, _2255, _2298, _2317,
    _2322, _2325, _2328, _2358,
    _2367, _2387, _2390, _2313,
    _2340, _2272, _2278, _2290,
    _2361, _2379, _2253, _2254,
    _2259, _2271, _2270, _2276,
    _2289, _2306, _2307, _2312,
    _2258, _2316, _2320, _2333,
    _2334, _2336, _2338, _2339,
    _2344, _2345, _2346, _2351,
    _2357, _2385, _2386, _2355,
    _2283, _2282, _2311, _2310,
    _2257, _2256, _2264, _2263,
    _2265, _2266, _2269, _2268,
    _2287, _2286, _2304, _2301,
    _2305, _2315, _2314, _2319,
    _2318, _2324, _2323, _2327,
    _2326, _2330, _2329, _2360,
    _2359, _2366, _2365, _2369,
    _2368, _2370, _2371, _2389
)
from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import (
    _2137, _2138, _2105, _2106,
    _2112, _2113, _2097, _2098,
    _2099, _2100, _2101, _2102,
    _2103, _2104, _2107, _2108,
    _2109, _2110, _2111, _2114,
    _2116, _2118, _2119, _2120,
    _2121, _2122, _2123, _2124,
    _2125, _2126, _2127, _2128,
    _2129, _2130, _2131, _2132,
    _2133, _2134, _2135, _2136
)
from mastapy.system_model.part_model.couplings import (
    _2167, _2168, _2156, _2158,
    _2159, _2161, _2162, _2163,
    _2164, _2165, _2166, _2169,
    _2177, _2175, _2176, _2178,
    _2179, _2180, _2182, _2183,
    _2184, _2185, _2186, _2188
)
from mastapy.system_model.connections_and_sockets import (
    _1879, _1874, _1875, _1878,
    _1887, _1890, _1894, _1898
)
from mastapy.system_model.connections_and_sockets.gears import (
    _1904, _1908, _1914, _1928,
    _1906, _1910, _1902, _1912,
    _1918, _1921, _1922, _1923,
    _1926, _1930, _1932, _1934,
    _1916
)
from mastapy.system_model.connections_and_sockets.couplings import (
    _1942, _1936, _1938, _1940,
    _1944, _1946
)
from mastapy.system_model.part_model import (
    _2024, _2025, _2028, _2030,
    _2031, _2032, _2035, _2036,
    _2039, _2040, _2023, _2041,
    _2044, _2048, _2049, _2050,
    _2052, _2054, _2055, _2057,
    _2058, _2060, _2062, _2063,
    _2064
)
from mastapy.system_model.part_model.shaft_model import _2067
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results import _2198

_WORM_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'WormGearSetLoadCase')
_ZEROL_BEVEL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ZerolBevelGearLoadCase')
_ZEROL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ZerolBevelGearSetLoadCase')
_PART_TO_PART_SHEAR_COUPLING_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PartToPartShearCouplingLoadCase')
_PART_TO_PART_SHEAR_COUPLING_HALF_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PartToPartShearCouplingHalfLoadCase')
_BELT_DRIVE_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BeltDriveLoadCase')
_CLUTCH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ClutchLoadCase')
_CLUTCH_HALF_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ClutchHalfLoadCase')
_CONCEPT_COUPLING_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConceptCouplingLoadCase')
_CONCEPT_COUPLING_HALF_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConceptCouplingHalfLoadCase')
_COUPLING_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CouplingLoadCase')
_COUPLING_HALF_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CouplingHalfLoadCase')
_CVT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CVTLoadCase')
_CVT_PULLEY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CVTPulleyLoadCase')
_PULLEY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PulleyLoadCase')
_SHAFT_HUB_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ShaftHubConnectionLoadCase')
_ROLLING_RING_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'RollingRingLoadCase')
_ROLLING_RING_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'RollingRingAssemblyLoadCase')
_SPRING_DAMPER_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpringDamperLoadCase')
_SPRING_DAMPER_HALF_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpringDamperHalfLoadCase')
_SYNCHRONISER_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SynchroniserLoadCase')
_SYNCHRONISER_HALF_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SynchroniserHalfLoadCase')
_SYNCHRONISER_PART_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SynchroniserPartLoadCase')
_SYNCHRONISER_SLEEVE_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SynchroniserSleeveLoadCase')
_TORQUE_CONVERTER_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'TorqueConverterLoadCase')
_TORQUE_CONVERTER_PUMP_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'TorqueConverterPumpLoadCase')
_TORQUE_CONVERTER_TURBINE_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'TorqueConverterTurbineLoadCase')
_CVT_BELT_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CVTBeltConnectionLoadCase')
_BELT_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BeltConnectionLoadCase')
_COAXIAL_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CoaxialConnectionLoadCase')
_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConnectionLoadCase')
_INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'InterMountableComponentConnectionLoadCase')
_PLANETARY_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PlanetaryConnectionLoadCase')
_ROLLING_RING_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'RollingRingConnectionLoadCase')
_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ShaftToMountableComponentConnectionLoadCase')
_BEVEL_DIFFERENTIAL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelDifferentialGearMeshLoadCase')
_CONCEPT_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConceptGearMeshLoadCase')
_FACE_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'FaceGearMeshLoadCase')
_STRAIGHT_BEVEL_DIFF_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelDiffGearMeshLoadCase')
_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelGearMeshLoadCase')
_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConicalGearMeshLoadCase')
_AGMA_GLEASON_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AGMAGleasonConicalGearMeshLoadCase')
_CYLINDRICAL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CylindricalGearMeshLoadCase')
_HYPOID_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HypoidGearMeshLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidConicalGearMeshLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidHypoidGearMeshLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase')
_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpiralBevelGearMeshLoadCase')
_STRAIGHT_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelGearMeshLoadCase')
_WORM_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'WormGearMeshLoadCase')
_ZEROL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ZerolBevelGearMeshLoadCase')
_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'GearMeshLoadCase')
_PART_TO_PART_SHEAR_COUPLING_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PartToPartShearCouplingConnectionLoadCase')
_CLUTCH_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ClutchConnectionLoadCase')
_CONCEPT_COUPLING_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConceptCouplingConnectionLoadCase')
_COUPLING_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CouplingConnectionLoadCase')
_SPRING_DAMPER_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpringDamperConnectionLoadCase')
_TORQUE_CONVERTER_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'TorqueConverterConnectionLoadCase')
_ABSTRACT_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AbstractAssemblyLoadCase')
_ABSTRACT_SHAFT_OR_HOUSING_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AbstractShaftOrHousingLoadCase')
_BEARING_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BearingLoadCase')
_BOLT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BoltLoadCase')
_BOLTED_JOINT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BoltedJointLoadCase')
_COMPONENT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ComponentLoadCase')
_CONNECTOR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConnectorLoadCase')
_DATUM_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'DatumLoadCase')
_EXTERNAL_CAD_MODEL_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ExternalCADModelLoadCase')
_FLEXIBLE_PIN_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'FlexiblePinAssemblyLoadCase')
_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AssemblyLoadCase')
_GUIDE_DXF_MODEL_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'GuideDxfModelLoadCase')
_IMPORTED_FE_COMPONENT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ImportedFEComponentLoadCase')
_MASS_DISC_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'MassDiscLoadCase')
_MEASUREMENT_COMPONENT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'MeasurementComponentLoadCase')
_MOUNTABLE_COMPONENT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'MountableComponentLoadCase')
_OIL_SEAL_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'OilSealLoadCase')
_PART_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PartLoadCase')
_PLANET_CARRIER_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PlanetCarrierLoadCase')
_POINT_LOAD_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PointLoadLoadCase')
_POWER_LOAD_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PowerLoadLoadCase')
_ROOT_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'RootAssemblyLoadCase')
_SPECIALISED_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpecialisedAssemblyLoadCase')
_UNBALANCED_MASS_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'UnbalancedMassLoadCase')
_VIRTUAL_COMPONENT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'VirtualComponentLoadCase')
_SHAFT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ShaftLoadCase')
_CONCEPT_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConceptGearLoadCase')
_CONCEPT_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConceptGearSetLoadCase')
_FACE_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'FaceGearLoadCase')
_FACE_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'FaceGearSetLoadCase')
_AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AGMAGleasonConicalGearLoadCase')
_AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AGMAGleasonConicalGearSetLoadCase')
_BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelDifferentialGearLoadCase')
_BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelDifferentialGearSetLoadCase')
_BEVEL_DIFFERENTIAL_PLANET_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelDifferentialPlanetGearLoadCase')
_BEVEL_DIFFERENTIAL_SUN_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelDifferentialSunGearLoadCase')
_BEVEL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelGearLoadCase')
_BEVEL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelGearSetLoadCase')
_CONICAL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConicalGearLoadCase')
_CONICAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConicalGearSetLoadCase')
_CYLINDRICAL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CylindricalGearLoadCase')
_CYLINDRICAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CylindricalGearSetLoadCase')
_CYLINDRICAL_PLANET_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CylindricalPlanetGearLoadCase')
_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'GearLoadCase')
_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'GearSetLoadCase')
_HYPOID_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HypoidGearLoadCase')
_HYPOID_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HypoidGearSetLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidConicalGearLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidConicalGearSetLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidHypoidGearLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidHypoidGearSetLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidSpiralBevelGearLoadCase')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase')
_PLANETARY_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PlanetaryGearSetLoadCase')
_SPIRAL_BEVEL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpiralBevelGearLoadCase')
_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpiralBevelGearSetLoadCase')
_STRAIGHT_BEVEL_DIFF_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelDiffGearLoadCase')
_STRAIGHT_BEVEL_DIFF_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelDiffGearSetLoadCase')
_STRAIGHT_BEVEL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelGearLoadCase')
_STRAIGHT_BEVEL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelGearSetLoadCase')
_STRAIGHT_BEVEL_PLANET_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelPlanetGearLoadCase')
_STRAIGHT_BEVEL_SUN_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StraightBevelSunGearLoadCase')
_WORM_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'WormGearLoadCase')
_ZEROL_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ZerolBevelGear')
_ZEROL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ZerolBevelGearSet')
_CONCEPT_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConceptGear')
_CONCEPT_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConceptGearSet')
_FACE_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'FaceGear')
_FACE_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'FaceGearSet')
_AGMA_GLEASON_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'AGMAGleasonConicalGear')
_AGMA_GLEASON_CONICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'AGMAGleasonConicalGearSet')
_BEVEL_DIFFERENTIAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialGear')
_BEVEL_DIFFERENTIAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialGearSet')
_BEVEL_DIFFERENTIAL_PLANET_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialPlanetGear')
_BEVEL_DIFFERENTIAL_SUN_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialSunGear')
_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelGear')
_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelGearSet')
_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConicalGear')
_CONICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConicalGearSet')
_CYLINDRICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalGear')
_CYLINDRICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalGearSet')
_CYLINDRICAL_PLANET_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'CylindricalPlanetGear')
_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'Gear')
_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'GearSet')
_HYPOID_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'HypoidGear')
_HYPOID_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'HypoidGearSet')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidConicalGear')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidConicalGearSet')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidHypoidGear')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidHypoidGearSet')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidSpiralBevelGear')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidSpiralBevelGearSet')
_PLANETARY_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'PlanetaryGearSet')
_SPIRAL_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'SpiralBevelGear')
_SPIRAL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'SpiralBevelGearSet')
_STRAIGHT_BEVEL_DIFF_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelDiffGear')
_STRAIGHT_BEVEL_DIFF_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelDiffGearSet')
_STRAIGHT_BEVEL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelGear')
_STRAIGHT_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelGearSet')
_STRAIGHT_BEVEL_PLANET_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelPlanetGear')
_STRAIGHT_BEVEL_SUN_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelSunGear')
_WORM_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'WormGear')
_WORM_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'WormGearSet')
_PART_TO_PART_SHEAR_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'PartToPartShearCoupling')
_PART_TO_PART_SHEAR_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'PartToPartShearCouplingHalf')
_BELT_DRIVE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'BeltDrive')
_CLUTCH = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Clutch')
_CLUTCH_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ClutchHalf')
_CONCEPT_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ConceptCoupling')
_CONCEPT_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ConceptCouplingHalf')
_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Coupling')
_COUPLING_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CouplingHalf')
_CVT = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CVT')
_CVT_PULLEY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'CVTPulley')
_PULLEY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Pulley')
_SHAFT_HUB_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'ShaftHubConnection')
_ROLLING_RING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'RollingRing')
_ROLLING_RING_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'RollingRingAssembly')
_SPRING_DAMPER = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SpringDamper')
_SPRING_DAMPER_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SpringDamperHalf')
_SYNCHRONISER = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Synchroniser')
_SYNCHRONISER_HALF = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserHalf')
_SYNCHRONISER_PART = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserPart')
_SYNCHRONISER_SLEEVE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'SynchroniserSleeve')
_TORQUE_CONVERTER = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverter')
_TORQUE_CONVERTER_PUMP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverterPump')
_TORQUE_CONVERTER_TURBINE = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'TorqueConverterTurbine')
_CVT_BELT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'CVTBeltConnection')
_BELT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'BeltConnection')
_COAXIAL_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'CoaxialConnection')
_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'Connection')
_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'InterMountableComponentConnection')
_PLANETARY_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'PlanetaryConnection')
_ROLLING_RING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'RollingRingConnection')
_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'ShaftToMountableComponentConnection')
_BEVEL_DIFFERENTIAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'BevelDifferentialGearMesh')
_CONCEPT_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ConceptGearMesh')
_FACE_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'FaceGearMesh')
_STRAIGHT_BEVEL_DIFF_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'StraightBevelDiffGearMesh')
_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'BevelGearMesh')
_CONICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ConicalGearMesh')
_AGMA_GLEASON_CONICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'AGMAGleasonConicalGearMesh')
_CYLINDRICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'CylindricalGearMesh')
_HYPOID_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'HypoidGearMesh')
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergCycloPalloidConicalGearMesh')
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergCycloPalloidHypoidGearMesh')
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'KlingelnbergCycloPalloidSpiralBevelGearMesh')
_SPIRAL_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'SpiralBevelGearMesh')
_STRAIGHT_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'StraightBevelGearMesh')
_WORM_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'WormGearMesh')
_ZEROL_BEVEL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ZerolBevelGearMesh')
_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'GearMesh')
_PART_TO_PART_SHEAR_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'PartToPartShearCouplingConnection')
_CLUTCH_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'ClutchConnection')
_CONCEPT_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'ConceptCouplingConnection')
_COUPLING_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'CouplingConnection')
_SPRING_DAMPER_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'SpringDamperConnection')
_TORQUE_CONVERTER_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'TorqueConverterConnection')
_ABSTRACT_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractAssembly')
_ABSTRACT_SHAFT_OR_HOUSING = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'AbstractShaftOrHousing')
_BEARING = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bearing')
_BOLT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bolt')
_BOLTED_JOINT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'BoltedJoint')
_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Component')
_CONNECTOR = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Connector')
_DATUM = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Datum')
_EXTERNAL_CAD_MODEL = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'ExternalCADModel')
_FLEXIBLE_PIN_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'FlexiblePinAssembly')
_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Assembly')
_GUIDE_DXF_MODEL = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'GuideDxfModel')
_IMPORTED_FE_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'ImportedFEComponent')
_MASS_DISC = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MassDisc')
_MEASUREMENT_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MeasurementComponent')
_MOUNTABLE_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MountableComponent')
_OIL_SEAL = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'OilSeal')
_PART = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Part')
_PLANET_CARRIER = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PlanetCarrier')
_POINT_LOAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PointLoad')
_POWER_LOAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PowerLoad')
_ROOT_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'RootAssembly')
_SPECIALISED_ASSEMBLY = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'SpecialisedAssembly')
_UNBALANCED_MASS = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'UnbalancedMass')
_VIRTUAL_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'VirtualComponent')
_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ShaftModel', 'Shaft')
_SYSTEM_DEFLECTION_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'SystemDeflectionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SystemDeflectionAnalysis',)


class SystemDeflectionAnalysis(_2198.SingleAnalysis):
    '''SystemDeflectionAnalysis

    This is a mastapy class.
    '''

    TYPE = _SYSTEM_DEFLECTION_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SystemDeflectionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def results_for_worm_gear_set_load_case(self, design_entity_analysis: '_6263.WormGearSetLoadCase') -> '_2388.WormGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_zerol_bevel_gear(self, design_entity: '_2137.ZerolBevelGear') -> '_2392.ZerolBevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_load_case(self, design_entity_analysis: '_6264.ZerolBevelGearLoadCase') -> '_2392.ZerolBevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set(self, design_entity: '_2138.ZerolBevelGearSet') -> '_2391.ZerolBevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_set_load_case(self, design_entity_analysis: '_6266.ZerolBevelGearSetLoadCase') -> '_2391.ZerolBevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling(self, design_entity: '_2167.PartToPartShearCoupling') -> '_2342.PartToPartShearCouplingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_load_case(self, design_entity_analysis: '_6210.PartToPartShearCouplingLoadCase') -> '_2342.PartToPartShearCouplingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half(self, design_entity: '_2168.PartToPartShearCouplingHalf') -> '_2341.PartToPartShearCouplingHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_HALF](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_half_load_case(self, design_entity_analysis: '_6209.PartToPartShearCouplingHalfLoadCase') -> '_2341.PartToPartShearCouplingHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_HALF_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_belt_drive(self, design_entity: '_2156.BeltDrive') -> '_2261.BeltDriveSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BeltDriveSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BELT_DRIVE](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_belt_drive_load_case(self, design_entity_analysis: '_6108.BeltDriveLoadCase') -> '_2261.BeltDriveSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BeltDriveSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BELT_DRIVE_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_clutch(self, design_entity: '_2158.Clutch') -> '_2274.ClutchSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_clutch_load_case(self, design_entity_analysis: '_6121.ClutchLoadCase') -> '_2274.ClutchSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_clutch_half(self, design_entity: '_2159.ClutchHalf') -> '_2273.ClutchHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_clutch_half_load_case(self, design_entity_analysis: '_6120.ClutchHalfLoadCase') -> '_2273.ClutchHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_HALF_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_concept_coupling(self, design_entity: '_2161.ConceptCoupling') -> '_2280.ConceptCouplingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_concept_coupling_load_case(self, design_entity_analysis: '_6126.ConceptCouplingLoadCase') -> '_2280.ConceptCouplingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_concept_coupling_half(self, design_entity: '_2162.ConceptCouplingHalf') -> '_2279.ConceptCouplingHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_HALF](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_concept_coupling_half_load_case(self, design_entity_analysis: '_6125.ConceptCouplingHalfLoadCase') -> '_2279.ConceptCouplingHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_HALF_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_coupling(self, design_entity: '_2163.Coupling') -> '_2292.CouplingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_coupling_load_case(self, design_entity_analysis: '_6139.CouplingLoadCase') -> '_2292.CouplingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_coupling_half(self, design_entity: '_2164.CouplingHalf') -> '_2291.CouplingHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_HALF](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_coupling_half_load_case(self, design_entity_analysis: '_6138.CouplingHalfLoadCase') -> '_2291.CouplingHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_HALF_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_cvt(self, design_entity: '_2165.CVT') -> '_2295.CVTSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CVT](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_cvt_load_case(self, design_entity_analysis: '_6141.CVTLoadCase') -> '_2295.CVTSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CVT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_cvt_pulley(self, design_entity: '_2166.CVTPulley') -> '_2294.CVTPulleySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTPulleySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CVT_PULLEY](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_cvt_pulley_load_case(self, design_entity_analysis: '_6142.CVTPulleyLoadCase') -> '_2294.CVTPulleySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTPulleySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CVT_PULLEY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_pulley(self, design_entity: '_2169.Pulley') -> '_2347.PulleySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PulleySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_PULLEY](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_pulley_load_case(self, design_entity_analysis: '_6219.PulleyLoadCase') -> '_2347.PulleySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PulleySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_PULLEY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_shaft_hub_connection(self, design_entity: '_2177.ShaftHubConnection') -> '_2352.ShaftHubConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftHubConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT_HUB_CONNECTION](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_shaft_hub_connection_load_case(self, design_entity_analysis: '_6225.ShaftHubConnectionLoadCase') -> '_2352.ShaftHubConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftHubConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT_HUB_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_rolling_ring(self, design_entity: '_2175.RollingRing') -> '_2350.RollingRingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_rolling_ring_load_case(self, design_entity_analysis: '_6223.RollingRingLoadCase') -> '_2350.RollingRingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_rolling_ring_assembly(self, design_entity: '_2176.RollingRingAssembly') -> '_2348.RollingRingAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_ASSEMBLY](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_rolling_ring_assembly_load_case(self, design_entity_analysis: '_6221.RollingRingAssemblyLoadCase') -> '_2348.RollingRingAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_ASSEMBLY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_spring_damper(self, design_entity: '_2178.SpringDamper') -> '_2363.SpringDamperSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_spring_damper_load_case(self, design_entity_analysis: '_6235.SpringDamperLoadCase') -> '_2363.SpringDamperSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_spring_damper_half(self, design_entity: '_2179.SpringDamperHalf') -> '_2362.SpringDamperHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_HALF](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_spring_damper_half_load_case(self, design_entity_analysis: '_6234.SpringDamperHalfLoadCase') -> '_2362.SpringDamperHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_HALF_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_synchroniser(self, design_entity: '_2180.Synchroniser') -> '_2375.SynchroniserSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_synchroniser_load_case(self, design_entity_analysis: '_6246.SynchroniserLoadCase') -> '_2375.SynchroniserSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_synchroniser_half(self, design_entity: '_2182.SynchroniserHalf') -> '_2372.SynchroniserHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_synchroniser_half_load_case(self, design_entity_analysis: '_6245.SynchroniserHalfLoadCase') -> '_2372.SynchroniserHalfSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserHalfSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_HALF_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_synchroniser_part(self, design_entity: '_2183.SynchroniserPart') -> '_2373.SynchroniserPartSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserPartSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_synchroniser_part_load_case(self, design_entity_analysis: '_6247.SynchroniserPartLoadCase') -> '_2373.SynchroniserPartSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserPartSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_PART_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_synchroniser_sleeve(self, design_entity: '_2184.SynchroniserSleeve') -> '_2374.SynchroniserSleeveSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSleeveSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_SLEEVE](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_synchroniser_sleeve_load_case(self, design_entity_analysis: '_6248.SynchroniserSleeveLoadCase') -> '_2374.SynchroniserSleeveSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SynchroniserSleeveSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SYNCHRONISER_SLEEVE_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_torque_converter(self, design_entity: '_2185.TorqueConverter') -> '_2381.TorqueConverterSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_torque_converter_load_case(self, design_entity_analysis: '_6252.TorqueConverterLoadCase') -> '_2381.TorqueConverterSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_torque_converter_pump(self, design_entity: '_2186.TorqueConverterPump') -> '_2380.TorqueConverterPumpSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterPumpSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_PUMP](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_torque_converter_pump_load_case(self, design_entity_analysis: '_6253.TorqueConverterPumpLoadCase') -> '_2380.TorqueConverterPumpSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterPumpSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_PUMP_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_torque_converter_turbine(self, design_entity: '_2188.TorqueConverterTurbine') -> '_2382.TorqueConverterTurbineSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterTurbineSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_TURBINE](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_torque_converter_turbine_load_case(self, design_entity_analysis: '_6254.TorqueConverterTurbineLoadCase') -> '_2382.TorqueConverterTurbineSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterTurbineSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_TURBINE_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_cvt_belt_connection(self, design_entity: '_1879.CVTBeltConnection') -> '_2293.CVTBeltConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTBeltConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CVT_BELT_CONNECTION](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_cvt_belt_connection_load_case(self, design_entity_analysis: '_6140.CVTBeltConnectionLoadCase') -> '_2293.CVTBeltConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CVTBeltConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CVT_BELT_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_belt_connection(self, design_entity: '_1874.BeltConnection') -> '_2260.BeltConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BeltConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_belt_connection_load_case(self, design_entity_analysis: '_6107.BeltConnectionLoadCase') -> '_2260.BeltConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BeltConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BELT_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_coaxial_connection(self, design_entity: '_1875.CoaxialConnection') -> '_2275.CoaxialConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_COAXIAL_CONNECTION](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_coaxial_connection_load_case(self, design_entity_analysis: '_6122.CoaxialConnectionLoadCase') -> '_2275.CoaxialConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_COAXIAL_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_connection(self, design_entity: '_1878.Connection') -> '_2288.ConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTION](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_connection_load_case(self, design_entity_analysis: '_6135.ConnectionLoadCase') -> '_2288.ConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection(self, design_entity: '_1887.InterMountableComponentConnection') -> '_2321.InterMountableComponentConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.InterMountableComponentConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_INTER_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_inter_mountable_component_connection_load_case(self, design_entity_analysis: '_6190.InterMountableComponentConnectionLoadCase') -> '_2321.InterMountableComponentConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.InterMountableComponentConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_planetary_connection(self, design_entity: '_1890.PlanetaryConnection') -> '_2343.PlanetaryConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PlanetaryConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_PLANETARY_CONNECTION](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_planetary_connection_load_case(self, design_entity_analysis: '_6211.PlanetaryConnectionLoadCase') -> '_2343.PlanetaryConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PlanetaryConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_PLANETARY_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_rolling_ring_connection(self, design_entity: '_1894.RollingRingConnection') -> '_2349.RollingRingConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_CONNECTION](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_rolling_ring_connection_load_case(self, design_entity_analysis: '_6222.RollingRingConnectionLoadCase') -> '_2349.RollingRingConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RollingRingConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ROLLING_RING_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection(self, design_entity: '_1898.ShaftToMountableComponentConnection') -> '_2356.ShaftToMountableComponentConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftToMountableComponentConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_shaft_to_mountable_component_connection_load_case(self, design_entity_analysis: '_6227.ShaftToMountableComponentConnectionLoadCase') -> '_2356.ShaftToMountableComponentConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftToMountableComponentConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh(self, design_entity: '_1904.BevelDifferentialGearMesh') -> '_2262.BevelDifferentialGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bevel_differential_gear_mesh_load_case(self, design_entity_analysis: '_6110.BevelDifferentialGearMeshLoadCase') -> '_2262.BevelDifferentialGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_concept_gear_mesh(self, design_entity: '_1908.ConceptGearMesh') -> '_2281.ConceptGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_concept_gear_mesh_load_case(self, design_entity_analysis: '_6128.ConceptGearMeshLoadCase') -> '_2281.ConceptGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_face_gear_mesh(self, design_entity: '_1914.FaceGearMesh') -> '_2309.FaceGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_face_gear_mesh_load_case(self, design_entity_analysis: '_6166.FaceGearMeshLoadCase') -> '_2309.FaceGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1928.StraightBevelDiffGearMesh') -> '_2364.StraightBevelDiffGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_mesh_load_case(self, design_entity_analysis: '_6238.StraightBevelDiffGearMeshLoadCase') -> '_2364.StraightBevelDiffGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bevel_gear_mesh(self, design_entity: '_1906.BevelGearMesh') -> '_2267.BevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6115.BevelGearMeshLoadCase') -> '_2267.BevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_conical_gear_mesh(self, design_entity: '_1910.ConicalGearMesh') -> '_2285.ConicalGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_conical_gear_mesh_load_case(self, design_entity_analysis: '_6132.ConicalGearMeshLoadCase') -> '_2285.ConicalGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1902.AGMAGleasonConicalGearMesh') -> '_2255.AGMAGleasonConicalGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_mesh_load_case(self, design_entity_analysis: '_6102.AGMAGleasonConicalGearMeshLoadCase') -> '_2255.AGMAGleasonConicalGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh(self, design_entity: '_1912.CylindricalGearMesh') -> '_2298.CylindricalGearMeshSystemDeflectionWithLTCAResults':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearMeshSystemDeflectionWithLTCAResults
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_cylindrical_gear_mesh_load_case(self, design_entity_analysis: '_6145.CylindricalGearMeshLoadCase') -> '_2298.CylindricalGearMeshSystemDeflectionWithLTCAResults':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearMeshSystemDeflectionWithLTCAResults
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh(self, design_entity: '_1918.HypoidGearMesh') -> '_2317.HypoidGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6186.HypoidGearMeshLoadCase') -> '_2317.HypoidGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1921.KlingelnbergCycloPalloidConicalGearMesh') -> '_2322.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(self, design_entity_analysis: '_6192.KlingelnbergCycloPalloidConicalGearMeshLoadCase') -> '_2322.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1922.KlingelnbergCycloPalloidHypoidGearMesh') -> '_2325.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(self, design_entity_analysis: '_6195.KlingelnbergCycloPalloidHypoidGearMeshLoadCase') -> '_2325.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1923.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> '_2328.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6198.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase') -> '_2328.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh(self, design_entity: '_1926.SpiralBevelGearMesh') -> '_2358.SpiralBevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6231.SpiralBevelGearMeshLoadCase') -> '_2358.SpiralBevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh(self, design_entity: '_1930.StraightBevelGearMesh') -> '_2367.StraightBevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_straight_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6241.StraightBevelGearMeshLoadCase') -> '_2367.StraightBevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_worm_gear_mesh(self, design_entity: '_1932.WormGearMesh') -> '_2387.WormGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_worm_gear_mesh_load_case(self, design_entity_analysis: '_6262.WormGearMeshLoadCase') -> '_2387.WormGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh(self, design_entity: '_1934.ZerolBevelGearMesh') -> '_2390.ZerolBevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_zerol_bevel_gear_mesh_load_case(self, design_entity_analysis: '_6265.ZerolBevelGearMeshLoadCase') -> '_2390.ZerolBevelGearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ZEROL_BEVEL_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_gear_mesh(self, design_entity: '_1916.GearMesh') -> '_2313.GearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_MESH](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_gear_mesh_load_case(self, design_entity_analysis: '_6172.GearMeshLoadCase') -> '_2313.GearMeshSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearMeshSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_MESH_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection(self, design_entity: '_1942.PartToPartShearCouplingConnection') -> '_2340.PartToPartShearCouplingConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_part_to_part_shear_coupling_connection_load_case(self, design_entity_analysis: '_6208.PartToPartShearCouplingConnectionLoadCase') -> '_2340.PartToPartShearCouplingConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_PART_TO_PART_SHEAR_COUPLING_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_clutch_connection(self, design_entity: '_1936.ClutchConnection') -> '_2272.ClutchConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_clutch_connection_load_case(self, design_entity_analysis: '_6119.ClutchConnectionLoadCase') -> '_2272.ClutchConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ClutchConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CLUTCH_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_concept_coupling_connection(self, design_entity: '_1938.ConceptCouplingConnection') -> '_2278.ConceptCouplingConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_concept_coupling_connection_load_case(self, design_entity_analysis: '_6124.ConceptCouplingConnectionLoadCase') -> '_2278.ConceptCouplingConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptCouplingConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_COUPLING_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_coupling_connection(self, design_entity: '_1940.CouplingConnection') -> '_2290.CouplingConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_coupling_connection_load_case(self, design_entity_analysis: '_6137.CouplingConnectionLoadCase') -> '_2290.CouplingConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CouplingConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_COUPLING_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_spring_damper_connection(self, design_entity: '_1944.SpringDamperConnection') -> '_2361.SpringDamperConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_CONNECTION](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_spring_damper_connection_load_case(self, design_entity_analysis: '_6233.SpringDamperConnectionLoadCase') -> '_2361.SpringDamperConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpringDamperConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SPRING_DAMPER_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_torque_converter_connection(self, design_entity: '_1946.TorqueConverterConnection') -> '_2379.TorqueConverterConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_CONNECTION](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_torque_converter_connection_load_case(self, design_entity_analysis: '_6251.TorqueConverterConnectionLoadCase') -> '_2379.TorqueConverterConnectionSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterConnectionSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_TORQUE_CONVERTER_CONNECTION_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_abstract_assembly(self, design_entity: '_2024.AbstractAssembly') -> '_2253.AbstractAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_abstract_assembly_load_case(self, design_entity_analysis: '_6098.AbstractAssemblyLoadCase') -> '_2253.AbstractAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AbstractAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_ASSEMBLY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing(self, design_entity: '_2025.AbstractShaftOrHousing') -> '_2254.AbstractShaftOrHousingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftOrHousingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_abstract_shaft_or_housing_load_case(self, design_entity_analysis: '_6099.AbstractShaftOrHousingLoadCase') -> '_2254.AbstractShaftOrHousingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftOrHousingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ABSTRACT_SHAFT_OR_HOUSING_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bearing(self, design_entity: '_2028.Bearing') -> '_2259.BearingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BearingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEARING](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bearing_load_case(self, design_entity_analysis: '_6106.BearingLoadCase') -> '_2259.BearingSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BearingSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEARING_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bolt(self, design_entity: '_2030.Bolt') -> '_2271.BoltSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BoltSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BOLT](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bolt_load_case(self, design_entity_analysis: '_6118.BoltLoadCase') -> '_2271.BoltSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BoltSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BOLT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bolted_joint(self, design_entity: '_2031.BoltedJoint') -> '_2270.BoltedJointSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BoltedJointSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bolted_joint_load_case(self, design_entity_analysis: '_6117.BoltedJointLoadCase') -> '_2270.BoltedJointSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BoltedJointSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BOLTED_JOINT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_component(self, design_entity: '_2032.Component') -> '_2276.ComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_COMPONENT](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_component_load_case(self, design_entity_analysis: '_6123.ComponentLoadCase') -> '_2276.ComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_COMPONENT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_connector(self, design_entity: '_2035.Connector') -> '_2289.ConnectorSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConnectorSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTOR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_connector_load_case(self, design_entity_analysis: '_6136.ConnectorLoadCase') -> '_2289.ConnectorSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConnectorSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONNECTOR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_datum(self, design_entity: '_2036.Datum') -> '_2306.DatumSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.DatumSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_DATUM](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_datum_load_case(self, design_entity_analysis: '_6151.DatumLoadCase') -> '_2306.DatumSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.DatumSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_DATUM_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_external_cad_model(self, design_entity: '_2039.ExternalCADModel') -> '_2307.ExternalCADModelSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ExternalCADModelSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_EXTERNAL_CAD_MODEL](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_external_cad_model_load_case(self, design_entity_analysis: '_6164.ExternalCADModelLoadCase') -> '_2307.ExternalCADModelSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ExternalCADModelSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_EXTERNAL_CAD_MODEL_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_flexible_pin_assembly(self, design_entity: '_2040.FlexiblePinAssembly') -> '_2312.FlexiblePinAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FlexiblePinAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_flexible_pin_assembly_load_case(self, design_entity_analysis: '_6168.FlexiblePinAssemblyLoadCase') -> '_2312.FlexiblePinAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FlexiblePinAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_FLEXIBLE_PIN_ASSEMBLY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_assembly(self, design_entity: '_2023.Assembly') -> '_2258.AssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ASSEMBLY](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_assembly_load_case(self, design_entity_analysis: '_6105.AssemblyLoadCase') -> '_2258.AssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ASSEMBLY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_guide_dxf_model(self, design_entity: '_2041.GuideDxfModel') -> '_2316.GuideDxfModelSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GuideDxfModelSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_guide_dxf_model_load_case(self, design_entity_analysis: '_6176.GuideDxfModelLoadCase') -> '_2316.GuideDxfModelSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GuideDxfModelSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_GUIDE_DXF_MODEL_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_imported_fe_component(self, design_entity: '_2044.ImportedFEComponent') -> '_2320.ImportedFEComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ImportedFEComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_IMPORTED_FE_COMPONENT](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_imported_fe_component_load_case(self, design_entity_analysis: '_6188.ImportedFEComponentLoadCase') -> '_2320.ImportedFEComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ImportedFEComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ImportedFEComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_IMPORTED_FE_COMPONENT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_mass_disc(self, design_entity: '_2048.MassDisc') -> '_2333.MassDiscSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MassDiscSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_MASS_DISC](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_mass_disc_load_case(self, design_entity_analysis: '_6200.MassDiscLoadCase') -> '_2333.MassDiscSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MassDiscSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_MASS_DISC_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_measurement_component(self, design_entity: '_2049.MeasurementComponent') -> '_2334.MeasurementComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MeasurementComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_MEASUREMENT_COMPONENT](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_measurement_component_load_case(self, design_entity_analysis: '_6201.MeasurementComponentLoadCase') -> '_2334.MeasurementComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MeasurementComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_MEASUREMENT_COMPONENT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_mountable_component(self, design_entity: '_2050.MountableComponent') -> '_2336.MountableComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_MOUNTABLE_COMPONENT](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_mountable_component_load_case(self, design_entity_analysis: '_6203.MountableComponentLoadCase') -> '_2336.MountableComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_MOUNTABLE_COMPONENT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_oil_seal(self, design_entity: '_2052.OilSeal') -> '_2338.OilSealSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.OilSealSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_OIL_SEAL](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_oil_seal_load_case(self, design_entity_analysis: '_6205.OilSealLoadCase') -> '_2338.OilSealSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.OilSealSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_OIL_SEAL_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_part(self, design_entity: '_2054.Part') -> '_2339.PartSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_PART](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_part_load_case(self, design_entity_analysis: '_6207.PartLoadCase') -> '_2339.PartSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_PART_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_planet_carrier(self, design_entity: '_2055.PlanetCarrier') -> '_2344.PlanetCarrierSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PlanetCarrierSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_planet_carrier_load_case(self, design_entity_analysis: '_6214.PlanetCarrierLoadCase') -> '_2344.PlanetCarrierSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PlanetCarrierSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_PLANET_CARRIER_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_point_load(self, design_entity: '_2057.PointLoad') -> '_2345.PointLoadSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PointLoadSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_POINT_LOAD](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_point_load_load_case(self, design_entity_analysis: '_6217.PointLoadLoadCase') -> '_2345.PointLoadSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PointLoadSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_POINT_LOAD_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_power_load(self, design_entity: '_2058.PowerLoad') -> '_2346.PowerLoadSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PowerLoadSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_POWER_LOAD](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_power_load_load_case(self, design_entity_analysis: '_6218.PowerLoadLoadCase') -> '_2346.PowerLoadSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.PowerLoadSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_POWER_LOAD_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_root_assembly(self, design_entity: '_2060.RootAssembly') -> '_2351.RootAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RootAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_root_assembly_load_case(self, design_entity_analysis: '_6224.RootAssemblyLoadCase') -> '_2351.RootAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.RootAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_ROOT_ASSEMBLY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_specialised_assembly(self, design_entity: '_2062.SpecialisedAssembly') -> '_2357.SpecialisedAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SPECIALISED_ASSEMBLY](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_specialised_assembly_load_case(self, design_entity_analysis: '_6228.SpecialisedAssemblyLoadCase') -> '_2357.SpecialisedAssemblySystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SPECIALISED_ASSEMBLY_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_unbalanced_mass(self, design_entity: '_2063.UnbalancedMass') -> '_2385.UnbalancedMassSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.UnbalancedMassSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_unbalanced_mass_load_case(self, design_entity_analysis: '_6259.UnbalancedMassLoadCase') -> '_2385.UnbalancedMassSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.UnbalancedMassSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_UNBALANCED_MASS_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_virtual_component(self, design_entity: '_2064.VirtualComponent') -> '_2386.VirtualComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_virtual_component_load_case(self, design_entity_analysis: '_6260.VirtualComponentLoadCase') -> '_2386.VirtualComponentSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_VIRTUAL_COMPONENT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_shaft(self, design_entity: '_2067.Shaft') -> '_2355.ShaftSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_shaft_load_case(self, design_entity_analysis: '_6226.ShaftLoadCase') -> '_2355.ShaftSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SHAFT_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_concept_gear(self, design_entity: '_2105.ConceptGear') -> '_2283.ConceptGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_concept_gear_load_case(self, design_entity_analysis: '_6127.ConceptGearLoadCase') -> '_2283.ConceptGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_concept_gear_set(self, design_entity: '_2106.ConceptGearSet') -> '_2282.ConceptGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_concept_gear_set_load_case(self, design_entity_analysis: '_6129.ConceptGearSetLoadCase') -> '_2282.ConceptGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONCEPT_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_face_gear(self, design_entity: '_2112.FaceGear') -> '_2311.FaceGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_face_gear_load_case(self, design_entity_analysis: '_6165.FaceGearLoadCase') -> '_2311.FaceGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_face_gear_set(self, design_entity: '_2113.FaceGearSet') -> '_2310.FaceGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_face_gear_set_load_case(self, design_entity_analysis: '_6167.FaceGearSetLoadCase') -> '_2310.FaceGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.FaceGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_FACE_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear(self, design_entity: '_2097.AGMAGleasonConicalGear') -> '_2257.AGMAGleasonConicalGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_load_case(self, design_entity_analysis: '_6101.AGMAGleasonConicalGearLoadCase') -> '_2257.AGMAGleasonConicalGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set(self, design_entity: '_2098.AGMAGleasonConicalGearSet') -> '_2256.AGMAGleasonConicalGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_agma_gleason_conical_gear_set_load_case(self, design_entity_analysis: '_6103.AGMAGleasonConicalGearSetLoadCase') -> '_2256.AGMAGleasonConicalGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bevel_differential_gear(self, design_entity: '_2099.BevelDifferentialGear') -> '_2264.BevelDifferentialGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bevel_differential_gear_load_case(self, design_entity_analysis: '_6109.BevelDifferentialGearLoadCase') -> '_2264.BevelDifferentialGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set(self, design_entity: '_2100.BevelDifferentialGearSet') -> '_2263.BevelDifferentialGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bevel_differential_gear_set_load_case(self, design_entity_analysis: '_6111.BevelDifferentialGearSetLoadCase') -> '_2263.BevelDifferentialGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear(self, design_entity: '_2101.BevelDifferentialPlanetGear') -> '_2265.BevelDifferentialPlanetGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialPlanetGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_PLANET_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bevel_differential_planet_gear_load_case(self, design_entity_analysis: '_6112.BevelDifferentialPlanetGearLoadCase') -> '_2265.BevelDifferentialPlanetGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialPlanetGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_PLANET_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear(self, design_entity: '_2102.BevelDifferentialSunGear') -> '_2266.BevelDifferentialSunGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialSunGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bevel_differential_sun_gear_load_case(self, design_entity_analysis: '_6113.BevelDifferentialSunGearLoadCase') -> '_2266.BevelDifferentialSunGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialSunGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_DIFFERENTIAL_SUN_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bevel_gear(self, design_entity: '_2103.BevelGear') -> '_2269.BevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bevel_gear_load_case(self, design_entity_analysis: '_6114.BevelGearLoadCase') -> '_2269.BevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bevel_gear_set(self, design_entity: '_2104.BevelGearSet') -> '_2268.BevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_bevel_gear_set_load_case(self, design_entity_analysis: '_6116.BevelGearSetLoadCase') -> '_2268.BevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.BevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_BEVEL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_conical_gear(self, design_entity: '_2107.ConicalGear') -> '_2287.ConicalGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_conical_gear_load_case(self, design_entity_analysis: '_6130.ConicalGearLoadCase') -> '_2287.ConicalGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_conical_gear_set(self, design_entity: '_2108.ConicalGearSet') -> '_2286.ConicalGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_conical_gear_set_load_case(self, design_entity_analysis: '_6134.ConicalGearSetLoadCase') -> '_2286.ConicalGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CONICAL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_cylindrical_gear(self, design_entity: '_2109.CylindricalGear') -> '_2304.CylindricalGearSystemDeflectionWithLTCAResults':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflectionWithLTCAResults
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_cylindrical_gear_load_case(self, design_entity_analysis: '_6143.CylindricalGearLoadCase') -> '_2304.CylindricalGearSystemDeflectionWithLTCAResults':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflectionWithLTCAResults
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_cylindrical_gear_set(self, design_entity: '_2110.CylindricalGearSet') -> '_2301.CylindricalGearSetSystemDeflectionWithLTCAResults':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflectionWithLTCAResults
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_cylindrical_gear_set_load_case(self, design_entity_analysis: '_6147.CylindricalGearSetLoadCase') -> '_2301.CylindricalGearSetSystemDeflectionWithLTCAResults':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflectionWithLTCAResults
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear(self, design_entity: '_2111.CylindricalPlanetGear') -> '_2305.CylindricalPlanetGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalPlanetGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_PLANET_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_cylindrical_planet_gear_load_case(self, design_entity_analysis: '_6148.CylindricalPlanetGearLoadCase') -> '_2305.CylindricalPlanetGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalPlanetGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_CYLINDRICAL_PLANET_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_gear(self, design_entity: '_2114.Gear') -> '_2315.GearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_gear_load_case(self, design_entity_analysis: '_6170.GearLoadCase') -> '_2315.GearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_gear_set(self, design_entity: '_2116.GearSet') -> '_2314.GearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_gear_set_load_case(self, design_entity_analysis: '_6175.GearSetLoadCase') -> '_2314.GearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.GearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_hypoid_gear(self, design_entity: '_2118.HypoidGear') -> '_2319.HypoidGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_hypoid_gear_load_case(self, design_entity_analysis: '_6185.HypoidGearLoadCase') -> '_2319.HypoidGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_hypoid_gear_set(self, design_entity: '_2119.HypoidGearSet') -> '_2318.HypoidGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_hypoid_gear_set_load_case(self, design_entity_analysis: '_6187.HypoidGearSetLoadCase') -> '_2318.HypoidGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_HYPOID_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_2120.KlingelnbergCycloPalloidConicalGear') -> '_2324.KlingelnbergCycloPalloidConicalGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(self, design_entity_analysis: '_6191.KlingelnbergCycloPalloidConicalGearLoadCase') -> '_2324.KlingelnbergCycloPalloidConicalGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_2121.KlingelnbergCycloPalloidConicalGearSet') -> '_2323.KlingelnbergCycloPalloidConicalGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(self, design_entity_analysis: '_6193.KlingelnbergCycloPalloidConicalGearSetLoadCase') -> '_2323.KlingelnbergCycloPalloidConicalGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2122.KlingelnbergCycloPalloidHypoidGear') -> '_2327.KlingelnbergCycloPalloidHypoidGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(self, design_entity_analysis: '_6194.KlingelnbergCycloPalloidHypoidGearLoadCase') -> '_2327.KlingelnbergCycloPalloidHypoidGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2123.KlingelnbergCycloPalloidHypoidGearSet') -> '_2326.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self, design_entity_analysis: '_6196.KlingelnbergCycloPalloidHypoidGearSetLoadCase') -> '_2326.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2124.KlingelnbergCycloPalloidSpiralBevelGear') -> '_2330.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6197.KlingelnbergCycloPalloidSpiralBevelGearLoadCase') -> '_2330.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2125.KlingelnbergCycloPalloidSpiralBevelGearSet') -> '_2329.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6199.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase') -> '_2329.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_planetary_gear_set(self, design_entity: '_2126.PlanetaryGearSet') -> '_2301.CylindricalGearSetSystemDeflectionWithLTCAResults':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflectionWithLTCAResults
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_PLANETARY_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_planetary_gear_set_load_case(self, design_entity_analysis: '_6212.PlanetaryGearSetLoadCase') -> '_2301.CylindricalGearSetSystemDeflectionWithLTCAResults':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSetSystemDeflectionWithLTCAResults
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_PLANETARY_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_spiral_bevel_gear(self, design_entity: '_2127.SpiralBevelGear') -> '_2360.SpiralBevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_load_case(self, design_entity_analysis: '_6230.SpiralBevelGearLoadCase') -> '_2360.SpiralBevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set(self, design_entity: '_2128.SpiralBevelGearSet') -> '_2359.SpiralBevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_spiral_bevel_gear_set_load_case(self, design_entity_analysis: '_6232.SpiralBevelGearSetLoadCase') -> '_2359.SpiralBevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.SpiralBevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear(self, design_entity: '_2129.StraightBevelDiffGear') -> '_2366.StraightBevelDiffGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_load_case(self, design_entity_analysis: '_6237.StraightBevelDiffGearLoadCase') -> '_2366.StraightBevelDiffGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set(self, design_entity: '_2130.StraightBevelDiffGearSet') -> '_2365.StraightBevelDiffGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_straight_bevel_diff_gear_set_load_case(self, design_entity_analysis: '_6239.StraightBevelDiffGearSetLoadCase') -> '_2365.StraightBevelDiffGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_DIFF_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_straight_bevel_gear(self, design_entity: '_2131.StraightBevelGear') -> '_2369.StraightBevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_straight_bevel_gear_load_case(self, design_entity_analysis: '_6240.StraightBevelGearLoadCase') -> '_2369.StraightBevelGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set(self, design_entity: '_2132.StraightBevelGearSet') -> '_2368.StraightBevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_straight_bevel_gear_set_load_case(self, design_entity_analysis: '_6242.StraightBevelGearSetLoadCase') -> '_2368.StraightBevelGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_GEAR_SET_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear(self, design_entity: '_2133.StraightBevelPlanetGear') -> '_2370.StraightBevelPlanetGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelPlanetGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_straight_bevel_planet_gear_load_case(self, design_entity_analysis: '_6243.StraightBevelPlanetGearLoadCase') -> '_2370.StraightBevelPlanetGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelPlanetGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_PLANET_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear(self, design_entity: '_2134.StraightBevelSunGear') -> '_2371.StraightBevelSunGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelSunGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_straight_bevel_sun_gear_load_case(self, design_entity_analysis: '_6244.StraightBevelSunGearLoadCase') -> '_2371.StraightBevelSunGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.StraightBevelSunGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_STRAIGHT_BEVEL_SUN_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_worm_gear(self, design_entity: '_2135.WormGear') -> '_2389.WormGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_worm_gear_load_case(self, design_entity_analysis: '_6261.WormGearLoadCase') -> '_2389.WormGearSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_LOAD_CASE](design_entity_analysis.wrapped if design_entity_analysis else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None

    def results_for_worm_gear_set(self, design_entity: '_2136.WormGearSet') -> '_2388.WormGearSetSystemDeflection':
        ''' 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.system_deflections.WormGearSetSystemDeflection
        '''

        method_result = self.wrapped.ResultsFor.Overloads[_WORM_GEAR_SET](design_entity.wrapped if design_entity else None)
        return constructor.new_override(method_result.__class__)(method_result) if method_result else None
