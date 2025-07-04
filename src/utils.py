import time
from functools import wraps
from src.logger import logger

def retry(exceptions, retries=3, delay=2):
    """
    A decorator to retry a function call upon specific exceptions.

    :param exceptions: A tuple of exception classes to catch.
    :param retries: The maximum number of retries.
    :param delay: The delay in seconds between retries.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            mtries = retries
            while mtries > 0:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(
                        f"Caught exception: {e}. Retrying in {delay}s... "
                        f"({retries - mtries + 1}/{retries})"
                    )
                    mtries -= 1
                    if mtries == 0:
                        logger.error("All retries failed.")
                        raise  # Re-raise the last exception
                    time.sleep(delay)
        return wrapper
    return decorator
