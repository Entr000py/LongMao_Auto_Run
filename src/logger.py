import logging
from logging.handlers import RotatingFileHandler
from src.config import config

def setup_logger():
    """
    Sets up the global logger based on the configuration.
    """
    log_level = config.get("logging.level", "INFO").upper()
    log_file = config.get("logging.file", "app.log")
    max_bytes = config.get("logging.max_bytes", 1024 * 1024)
    backup_count = config.get("logging.backup_count", 5)

    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Console handler
    if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    # File handler with rotation
    if not any(isinstance(h, RotatingFileHandler) for h in logger.handlers):
        fh = RotatingFileHandler(
            log_file, maxBytes=max_bytes, backupCount=backup_count
        )
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger

# Global logger instance
logger = setup_logger()
