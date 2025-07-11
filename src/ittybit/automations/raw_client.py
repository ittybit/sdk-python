# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.unchecked_base_model import construct_type
from ..requests.workflow_task_step import WorkflowTaskStepParams
from ..types.automation_list_response import AutomationListResponse
from ..types.automation_response import AutomationResponse
from ..types.confirmation_response import ConfirmationResponse
from .requests.automations_create_request_trigger import AutomationsCreateRequestTriggerParams
from .requests.automations_update_request_trigger import AutomationsUpdateRequestTriggerParams
from .types.automations_create_request_status import AutomationsCreateRequestStatus
from .types.automations_update_request_status import AutomationsUpdateRequestStatus

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawAutomationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AutomationListResponse]:
        """
        Retrieves a paginated list of all automations for the current project

        Parameters
        ----------
        page : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AutomationListResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "automations",
            method="GET",
            params={
                "page": page,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutomationListResponse,
                    construct_type(
                        type_=AutomationListResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self,
        *,
        trigger: AutomationsCreateRequestTriggerParams,
        workflow: typing.Sequence[WorkflowTaskStepParams],
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        status: typing.Optional[AutomationsCreateRequestStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AutomationResponse]:
        """
        Creates a new automation.

        Parameters
        ----------
        trigger : AutomationsCreateRequestTriggerParams

        workflow : typing.Sequence[WorkflowTaskStepParams]

        name : typing.Optional[str]

        description : typing.Optional[str]

        status : typing.Optional[AutomationsCreateRequestStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AutomationResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "automations",
            method="POST",
            json={
                "name": name,
                "description": description,
                "trigger": convert_and_respect_annotation_metadata(
                    object_=trigger, annotation=AutomationsCreateRequestTriggerParams, direction="write"
                ),
                "workflow": convert_and_respect_annotation_metadata(
                    object_=workflow, annotation=typing.Sequence[WorkflowTaskStepParams], direction="write"
                ),
                "status": status,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutomationResponse,
                    construct_type(
                        type_=AutomationResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AutomationResponse]:
        """
        Retrieve the automation object for a automation with the given ID.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AutomationResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"automations/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutomationResponse,
                    construct_type(
                        type_=AutomationResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConfirmationResponse]:
        """
        Permanently removes an automation from the system. This action cannot be undone.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConfirmationResponse]
            Accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"automations/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfirmationResponse,
                    construct_type(
                        type_=ConfirmationResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        trigger: typing.Optional[AutomationsUpdateRequestTriggerParams] = OMIT,
        workflow: typing.Optional[typing.Sequence[WorkflowTaskStepParams]] = OMIT,
        status: typing.Optional[AutomationsUpdateRequestStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AutomationResponse]:
        """
        Updates an automation's `name`, `description`, `trigger`, `workflow`, or `status`. Only the specified fields will be updated.

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        trigger : typing.Optional[AutomationsUpdateRequestTriggerParams]

        workflow : typing.Optional[typing.Sequence[WorkflowTaskStepParams]]

        status : typing.Optional[AutomationsUpdateRequestStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AutomationResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"automations/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "trigger": convert_and_respect_annotation_metadata(
                    object_=trigger, annotation=AutomationsUpdateRequestTriggerParams, direction="write"
                ),
                "workflow": convert_and_respect_annotation_metadata(
                    object_=workflow, annotation=typing.Sequence[WorkflowTaskStepParams], direction="write"
                ),
                "status": status,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutomationResponse,
                    construct_type(
                        type_=AutomationResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAutomationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AutomationListResponse]:
        """
        Retrieves a paginated list of all automations for the current project

        Parameters
        ----------
        page : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AutomationListResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "automations",
            method="GET",
            params={
                "page": page,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutomationListResponse,
                    construct_type(
                        type_=AutomationListResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self,
        *,
        trigger: AutomationsCreateRequestTriggerParams,
        workflow: typing.Sequence[WorkflowTaskStepParams],
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        status: typing.Optional[AutomationsCreateRequestStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AutomationResponse]:
        """
        Creates a new automation.

        Parameters
        ----------
        trigger : AutomationsCreateRequestTriggerParams

        workflow : typing.Sequence[WorkflowTaskStepParams]

        name : typing.Optional[str]

        description : typing.Optional[str]

        status : typing.Optional[AutomationsCreateRequestStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AutomationResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "automations",
            method="POST",
            json={
                "name": name,
                "description": description,
                "trigger": convert_and_respect_annotation_metadata(
                    object_=trigger, annotation=AutomationsCreateRequestTriggerParams, direction="write"
                ),
                "workflow": convert_and_respect_annotation_metadata(
                    object_=workflow, annotation=typing.Sequence[WorkflowTaskStepParams], direction="write"
                ),
                "status": status,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutomationResponse,
                    construct_type(
                        type_=AutomationResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AutomationResponse]:
        """
        Retrieve the automation object for a automation with the given ID.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AutomationResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"automations/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutomationResponse,
                    construct_type(
                        type_=AutomationResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConfirmationResponse]:
        """
        Permanently removes an automation from the system. This action cannot be undone.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConfirmationResponse]
            Accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"automations/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfirmationResponse,
                    construct_type(
                        type_=ConfirmationResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        trigger: typing.Optional[AutomationsUpdateRequestTriggerParams] = OMIT,
        workflow: typing.Optional[typing.Sequence[WorkflowTaskStepParams]] = OMIT,
        status: typing.Optional[AutomationsUpdateRequestStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AutomationResponse]:
        """
        Updates an automation's `name`, `description`, `trigger`, `workflow`, or `status`. Only the specified fields will be updated.

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        trigger : typing.Optional[AutomationsUpdateRequestTriggerParams]

        workflow : typing.Optional[typing.Sequence[WorkflowTaskStepParams]]

        status : typing.Optional[AutomationsUpdateRequestStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AutomationResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"automations/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "trigger": convert_and_respect_annotation_metadata(
                    object_=trigger, annotation=AutomationsUpdateRequestTriggerParams, direction="write"
                ),
                "workflow": convert_and_respect_annotation_metadata(
                    object_=workflow, annotation=typing.Sequence[WorkflowTaskStepParams], direction="write"
                ),
                "status": status,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutomationResponse,
                    construct_type(
                        type_=AutomationResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
