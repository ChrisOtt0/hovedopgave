import logging
import sys
import os

from modules.lib import App

logging.basicConfig()
logger = logging.getLogger("rflash")


def set_log_handlers():
    global logger
    formatter = logging.Formatter(
        fmt="[%(asctime)s] %(levelname)s: %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(
        os.path.join(os.path.expanduser("~"), ".local", "logs", "rflash.log"), 
        mode="a", encoding="utf-8"
    )
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


if __name__ == '__main__':
    # Setup root logger
    # Child loggers may have their own effective level or settings
    # If not, they will default to this root logger
    logger.setLevel(logging.DEBUG)
    
    App().run()
