from . import event_types
from tools.logger import logger
from tools.common import generate_uid


class Event:
    def __init__(self):
        self.uid = generate_uid()
