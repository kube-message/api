import falcon

from ..services import messenger
from .. import serializers
from ..utils import get_logger


logger = get_logger()


class MessageDetailResource(object):
    @staticmethod
    def on_get(request, response, message_id):
        """
        Handle GET requests for message objects.
        Args:
            request: Falcon request object
            response: Falcon response object
            message_id (int): a message ID

        Returns:
            falcon.Response
        """
        message = messenger.get_message_by_id(message_id)
        if message is None:
            response.status = falcon.HTTP_404
        else:
            pass
