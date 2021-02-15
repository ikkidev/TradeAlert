import json


def get_secret(path):
    with open(path, 'r') as secret:
        data = secret.read()

    secret_json = json.loads(data)
    return secret_json
