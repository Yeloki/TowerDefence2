import logging
import logging.config
from .common import get_base_path
from .settings import SETTINGS

LOG_CONFIG = {
    'version': 1,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': get_base_path() / SETTINGS['project']['logs'] / 'latest.log',
            "formatter": "DEBUG",
        },
    },
    'loggers': {
        'default': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
    "formatters": {
        "DEBUG": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },

    },
}
logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger('default')
