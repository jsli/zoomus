"""Zoom.us REST API Python Client -- User component"""

from __future__ import absolute_import

from zoomus import util
from zoomus.components_v2 import base


__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class UserComponentV2(base.BaseComponentV2):
    """Component dealing with all user related matters"""

    def list(self, **kwargs):
        return self.get_request("/users", params=kwargs)

    def create(self, **kwargs):
        util.require_keys(kwargs, ['action', 'user_info'])
        action_values = ['create', 'autoCreate', 'custCreate', 'ssoCreate']
        if kwargs['action'] not in action_values:
            raise ValueError("'action' must be one of {}".format(action_values))

        user_info = kwargs['user_info']
        util.require_keys(user_info, ['email', 'type'])
        user_type_values = [1, 2, 3]
        if int(user_info['type']) not in user_type_values:
            raise ValueError("'user_info.type' must be one of {}".format(user_type_values))

        return self.post_request("/users", data=kwargs)

    def retrieve(self, user_id, **kwargs):
        return self.get_request("/users/%s" % user_id, params=kwargs)

    def retrieve_token(self, user_id, **kwargs):
        return self.get_request("/users/%s/token" % user_id, params=kwargs)

    def revoke_token(self, user_id, **kwargs):
        return self.delete_request("/users/%s/token" % user_id, params=kwargs)

    def update(self, user_id, **kwargs):
        return self.patch_request("/users/%s" % user_id, data=kwargs)

    def delete(self, user_id, **kwargs):
        action_values = ['disassociate', 'delete']
        if ('action' in kwargs) and (kwargs['action'] not in action_values):
            raise ValueError("'action' must be one of {}".format(action_values))
        return self.delete_request("/users/%s" % user_id, params=kwargs)

    def list_assistants(self, user_id, **kwargs):
        return self.get_request("/users/%s/assistants" % user_id, params=kwargs)

    def add_assistants(self, user_id, **kwargs):
        return self.post_request("/users/%s/assistants" % user_id, data=kwargs)

    def delete_assistants(self, user_id, **kwargs):
        return self.delete_request("/users/%s/assistants" % user_id, params=kwargs)

    def delete_assistant(self, user_id, assistant_id, **kwargs):
        return self.delete_request("/users/%s/assistants/%s" % (user_id, assistant_id), params=kwargs)

    def retrieve_settings(self, user_id, **kwargs):
        return self.get_request("/users/%s/settings" % user_id, params=kwargs)

    def update_settings(self, user_id, **kwargs):
        return self.patch_request("/users/%s/settings" % user_id, data=kwargs)

    def update_status(self, user_id, **kwargs):
        util.require_keys(kwargs, 'action')
        action_values = ['activate', 'deactivate']
        if kwargs['action'] not in action_values:
            raise ValueError("'action' must be one of {}".format(action_values))
        return self.put_request("/users/%s/status" % user_id, data=kwargs)

    def update_password(self, user_id, **kwargs):
        util.require_keys(kwargs, 'password')
        return self.put_request("/users/%s/password" % user_id, data=kwargs)

    def verify_zpk(self, **kwargs):
        util.require_keys(kwargs, 'zpk')
        return self.get_request("/users/zpk", params=kwargs)

    def verify_email(self, **kwargs):
        util.require_keys(kwargs, 'email')
        return self.get_request("/users/email", params=kwargs)

    """
    TODO:
        * Upload a user's picture
    """
