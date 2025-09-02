import os
import telebot

BOT_TOKEN = os.getenv("8115790971:AAFO62ui_Vv1KUabC8fYrmZkhhFWdga4dyY")  # token will come from environment
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! ✅ Your bot is running from GitHub + free hosting 🎉")

bot.polling()
