import requests

class ReqResClient:
    BASE_URL = "https://reqres.in/api"

    @staticmethod
    def get_user(user_id):
        response = requests.get(f"{ReqResClient.BASE_URL}/users/{user_id}")
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
            