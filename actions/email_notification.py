import settings
from utils import system_message
from http import HTTPStatus
from starlette.requests import Request
from services.email_notification import EmailNotificationServices
from parsers.email.user_email_notification_parser import UserEmailSenderInput
from parsers.email.gov_email_notification_parser import GovEmailSenderInput
from utils import response_generator
from exceptions.notification_service import(
    ServerException,
    RecipientException,
    DataRefusedException,
    AuthenticationException
)
LOGGER = settings.LOGGER

class SendEmailAction:

    async def send_email_to_user_for_alert_status_upadate_action(self, request: Request):
        LOGGER.debug (f"Descompactando requisição")
        body: dict = await request.json()
        alert_id = body.get("alert_id")
        name = body.get("name")
        email = body.get("email")

        try:
            notification_services = EmailNotificationServices()
            input_data = UserEmailSenderInput(alert_id=alert_id,
                                              name=name,
                                              email=email)
            await notification_services.user_email_sender_for_update_alert_status(input=input_data)
            return response_generator.generate(
                message=[system_message.SUCESS_OPERATION],
                data={},
                status_code=HTTPStatus.OK,
            )
        except RecipientException:
            return response_generator.generate(
                message=[system_message.RECIPIENT_EXCEPTION],
                data={},
                status_code=HTTPStatus.NOT_FOUND,
            )
        except DataRefusedException:
            return response_generator.generate(
                message=[system_message.DATA_EXCEPTION],
                data={},
                status_code=HTTPStatus.FORBIDDEN,
            )
        except AuthenticationException:
            return response_generator.generate(
                message=[system_message.AUTHENTICATE_ERROR],
                data={},
                status_code=HTTPStatus.UNAUTHORIZED,
            )
        except ServerException:
            return response_generator.generate(
                message=[system_message.CRITICAL_ERROR],
                data={},
                status_code=HTTPStatus.BAD_GATEWAY,
            )
        except Exception:
            return response_generator.generate(
                message=[system_message.CRITICAL_ERROR],
                data={},
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            )

    async def send_email_to_user_for_new_alert_action(self, request: Request):
        LOGGER.debug (f"Descompactando requisição")
        body: dict = await request.json()
        alert_id = body.get("alert_id")
        name = body.get("name")
        email = body.get("email")

        try:
            notification_services = EmailNotificationServices()
            input_data = UserEmailSenderInput(alert_id=alert_id,
                                              name=name,
                                              email=email)
            await notification_services.user_email_sender_for_new_alert(input=input_data)
            return response_generator.generate(
                message=[system_message.SUCESS_OPERATION],
                data={},
                status_code=HTTPStatus.OK,
            )
        except RecipientException:
            return response_generator.generate(
                message=[system_message.RECIPIENT_EXCEPTION],
                data={},
                status_code=HTTPStatus.NOT_FOUND,
            )
        except DataRefusedException:
            return response_generator.generate(
                message=[system_message.DATA_EXCEPTION],
                data={},
                status_code=HTTPStatus.FORBIDDEN,
            )
        except AuthenticationException:
            return response_generator.generate(
                message=[system_message.AUTHENTICATE_ERROR],
                data={},
                status_code=HTTPStatus.UNAUTHORIZED,
            )
        except ServerException:
            return response_generator.generate(
                message=[system_message.CRITICAL_ERROR],
                data={},
                status_code=HTTPStatus.BAD_GATEWAY,
            )
        except Exception:
            return response_generator.generate(
                message=[system_message.CRITICAL_ERROR],
                data={},
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            )

    async def send_email_to_gov_for_new_user_alert(self, request: Request):
        LOGGER.debug (f"Descompactando requisição")
        body : dict = await request.json()
        alert_id= body.get("alert_id")
        organization_name = body.get("name")
        email = body.get("email")
        title = body.get("title")

        try:
            notification_services = EmailNotificationServices()
            input_data = GovEmailSenderInput(alert_id=alert_id,
                                             gov_name=organization_name,
                                             email=email,
                                             title=title)
            await notification_services.gov_email_sender_for_new_alert_has_create(input=input_data)
            return response_generator.generate(
                message=[system_message.SUCESS_OPERATION],
                data={},
                status_code=HTTPStatus.OK,
            )
        except RecipientException:
            return response_generator.generate(
                message=[system_message.RECIPIENT_EXCEPTION],
                data={},
                status_code=HTTPStatus.NOT_FOUND,
            )
        except DataRefusedException:
            return response_generator.generate(
                message=[system_message.DATA_EXCEPTION],
                data={},
                status_code=HTTPStatus.FORBIDDEN,
            )
        except AuthenticationException:
            return response_generator.generate(
                message=[system_message.AUTHENTICATE_ERROR],
                data={},
                status_code=HTTPStatus.UNAUTHORIZED,
            )
        except ServerException:
            return response_generator.generate(
                message=[system_message.CRITICAL_ERROR],
                data={},
                status_code=HTTPStatus.BAD_GATEWAY,
            )
        except Exception:
            return response_generator.generate(
                message=[system_message.CRITICAL_ERROR],
                data={},
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            )
