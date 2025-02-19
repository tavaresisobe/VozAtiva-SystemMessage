from datetime import datetime, timedelta
from pydantic import BaseModel, Field, StrictStr

class GovEmailSenderInput(BaseModel):
    alert_id: StrictStr = Field(..., description="Alert id")
    title: StrictStr = Field(..., description="Alert title")
    gov_name: StrictStr = Field(..., description="Name of organization")
    email: StrictStr = Field(..., description="E-mail")
    date: StrictStr = Field(
        default_factory=lambda: datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        description="Current date and time in d/m/y format"
    )

    def new_alert_for_gov_message(self) -> str:
        return f"""
        Prezado(a) {self.gov_name},

        Uma nova denúncia foi registrada e atribuída à sua organização para análise e providências.
        Os detalhes da denúncia são os seguintes:

        - ID da denúncia: {self.alert_id}
        - Título da denúncia: {self.title}
        - Data e horário do registro: {self.date}

        Por favor, acesse o sistema para mais informações e para gerenciar esta denúncia.

        Atenciosamente,
        Equipe Voz Ativa.
        """

    def new_alert_for_gov_subject(self) -> str:
        return f"Nova denúncia atribuída: {self.title}"
