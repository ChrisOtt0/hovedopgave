from constants import *
from pytest_check import check


class TestClassFunctionalMeassurements(AbstractFunctionalTestClass):
    # region Meassurements

    # Single Phase Voltage - Read
    # Upper bound:
    # Lower bound:
    def test_single_phase_read_voltage(self):
        # Arrange
        testURL = self.URL + "/SingleMeassurement"
        _input = {
            "functionCode": ██,
            "address": ██,
            "count": ██,
            "data": []
        }
        upperBound = 250.0
        lowerBound = 0.0

        # Act
        if not self.try_act(testURL, _input):
            raise ConnectionError(f"Connection to the 3PhPM RPi test-server could not be established. Provided the following URL: {testURL}")

        # Collect & Assert
        response = self.get_response()
        assert response.status_code == HttpStatusCode.Ok, f"Request to 3PhPM RPi test-server failed. Received HTTP status code: {response.status_code}"
        
        data = response.json()

        timestamp = data["timestamp"]
        commandStateDn = data["data"]["CommandStateDn"]
        commandStateErr = data["data"]["CommandStateErr"]
        commResponse = data["data"]["CommResponse"]
        timeElapsed = data["data"]["TimeElapsed"]
        result = data["data"]["Result"]

        with check:
            assert commandStateDn == True, f"Single Phase Read Voltage command failed. Expected command to succeed. Provided Modbus request: {_input}"
        with check:
            assert commandStateErr == False, f"Single Phase Read Voltage command failed. Expected command to succeed. Provided Modbus request: {_input}"

        assert commResponse == CommResponse.Ack, f"Single Phase Read Voltage command failed. Expected command to suceed. Received CommResponse: {CommResponse(commResponse).name}"
        result = result["0"]
        assert result <= upperBound, f"Single Phase Read Voltage command succeeded, but was out of acceptable bounds. Received voltage: {result}"
        assert result >= lowerBound, f"Single Phase Read Voltage command succeeded, but was out of acceptable bounds. Received voltage: {result}"

        
    # 3-Phase Voltage - Read
    # Upper bound:
    # Lower bound:
    def test_3_phase_read_voltage(self):
        # Arrange
        testURL = self.URL + "/SingleMeassurement"
        _input = {
            "functionCode": ██,
            "address": ██,
            "count": ██,
            "data": []
        }
        upperBound = 230.0
        lowerBound = 0.0

        # Act
        if not self.try_act(testURL, _input):
            raise ConnectionError(f"Connection to the 3PhPM RPi test-server could not be established. Provided the following URL: {testURL}")

        # Collect & Assert
        response = self.get_response()
        assert response.status_code == HttpStatusCode.Ok, f"Request to 3PhPM RPi test-server failed. Received HTTP status code: {response.status_code}"
        
        data = response.json()

        timestamp = data["timestamp"]
        commandStateDn = data["data"]["CommandStateDn"]
        commandStateErr = data["data"]["CommandStateErr"]
        commResponse = data["data"]["CommResponse"]
        timeElapsed = data["data"]["TimeElapsed"]
        result = data["data"]["Result"]

        with check:
            assert commandStateDn == True, f"3-Phase Read Voltage command failed. Expected command to succeed. Provided Modbus request: {_input}"
        with check:
            assert commandStateErr == False, f"3-Phase Read Voltage command failed. Expected command to succeed. Provided Modbus request: {_input}"

        assert commResponse == CommResponse.Ack, f"3-Phase Read Voltage command failed. Expected command to succeed. Received CommResponse: {CommResponse(commResponse).name}"
        result = result["0"]
        assert result <= upperBound, f"3-Phase Read Voltage command succeeded, but was out of acceptable bounds. Received voltage: {result}"
        assert result >= lowerBound, f"3-Phase Read Voltage command succeeded, but was out of acceptable bounds. Received voltage: {result}"

    #endregion


class TestClassFunctionalWebserver(AbstractFunctionalTestClass):
    #region WebserverLogin

    # WebserverLogin1 - Valid login
    def test_login1(self):
        # Arrange
        testURL = self.URL + "/WebserverLogin1"
        _input = {
            "username": "██",
            "password": "██"
        }

        # Act
        if not self.try_act(testURL, _input):
            raise ConnectionError(f"Connection to the 3PhPM RPi test-server could not be established. Provided the following URL: {testURL}")
        
        # Collect & Assert
        response = self.get_response()
        assert response.status_code == HttpStatusCode.Ok, f"Request to 3PhPM RPi test-server failed. Received HTTP status code: {response.status_code}"
        
        data = response.json()

        timestamp = data["timestamp"]
        httpCode = data["data"]["HttpCode"]
        httpHeaders = data["data"]["HttpHeaders"]
        httpBody = data["data"]["HttpBody"]
        timeElapsed = data["data"]["TimeElapsed"]

        assert httpCode == HttpStatusCode.Ok, f"Login request to 3PhPM did not succeed as expected. Received status {HttpStatusCode(httpCode).name}: {httpBody}"

    
    # WebserverLogin1 - Invalid username
    def test_login2(self):
        # Arrange
        testURL = self.URL + "/WebserverLogin2"
        _input = {
            "username": "invalid",
            "password": "██"
        }

        # Act
        if not self.try_act(testURL, _input):
            raise ConnectionError(f"Connection to the 3PhPM RPi test-server could not be established. Provided the following URL: {testURL}")
        
        # Collect & Assert
        response = self.get_response()
        assert response.status_code == HttpStatusCode.Ok, f"Request to 3PhPM RPi test-server failed. Received HTTP status code: {response.status_code}"
        
        data = response.json()

        timestamp = data["timestamp"]
        httpCode = data["data"]["HttpCode"]
        httpHeaders = data["data"]["HttpHeaders"]
        httpBody = data["data"]["HttpBody"]
        timeElapsed = data["data"]["TimeElapsed"]

        assert httpCode == HttpStatusCode.Unauthorized, f"Login request to 3PhPM did not fail as expected. Received status {HttpStatusCode(httpCode).name}: {httpBody}"


    # WebserverLogin2 - Invalid password
    def test_login3(self):
        # Arrange
        testURL = self.URL + "/WebserverLogin3"
        _input = {
            "username": "██",
            "password": "invalid"
        }

        # Act
        if not self.try_act(testURL, _input):
            raise ConnectionError(f"Connection to the 3PhPM RPi test-server could not be established. Provided the following URL: {testURL}")
        
        # Collect & Assert
        response = self.get_response()
        assert response.status_code == HttpStatusCode.Ok, f"Request to 3PhPM RPi test-server failed. Received HTTP status code: {response.status_code}"
        
        data = response.json()

        timestamp = data["timestamp"]
        httpCode = data["data"]["HttpCode"]
        httpHeaders = data["data"]["HttpHeaders"]
        httpBody = data["data"]["HttpBody"]
        timeElapsed = data["data"]["TimeElapsed"]

        assert httpCode == HttpStatusCode.Unauthorized, f"Login request to 3PhPM did not fail as expected. Received status {HttpStatusCode(httpCode).name}: {httpBody}"


    # WebserverLogin3 - Invalid username and password
    def test_login4(self):
        # Arrange
        testURL = self.URL + "/WebserverLogin4"
        _input = {
            "username": "invalid",
            "password": "invalid"
        }

        # Act
        if not self.try_act(testURL, _input):
            raise ConnectionError(f"Connection to the 3PhPM RPi test-server could not be established. Provided the following URL: {testURL}")
        
        # Collect & Assert
        response = self.get_response()
        assert response.status_code == HttpStatusCode.Ok, f"Request to 3PhPM RPi test-server failed. Received HTTP status code: {response.status_code}"
        
        data = response.json()

        timestamp = data["timestamp"]
        httpCode = data["data"]["HttpCode"]
        httpHeaders = data["data"]["HttpHeaders"]
        httpBody = data["data"]["HttpBody"]
        timeElapsed = data["data"]["TimeElapsed"]

        assert httpCode == HttpStatusCode.Unauthorized, f"Login request to 3PhPM did not fail as expected. Received status {HttpStatusCode(httpCode).name}: {httpBody}"


    # WebserverLogin4 - Cannot access /readings pre-login
    def test_login5(self):
        # Arrange
        testURL = self.URL + "/WebserverLogin5"
        _input = {}

        # Act
        if not self.try_act(testURL, _input):
            raise ConnectionError(f"Connection to the 3PhPM RPi test-server could not be established. Provided the following URL: {testURL}")
        
        # Collect & Assert
        response = self.get_response()
        assert response.status_code == HttpStatusCode.Ok, f"Request to 3PhPM RPi test-server failed. Received HTTP status code: {response.status_code}"
        
        data = response.json()

        timestamp = data["timestamp"]
        httpCode = data["data"]["HttpCode"]
        httpHeaders = data["data"]["HttpHeaders"]
        httpBody = data["data"]["HttpBody"]
        timeElapsed = data["data"]["TimeElapsed"]

        assert httpCode == HttpStatusCode.TemporaryRedirect, f"Login request to 3PhPM did not fail as expected. Received status {HttpStatusCode(httpCode).name}: {httpBody}"

    #endregion


    #region WebserverLogout

    # WebserverLogout1 - Successful redirect
    def test_logout1(self):
        # Arrange
        testURL = self.URL + "/WebserverLogout1"
        _input = {
            "username": "██",
            "password": "██"
        }

        # Act
        if not self.try_act(testURL, _input):
            raise ConnectionError(f"Connection to the 3PhPM RPi test-server could not be established. Provided the following URL: {testURL}")
        
        # Collect & Assert
        response = self.get_response()
        assert response.status_code == HttpStatusCode.Ok, f"Request to 3PhPM RPi test-server failed. Received HTTP status code: {response.status_code}"
        
        data = response.json()

        timestamp = data["timestamp"]
        httpCode = data["data"]["HttpCode"]
        httpHeaders = data["data"]["HttpHeaders"]
        httpBody = data["data"]["HttpBody"]
        timeElapsed = data["data"]["TimeElapsed"]

        assert httpCode == HttpStatusCode.Found, f"Logout request to 3PhPM did not succeed as expected. Received status {HttpStatusCode(httpCode).name}: {httpBody}"
        ## For later:
        ## Check that response headers contains the location to go to after successful logout

    
    # WebserverLogout2 - No access to /readings after logout (Reusing token pre-logout)
    def test_logout2(self):
        # Arrange
        testURL = self.URL + "/WebserverLogout2"
        _input = {
            "username": "██",
            "password": "██"
        }

        # Act
        if not self.try_act(testURL, _input):
            raise ConnectionError(f"Connection to the 3PhPM RPi test-server could not be established. Provided the following URL: {testURL}")
        
        # Collect & Assert
        response = self.get_response()
        assert response.status_code == HttpStatusCode.Ok, f"Request to 3PhPM RPi test-server failed. Received HTTP status code: {response.status_code}"
        
        data = response.json()

        timestamp = data["timestamp"]
        httpCode = data["data"]["HttpCode"]
        httpHeaders = data["data"]["HttpHeaders"]
        httpBody = data["data"]["HttpBody"]
        timeElapsed = data["data"]["TimeElapsed"]

        assert httpCode == HttpStatusCode.Unauthorized, f"Logout request to 3PhPM did not succeed as expected. Received status {HttpStatusCode(httpCode).name}: {httpBody}"

    
    # WebserverLogout3 - Not logged in (No token used at all)
    def test_logout3(self):
        # Arrange
        testURL = self.URL + "/WebserverLogout3"
        _input = {}

        # Act
        if not self.try_act(testURL, _input):
            raise ConnectionError(f"Connection to the 3PhPM RPi test-server could not be established. Provided the following URL: {testURL}")
        
        # Collect & Assert
        response = self.get_response()
        assert response.status_code == HttpStatusCode.Ok, f"Request to 3PhPM RPi test-server failed. Received HTTP status code: {response.status_code}"
        
        data = response.json()

        timestamp = data["timestamp"]
        httpCode = data["data"]["HttpCode"]
        httpHeaders = data["data"]["HttpHeaders"]
        httpBody = data["data"]["HttpBody"]
        timeElapsed = data["data"]["TimeElapsed"]

        assert httpCode == HttpStatusCode.Unauthorized, f"Logout request to 3PhPM did not succeed as expected. Received status {HttpStatusCode(httpCode).name}: {httpBody}"

    #endregion