from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, ExerciseSchema, UpdateExerciseResponseSchema, UpdateExerciseRequestSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response


def assert_create_exercise_response(response: CreateExerciseResponseSchema, request: CreateExerciseRequestSchema):
    """
    Проверка, что фактический ответ на создание задания соответствует ожидаемому запросу

    :param request: запрос на создание задания
    :param response: ответ на создание задания
    :raises AssertionError: если хоть одно поле не совпадает
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверка, что фактические данные задания соответствует ожидаемым
    :param actual: фактические данные
    :param expected: ожидаемые данные
    :raises AssertionError: если одно поле не совпадает
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema

):
    """
    Проверка, что тело ответа на получение соответствует телу ответа на создание
    :param get_exercise_response: ответ на получение задания
    :param create_exercise_response: ответ на создание задания
    :raises AssertionError: если фактический ответ не соответствует ожидаемому
    """
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)


def assert_update_exercise_response(response: UpdateExerciseResponseSchema, request: UpdateExerciseRequestSchema):
    """
    Проверка, что фактический ответ соответствует запросу
    :param response: фактические данные
    :param request: ожидаемые данные
    :raises AssertionError: если хоть одно поле не совпадает
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")

def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Проверка если файл не найден
    :param actual: фактический ответ
    :raises AssertionError: если фактический ответ не соответствует "Exercise not found"
    """
    expected = InternalErrorResponseSchema(details="Exercise not found")

    assert_internal_error_response(actual, expected)

def assert_get_exercises_responses(get_exercise_response: GetExercisesResponseSchema,
                                   create_exercises_response: list[CreateExerciseResponseSchema]):
    """
    Проверяет, что ответ получение списка заданий соответствует списку ответа создания заданий
    :param get_exercise_response: Ответ API при запросе получения списка заданий
    :param create_exercises_response: Ответ API при создании списка заданий
    """
    assert_length(get_exercise_response.exercises, create_exercises_response, "exercises")

    for index, create_exercise in enumerate(create_exercises_response):
        assert_exercise(get_exercise_response.exercises[index], create_exercise.exercise)


