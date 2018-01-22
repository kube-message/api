import falcon

from ..services import alerts
from .. import serializers
from .shared import get_data_from_request
from ..utils import get_logger


logger = get_logger()


class AlertsResource(object):
    @staticmethod
    def on_get(request, response, user_id):
        alerts_list = alerts.get_alerts_for_user(user_id)
        response.status = falcon.HTTP_200
        response.data = serializers.alert_proto_list_to_json(alerts_list)

    @staticmethod
    def on_put(request, response, user_id):
        uniq = get_data_from_request(request).get("uniq")
        success = alerts.mark_alert_seen(user_id, uniq)
        if success:
            response.status = falcon.HTTP_201
        else:
            response.status = falcon.HTTP_500
