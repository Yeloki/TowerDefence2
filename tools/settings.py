import logging

import yaml
from .common import find_settings


def make_fields_better(obj):
    if isinstance(obj, dict):
        for row in obj:
            obj[row] = make_fields_better(obj[row])
    elif isinstance(obj, list):
        for i in len(obj):
            obj[i] = make_fields_better(obj[i])
    elif isinstance(obj, str):
        if obj.isdigit():
            obj = int(obj)
        else:
            try:
                obj = float(obj)
            except ValueError:
                pass
    return obj


settings_path = find_settings()
settings_file = open(settings_path, mode='r')
SETTINGS = make_fields_better(yaml.load(settings_file, yaml.BaseLoader))
settings_file.close()
