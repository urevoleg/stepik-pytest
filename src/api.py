import requests

def get_data():
    response = requests.get("http://example.com")
    response.raise_for_status()
    return response.json()


def get_status_code_from_response(response):
    return response.status_code