from collections import namedtuple

import grpc

from ..proto import messenger
from .shared import get_metadata
from ..utils import get_logger


logger = get_logger()

channel = grpc.insecure_channel("messenger:8081")
client = messenger.MessengerStub(channel)


e_points = [
    "send_message",
    "get_threads_for_user",
    "get_thread_messages",
    "create_thread",
    "get_thread_detail",
]
Endpoints = namedtuple("Endpoints", e_points)
endpoints = Endpoints(*e_points)


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


def is_user_in_thread(user_id, thread_id):
    thread = get_thread_detail(thread_id)
    return user_id in set(thread.participants)


def send_message(thread_id, sender_id, text):
    message = messenger.Message(thread_id=thread_id, sender_id=sender_id, text=text)
    request = messenger.SendMessageRequest(message=message)
    response = client.send_message(request, metadata=get_metadata(endpoints.send_message))
    return response.message


def get_thread_detail(thread_id):
    request = messenger.GetThreadDetailRequest(thread_id=thread_id)
    response = client.get_thread_detail(request, metadata=get_metadata(endpoints.get_thread_detail))
    return response.thread


def get_threads_for_user(user_id):
    request = messenger.GetThreadsForUserRequest(user_id=user_id)
    response = client.get_threads_for_user(request, metadata=get_metadata(endpoints.get_threads_for_user))
    return response.threads
