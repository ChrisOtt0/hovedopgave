import requests


BASEURL = "█████████████"


class AbstractTestClass:
    requestSession = requests.Session()
    requestSession.verify = False

    def try_act(self, url, data):
        return self.requestSession.post(url, json=data)