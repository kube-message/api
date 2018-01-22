import falcon
import json

from ..services import alerts, messenger
from .. import serializers
from .shared import get_data_from_request
from ..utils import get_logger


logger = get_logger()


class ThreadMessageListResource(object):
    @staticmethod
    def on_get(request, response, thread_id):
        message_objects = messenger.get_messages_for_thread(thread_id)
        response.data = serializers.message_proto_list_to_json(message_objects)
        response.status = falcon.HTTP_200

    @staticmethod
    def on_post(request, response, thread_id):
        data = get_data_from_request(request)
        try:
            sender_id, text = data["sender_id"], data["text"]
        except KeyError as err:
            response.status = falcon.HTTP_400
            response.data = json.dumps({"error": "error sending message: %s" % err}).encode()
            return

        message = messenger.send_message(thread_id, sender_id, text)
        response.status = falcon.HTTP_201
        alerts.send_alerts_for_thread_participants(thread_id, thread_id)
        response.data = serializers.message_proto_to_json(message)
