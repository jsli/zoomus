"""Zoom.us REST API Python Client"""

from __future__ import absolute_import

from zoomus import util

__author__ = "Patrick R. Schmid"
__email__ = "prschmid@act.md"


class BaseComponentV2(util.ApiClient):
    """A base component"""

    def __init__(self, base_uri=None, config=None, timeout=15, **kwargs):
        """Setup a base component

        :param base_uri: The base URI to the API
        :param config: The config details
        :param timeout: The timeout to use for requests
        :param \*\*kwargs: Any other attributes. These will be added as
                           attributes to the ApiClient object.
        """
        config = config or {}
        config.update({
            'headers': {
                'Content-Type': 'application/json; charset=utf-8',
                'Accept-Type': 'application/json; charset=utf-8'
            }
        })
        super(BaseComponentV2, self).__init__(
            base_uri=base_uri, timeout=timeout, config=config, **kwargs)

    def get_request(
            self, endpoint, params=None, headers=None):
        """Helper function for GET requests

        :param endpoint: The endpoint
        :param params: The URL parameters
        :param headers: request headers
        :return: The :class:``requests.Response`` object for this request
        """
        params = params or {}
        params.update(self.config)
        return super(BaseComponentV2, self).get_request(
            endpoint, params=params, headers=headers)

    def post_request(
            self, endpoint, params=None, data=None, headers=None, cookies=None):
        """Helper function for POST requests

        :param endpoint: The endpoint
        :param params: The URL parameters
        :param data: The data (either as a dict or dumped JSON string) to
                     include with the POST
        :param headers: request headers
        :param cookies: request cookies
        :return: The :class:``requests.Response`` object for this request
        """
        params = params or {}
        params.update(self.config)
        headers = headers or {}
        headers.update(self.config['headers'])
        return super(BaseComponentV2, self).post_request(
            endpoint, params=params, data=data, headers=headers,
            cookies=cookies)

    def patch_request(
            self, endpoint, params=None, data=None, headers=None, cookies=None):
        """Helper function for PATCH requests

        :param endpoint: The endpoint
        :param params: The URL parameters
        :param data: The data (either as a dict or dumped JSON string) to
                     include with the POST
        :param headers: request headers
        :param cookies: request cookies
        :return: The :class:``requests.Response`` object for this request
        """
        params = params or {}
        params.update(self.config)
        headers = headers or {}
        headers.update(self.config['headers'])
        return super(BaseComponentV2, self).patch_request(
            endpoint, params=params, data=data, headers=headers,
            cookies=cookies)

    def put_request(
            self, endpoint, params=None, data=None, headers=None, cookies=None):
        """Helper function for PATCH requests

        :param endpoint: The endpoint
        :param params: The URL parameters
        :param data: The data (either as a dict or dumped JSON string) to
                     include with the POST
        :param headers: request headers
        :param cookies: request cookies
        :return: The :class:``requests.Response`` object for this request
        """
        params = params or {}
        params.update(self.config)
        headers = headers or {}
        headers.update(self.config['headers'])
        return super(BaseComponentV2, self).put_request(
            endpoint, params=params, data=data, headers=headers,
            cookies=cookies)

    def delete_request(
            self, endpoint, params=None, data=None, headers=None, cookies=None):
        """Helper function for DELETE requests

        :param endpoint: The endpoint
        :param params: The URL parameters
        :param data: The data (either as a dict or dumped JSON string) to
                     include with the DELETE
        :param headers: request headers
        :param cookies: request cookies
        :return: The :class:``requests.Response`` object for this request
        """
        params = params or {}
        params.update(self.config)
        headers = headers or {}
        headers.update(self.config['headers'])
        return super(BaseComponentV2, self).delete_request(
            endpoint, params=params, data=data, headers=headers,
            cookies=cookies)

    def compose_header(self, header):
        pass
