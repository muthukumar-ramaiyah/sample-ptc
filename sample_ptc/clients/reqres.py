import requests

class ReqResClient:
    BASE_URL = "https://reqres.in/api"
    HEADERS = {
        "Content-Type": "application/json",
        'x-api-key': 'reqres-free-v1'
        }

    @staticmethod
    def get_user(user_id):

        response = requests.get(f"{ReqResClient.BASE_URL}/users/{user_id}", headers=ReqResClient.HEADERS)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    @staticmethod
    def create_user(name, job):
        payload = {"name": name, "job": job}
        response = requests.post(f"{ReqResClient.BASE_URL}/users", json=payload, headers=ReqResClient.HEADERS)
        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()

