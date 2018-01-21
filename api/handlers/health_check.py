import falcon
import json


class HealthCheckResource(object):
    @staticmethod
    def on_get(request, response):
        response.status = falcon.HTTP_200
        response.data = json.dumps({"status": "OK"}).encode()
