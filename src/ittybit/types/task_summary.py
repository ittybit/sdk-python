# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .task_summary_kind import TaskSummaryKind
from .task_summary_status import TaskSummaryStatus


class TaskSummary(UncheckedBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the task.
    """

    object: str = pydantic.Field()
    """
    Object type, always 'task'.
    """

    kind: TaskSummaryKind = pydantic.Field()
    """
    The type of operation the task performs.
    """

    status: TaskSummaryStatus = pydantic.Field()
    """
    Current status of the task.
    """

    progress: typing.Optional[int] = pydantic.Field(default=None)
    """
    Task progress percentage.
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message if the task failed.
    """

    created_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the entity that created the task (e.g., user ID, automation ID).
    """

    created: dt.datetime = pydantic.Field()
    """
    Timestamp when the task was created.
    """

    updated: dt.datetime = pydantic.Field()
    """
    Timestamp when the task was last updated.
    """

    parent_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the parent task if this is part of a workflow.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
