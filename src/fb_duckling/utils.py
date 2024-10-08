from dotenv import load_dotenv
from os import path, getenv
from datetime import datetime


env_path = "./.env"
env_default_path = "./.env.default"

if path.isfile(env_path):
    load_dotenv(env_path)
    print("loaded env variables from: {}".format(env_path))
elif path.isfile(env_default_path):
    load_dotenv(env_default_path)
    print("loaded env variables from: {}".format(env_default_path))


def get_default_port():
    port = getenv("DEFAULT_PORT")
    if isinstance(port, str):
        return int(port)
    elif isinstance(port, int):
        return port
    else:
        return None


def get_default_url():
    url = getenv("DEFAULT_URL")
    if isinstance(url, str):
        return str(getenv("DEFAULT_URL"))
    else:
        return None


def get_default_locale():
    locale = getenv("DEFAULT_LOCALE")
    if isinstance(locale, str):
        return locale
    else:
        return None

    
def get_default_timezone():
    timezone = getenv("DEFAULT_TIMEZONE")
    if isinstance(timezone, str):
        return timezone
    else:
        return None


def get_default_reftime():
    return int(datetime.now().timestamp() * 1000)
