import yaml
from pathlib import Path

class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, config_path="config/config.yaml"):
        if not hasattr(self, "config"):
            self.config_path = Path(config_path)
            self.load_config()

    def load_config(self):
        """Loads the YAML configuration file."""
        with open(self.config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

    def get(self, key, default=None):
        """
        Retrieves a configuration value.
        Nested keys can be accessed using dot notation (e.g., "nox.executable_path").
        """
        keys = key.split(".")
        value = self.config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value

# Global config instance
config = Config()
