import pyautogui as pg
import time
import win32api
import win32con
import subprocess
from src.config import config
from src.image_locator import ImageLocator
from src.logger import logger
from src.exceptions import NoxError, ImageNotFoundError, ConfigError

class Automator:
    def __init__(self):
        self.config = config
        self.locator = ImageLocator()
        self.nox_region = None

    def get_screen_resolution(self):
        """Gets the current screen resolution."""
        x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        logger.info(f"Screen resolution: {x}x{y}")
        return x, y

    def start_nox(self):
        """Starts the Nox player."""
        nox_path = self.config.get("nox.executable_path")
        try:
            subprocess.Popen(nox_path)
            logger.info("Starting Nox...")
            time.sleep(self.config.get("automation.nox_boot_time", 20))
        except FileNotFoundError:
            raise NoxError(f"Nox executable not found at '{nox_path}'.")

    def kill_nox(self):
        """Kills the Nox player process."""
        logger.info("Killing Nox...")
        subprocess.run("taskkill /f /t /im nox.exe", capture_output=True, text=True)
        time.sleep(3)

    def find_nox_region(self):
        """Finds the Nox window region on the screen."""
        x, y = self.get_screen_resolution()
        header_image = "header1080" if y <= 1080 else "header1440"
        
        logger.info("Locating Nox window...")
        try:
            position = self.locator.locate_on_screen(header_image, timeout=20)
            self.nox_region = (position.left, position.top, position.width, y)
            logger.info(f"Nox window found at: {self.nox_region}")
        except ImageNotFoundError:
            raise NoxError("Nox window not found.")

    def vx_login(self):
        """Performs WeChat login."""
        account = self.config.get("wechat.account")
        password = self.config.get("wechat.password")

        if not account or not password:
            raise ConfigError("WeChat account or password not set in config.yaml.")

        logger.info("Starting WeChat login...")
        self.locator.click("acc1080", region=self.nox_region)
        pg.typewrite(account)
        
        self.locator.click("pw1080", region=self.nox_region)
        pg.typewrite(password)

        self.locator.click("login", region=self.nox_region, confidence=0.4)

    def run_automation_flow(self):
        """Runs the main automation flow."""
        logger.info("Starting automation flow...")
        
        self.locator.click("lm1080", region=self.nox_region)
        time.sleep(self.config.get("automation.action_delay", 2))
        
        self.locator.click("lm_vx", region=self.nox_region, confidence=0.5)
        time.sleep(self.config.get("automation.action_delay", 2))

        self.locator.click("ygrun", region=self.nox_region)
        time.sleep(8)

        set_region = (self.nox_region[0] + round(2/3 * self.nox_region[2]), self.nox_region[1], 300, self.nox_region[3])
        self.locator.click("set", region=set_region)
            
        self.locator.click("moreset", region=set_region)

        rec_header = self.locator.locate_on_screen("recmain", timeout=20)
        rec_field = (rec_header.left + round(1/2 * rec_header.width), rec_header.top + rec_header.height, rec_header.width, 100)
        self.locator.click("playrec", region=rec_field)

    def run(self):
        """Main execution method."""
        logger.info("Automation process started.")
        try:
            self.kill_nox()
            self.start_nox()
            self.find_nox_region()
            
            # Using a try-except block to gracefully handle login failures
            try:
                self.locator.wait_for_image("vxlogo", region=self.nox_region, timeout=15)
                self.vx_login()
            except (ImageNotFoundError, ConfigError) as e:
                logger.warning(f"WeChat login skipped: {e}")

            self.run_automation_flow()
            logger.info("Automation flow completed successfully.")

        except (NoxError, ImageNotFoundError, ConfigError) as e:
            logger.error(f"A critical error occurred: {e}")
            # Optionally, add more specific recovery logic here
        
        finally:
            logger.info("Automation finished. Cleaning up...")
            self.kill_nox()
            logger.info("Automation process finished.")

