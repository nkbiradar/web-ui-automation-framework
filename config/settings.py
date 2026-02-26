import configparser
import os

config = configparser.ConfigParser()

config_path = os.path.join(os.path.dirname(__file__), "config.ini")
config.read(config_path)

BROWSER = config.get("settings", "browser")
BASE_URL = config.get("settings", "base_url")