# This file was auto-generated by Fern from our API Definition.

import typing_extensions


class SignatureParams(typing_extensions.TypedDict):
    domain: str
    """
    Domain of the signed URL
    """

    filename: str
    """
    Filename of the signed file
    """

    folder: typing_extensions.NotRequired[str]
    """
    Folder of the signed file
    """

    expiry: int
    """
    Expiry timestamp of the signed URL
    """

    method: str
    """
    HTTP method for the signed URL
    """

    signature: str
    """
    Generated signature for the signed URL
    """

    url: str
    """
    Generated signed URL
    """
