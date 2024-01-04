from constants import *
from pytest_check import check


class TestClassSystem(AbstractTestClass):
    URL = BASEURL + "/System"

    # WebserverLogin1 - Valid login
    def test_login1(self):
        # Arrange
        testURL = self.URL + "/WebserverLogin1"
        data = {
            "username": "user",
            "password": "pass"
        }

        # Act
        response = self.try_act(testURL, data)
        data = response.json()

        timestamp = data["timestamp"]
        httpCode = data["data"]["HttpCode"]
        httpHeaders = data["data"]["HttpHeaders"]
        httpBody = data["data"]["HttpBody"]
        timeElapsed = data["data"]["TimeElapsed"]

        # Assert
        assert response.status_code == 200

        check.equal(httpCode, 200)