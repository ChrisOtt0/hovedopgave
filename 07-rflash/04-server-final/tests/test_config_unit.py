import pytest
from pytest_check import check

from modules.config import *


class TestClassDevice:
    def test_valid_device(self):
        json_valid_device = '{"device":"R7FA6M2AF3CFB","interface":"JTAG","jtagconf":null,"speed":"auto"}'
        conf = Config(json_valid_device)
        assert conf.device == "R7FA6M2AF3CFB"

    def test_none_supplied(self):
        json_no_device = '{"device":null,"interface":"JTAG","jtagconf":null,"speed":"auto"}'
        with pytest.raises(Exception):
            Config(json_no_device)

class TestClassInterface:
    def test_valid_jtag(self):
        json_jtag = '{"device":"R7FA6M2AF3CFB","interface":"JTAG","jtagconf":null,"speed":"auto"}'
        conf = Config(json_jtag)
        assert conf.interface == Interface.JTAG

    def test_valid_swd(self):
        json_swd = '{"device":"R7FA6M2AF3CFB","interface":"SWD","jtagconf":null,"speed":"auto"}'
        conf = Config(json_swd)
        assert conf.interface == Interface.SWD

    def test_valid_cjtag(self):
        json_cjtag = '{"device":"R7FA6M2AF3CFB","interface":"cJTAG","jtagconf":null,"speed":"auto"}'
        conf = Config(json_cjtag)
        assert conf.interface == Interface.cJTAG

    def test_valid_fine(self):
        json_fine = '{"device":"R7FA6M2AF3CFB","interface":"FINE","jtagconf":null,"speed":"auto"}'
        conf = Config(json_fine)
        assert conf.interface == Interface.FINE

    def test_valid_spd(self):
        json_spd = '{"device":"R7FA6M2AF3CFB","interface":"SPD","jtagconf":null,"speed":"auto"}'
        conf = Config(json_spd)
        assert conf.interface == Interface.SPD


    def test_valid_icsp(self):
        json_icsp = '{"device":"R7FA6M2AF3CFB","interface":"ICSP","jtagconf":null,"speed":"auto"}'
        conf = Config(json_icsp)
        assert conf.interface == Interface.ICSP

    def test_invalid_if(self):
        json_invalid = '{"device":"R7FA6M2AF3CFB","interface":"INVALID_IF","jtagconf":null,"speed":"auto"}'

        with pytest.raises(Exception) as e_info:
            Config(json_invalid)


class TestClassJTAGConf:
    def test_valid_jtagconf(self):
        json_valid_jtagconf = '{"device":"R7FA6M2AF3CFB","interface":"JTAG","jtagconf":"3 7","speed":"auto"}'
        conf = Config(json_valid_jtagconf)

        check.equal(3, conf.jtagconf.IRPre)
        check.equal(7, conf.jtagconf.DRPre)

    def test_default_jtagconf(self):
        json_def_jtagconf = '{"device":"R7FA6M2AF3CFB","interface":"JTAG","jtagconf":null,"speed":"auto"}'
        conf = Config(json_def_jtagconf)

        check.equal(-1, conf.jtagconf.IRPre)
        check.equal(-1, conf.jtagconf.DRPre)

    def test_invalid_jtagconf(self):
        json_def_jtagconf = '{"device":"R7FA6M2AF3CFB","interface":"JTAG","jtagconf":"INVALID_JTAGCONF","speed":"auto"}'
        with pytest.raises(Exception):
            Config(json_def_jtagconf)

    def test_invalid_jtagconf_with_space(self):
        json_def_jtagconf = '{"device":"R7FA6M2AF3CFB","interface":"JTAG","jtagconf":"INVALID_JTAGCONF INVALID_JTAGCONF","speed":"auto"}'
        with pytest.raises(Exception):
            Config(json_def_jtagconf)


class TestClassSpeed:
    def test_speed_auto(self):
        json_speed_auto = '{"device":"R7FA6M2AF3CFB","interface":"JTAG","jtagconf":"3 7","speed":"auto"}'
        conf = Config(json_speed_auto)

        assert conf.speed == "auto"

    def test_speed_adaptive(self):
        json_speed_adaptive = '{"device":"R7FA6M2AF3CFB","interface":"JTAG","jtagconf":"3 7","speed":"adaptive"}'
        conf = Config(json_speed_adaptive)

        assert conf.speed == "adaptive"

    def test_speed_val(self):
        json_speed_val = '{"device":"R7FA6M2AF3CFB","interface":"JTAG","jtagconf":"3 7","speed":"4000"}'
        conf = Config(json_speed_val)

        assert conf.speed == "4000"

    def test_speed_negative_val(self):
        json_speed_negative_val = '{"device":"R7FA6M2AF3CFB","interface":"JTAG","jtagconf":"3 7","speed":"-4000"}'
        with pytest.raises(Exception):
            Config(json_speed_negative_val)

    def test_speed_none_provided(self):
        json_speed_none = '{"device":"R7FA6M2AF3CFB","interface":"JTAG","jtagconf":"3 7"}'
        conf = Config(json_speed_none)

        assert conf.speed == "auto"