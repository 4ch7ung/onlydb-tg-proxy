#!/usr/bin/env python3

import requests

import logging

BOT_URL = "https://api.telegram.org/bot"
SEND_METHOD = "sendMessage"


class BotConnector:
    def __init__(self, api_key: str, chat_id: str):
        self.api_key = api_key
        self.chat_id = chat_id

        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.logger = logging.getLogger(__name__)

    def send_message(self, message: str):
        method_url = "{}{}/{}".format(BOT_URL, self.api_key, SEND_METHOD)

        json = {
            "chat_id": self.chat_id,
            "text": message
        }
        self.logger.info("Sending message to chat '{}': {}", self.chat_id, message)
        res = requests.post(url=method_url, json=json)
        self.logger.debug(res)
