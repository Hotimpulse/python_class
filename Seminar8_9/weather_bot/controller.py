import datetime as dt
import requests

def start(update, context):
    update.message.reply_text("Hello! You could start with /forecast or /help")
    

def commands(update, context):
    update.message.reply_text("""
    Here's a list of commands:
     /start -> begin using the bot
     /help -> list of this bot's commands
     /forecast -> type any city's name to get a current report
     """) 

# def handle_msg(update, context):
#     update.message.reply_text(f"{update.message.text} is not a command. Try /help")

def get_weather(update, context):
    CITY = update.message.text
    update.message.reply_text("Enter a city's name: ")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&lang=en&appid=a9adf5362d777b3a3e388cb43506243e&units=metric'
    response = requests.get(url).json()
    print(response)
    temp = response['main']['temp']
    desc = response['weather'][0]['description']
    temp = response['main']['temp']
    wind = response['wind']['speed']
    sunrise = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
    update.message.reply_text(f"""
        Here's your weather report: 
        Temperature in {CITY} is: {temp}°C
        Weather in {CITY} is: {desc}
        Wind speed in {CITY} is: {wind} m/s
        The sun in {CITY} rises at: {sunrise}
        The sun in {CITY} sets at: {sunset}
        """)