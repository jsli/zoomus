"""Zoom.us REST API Python Client -- Report component"""

from __future__ import absolute_import

from zoomus import util
from zoomus.components_v2 import base


__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class ReportComponentV2(base.BaseComponentV2):
    """Component dealing with all report related matters"""

    def daily(self, **kwargs):
        return self.get_request("/report/daily", params=kwargs)

    def hosts(self, **kwargs):
        util.require_keys(kwargs, ['from', 'to'])
        return self.get_request("/report/users", params=kwargs)

    def meetings(self, user_id, **kwargs):
        util.require_keys(kwargs, ['from', 'to'])
        return self.get_request("/report/users/%s/meetings" % user_id, params=kwargs)

    def meeting_detail(self, meeting_id, **kwargs):
        return self.get_request("/report/meetings/%s" % meeting_id, params=kwargs)

    def meeting_participants(self, meeting_id, **kwargs):
        return self.get_request("/report/meetings/%s/participants" % meeting_id, params=kwargs)

    def meeting_polls(self, meeting_id, **kwargs):
        return self.get_request("/report/meetings/%s/polls" % meeting_id, params=kwargs)

    def webinar_detail(self, webinar_id, **kwargs):
        return self.get_request("/report/webinars/%s" % webinar_id, params=kwargs)

    def webinar_participants(self, webinar_id, **kwargs):
        return self.get_request("/report/webinars/%s/participants" % webinar_id, params=kwargs)

    def webinar_polls(self, webinar_id, **kwargs):
        return self.get_request("/report/webinars/%s/polls" % webinar_id, params=kwargs)

    def webinar_qa(self, webinar_id, **kwargs):
        return self.get_request("/report/webinars/%s/qa" % webinar_id, params=kwargs)

    def telephone(self, **kwargs):
        util.require_keys(kwargs, ['from', 'to'])
        return self.get_request("/report/telephone", params=kwargs)
