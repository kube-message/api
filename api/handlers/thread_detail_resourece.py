import falcon

from ..services import messenger
from .. import serializers
from ..utils import get_logger


logger = get_logger()


class ThreadDetailResource(object):
    @staticmethod
    def on_get(request, response, thread_id):
        thread = messenger.get_thread_detail(thread_id)
        response.data = serializers.thread_proto_to_json(thread)
        response.status = falcon.HTTP_200
