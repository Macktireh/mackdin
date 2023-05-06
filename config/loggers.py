import os
import logging
import logging.config

from pathlib import Path
from typing import Union
from dotenv import load_dotenv

from django.core.exceptions import ImproperlyConfigured
from django.utils.log import DEFAULT_LOGGING


BASE_DIR = Path(__file__).resolve().parent.parent

load = load_dotenv(os.path.join(BASE_DIR, ".env"))


def get_env_variable(var_name: str, default: Union[str, None] = None) -> str:
    try:
        return os.environ[var_name] if os.environ[var_name] else default
    except KeyError:
        if default is not None:
            return default
        error_msg = f"Set the {var_name} environment variable"
        raise ImproperlyConfigured(error_msg)


logger = logging.getLogger(__name__)
LOG_LEVEL = "INFO"
FILE_LOGGER = True if get_env_variable("FILE_LOGGER", "False") == "True" else False
LOG_FILE_PATH = os.path.join(BASE_DIR, "logs/logs.log")

# ADMINS = [
#     tuple(map(str.strip, i.split("/")))
#     for i in get_env_variable("ADMINS", "").split("%%")
# ]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
        "console": {
            "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        },
        "verbose": {
            "format": "{levelname} {asctime} {name} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
        "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "": {"level": "INFO", "handlers": ["console"], "propagate": False},
        "django": {
            "handlers": ["console"],
            "propagate": True,
        },
        "django.request": {
            "handlers": ["mail_admins", "console"],
            "level": "INFO",
            "propagate": False,
        },
        "apps": {"level": "INFO", "handlers": ["console"], "propagate": False},
    },
}


if FILE_LOGGER:
    # create log file handler if it doesn't exist
    if not os.path.exists(os.path.join(BASE_DIR, "logs")):
        os.mkdir(os.path.join(BASE_DIR, "logs"))

    LOGGING["handlers"].update(
        {
            "file": {
                "level": "DEBUG",
                "class": "logging.FileHandler",
                "formatter": "verbose",
                "filename": LOG_FILE_PATH,
            }
        }
    )
    LOGGING["loggers"]["django"]["handlers"] = [
        "console",
        "file",
    ]
    LOGGING["loggers"]["django.request"]["handlers"] = [
        "mail_admins",
        "console",
        "file",
    ]
