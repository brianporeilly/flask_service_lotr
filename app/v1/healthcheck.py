from flask import request
import json


def healthcheck() -> (str, int):
    response = {"host": request.host, "message": "I'm healthy!"}
    return json.dumps(response), 200
