"""
Custom exceptions for the application.
"""

class LongMaoError(Exception):
    """Base exception class for this application."""
    pass

class ConfigError(LongMaoError):
    """Raised for errors in the configuration."""
    pass

class NoxError(LongMaoError):
    """Raised for errors related to the Nox player."""
    pass

class ImageNotFoundError(LongMaoError):
    """Raised when an image cannot be found on the screen."""
    pass
