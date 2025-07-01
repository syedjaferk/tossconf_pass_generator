from pydantic import BaseModel, EmailStr, Field, SecretStr
from typing import List


class Email(BaseModel):
    from_mail_id: EmailStr
    app_password: SecretStr
    to_mail_id: EmailStr
    receiver_name: str
    subject: str
    html_body: str
    attachments: List[str] = Field(default_factory=list)
