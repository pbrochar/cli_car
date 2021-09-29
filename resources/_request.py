from requests import Request, Session, Response
from requests.models import HTTPError
from .token import get_token, refresh_token
from typing import Optional, Dict, Any


def _request(method: str, url: str, data: Optional[str] = None, headers: Optional[Dict[str, Any]] = None, params: Optional[dict] = None) -> Response:
    s = Session()
    token = get_token()
    req = Request(method, url, data=data, headers=headers, params=params)
    prepped = s.prepare_request(req)
    prepped.headers["Authorization"] = token
    response = s.send(prepped)
    try:
        response.raise_for_status()
    except HTTPError as e:
        if e.response.status_code == 401:
            token = refresh_token()
            prepped.headers["Authorization"] = token
            response = s.send(prepped)
            response.raise_for_status()
        else:
            raise
    return response
