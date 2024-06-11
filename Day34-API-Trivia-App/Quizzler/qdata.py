import requests


def get_new_questions():
    req_params = {
        "amount": 10,
        "type": "boolean"
    }
    response = requests.get(url="https://opentdb.com/api.php",
                            params=req_params)
    if response.status_code == 200:
        question_data = response.json()["results"]
        return question_data
    else:
        response.raise_for_status()