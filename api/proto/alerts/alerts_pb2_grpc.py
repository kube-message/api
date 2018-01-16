# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import alerts_pb2 as alerts__pb2


class AlertsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAlertsForUser = channel.unary_unary(
        '/alerts.Alerts/GetAlertsForUser',
        request_serializer=alerts__pb2.GetAlertsForUserRequest.SerializeToString,
        response_deserializer=alerts__pb2.GetAlertsForUserResponse.FromString,
        )
    self.MarkAlertSeen = channel.unary_unary(
        '/alerts.Alerts/MarkAlertSeen',
        request_serializer=alerts__pb2.MarkAlertSeenRequest.SerializeToString,
        response_deserializer=alerts__pb2.MarkAlertSeenResponse.FromString,
        )
    self.SendAlert = channel.unary_unary(
        '/alerts.Alerts/SendAlert',
        request_serializer=alerts__pb2.SendAlertRequest.SerializeToString,
        response_deserializer=alerts__pb2.SendAlertResponse.FromString,
        )


class AlertsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetAlertsForUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MarkAlertSeen(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendAlert(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AlertsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAlertsForUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetAlertsForUser,
          request_deserializer=alerts__pb2.GetAlertsForUserRequest.FromString,
          response_serializer=alerts__pb2.GetAlertsForUserResponse.SerializeToString,
      ),
      'MarkAlertSeen': grpc.unary_unary_rpc_method_handler(
          servicer.MarkAlertSeen,
          request_deserializer=alerts__pb2.MarkAlertSeenRequest.FromString,
          response_serializer=alerts__pb2.MarkAlertSeenResponse.SerializeToString,
      ),
      'SendAlert': grpc.unary_unary_rpc_method_handler(
          servicer.SendAlert,
          request_deserializer=alerts__pb2.SendAlertRequest.FromString,
          response_serializer=alerts__pb2.SendAlertResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'alerts.Alerts', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
