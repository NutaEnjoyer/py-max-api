from dotenv import load_dotenv
import os
from client.bot import Bot

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

user_id = 4716849


bot = Bot(bot_token)

# me = bot.upload_photo(
#     path="photo.png",
# )

me = bot.get_chat(chat_link=-68056075837489)
print(me)
