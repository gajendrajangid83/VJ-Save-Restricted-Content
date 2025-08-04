import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7974726072:AAGW5SmG5nw6k4MA1A6zmycB1Qg-NMyVuJ8")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21157244"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4981c2699bd91c7db836ec8f77e5b0f0")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1783306092"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "saraswatisharma")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
