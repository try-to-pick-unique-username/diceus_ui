import logging
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
logger = logging.getLogger(__name__)
formatter = logging.Formatter("%(asctime)s - (%(module)s:%(lineno)s) - %(levelname)s - %(message)s ",
                              datefmt="%Y-%m-%d %H:%M:%S")
logger.setLevel(logging.DEBUG)
log_path = '%s/logs' % ROOT_DIR
log_file = log_path + '/autotests.log'
if not os.path.exists(log_path):
    os.mkdir(log_path)
if not os.path.exists(log_file):
    with open(log_file, 'a') as file:
        pass
    file.close()

ch = logging.StreamHandler()
fh = logging.FileHandler(log_file, encoding='utf-8')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)


def log_exception(error_message):
    """
    function for write to log and return message for print
    :param error_message: message for log
    :return: message
    """
    logger.exception(msg=error_message)
    return error_message
