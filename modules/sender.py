import requests

class Sender:
    def __init__(self, base_url, auth=None):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json"
        }
        if auth:
            self.headers["Authorization"] = auth

    def get(self, path):
        url = self.base_url + path
        return requests.get(url, headers=self.headers)

    def post(self, path, payload):
        url = self.base_url + path
        return requests.post(url, json=payload, headers=self.headers)

    def put(self, path, payload):
        url = self.base_url + path
        return requests.put(url, json=payload, headers=self.headers)

    def delete(self, path):
        url = self.base_url + path
        return requests.delete(url, headers=self.headers)