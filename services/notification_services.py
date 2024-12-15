import settings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from parsers.email.user_email_notification_parser import UserEmailSenderInput
from parsers.email.gov_email_notification_parser import GovEmailSenderInput
from smtplib import (
    SMTPException,
    SMTPAuthenticationError,
    SMTPConnectError,
    SMTPServerDisconnected,
    SMTPRecipientsRefused,
    SMTPDataError,
    SMTPHeloError,
)
from exceptions.notification_service import(
    ServerException,
    RecipientException,
    DataRefusedException,
    AuthenticationException
)

LOGGER = settings.LOGGER

class SMTPNotificationServices:
    def __init__(self):
        self.email_user = settings.EMAIL
        self.app_password = settings.PASS
        self.smtp_server = settings.SMTP_SERVER
        self.port = settings.SERVER_PORT

    def send_email_to_user(self, input: UserEmailSenderInput, body: str, subject: str) -> None:
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_user
            msg['To'] = input.email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            self.send_mail(msg=msg)
        except Exception as error:
            LOGGER.error("Email não enviado")
            raise error

    def send_email_to_gov(self, input: GovEmailSenderInput, body: str, subject: str) -> None:
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_user
            msg['To'] = input.email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            self.send_mail(msg=msg)
        except Exception as error:
            LOGGER.error("Email não enviado")
            raise error

    def send_mail(self, msg: MIMEMultipart) -> None:
        try:
            LOGGER.debug("Enviando email")
            with smtplib.SMTP(self.smtp_server, self.port, local_hostname="localhost.localdomain") as server:
                #server.set_debuglevel(1)
                server.ehlo()
                server.starttls()
                server.login(self.email_user, self.app_password)
                server.send_message(msg)
            LOGGER.debug("Email enviado")
        except SMTPAuthenticationError:
            LOGGER.error("Falha na autenticação. Verifique o e-mail e a senha configurados.")
            raise AuthenticationException
        except SMTPConnectError:
            LOGGER.error("Não foi possível conectar ao servidor SMTP. Verifique a configuração do servidor.")
            raise ServerException
        except SMTPServerDisconnected:
            LOGGER.error("Conexão com o servidor SMTP foi encerrada inesperadamente.")
            raise ServerException
        except SMTPDataError:
            LOGGER.error("Erro ao enviar os dados para o servidor SMTP.")
            raise DataRefusedException
        except SMTPRecipientsRefused:
            LOGGER.error("O servidor SMTP recusou todos os destinatários.")
            raise RecipientException
        except SMTPHeloError:
            LOGGER.error("O servidor SMTP rejeitou o comando HELO/EHLO.")
            raise ServerException
        except SMTPException as e:
            LOGGER.error(f"Erro genérico de SMTP: {e}")
            raise ServerException
        except Exception as e:
            LOGGER.error(f"Erro inesperado ao enviar o e-mail: {e}")
            raise ServerException
