from constants import *
from pytest_check import check


class TestClassIntegrationMisc(AbstractIntegrationTestClass):
    #region Conectivity
    # Test connection established
    def test_connectivity1(self):
        # Arrange
        testURL = self.URL + "/Connectivity1"
        _input = {}

        # Act
        if not self.try_act(testURL, _input):
            raise ConnectionError(f"Connection to the 3PhPM RPi test-server could not be established. Provided the following URL: {testURL}")
        
        # Collect & Assert
        response = self.get_response()
        assert response.status_code == HttpStatusCode.Ok, f"Request to 3PhPM RPi test-server failed. Received HTTP status code: {response.status_code}"

        data = response.json()

        timestamp = data["timestamp"]
        connected = data["data"]["Connected"]
        modbusMasterState = data["data"]["ModbusMasterState"]
        timeElapsed = data["data"]["TimeElapsed"]

        with check:
            assert connected == True, "Connection to 3PhPM failed. Should have been able to connect to secondary Modbus device."

        assert modbusMasterState == ModbusMasterState.Ready, f"Expected master Modbus device to be in state: Ready. Actual state: {ModbusMasterState(modbusMasterState).name}"
    #endregion


class TestClassIntegrationRead(AbstractIntegrationTestClass):
    # Valid Read
    def test_read1(self):
        # Arrange
        testURL = self.URL + "/Read1"
        _input = {
            "functionCode": ██,
            "address": ██,
            "count": ██,
            "data": []
        }

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
        timeElapsed = data["data"]["TimeElapsed"]
        commResponse = data["data"]["CommResponse"]

        with check:
            assert commandStateDn == True, f"Read1 command failed. Expected command to succeed. Provided Modbus request: {_input}"
        with check:
            assert commandStateErr == False, f"Read1 command failed. Expected command to succeed. Provided Modbus request: {_input}"
        assert commResponse == CommResponse.Ack, f"Read1 command failed. Expected command to succeed. Received CommResponse: {CommResponse(commResponse).name}"

    
    # Invalid Address
    def test_read2(self):
        # Arrange
        testURL = self.URL + "/Read2"
        _input = {
            "functionCode": ██,
            "address": ██,
            "count": ██,
            "data": []
        }

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
        timeElapsed = data["data"]["TimeElapsed"]
        commResponse = data["data"]["CommResponse"]

        with check:
            assert commandStateDn == False, f"Read2 command did not fail as expected. Provided Modbus request: {_input}"
        with check:
            assert commandStateErr == True, f"Read2 command did not fail as expected. Provided Modbus request: {_input}"
        assert commResponse == CommResponse.Critical, f"Read2 command did not fail as expected. Received CommResponse: {CommResponse(commResponse).name}"


    # Invalid Function
    def test_read3(self):
        # Arrange
        testURL = self.URL + "/Read3"
        _input = {
            "functionCode": ██,
            "address": ██,
            "count": ██,
            "data": []
        }

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
        timeElapsed = data["data"]["TimeElapsed"]
        commResponse = data["data"]["CommResponse"]

        with check:
            assert commandStateDn == False, f"Read3 command did not fail as expected. Provided Modbus request: {_input}"
        with check:
            assert commandStateErr == True, f"Read3 command did not fail as expected. Provided Modbus request: {_input}"
        assert commResponse == CommResponse.Critical, f"Read3 command did not fail as expected. Received CommResponse: {CommResponse(commResponse).name}"



class TestClassIntegrationWrite(AbstractIntegrationTestClass):
    # Valid Write
    def test_write1(self):
        # Arrange
        testURL = self.URL + "/Write1"
        _input = {
            "functionCode": ██,
            "address": ██,
            "count": ██,
            "data": [ ██ ]
        }

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

        with check:
            assert commandStateDn == True, f"Write1 command failed. Expected command to succeed. Provided Modbus request: {_input}"
        with check:
            assert commandStateErr == False, f"Write1 command failed. Expected command to succeed. Provided Modbus request: {_input}"
        assert commResponse == CommResponse.Ack, f"Write1 command failed. Expected command to succeed. Received CommResponse: {CommResponse(commResponse).name}"


    # Invalid Address
    def test_write2(self):
        # Arrange
        testURL = self.URL + "/Write2"
        _input = {
            "functionCode": ██,
            "address": ██,
            "count": ██,
            "data": [ ██ ]
        }

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

        with check:
            assert commandStateDn == False, f"Write2 command did not fail as expected. Provided Modbus request: {_input}"
        with check:
            assert commandStateErr == True, f"Write2 command did not fail as expected. Provided Modbus request: {_input}"
        assert commResponse == CommResponse.Critical, f"Write2 command did not fail as expected. Received CommResponse: {CommResponse(commResponse).name}"


    # Invalid Function
    def test_write3(self):
        # Arrange
        testURL = self.URL + "/Write3"
        _input = {
            "functionCode": ██,
            "address": ██,
            "count": ██,
            "data": [ ██ ]
        }

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

        with check:
            assert commandStateDn == False, f"Write3 command did not fail as expected. Provided Modbus request: {_input}"
        with check:
            assert commandStateErr == True, f"Write3 command did not fail as expected. Provided Modbus request: {_input}"
        assert commResponse == CommResponse.Critical, f"Write3 command did not fail as expected. Received CommResponse: {CommResponse(commResponse).name}"


    # Invalid data to write
    def test_write4(self):
        # Arrange
        testURL = self.URL + "/Write4"
        _input = {
            "functionCode": ██,
            "address": ██,
            "count": ██,
            "data": [ ██ ]
        }

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

        with check:
            assert commandStateDn == False, f"Write4 command did not fail as expected. Provided Modbus request: {_input}"
        with check:
            assert commandStateErr == True, f"Write4 command did not fail as expected. Provided Modbus request: {_input}"
        assert commResponse == CommResponse.Critical, f"Write4 command did not fail as expected. Received CommResponse: {CommResponse(commResponse).name}"