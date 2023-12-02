import requests
from pydantic import BaseModel


def validate_request_json(json: str | BaseModel):
    if isinstance(json, dict):
        return json
    return json.model_dump(by_alias=True, exclude_none=True)  # exclude_none=True - turn off not-required fields


def validate_status_code(response: requests.Response, status_code: int):
    assert response.status_code == status_code, \
        f'status code must be equal to status_code, but it is {response.status_code}'
