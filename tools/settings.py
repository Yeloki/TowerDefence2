import yaml
from common import find_settings

settings_path = find_settings()
settings_file = open(settings_path, mode='r')
settings_yaml = yaml.load(settings_file, yaml.BaseLoader)

NAME = settings_yaml['project']['name']
SOURCES = settings_yaml['project']['sources']
LOGS = settings_yaml['project']['logs']

settings_file.close()
