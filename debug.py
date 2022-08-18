import logging
from re import I

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s - %(levelname)s : %(message)s')


def log(str): logging.debug(str)


def warning(str): logging.warning(str)


def info(str): logging.info(str)
