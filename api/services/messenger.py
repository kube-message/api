from collections import namedtuple

import grpc

from ..proto import messenger
from ..utils import get_logger


logger = get_logger()

channel = grpc.insecure_channel("messenger:8081")
client = messenger.MessengerStub(channel)


Endpoints = namedtuple("Endpoints", ["send_message", "get_threads_for_user", "get_thread_messages", "create_thread"])
endpoints = Endpoints("send_message", "get_threads_for_user", "get_thread_messages", "create_thread")


def get_metadata(endpoint):
    return [("caller", "messenger-cli"), ("endpoint", endpoint)]


def create_thread(participants):
    request = messenger.CreateThreadRequest(participants=participants)
    response = client.create_thread(request, metadata=get_metadata(endpoints.create_thread))
    if response.error.message:
        logger.error("error creating thread: %s", response.error.message)
        return None, response.error
    return response.thread, None


def get_messages_for_thread(thread_id):
    request = messenger.GetThreadMessagesRequest(thread_id=thread_id)
    response = client.get_thread_messages(request, metadata=get_metadata(endpoints.get_thread_messages))
    return response.messages
