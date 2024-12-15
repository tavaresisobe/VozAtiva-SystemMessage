from datetime import datetime, timedelta
from pydantic import BaseModel, Field, StrictStr

class UserEmailSenderInput(BaseModel):
    alert_id: StrictStr = Field(..., description="Alert id")
    name: StrictStr = Field(..., description="Name of user")
    email: StrictStr = Field(..., description="E-mail")
    date: StrictStr = Field(
        default_factory=lambda: datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        description="Current date and time in d/m/y format"
    )

    def create_new_alert_message(self) -> str:
        return f"""
        Prezado(a) {self.name},

        Sua denúncia foi registrada com sucesso! O código de identificação da sua denúncia é: {self.alert_id}.
        Nossa equipe e o órgão responsável estão cientes e irão analisar a situação.

        Em caso de dúvidas, entre em contato com nossa central de suporte.

        Atenciosamente,
        Equipe Voz Ativa.
        """

    def create_new_alert_subject(self) -> str:
        return f"Confirmação de registro da denúncia: {self.alert_id}"

    def update_alert_status_message(self) -> str:
        return f"""
        Prezado(a) {self.name},

        Informamos que o status da sua denúncia (ID: {self.alert_id}) foi atualizado. 
        Por favor, acesse o sistema para verificar os detalhes.

        Caso tenha alguma dúvida, entre em contato com nossa equipe.

        Atenciosamente,
        Equipe Voz Ativa.
        """

    def update_alert_status_subject(self) -> str:
        return f"Atualização do status da denúncia: {self.alert_id}"
