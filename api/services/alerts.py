from collections import namedtuple

import grpc

from ..proto import alerts
from .shared import get_metadata
from ..utils import get_logger


logger = get_logger()


channel = grpc.insecure_channel("alerts:8081")
client = alerts.AlertsStub(channel)


e_points = [
    "get_alerts_for_user",
    "mark_alert_seen",
    "send_alert",
]
Endpoints = namedtuple("Endpoints", e_points)
endpoints = Endpoints(*e_points)


def get_thread_action_path(thread_id):
    return "/threads/{}/messages".format(thread_id)


def get_alerts_for_user(user_id):
    request = alerts.GetAlertsForUserRequest(user_id=user_id)
    response = client.get_alerts_for_user(request, metadata=get_metadata(endpoints.get_alerts_for_user))
    return response.alerts


def mark_alert_seen(user_id, uniq):
    request = alerts.MarkAlertSeenRequest(user_id=user_id, uniq=uniq)
    response = client.mark_alert_seen(request, metadata=get_metadata(endpoints.mark_alert_seen))
    if response.error.message:
        return False
    return True


def send_alert(alert):
    request = alerts.SendAlertRequest(alert=alert)
    response = client.SendAlert(request, metadata=get_metadata(endpoints.send_alert))
    return response.error


async def send_alerts_for_thread_participants(participants, thread_id):
    for participant in participants:
        alert = alerts.Alert(
            recipient_id=participant,
            thread_id=thread_id,
            message="New message",
            action_path=get_thread_action_path(thread_id),
        )
        send_alert(alert)
