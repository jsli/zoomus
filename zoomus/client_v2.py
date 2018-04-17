"""Zoom.us REST API Python Client"""

from __future__ import absolute_import

import time

import jwt

from zoomus import (
    components_v2,
    util)

__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class ZoomClientV2(util.ApiClient):
    """Zoom.us REST API-V2 Python Client"""

    BASE_URI = 'https://api.zoom.us/v2'
    """Base URL for Zoom API-V2"""

    def __init__(
            self, access_token, timeout=15, debug=True):
        """Create a new Zoom client

        :param access_token: The Zooom.us access_token
        :param timeout: The time out to use for API requets
        """
        super(ZoomClientV2, self).__init__(
            base_uri=ZoomClientV2.BASE_URI, timeout=timeout)

        # Setup the config details
        self.config = {
            'access_token': access_token,
            'debug': debug
        }

        # Register all of the components
        self.components = {
            'user': components_v2.user.UserComponentV2(
                base_uri=ZoomClientV2.BASE_URI, config=self.config),
            'meetings': components_v2.meeting.MeetingComponentV2(
                base_uri=ZoomClientV2.BASE_URI, config=self.config),
            'recording': components_v2.recording.RecordingComponentV2(
                base_uri=ZoomClientV2.BASE_URI, config=self.config),
        }

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return

    @property
    def access_token(self):
        """The Zoom.us access_token"""
        return self.config.get('access_token')

    @access_token.setter
    def access_token(self, value):
        """Set the access_token"""
        self.config['access_token'] = value

    @classmethod
    def generate_access_token(cls, api_key, api_secret, exp=60):
        """generate access token, default exp = 60s"""
        payload = {
            'iss': api_key,
            'exp': int((time.time() + exp) * 1000)
        }
        token = jwt.encode(payload, api_secret, algorithm='HS256')
        return token

    @property
    def user(self):
        """Get the user component"""
        return self.components.get('user')
