import yaml
import os

CONFIG = None
WORKDIR = os.path.dirname(os.path.abspath(__file__))

if os.path.exists(f'{WORKDIR}\\storage\\config.yml'):
    with open(f'{WORKDIR}\\storage\\config.yml', 'r') as file:
        CONFIG = yaml.safe_load(file)
else:
    CONFIG = {
        'user': os.environ.get('GITEA_USER'),
        'url': os.environ.get('GITEA_URL'),
        'token': os.environ.get('GITEA_TOKEN'),
    }