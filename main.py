from src.automator import Automator
from src.logger import setup_logger

def main():
    """
    Main function to run the automation.
    """
    logger = setup_logger()
    logger.info("Application starting...")
    
    try:
        automator = Automator()
        automator.run()
        logger.info("Application finished successfully.")
    except Exception as e:
        logger.critical(f"An unhandled exception occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()
