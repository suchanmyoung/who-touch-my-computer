import logging
import logging.config

logger = logging.getLogger(__name__)

info_fileHandler = logging.FileHandler("./log/info.log")
info_fileHandler.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
info_fileHandler.setFormatter(formatter)

logger.addHandler(streamHandler)
logger.addHandler(info_fileHandler)

logger.setLevel(level=logging.DEBUG)