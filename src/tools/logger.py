import logging
import logging.config
from .common import get_base_path, generate_uuid
from .settings import SETTINGS
from os import rename

try:
    with open(get_base_path() / SETTINGS['project']['logs'] / 'latest.log') as file:
        last_time = file.readline().split('|')[1].rstrip().lstrip().replace(':', '-')

    rename(get_base_path() / SETTINGS['project']['logs'] / 'latest.log',
           get_base_path() / SETTINGS['project']['logs'] / f'{last_time}.log')
except FileNotFoundError as e:
    pass

LOG_CONFIG = {
    'version': 1,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': get_base_path() / SETTINGS['project']['logs'] / 'latest.log',
            'formatter': 'DEBUG',
        },
    },
    'loggers': {
        'default': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,

        },
    },
    'formatters': {
        'DEBUG': {
            'format': f'{generate_uuid()} | %(asctime)s | %(name)s | %(levelname)-10s | %(uuid)s | %(message)s',
            'default': {'uuid': 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'},
        },

    },
}

logging.captureWarnings(True)
logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger('default')
logger.handlers[0].formatter._style._defaults = LOG_CONFIG['formatters']['DEBUG']['default']
