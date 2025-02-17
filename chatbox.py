## this file is based on version 13.7 of python telegram chatbot
## and version 1.26.18 of urllib3
## chatbot.py
import openai
import os
import telegram
from telegram.ext import Updater, MessageHandler, Filters
# The messageHandler is used for all message updatesimport configparser
import configparser
import logging
import requests


OPENAI_API_KEY = "3ce13f11-cb8f-45e3-8f86-b2f95ef508a6"
openai.api_key = OPENAI_API_KEY
apiKey = OPENAI_API_KEY
basicUrl = "https://genai.hkbu.edu.hk/general/rest"
modelName = "gpt-4-o-mini"
apiVersion = "2024-05-01-preview"

def ask_gpt4(prompt):
    conversation = [{"role": "user", "content": prompt}]
    url = basicUrl + "/deployments/" + modelName + "/chat/completions/?api-version=" + apiVersion
    headers = {'Content-Type': 'application/json', 'api-key': apiKey}
    payload = {'messages': conversation}
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['choices'][0]['message']['content']
    else:
        return 'Error:', response

def main():
    # Load your token and create an Updater for your Bot
    config = configparser.ConfigParser()
    config.read('/Users/macbookpro/Desktop/comp7940-lab3/config.ini', encoding='utf-8')
    print(config['TELEGRAM'])
    updater = Updater(token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
    dispatcher =updater.dispatcher
    # You can set this logging module,
    # so you will know when and why things do not work as expected
    logging.basicConfig(format='%(asctime)s-%(name)s-%(levelname)s -%(message)s',
    level=logging.INFO)
    # register a dispatcher to handle message:
    # here we register an echo dispatcher
    echo_handler = MessageHandler(Filters.text &(~Filters.command), echo)
    dispatcher.add_handler(echo_handler)
    # To start the bot:
    updater.start_polling()
    updater.idle()

def echo(update, context):
    reply_message = ask_gpt4(update.message.text)
    logging.info("Update:" + str(update))
    logging.info("context:" + str(context))
    context.bot.send_message(chat_id=update.effective_chat.id, text= reply_message)


if __name__ == '__main__':
    main()
