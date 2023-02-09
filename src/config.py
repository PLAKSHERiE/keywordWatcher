from environs import Env

env = Env()
env.read_env()

API_ID = env.int("API_ID")
API_HASH = env.str("API_HASH")
DEVICE_MODEL = env.str("DEVICE_MODEL")
SYSTEM_VERSION = env.str("SYSTEM_VERSION")
APP_VERSION = env.str("APP_VERSION")

PHONE = env.str("PHONE")
PASSWORD = env.str("PASSWORD")

KEYWORDS = env.str("KEYWORDS").split(',')

WHO_TO_SEND_USERNAME = env.str("WHO_TO_SEND_USERNAME")
