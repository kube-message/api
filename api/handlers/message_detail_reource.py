import falcon

from ..services import messenger
from .. import serializers
from ..utils import get_logger


logger = get_logger()


class MessageDetailResource(object):
    @staticmethod
    def on_get(request, response, message_id):
        """
        Gets a single message by ID.

        Args:
            request: Falcon request object
            response: Falcon response object
            message_id (int): a message ID

        Returns:
            falcon.Response
        """
        message = messenger.get_message_detail(message_id)
        if message is None:
            response.status = falcon.HTTP_404
        else:
            response.status = falcon.HTTP_200
            response.data = serializers.message_proto_to_json(message)
