"""Zoom.us REST API Python Client -- Meeting component"""

from __future__ import absolute_import

from zoomus import util
from zoomus.components_v2 import base


__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class RecordingComponentV2(base.BaseComponentV2):
    """Component dealing with all meeting related matters"""

    def list(self, user_id, **kwargs):
        util.require_keys(kwargs, ['from', 'to'])
        return self.get_request("/users/%s/recordings" % user_id, params=kwargs)

    def retrieve_by_meeting(self, meeting_id, **kwargs):
        return self.get_request("/meetings/%s/recordings" % meeting_id, params=kwargs)

    def delete_by_meeting(self, meeting_id, **kwargs):
        action_values = ['trash', 'delete']
        if ('action' in kwargs) and (kwargs['action'] not in action_values):
            raise ValueError("'action' must be one of {}".format(action_values))
        return self.delete_request("/meetings/%s/recordings" % meeting_id, params=kwargs)

    def delete(self, meeting_id, recording_id, **kwargs):
        action_values = ['trash', 'delete']
        if ('action' in kwargs) and (kwargs['action'] not in action_values):
            raise ValueError("'action' must be one of {}".format(action_values))
        return self.delete_request("/meetings/%s/recordings/%s" % (meeting_id, recording_id), params=kwargs)

    def recover_by_meeting(self, meeting_id, **kwargs):
        action_values = ['recover']
        if ('action' in kwargs) and (kwargs['action'] not in action_values):
            raise ValueError("'action' must be one of {}".format(action_values))
        return self.put_request("/meetings/%s/recordings" % meeting_id, params=kwargs)

    def recover(self, meeting_id, recording_id, **kwargs):
        action_values = ['recover']
        if ('action' in kwargs) and (kwargs['action'] not in action_values):
            raise ValueError("'action' must be one of {}".format(action_values))
        return self.put_request("/meetings/%s/recordings/%s" % (meeting_id, recording_id), params=kwargs)
