import pytest
from pytest_check import check
import requests

def test_external_data():
    expected = 230.43
    response = requests.get("https://192.168.1.236:5001/TestData/GetData")

    assert response.status_code == 200

    check.equal(expected, response.json()["val"])
