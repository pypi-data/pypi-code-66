# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from .. import PipelineComponent


class _PipelineStack:
    """ A stack stores all :class`azure.ml.component.pipeline`
    in creating state created by :class`azure.ml.component.dsl.pipeline`

    """

    def __init__(self):
        self.items = []

    def top(self) -> PipelineComponent:
        return self.items[-1]

    def pop(self) -> PipelineComponent:
        return self.items.pop()

    def push(self, item: PipelineComponent):
        error_msg = "_PipelineStack only allows pushing `azure.ml.component.PipelineComponent` element"
        assert isinstance(item, PipelineComponent), error_msg
        return self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


_pipeline_stack = _PipelineStack()
