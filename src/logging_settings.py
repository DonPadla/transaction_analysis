import logging
import os

if not os.path.isdir("../logs"):
    os.mkdir("../logs")

file_adress = os.path.abspath(
    os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), "../logs/logs.log"))
logger = logging.getLogger('utils')
file_handler = logging.FileHandler(
    file_adress, 'w'
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
