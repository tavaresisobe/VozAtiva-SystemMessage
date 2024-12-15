import settings
from services.notification_services import SMTPNotificationServices
from parsers.email.user_email_notification_parser import UserEmailSenderInput
from parsers.email.gov_email_notification_parser import GovEmailSenderInput
from services.notification_services import SMTPNotificationServices

LOGGER = settings.LOGGER

class EmailNotificationServices():
    def __init__(self):
        self.smtp_services = SMTPNotificationServices()

    async def user_email_sender_for_new_alert(self, input: UserEmailSenderInput) -> None:
        LOGGER.debug("Criando conteúdo do email")
        content = input.create_new_alert_message()
        title = input.create_new_alert_subject()
        self.smtp_services.send_email_to_user(input=input, body=content, subject=title)

    async def user_email_sender_for_update_alert_status(self, input: UserEmailSenderInput) -> None:
        LOGGER.debug("Criando conteúdo do email")
        content = input.update_alert_status_message()
        title = input.update_alert_status_subject()
        self.smtp_services.send_email_to_user(input=input, body=content, subject=title)

    async def gov_email_sender_for_new_alert_has_create(self, input: GovEmailSenderInput) -> None:
        LOGGER.debug("Criando conteúdo do email")
        content = input.new_alert_for_gov_message()
        title = input.new_alert_for_gov_subject()
        self.smtp_services.send_email_to_gov(input=input, body=content, subject=title)
