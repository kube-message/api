import json


def message_proto_to_dict(proto):
    return {
        "id": proto.id,
        "sender_id": proto.sender_id,
        "text": proto.text,
        "thread_id": proto.thread_id
    }


def message_proto_to_json(proto):
    return json.dumps(message_proto_to_dict(proto)).encode()


def message_proto_list_to_json(messages):
    return json.dumps([message_proto_to_dict(message) for message in messages]).encode()


def thread_proto_to_dict(proto):
    return {
        "id": proto.id,
        "participants": list(proto.participants)
    }


def thread_proto_to_json(proto):
    return json.dumps(thread_proto_to_dict(proto)).encode()


def thread_proto_list_to_json(threads):
    return json.dumps([thread_proto_to_dict(thread) for thread in threads]).encode()


def alert_proto_to_dict(proto):
    return {
        "recipient_id": proto.recipient_id,
        "uniq": proto.uniq,
        "thread_id": proto.thread_id,
        "message": proto.message,
        "timestamp": proto.timestamp,
        "action_path": proto.action_path,
        "ttl": proto.ttl,
        "seen": proto.seen,
    }


def alert_proto_to_json(proto):
    return json.dumps(alert_proto_to_dict(proto)).encode()


def alert_proto_list_to_json(alerts):
    return json.dumps([alert_proto_to_dict(alert) for alert in alerts]).encode()

