from controller import *
import telegram.ext


TOKEN = '5708796742:AAE3AujmE5BS50AQgHtE6JH5dpI8YXZODuU'

updater = telegram.ext.Updater(TOKEN, use_context=True)

disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", commands))
disp.add_handler(telegram.ext.CommandHandler("forecast", get_weather))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_msg))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, get_weather))

updater.start_polling()
