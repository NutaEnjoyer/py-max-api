from dotenv import load_dotenv
import os
from client.bot import Bot
from time import sleep

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

if not bot_token:
    raise ValueError("BOT_TOKEN is not set")

user_id = 4716849


bot = Bot(bot_token)

# me = bot.upload_photo(
#     path="photo.png",
# )

me = bot.send_message(user_id=user_id, text="Hello, world!")
# print(me)
me = bot.get_message(message_id=me.message_id)
print(f"me: {me}")
