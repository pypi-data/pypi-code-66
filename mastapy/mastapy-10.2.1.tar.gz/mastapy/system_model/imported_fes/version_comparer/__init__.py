'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2017 import DesignResults
    from ._2018 import ImportedFEResults
    from ._2019 import ImportedFEVersionComparer
    from ._2020 import LoadCaseResults
    from ._2021 import LoadCasesToRun
    from ._2022 import NodeComparisonResult
