import telegram
from telegram.ext import Updater, CommandHandler

# Telegram bot token
bot_token = 'YOUR_BOT_TOKEN'


# Define a function to handle the /start command
def start(update):
    update.message.reply_text('Hi, I am your bot! Nice to meet you.')


# Create the updater and pass it your bot's token
updater = Updater(bot_token)

# Get the dispatcher to register handlers
dp = updater.dispatcher

# Register the /start command handler
dp.add_handler(CommandHandler('start', start))

# Start the bot
updater.start_polling()

# Run the bot until you press Ctrl-C
updater.idle()
