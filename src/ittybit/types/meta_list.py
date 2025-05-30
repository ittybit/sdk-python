# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel


class MetaList(UncheckedBaseModel):
    request_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Request ID
    """

    type: typing.Optional[typing.Literal["list"]] = pydantic.Field(default=None)
    """
    Type of the primary data value in the response
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of items per page.
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of items matching the query.
    """

    page: typing.Optional[int] = pydantic.Field(default=None)
    """
    Current page number.
    """

    pages: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of pages.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
