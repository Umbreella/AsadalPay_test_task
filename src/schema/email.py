from pydantic import BaseModel, EmailStr


class EmailCreateSchema(BaseModel):
    to: EmailStr
    subject: str
    message: str
