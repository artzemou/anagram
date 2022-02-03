import logging
from logging.handlers import RotatingFileHandler

class Full_log():
    """
        setup  full logging in a single call using a kind-of Façade pattern
    """
    def __init__(self, name):
        logger=logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter=logging.Formatter('%(asctime)s ::%(filename)s :: %(levelname)s :: %(message)s')
        file_handler = RotatingFileHandler(name+'.log', 'a', 100000,1)

        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        stream_handler= logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s \t %(filename)s \t %(message)s', "%H:%M:%S")
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

