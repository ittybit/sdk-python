# This file was auto-generated by Fern from our API Definition.

import typing_extensions
from ..core.serialization import FieldMetadata


class LinksListParams(typing_extensions.TypedDict):
    self_: typing_extensions.NotRequired[typing_extensions.Annotated[str, FieldMetadata(alias="self")]]
    first: typing_extensions.NotRequired[str]
    next: typing_extensions.NotRequired[str]
    prev: typing_extensions.NotRequired[str]
    last: typing_extensions.NotRequired[str]
