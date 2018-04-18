"""Zoom.us REST API Python Client -- Meeting component"""

from __future__ import absolute_import

from zoomus import util
from zoomus.components_v2 import base


__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class WebinarComponentV2(base.BaseComponentV2):
    """Component dealing with all meeting related matters"""

    def list(self, user_id, **kwargs):
        return self.get_request("/users/%s/webinars" % user_id, params=kwargs)

    def create(self, user_id, **kwargs):
        return self.post_request("/users/%s/webinars" % user_id, data=kwargs)

    def retrieve(self, webinar_id, **kwargs):
        return self.get_request("/webinars/%s" % webinar_id, params=kwargs)

    def update(self, webinar_id, **kwargs):
        return self.patch_request("/webinars/%s" % webinar_id, params=kwargs)

    def delete(self, webinar_id, **kwargs):
        return self.delete_request("/webinars/%s" % webinar_id, params=kwargs)

    def update_status(self, webinar_id, **kwargs):
        return self.put_request("/webinars/%s/status" % webinar_id, data=kwargs)

    def list_panelists(self, webinar_id, **kwargs):
        return self.get_request("/webinars/%s/panelists" % webinar_id, params=kwargs)

    def add_panelists(self, webinar_id, **kwargs):
        return self.post_request("/webinars/%s/panelists" % webinar_id, data=kwargs)

    def remove_panelists(self, webinar_id, **kwargs):
        return self.delete_request("/webinars/%s/panelists" % webinar_id, params=kwargs)

    def remove_panelist(self, webinar_id, panelist_id, **kwargs):
        return self.delete_request("/webinars/%s/panelists/%s" % (webinar_id, panelist_id), params=kwargs)

    def list_registrants(self, webinar_id, **kwargs):
        return self.get_request("/webinars/%s/registrants" % webinar_id, params=kwargs)

    def add_registrant(self, webinar_id, **kwargs):
        return self.post_request("/webinars/%s/registrants" % webinar_id, data=kwargs)

    def update_registrant_status(self, webinar_id, **kwargs):
        util.require_keys(kwargs, 'action')
        action_values = ['approve', 'cancel', 'deny']
        if kwargs['action'] not in action_values:
            raise ValueError("'action' must be one of {}".format(action_values))
        if 'occurrence_id' in kwargs:
            params = {'occurrence_id': kwargs['occurrence_id']}
            kwargs.pop('occurrence_id')
        else:
            params = {}
        return self.put_request("/webinars/%s/registrants/status" % webinar_id, params=params, data=kwargs)
