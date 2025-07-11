# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .workflow_task_step_kind import WorkflowTaskStepKind
from .workflow_task_step_next_item import WorkflowTaskStepNextItem


class WorkflowTaskStep(UncheckedBaseModel):
    kind: WorkflowTaskStepKind
    ref: typing.Optional[str] = None
    next: typing.Optional[typing.List[WorkflowTaskStepNextItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
