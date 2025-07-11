# This file was auto-generated by Fern from our API Definition.

import typing_extensions
from ..types.meta import Meta
from .confirmation import ConfirmationParams
from .error import ErrorParams
from .links import LinksParams


class ConfirmationResponseParams(typing_extensions.TypedDict):
    meta: typing_extensions.NotRequired[Meta]
    data: typing_extensions.NotRequired[ConfirmationParams]
    error: typing_extensions.NotRequired[ErrorParams]
    links: typing_extensions.NotRequired[LinksParams]
