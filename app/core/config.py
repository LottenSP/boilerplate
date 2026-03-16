import os
from functools import lru_cache

class Settings:
        APP_NAME:       str = os.getenv("APP_NAME", "Boilerplate")
        APP_ENV:        str = os.getenv("APP_ENV",  "development")
        DEBUG:          bool = os.getenv("DEBUG", "false").lower() == "true"

        DATABASE_URL:   str = os.getenv("DATABASE_URL")
        SECRET_KEY:     str = os.getenv("SECRET_KEY")

@lru_cache()
def get_settings():
    return Settings()