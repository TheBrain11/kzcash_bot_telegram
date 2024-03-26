#!venv/bin/python


import os 
import config
import telebot
import requests
from bitcoinrpc.authproxy import AuthServiceProxy

bot = telebot.TeleBot(config.token)
rpc_connection = AuthServiceProxy(f"http://{config.rpc_user}:{config.rpc_password}@{config.rpc_host}:{config.rpc_port}")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I am a command bot. Select one of the following commands:\n/getnewaddress - Get a new address\n/getbalance - Get balance")


@bot.message_handler(commands=['getnewaddress'])
def get_new_address(message):
    new_address = os.popen("~/kzcash-cli getnewaddress").read()
    bot.send_message(message.chat.id, f"New address generated: {new_address}")    

@bot.message_handler(commands=['getbalance'])
def get_balance(message):
    balance = os.popen("~/kzcash-cli getbalance").read()
    bot.send_message(message.chat.id, f"Current balance: {balance}")

@bot.message_handler(func=lambda message: True)
def repeat_all_messages(message):
    bot.send_message(message.chat.id, "Unknown command. Available commands: /getnewaddress, /getbalance")

if __name__ == '__main__':
    bot.polling(none_stop=True)


