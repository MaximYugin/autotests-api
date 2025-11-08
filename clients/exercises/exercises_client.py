
from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response

from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.users.private_users_client import PrivateUsersClient



class Exercise:
    """
    Описание структуры упражнений
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение упражнений
    """
    courseId: str


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа упражнений
    """
    exercises: list[Exercise]


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа создания упражнения
    """
    exercise: Exercise


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на обновление упражнения
    """
    exercise: Exercise


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на получение упражнения
    """
    exercise: Exercise


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения упражнений
        :param query: словарь с courseId
        :return: ответ от сервера вида httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания упражнения
        :param request: словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ от сервера вида httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения
        :param exercise_id: Идентификатор упражнения
        :return: ответ от сервера вида httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления упражнения
        :param exercise_id: Идентификатор упражнения
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ от сервера вида httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения
        :param exercise_id: Идентификатор упражнения
        :return: ответ от сервера вида httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод получения упражнения
        :param exercise_id: Идентификатор упражнения
        :return: ответ от сервера вида httpx.Response
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод получения упражнений
        :param query: словарь с courseId
        :return: ответ от сервера вида httpx.Response
        """
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Метод создания упражнения
        :param request: словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ от сервера вида httpx.Response
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Метод обновления упражнения
        :param exercise_id: Идентификатор упражнения
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ от сервера вида httpx.Response
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


# Добавляем builder для ExercisesClient
def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
