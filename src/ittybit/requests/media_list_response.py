# This file was auto-generated by Fern from our API Definition.

import typing

import typing_extensions
from .links_list import LinksListParams
from .media import MediaParams
from .meta_list import MetaListParams


class MediaListResponseParams(typing_extensions.TypedDict):
    meta: typing_extensions.NotRequired[MetaListParams]
    data: typing_extensions.NotRequired[typing.Sequence[MediaParams]]
    links: typing_extensions.NotRequired[LinksListParams]
