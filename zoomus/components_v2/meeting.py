"""Zoom.us REST API Python Client -- Meeting component"""

from __future__ import absolute_import

from zoomus import util
from zoomus.components_v2 import base


__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class MeetingComponentV2(base.BaseComponentV2):
    """Component dealing with all meeting related matters"""

    def list(self, user_id, **kwargs):
        return self.get_request("/users/%s/meetings" % user_id, params=kwargs)

    def create(self, user_id, **kwargs):
        return self.post_request("/users/%s/meetings" % user_id, data=kwargs)

    def retrieve(self, meeting_id, **kwargs):
        return self.get_request("/meetings/%s" % meeting_id, params=kwargs)

    def update(self, meeting_id, **kwargs):
        return self.patch_request("/meetings/%s" % meeting_id, data=kwargs)

    def delete(self, meeting_id, **kwargs):
        return self.delete_request("/meetings/%s" % meeting_id, params=kwargs)

    def update_status(self, meeting_id, **kwargs):
        action_values = ['end']
        if ('action' in kwargs) and (kwargs['action'] not in action_values):
            raise ValueError("'action' must be one of {}".format(action_values))
        return self.put_request("/meetings/%s" % meeting_id, data=kwargs)

    def list_registrants(self, meeting_id, **kwargs):
        return self.get_request("/meetings/%s/registrants" % meeting_id, params=kwargs)

    def add_registrants(self, meeting_id, **kwargs):
        util.require_keys(kwargs, ['email', 'first_name', 'last_name'])
        params = {'occurrence_ids': kwargs['occurrence_ids']} if 'occurrence_ids' in kwargs else {}
        return self.post_request("/meetings/%s/registrants" % meeting_id, params=params, data=kwargs)

    def update_registrants(self, meeting_id, **kwargs):
        util.require_keys(kwargs, 'action')
        params = {'occurrence_id': kwargs['occurrence_id']} if 'occurrence_id' in kwargs else {}
        return self.put_request("/meetings/%s/registrants" % meeting_id, params=params, data=kwargs)
