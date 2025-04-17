import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7436449121:AAF44P_YmCvmJvyBmLNuzx_iCsBBvpN4Y3w")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "18579024"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "124981da628d86e21ee492da77cd4037")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "574224129"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://vikassonawale0:JWyQFas7vlG1bkaL@cluster0.beermge.mongodb.net/?retryWrites=true&w=majority") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
