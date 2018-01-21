import falcon

from ..services import messenger
from .. import serializers
from ..utils import get_logger


logger = get_logger()


class ThreadUserListResource(object):
    @staticmethod
    def on_get(request, response, user_id):
        threads = messenger.get_threads_for_user(user_id)
        response.data = serializers.thread_proto_list_to_json(threads)
        response.status = falcon.HTTP_200
