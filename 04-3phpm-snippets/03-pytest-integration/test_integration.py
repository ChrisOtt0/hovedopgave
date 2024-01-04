from constants import *
from pytest_check import check


class TestClassIntegration(AbstractTestClass):
    URL = BASEURL + "/Integration"

    # Valid Read
    def test_read1(self):
        # Arrange
        testURL = self.URL + "/Read1"
        data = {
            "functionCode": ██,
            "address": ██,
            "count": ██,
            "data": ██
        }

        # Act
        response = self.try_act(testURL, data)
        data = response.json()

        timestamp = data["timestamp"]
        commandStateDn = data["data"]["CommandStateDn"]
        commandStateErr = data["data"]["CommandStateErr"]
        timeElapsed = data["data"]["TimeElapsed"]
        result = data["data"]["Result"]

        # Assert
        assert response.status_code == 200

        check.equal(commandStateDn, True)
        check.equal(commandStateErr, False)