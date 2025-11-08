from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from typing import List


class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    maxScore: int | None
    minScore: int | None
    description: str
    preview_file: FileSchema = Field(alias="previewFile")  # Вложенная структура файла
    estimatedTime: str | None
    created_by_user: UserSchema = Field(alias="createdByUser")  # Вложенная структура пользователя


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списков курсов
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class GetCoursesResponseSchema(BaseModel):
    courses: List[CourseSchema]


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на получение курса
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")  # Вложенная структура файла
    created_by_user_id: str = Field(alias="createdByUserId")  # Вложенная структура пользователя


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение курса
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")

class GetCourseResponseSchema(BaseModel):
    course: CourseSchema