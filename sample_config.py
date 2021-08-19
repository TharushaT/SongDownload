import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1953870935:AAF3yYLfO52PlnvXcDF2IaBDUNsQBIRnMhY")

    APP_ID = int(os.environ.get("APP_ID", 3678414))

    API_HASH = os.environ.get("API_HASH", "7093f9c89addce5894492a30f73be34d")
