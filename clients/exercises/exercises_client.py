from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение упражнений
    """
    courseId: str


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


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры на обновление курса
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """
    def get_exercises_api(self, query) -> Response:
        """
        Метод получения упражнений
        :param query: словарь с courseId
        :return: ответ от сервера вида httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def create_exercise_api(self, request) -> Response:
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

    def update_exercise_api(self, exercise_id: str, request) -> Response:
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
