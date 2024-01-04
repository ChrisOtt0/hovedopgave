import json
import logging
from enum import StrEnum


logger = logging.getLogger("rflash.config")


class Interface(StrEnum):
    JTAG = "JTAG"
    SWD = "SWD"
    cJTAG = "cJTAG"
    FINE = "FINE"
    SPD = "SPD"
    ICSP = "ICSP"

    @classmethod
    def has_value(self, value):
        """
        Returns True if InterfaceEnum has enumerable option for provided value.
        """
        return value in iter(self)


class JTAGConf:
    def __init__(self, jtagconf: str):
        """
        Initializes JTAGConf property. If none provided, default '-1 -1' will be used.
        """
        irpre = None
        drpre = None

        if jtagconf == None:
            self.IRPre = -1
            self.DRPre = -1
            return

        if not " " in jtagconf:
            raise Exception("Provided JSON is invalid. Provided value for key [jtagconf] is not valid: [{}]".format(jtagconf))
        
        try:
            jtagconf_values = jtagconf.split(" ", 1)
            irpre = int(jtagconf_values[0])
            drpre = int(jtagconf_values[1])
        except Exception as err:
            raise Exception("Provided JSON is invalid. Provided value for key [jtagconf] is not valid: [{}]\n{}".format(jtagconf, err))
            

        self.IRPre  = irpre
        self.DRPre = drpre


class Config:
    def __init__(self, json_input):
        data = None
        try:
            data = json.loads(json_input)
            self._validate_json(data)
        except Exception as err:
            raise err


    def _validate_json(self, loaded_json: dict):
        """
        Validates json input.
        """
        # Check valid keys
        valid_keys = [
            "device",
            "interface",
            "jtagconf",
            "speed"
        ]

        keys = loaded_json.keys()
        for key in keys:
            if key not in valid_keys:
                raise Exception("Provided JSON is invalid. JSON Object Literal with key [{}] is invalid.".format(key))
            
        if "device" in keys and (loaded_json["device"] != None and loaded_json["device"] != ""):
            self.device = loaded_json["device"]
        else:
            raise Exception("Provided JSON is invalid. Cannot flash unknown device type.")

        # Check valid interface
        if "interface" in keys:
            if not Interface.has_value(loaded_json["interface"]):
                raise Exception("Provided JSON is invalid. JSON Object Literal with key [{}] has an invalid value: [{}]".format("interface", loaded_json["interface"]))
            else:
                self.interface = loaded_json["interface"]
        else:
            self.interface = Interface.JTAG        
        
        # Check valid jtagconf
        if "jtagconf" in keys:
            self.jtagconf = JTAGConf(loaded_json["jtagconf"])
        else:
            self.jtagconf = JTAGConf("")
        
        # Check valid speed
        if "speed" in keys:
            if loaded_json["speed"] == "auto" or loaded_json["speed"] == "adaptive":
                self.speed = loaded_json["speed"]
            else:
                try:
                    val = int(loaded_json["speed"])
                    if val < 0:
                        raise Exception("Provided JSON is invalid. Provided value for key [speed] cannot be a negative number.")
                    self.speed = loaded_json["speed"]
                except:
                    raise Exception("Provided JSON is invalid. Provided value for key [speed] is invalid.")
        else:
            self.speed = "auto"