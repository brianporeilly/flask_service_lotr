import json
import uuid

import sentry_sdk


class AppError(Exception):
    def __init__(self, message, status_code, original_exception=None):
        self.id = str(uuid.uuid4())
        self.message = message
        self.status_code = status_code
        self.original_exception = original_exception
        sentry_sdk.capture_exception(self.original_exception, scope=self.to_dict())
        super().__init__(self.message)

    def to_dict(self):
        return {
            "error_id": self.id,
            "message": "An error has occurred, please provide the above error_id to the support team",
            "status_code": self.status_code,
        }

    def to_json(self):
        return json.dumps(self.to_dict())
