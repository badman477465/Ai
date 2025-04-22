import asyncio
from pyrogram import Client, filters
import openai
import os

api_id = 20045649
api_hash = "dbed4fbace68eadb961a1ce441801ae2"
bot_token = os.getenv("BOT_TOKEN")
session_string = os.getenv("SESSION_STRING")
openai.api_key = os.getenv("OPENAI_API_KEY")
chat_id = int(os.getenv("CHAT_ID"))

app = Client("miss_rehana", api_id=api_id, api_hash=api_hash, bot_token=bot_token, in_memory=True)

@app.on_message(filters.private & filters.text)
async def handle_message(client, message):
    if str(message.chat.id) != str(chat_id):
        return

    user_input = message.text
    await message.reply_chat_action("typing")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        bot_reply = response.choices[0].message.content.strip()
    except Exception as e:
        bot_reply = "Something went wrong. Please try again later."

    await message.reply_text(bot_reply)

if __name__ == "__main__":
    print("Bot is running...")
    app.run()