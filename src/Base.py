import requests
from requests.exceptions import ConnectTimeout
from abc import ABC
from exceptions import MissingAuthKeyError
import json

SAND_BOX_API = "https://sandbox.conduit.financial/"
PRODUCTION_API = ""


class BaseClient(object):
    def __init__(self, production: bool = False) -> any:
        self.api_key = ""
        self.base_url = ""
        self.production = production
        #   if not api_key:
        #     raise MissingAuthKeyError("Missing Authorization key argument or env variable")
        if self.production:
            self.base_url = PRODUCTION_API
        else:
            self.base_url = SAND_BOX_API

    def get_auth_header(self):
        """_summary_

        Returns:
            dict: _description_
        """
        return {
            "Content-Type": "application/json",
            "X-API-Key": "",
            "X-API-Secret": "",
            "user-agent": "Conduit  python SDK",
        }

    def _handle_request(
            self,
            method_type,
            url_path,
            data=None,
            params=None):
        """
        Generic function to handle all API url calls
        Returns a python tuple of status code,data
        """
        if data is None:
            payload=None
        else:
           payload = json.dumps({"data": data})

        
        try:
            response = requests.request(
                url=self.base_url + url_path,
                method=method_type,
                headers=self.get_auth_header(),
                data=payload,
                params=params,
            )

            print(response.url)
            if response.status_code == 400 or 401:
                return response.json()

            if response.status_code in [200, 201]:
                return response.json()
            else:
                return response.json()
        except ConnectTimeout:
            return "The request timed out"
