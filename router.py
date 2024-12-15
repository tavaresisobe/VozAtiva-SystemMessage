from starlette.routing import Route
from actions.email_notification import SendEmailAction

BASE_PATH = "/notification/v1"

class Router:

    def get_routes():
        return [
            Route(
                 f"{BASE_PATH}/sendemail/gov/new-alert",
                 SendEmailAction().send_email_to_gov_for_new_user_alert,
                 methods=["POST"]
            ),
            Route(
                f"{BASE_PATH}/sendemail/user/update-alert-status",
                SendEmailAction().send_email_to_user_for_alert_status_upadate_action,
                methods=["POST"]
            ),
            Route(
                f"{BASE_PATH}/sendemail/user/create-alert",
                SendEmailAction().send_email_to_user_for_new_alert_action,
                methods=["POST"]
            )
        ]
