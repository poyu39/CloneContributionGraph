import yaml
import os

CONFIG = None
WORKDIR = os.path.dirname(os.path.abspath(__file__))

with open(f'{WORKDIR}\\storage\\config.yml', 'r') as file:
    CONFIG = yaml.safe_load(file)