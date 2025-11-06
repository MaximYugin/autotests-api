from concurrent import futures  # Импорт пула потоков для асинхронного выполнения

import grpc  # Импорт библиотеки grpc

import course_service_pb2  # Сгенерированные классы для работы с grpc-сообщениями
import course_service_pb2_grpc  # Сгенерированный класс для работы с сервисом

class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    def GetCourse(self, request, context):
        print(f"Запрос GetCourse {request.course_id}")
        return course_service_pb2.GetCourseResponse(course_id=request.course_id, title='3213', description="Будем изучать написание API автотестов")


def serv():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("grpc сервер запущен на порту 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serv()



