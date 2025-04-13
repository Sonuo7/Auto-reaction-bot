from os import environ

API_HASH = environ.get("API_HASH", "3b33568aa7119719d1f37cb15b3ae587")
API_ID = int(environ.get("API_ID", "28137469"))
BOT_TOKEN = environ.get("BOT_TOKEN", "")
BOT_OWNER = int(environ.get("BOT_OWNER", "897584437"))
BOT_USERNAME = environ.get("BOT_USERNAME", "Nazriyarection_bot")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002169575469"))
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002189546391"))
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://sonuoj:sonuhij@cluster0.a9dkw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    # wes response configuration
    BOT_UPTIME = time.time()
    PORT = int(os.environ.get("PORT", "8080"))

# Define default emojis list
EMOJIS = [
    "👍", "🤷‍♂", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", 
    "🥶", "🤩", "🥳", "😎", "🙏", "👌", "🤣", "😇", "🥱", "🥴", "😍", "🤓", 
    "❤‍🔥", "🌚", "😐", "💯", "🦄", "⚡", "👾", "🏆", "💔", "🤨", "🌟", "😡", 
    "👅", "🆒", "😘", "😈", "😴", "😭", "👻", "🌈", "👨‍💻", "👀", "🎃", "🙄", 
    "🤧", "😨", "🤝", "🤐", "🤗", "🫡", "🤭", "🥸", "🤫", "😶‍🌫", "🤪", "😏"
]
