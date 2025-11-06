from concurrent import futures  # Импорт пула потоков для асинхронного выполнения

import grpc  # Импорт библиотеки grpc

import user_service_pb2  # Сгенерированные классы для работы с grpc-сообщениями
import user_service_pb2_grpc  # Сгенерированный класс для работы с сервисом


# Реализация grpc-сервиса
class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):
    """Реализация методов grpc-сервиса UserService"""

    def GetUser(self, request, context):
        """Метод GetUser обрабатывает входящий запрос"""
        print(f'Получен запрос к методу GetUser от пользователя: {request.username}')

        # Формируем и возвращаем ответное сообщение
        return user_service_pb2.GetUserResponse(message=f"Привет, {request.username}!")


# Функция для запуска grpc-сервера
def serve():
    """Функция создает и запускает grpc-сервер"""

    # Создаем сервер с использованием пула потоков (до 10 потоков)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Регистрируем сервис UserService на сервере
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)

    # Настраиваем сервер для прослушивания порта 50051
    server.add_insecure_port('[::]:50051')

    # Запускаем сервер
    server.start()
    print("grpc сервер запущен на порту 50051...")

    # Ожидаем завершения работы сервера
    server.wait_for_termination()


# Запуск сервера при выполнении скрипта
if __name__ == "__main__":
    serve()