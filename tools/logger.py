import logging
import logging.config

LOG_CONFIG = {
    "version": 1,
    "handlers": {
        "fileHandler": {
            "class": "logging.FileHandler",
            "formatter": "default",
            "filename": "controller.log"
        }
    },
    "loggers": {
        "controller": {
            "handlers": ["fileHandler"],
        }
    },
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }

    }
}
logging.config.dictConfig(LOG_CONFIG)
