import yaml

CONFIG = None

with open('.\\storage\\config.yml', 'r') as file:
    CONFIG = yaml.safe_load(file)