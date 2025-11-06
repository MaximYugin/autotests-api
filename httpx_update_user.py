import httpx

from tools.fakers import get_random_email

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print("Create user:", create_user_response_data)

auth_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

auth_user_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=auth_payload)
auth_user_response_data = auth_user_response.json()
print("Auth user:", auth_user_response_data)

patch_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
patch_user_accessToken = {"Authorization": f"Bearer {auth_user_response_data['token']['accessToken']}"}
patch_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
                                  json=patch_user_payload, headers=patch_user_accessToken)
patch_user_response_data = patch_user_response.json()
print("Обновлена почта", patch_user_response_data)

