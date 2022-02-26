import telebot;
import matplotlib.pyplot as plt;
import seaborn as sns;
import pandas as pd;
import numpy as np;

API_KEY = '5106214584:AAE7XYVPvggV8-f-bHLm7MlZNTO0wQYd9Og'
#API_KEY = os.getenv(KEY)
#print(KEY)
#print(API_KEY)
bot = telebot.TeleBot(API_KEY);
#Starrting bot displays all commands
@bot.message_handler(commands = ['start'])
def start(message):
  response = "/Greet: Introduction to MindBuddy \n "+"Age (your age): Reccommends fun activities for your age group \n"+"/app: Link to mental health app\n"+"/alexa: Chat bot on your very own alexa\n"+"help: Links to resources for you to get the help you deserve\n"+'/data: Shows the data and graphs about mental health statistics, for your own curiosity and betterment\n'+'/feedback: Allows you to give feedback about MindBuddy'
  bot.send_message(message.chat.id, response);

#Greeting and Info
@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.send_message(message.chat.id, "Hello, I am MindBuddy. I can help you with anything")
 

#Hello functions
@bot.message_handler(commands=['Hi'])
def hi(message):
  #print(message);
  bot.send_message(message.chat.id, "Hello, friend!")

@bot.message_handler(commands=['Hello'])
def hello(message):
  bot.send_message(message.chat.id, "How are you doing?")

@bot.message_handler(commands=['Hey'])
def hey(message):
  bot.send_message(message.chat.id, "What's up?")


#Ask for age and suggest ideas
def age_request(message):
  request = message.text.split()
  if len(request)<2 or request[0].lower() not in 'age':
    return False;
  else:
    return True;

@bot.message_handler(func=age_request)
def send_Activities(message):
  request = message.text.split()[1]  
  request = int(request);
  if(request < 0 or request > 130):
    bot.send_message(message.chat.id,"Enter a realistic age")
    return
  
  print(request);

  if(18 >= request > 0):
    activity = 'very young'
  elif(35 >= request > 18):
    activity = "young"
  elif(50 >= request > 35):
    activity = ''
  elif(60 >= request > 50):
    activity = 'yay'
  elif(70 >= request > 60):
    activity = "very old"
  elif(80 >= request > 70):
    activity = ""
  else:
    activity = 'hello'

  bot.send_message(message.chat.id, activity)

#Help Message
def help_request(message):
  request = message.text.lower().split()
  if request[0] not in 'help':
    return False;
  else:
    return True;
@bot.message_handler(func = help_request)
def sending(message):
  response = "Samaritans of Singapore(SOS) | 1767 OR 1800 221 4444 | 24 Hours \n\n"+"Institute of Mental Health (IMH) | 6389 2222 | 24 Hours \n\n"+"Community Health Assessment Team (CHAT) | 6493-6500 OR 6501 | 12pm to 9pm (Tue to Sat) \n\n"+"Singapore Association for Mental Health (SAMH) | 1800 283 7019 | 9am to 6pm weekdays\n\n"+"TOUCHline  | 1800 377 2252 | 9am to 6pm weekdays\n\n"+"Silver Ribbon | 6386 1928 or 6509 0271| 9am to 5pm weekdays except public holidays \n\n" +"Care Corner Counselling Centre (Mandarin) | 1800 3535 800 | 10am to 10pm except public holidays"
  bot.send_message(message.chat.id, response)

  
#/app and /alexa
@bot.message_handler(commands=['app'])
def app(message):
  #print(message);
  bot.send_message(message.chat.id, "<Insert Link to App>")

@bot.message_handler(commands=['alexa'])
def hi(message):
  #print(message);
  bot.send_message(message.chat.id, "<Insert Link to Alexa>")


#Data and Feedback
@bot.message_handler(commands=['data'])
def hi(message):
  #print(message);
  bot.send_message(message.chat.id, "<Insert Link to Data Aanalysis>")

@bot.message_handler(commands=['feedback'])
def hi(message):
  #print(message);
  bot.send_message(message.chat.id, "Please give us any feedback about our bot, positive, negative, places for improvement and more at MindBuddyBot@gmail.com so that we may serve you better in the future")

bot.polling()