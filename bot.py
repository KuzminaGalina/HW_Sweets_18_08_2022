from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from config import TOKEN
from functions import*

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher



start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, main)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

print('server started')
updater.start_polling()
updater.idle()