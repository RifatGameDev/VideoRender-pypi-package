from VideoRender.logger import logger
from VideoRender.custom_exception import InvalidURLException

# logger.info("This is a test log message from test.py")

try:
    raise InvalidURLException()
except Exception as e:
    logger.error(f"Caught an exception: {e}")
