from flask import Blueprint
from app.v1.healthcheck import healthcheck
from app.v1.lotr_quote import lotr_quote

v1_api = Blueprint("v1_api", __name__)

v1_api.add_url_rule("/healthcheck/", view_func=healthcheck, methods=["GET"])
v1_api.add_url_rule("/lotr-quote/<name>", view_func=lotr_quote, methods=["GET"])
