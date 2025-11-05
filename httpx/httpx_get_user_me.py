import httpx  # Импортируем библиотеку HTTPX

# # Данные для входа в систему
# login_payload = {
#     "email": "user@example.com",
#     "password": "string"
# }
#
# # Выполняем запрос на аутентификацию
# login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
# login_response_data = login_response.json()
#
# # Выводим полученные токены
# print("Login response:", login_response_data)
# print("Status Code:", login_response.status_code)
#
# # Формируем payload для обновления токена
# refresh_payload = {
#     "refreshToken": login_response_data["token"]["refreshToken"]
# }
#
# # Выполняем запрос на обновление токена
# refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
# refresh_response_data = refresh_response.json()
#
# # Выводим обновленные токены
# print("Refresh response:", refresh_response_data)
# print("Status Code:", refresh_response.status_code)

payload_login = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload_login)
login_response_data = login_response.json()
print("login_response_data:", login_response_data)
print(login_response.status_code)
login_response_token = login_response_data["token"]["accessToken"]

headers = {"Authorization": f"Bearer {login_response_token}"}
response_me = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
response_me_data = response_me.json()
print("response_me_data:", response_me_data)
print(response_me.status_code)
