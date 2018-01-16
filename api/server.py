from wsgiref import simple_server

import falcon

from . import handlers
from .middleware import ResponseLoggerMiddleware


app = falcon.API(middleware=[ResponseLoggerMiddleware()])

"""
Messages URL"s
"""
# app.add_route("/messages/{message_id}", handlers.MessageDetailResource())

"""
Thread URL"s
"""
app.add_route("/threads", handlers.ThreadListResource())
app.add_route("/threads/{thread_id:int}", handlers.ThreadDetailResource())
app.add_route("/threads/users/{user_id:int}", handlers.ThreadUserListResource())
app.add_route("/threads/{thread_id:int}/messages", handlers.ThreadMessageListResource())

"""
Health Check
"""
app.add_route("/shc", handlers.HealthCheckResource())


if __name__ == "__main__":
    httpd = simple_server.make_server("0.0.0.0", 8080, app)
    httpd.serve_forever()
