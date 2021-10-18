import json
import requests
from requests.models import HTTPError
from errors import HTTP400Error


class APIEndpoint:
    URL = "https://api.notion.com/v1"

    def __init__(self, api) -> None:
        self._api_key = api.api_key

    def get(self, path, **kwargs):
        return self._request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self._request("POST", path, **kwargs)

    def _request(self, method, path, **kwargs):
        try:
            headers = {}
            headers['Authorization'] = f"Bearer {self._api_key}"
            headers['Content-Type'] = 'application/json'
            headers['Notion-Version'] = '2021-05-13'
            print(kwargs.get('payload'))
            response = requests.request(method,
                                        self.URL + path,
                                        headers=headers,
                                        data=json.dumps(kwargs.get('payload'))
                                        )
            response.raise_for_status()
            return response.json()
        except HTTP400Error:
            raise HTTP400Error(response.json())
        except HTTPError:
            response = response.json()
            error_msg = "\nstatus:- %s\ncode:- %s\nmessage:-%s" % (
                        response.get('status'), response.get('code'),
                        response.get('message'))
            raise HTTPError(error_msg)
