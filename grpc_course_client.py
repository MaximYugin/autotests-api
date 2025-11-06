import grpc  # Импорт библиотеки grpc

import course_service_pb2  # Сгенерированные классы для работы с grpc-сообщениями
import course_service_pb2_grpc  # Сгенерированный класс для работы с сервисом

# Устанавливаем соединение с сервером
channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

# Отправляем запрос
response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id='1'))
print(response)

