import logging
import logging.config
from .common import get_base_path, generate_uuid
from .settings import SETTINGS
from os import rename, mkdir

try:
    with open(get_base_path() / SETTINGS['project']['logs'] / 'latest.log', "w+") as file:
        fist_row = file.readline().split('|')
        if len(fist_row) > 1:
            last_time = fist_row[1].rstrip().lstrip().replace(':', '-')
            rename(get_base_path() / SETTINGS['project']['logs'] / 'latest.log',
                   get_base_path() / SETTINGS['project']['logs'] / f'{last_time}.log')
except FileNotFoundError as e:
    mkdir(get_base_path() / SETTINGS['project']['logs'])
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
            'format': f'%(asctime)s | %(name)s | %(levelname)-10s | {generate_uuid()} | %(uuid)s | %(message)s',
            'default': {'uuid': 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'},
        },

    },
}

logging.captureWarnings(True)
logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger('default')
logger.handlers[0].formatter._style._defaults = LOG_CONFIG['formatters']['DEBUG']['default']
