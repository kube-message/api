import json

from . import config


def message_proto_to_json(proto):
    return json.dumps({
        "id": proto.id,
        "sender_id": proto.sender_id,
        "text": proto.text,
        "thread_id": proto.thread_id
    }).encode()


def thread_proto_to_json(proto):
    return json.dumps({
        "id": proto.id,
        "participants": list(proto.participants)
    }).encode()
