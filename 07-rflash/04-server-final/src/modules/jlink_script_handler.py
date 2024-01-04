import os
import subprocess
from datetime import datetime
import logging

from .config import Config


logger = logging.getLogger("rflash.jlink_script_handler")


EXECUTABLE = "/home/agramkow/code/jlink/./JLinkExe"


class JLinkScriptHandler:
    def __init__(self, config: Config):
        self._config = config
        self._script = ""
        self._script_path = "/var/tmp/rflash_jlink_script_" + datetime.now().strftime("%d-%m-%Y-%H-%M-%S") + ".jlink"

    def handle(self, bin_path):
        """
        Handle JLink flashing via provided configuration.\n
        Returns stdout & stderr of JLinkExe tool.
        """
        try:
            self._build(bin_path)
            logger.debug(self._script)
            self._create()
            output = self._execute()
            self._remove()

            return output
        except Exception as err:
            raise err
    
    def _build(self, bin_path):
        """
        Builds temporary JLink Commander Script from configuration.
        """
        logger.info("Building script...")
        self._script += "Device " + self._config.device + "\n"
        self._script += "SI " + self._config.interface + "\n"
        self._script += "JTAGConf " + str(self._config.jtagconf.IRPre) + " " + str(self._config.jtagconf.DRPre) + "\n"
        self._script += "Speed " + self._config.speed + "\n"
        self._script += "Erase\n"
        self._script += "LoadFile " + bin_path + "\n"
        self._script += "Exit\n"
    
    def _create(self):
        """
        Creates temporary JLink Commander Script.
        """
        try:
            with open(self._script_path, "w") as file:
                file.write(self._script)
        except Exception as e:
            raise Exception("An error occured while trying to create tmp jlink script: {}", e)
    
    def _execute(self):
        """
        Calls subprocess to execute temporary JLink Commander Script.\n
        Returns process output.
        """
        logger.info("Executing JLink script...")
        process = subprocess.Popen([EXECUTABLE + " -CommanderScript " + self._script_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        return process.stdout.read().decode("utf-8")
    
    def _remove(self):
        """
        Removes temporary JLink Commander Script.
        """
        logger.info("Cleaning up generated script...")
        try:
            if os.path.isfile(self._script_path):
                os.remove(self._script_path)
        except Exception as err:
            raise Exception("An error occured while trying to remove tmp jlink script: {}", err)