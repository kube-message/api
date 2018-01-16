import falcon
import json

from .services import messenger
from . import serializers
from .utils import get_logger


logger = get_logger()


class HealthCheckResource(object):
    @staticmethod
    def on_get(request, response):
        response.status = falcon.HTTP_200
        response.data = json.dumps({"status": "OK"})


def get_data_from_request(request):
    """
    Deserializes the JSON in the request body and returns the result

    Args:
        request (falcon.Request)

    Returns:
        [dict, list]: The deserialized JSON. If nothing can be read returns an empty dict
    """
    data = {}
    try:
        data = json.loads(request.stream.read())
    except ValueError as err:
        logger.warn("error parsing JSON: %s", err)
    return data


class ThreadListResource(object):
    @staticmethod
    def on_post(request, response):
        data = get_data_from_request(request)
        participants = data.get("participants")
        if not participants:
            response.status = falcon.HTTP_BAD_REQUEST
            response.data = json.dumps({"error": "particiapnts is a required field."})
            return
        thread, error = messenger.create_thread(participants)
        if not error:
            response.data = json.dumps({"thread_id": thread.id, "participants": list(thread.participants)}).encode()
            response.status = falcon.HTTP_202
        else:
            response.data = json.dumps({"error": error.error_code})
            response.status = falcon.HTTP_500


class ThreadMessageListResource(object):
    @staticmethod
    def on_get(request, response, thread_id):
        message_objects = messenger.get_messages_for_thread(thread_id)
        response.data = json.dumps(
            [serializers.message_proto_to_json(m) for m in message_objects]
        ).encode()
        response.status = falcon.HTTP_200

    # @staticmethod
    # def on_post(request, response, thread_id):
    #     data = get_data_from_request(request)
    #     try:
    #         sender_id, text = data["sender_id"], data["text"]
    #     except KeyError as err:
    #         response.status = falcon.HTTP_400
    #         response.data = json.dumps({"error": "error sending message: %s" % err})
    #         return

    #     if threads.is_user_in_thread(sender_id, thread_id):
    #         message = messages.send_message(thread_id, sender_id, text)
    #         response.status = falcon.HTTP_201
    #         serializer = ModelSerializer(message, ['text', 'thread_id'])
    #         alerts.send_alerts_for_thread_participants(thread_id)
    #         response.data = json.dumps(serializer.build_response())
    #     else:
    #         response.status = falcon.HTTP_400
    #         response.data = json.dumps({"error": "error sending message: sender not in thread"})
    #         return


# class ThreadDetailResource(object):
#     @staticmethod
#     def on_get(request, response, thread_id):
#         thread = threads.get_thread_by_id(thread_id)
#         response.data = json.dumps(ModelSerializer(thread, ["participants"]).build_response())
#         response.status = falcon.HTTP_200


# class ThreadUserListResource(object):
#     @staticmethod
#     def on_get(request, response, user_id):
#         user_threads = threads.get_threads_for_user(user_id)
#         response.data = json.dumps([ModelSerializer(t, ["pk", "particiapnts"]).build_response() for t in user_threads])
#         response.status = falcon.HTTP_200


# class MessageListResource(object):
#     @staticmethod
#     def on_post(request, response):
#         data = get_data_from_request(request)
#         try:
#             thread_id, sender_id, text = data["thread_id"], data["sender_id"], data["text"]
#         except KeyError as err:
#             response.status = falcon.HTTP_400
#             response.data = json.dumps({"error": "error sending message: %s" % err})
#             return

#         if threads.is_user_in_thread(sender_id, thread_id):
#             message = messages.send_message(thread_id, sender_id, text)
#             response.status = falcon.HTTP_201
#             serializer = ModelSerializer(message, ['text', 'thread_id'])
#             alerts.send_alerts_for_thread_participants(thread_id)
#             response.data = json.dumps(serializer.build_response())
#         else:
#             response.status = falcon.HTTP_400
#             response.data = json.dumps({"error": "error sending message: sender not in thread"})
#             return


# class MessageDetailResource(object):
#     @staticmethod
#     def on_get(request, response, message_id):
#         """
#         Handle GET requests for message objects.
#         Args:
#             request: Falcon request object
#             response: Falcon response object
#             message_id (int): a message ID

#         Returns:
#             falcon.Response
#         """
#         message = messages.get_message_by_id(message_id)
#         if message is None:
#             response.status = falcon.HTTP_404
#         else:
#             serializer = ModelSerializer(message, ['text', 'sender_id', 'thread_id'])
#             response.data = json.dumps(serializer.build_response())