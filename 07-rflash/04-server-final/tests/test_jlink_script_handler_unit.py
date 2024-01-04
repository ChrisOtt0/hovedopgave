import pytest
from pytest_check import check
import os

from modules.config import Config
from modules.jlink_script_handler import *;


class AbstractTestClass:
    VALID_CONF = Config('{"device":"R7FA6M2AF3CFB","interface":"JTAG","jtagconf":null,"speed":"auto"}')

class TestClassBuild(AbstractTestClass):
    def test_build_valid(self):
        # Arrange
        bin_path = "Test"
        handler = JLinkScriptHandler(self.VALID_CONF)

        expected = "\
Device R7FA6M2AF3CFB\n\
SI JTAG\n\
JTAGConf -1 -1\n\
Speed auto\n\
Erase\n\
LoadFile " + bin_path + "\n\
Exit\n"

        # Act
        handler._build(bin_path)

        # Assert
        assert expected == handler._script

    def test_build_invalid(self):
        # Arrange
        bin_path = "Test"
        handler = JLinkScriptHandler(self.VALID_CONF)

        expected = "\
Device \n\
SI JTAG\n\
JTAGConf -1 -1\n\
Speed 4000\n\
Erase\n\
LoadFile " + bin_path + "\n\
Exit\n"

        # Act
        handler._build(bin_path)

        # Assert
        assert expected != handler._script


class TestClassCreate(AbstractTestClass):
    def test_can_create(self):
        handler = JLinkScriptHandler(self.VALID_CONF)

        handler._create()
        res = os.path.isfile(handler._script_path)
        os.remove(handler._script_path)

        assert res is True

class TestClassRemove(AbstractTestClass):
    def test_can_remove(self):
        handler = JLinkScriptHandler(self.VALID_CONF)

        handler._create()
        handler._remove()
        res = os.path.isfile(handler._script_path)
        if res:
            os.remove(handler._script_path)

        assert res is False
        