#first we import the module that would allow us to code the front-end of the telegram bot
#these classes are imported from the module 
#Updater receives the message from the bot and sends it to dispatcher
#CommandHandler handles telegram commands
#MessageHandler handles telegram messages which might contain texts, media or status updates
#Filters are predefined filter arguments which are used by MessageHandler to filter messages
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#user-defined function which sends a message through the bot when we send the /hello commmand
def hello(update, context):
#it sends it through context.bot.send_message() method
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')

 #the updater uses the API token to update the messages received by the bot
updater = Updater(token='5606784564:AAGhG941aNsJUqpK0JGvvyVqcuVgQ7I0CbQ', use_context=True)
#it then sends these messages to the dispatcher
dispatcher = updater.dispatcher'

#basically here we link the /hello command with the user-defined hello function
hello_handler = CommandHandler('hello', hello)
#the CommandHandler is then registered to the dispatcher
dispatcher.add_handler(hello_handler)
#the last command starts the bot
updater.start_polling()
