import falcon
import json

from ..services import messenger
from .. import serializers
from .shared import get_data_from_request
from ..utils import get_logger


logger = get_logger()


class ThreadListResource(object):
    @staticmethod
    def on_post(request, response):
        data = get_data_from_request(request)
        participants = data.get("participants")
        if not participants:
            response.status = falcon.HTTP_BAD_REQUEST
            response.data = json.dumps({"error": "particiapnts is a required field."}).encode()
            return
        thread, error = messenger.create_thread(participants)
        if not error:
            response.data = serializers.thread_proto_to_json(thread)
            response.status = falcon.HTTP_202
        else:
            response.data = json.dumps({"error": error.error_code}).encode()
            response.status = falcon.HTTP_500
