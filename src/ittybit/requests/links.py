# This file was auto-generated by Fern from our API Definition.

import typing_extensions
from ..core.serialization import FieldMetadata


class LinksParams(typing_extensions.TypedDict):
    self_: typing_extensions.NotRequired[typing_extensions.Annotated[str, FieldMetadata(alias="self")]]
    parent: typing_extensions.NotRequired[str]
