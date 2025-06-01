import logging
import sys 
import os

class Logger:

    def __init__(self, config: dict):
        self.path = config.get("log_path",".../log/app.log")
        self.app = config.get("application_name","LVD")
        self.debug = config.get("debug",True)
        self.level = config.get("level","INFO").upper()
    
    def Setup(self)-> logging.Logger:
        logger = logging.getLogger(self.app)
        logger.setLevel(getattr(logging, self.level, logging.INFO))
        logger.propagate = False

        if logger.handlers:
            return logger
        
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

        file_handler = logging.FileHandler(self.path, encoding="utf-8")
        file_formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
                                           datefmt="%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        if self.debug:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(file_formatter)
            logger.addHandler(console_handler)

        logger.info("Logger init success")

        return logger
