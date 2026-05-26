<<<<<<< HEAD
import logging
from logging.handlers import RotatingFileHandler
from config import LOG_LEVEL


def setup_logging():
    logger = logging.getLogger('jobbot')
    logger.setLevel(LOG_LEVEL)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        file_handler = RotatingFileHandler('jobbot.log', maxBytes=1024 * 1024, backupCount=3, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
=======
import logging
from logging.handlers import RotatingFileHandler
from config import LOG_LEVEL


def setup_logging():
    logger = logging.getLogger('jobbot')
    logger.setLevel(LOG_LEVEL)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        file_handler = RotatingFileHandler('jobbot.log', maxBytes=1024 * 1024, backupCount=3, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
>>>>>>> origin/main
