"""Script configuration."""
from os import environ, path
from dotenv import load_dotenv

# Load secrets from .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


MIXPANEL_API_TOKEN = environ.get('MIXPANEL_API_TOKEN')
