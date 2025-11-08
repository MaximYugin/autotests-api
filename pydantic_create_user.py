import uuid

from pydantic import BaseModel, HttpUrl, EmailStr, Field


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_mame: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса создания пользователя.
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_mame: str = Field(alias="middleName")


class CreateUserResponseSchema(UserSchema):
    """
    Описание структуры ответа на создание пользователя.
    """
    user: UserSchema
