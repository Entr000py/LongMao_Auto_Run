import pyautogui as pg
import time
from pathlib import Path
from src.config import config
from src.logger import logger
from src.exceptions import ImageNotFoundError
from src.utils import retry

class ImageLocator:
    def __init__(self):
        self.assets_path = Path(config.get("assets.path", "assets"))
        self.confidence = config.get("assets.confidence", 0.6)
        self.timeout = config.get("automation.locate_timeout", 10)

    def get_image_path(self, image_name):
        """Constructs the full path to an image file."""
        return str(self.assets_path / f"{image_name}.png")

    @retry(exceptions=(ImageNotFoundError,), retries=3, delay=2)
    def locate_on_screen(self, image_name, region=None, confidence=None, timeout=None):
        """
        Locates an image on the screen within a given region and timeout.
        Returns the position (left, top, width, height) or raises ImageNotFoundError.
        """
        image_path = self.get_image_path(image_name)
        confidence = confidence or self.confidence
        timeout = timeout or self.timeout
        
        logger.debug(f"Locating image '{image_name}' with confidence {confidence} and timeout {timeout}s.")
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                position = pg.locateOnScreen(image_path, region=region, confidence=confidence)
                if position:
                    logger.info(f"Image '{image_name}' found at {position}.")
                    return position
            except pg.PyAutoGUIException as e:
                logger.error(f"PyAutoGUI error while locating image {image_name}: {e}")
            time.sleep(0.5)
        
        raise ImageNotFoundError(f"Image '{image_name}' not found within {timeout}s.")

    def click(self, image_name, region=None, confidence=None, timeout=None):
        """
        Locates an image and clicks on it.
        """
        position = self.locate_on_screen(image_name, region=region, confidence=confidence, timeout=timeout)
        pg.click(position)
        logger.info(f"Clicked on image '{image_name}' at {position}.")

    def wait_for_image(self, image_name, region=None, timeout=None):
        """
        Waits for an image to appear on the screen.
        """
        logger.info(f"Waiting for image '{image_name}' to appear.")
        self.locate_on_screen(image_name, region=region, timeout=timeout)
