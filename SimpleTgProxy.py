#!/usr/bin/env python3

import threading
import json

from BotConnector import BotConnector

from flask import Flask
from flask import request

import logging


class SimpleTgProxy:
    def __init__(self, bot: BotConnector):
        self.app = Flask(__name__)
        self.app.add_url_rule('/sendMessage', view_func=self.handle_send_message, methods=['POST'])
        self.host = None
        self.port = None
        self.bot = bot

        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.logger = logging.getLogger(__name__)

    def handle_send_message(self):
        request_json = json.loads(request.data)

        self.logger.info("Receive request: {}".format(request))
        self.logger.debug("Request data: {}".format(request_json))

        message = request_json['message']

        self.bot.send_message(message=message)
        return '', 204

    def run(self, host, port):
        self.logger.info("Starting OnlyDbTgProxy: http://{}:{}".format(host, port))
        self.host = host
        self.port = port
        self.app.run(host, port)

    def run_async(self, host, port):
        thread = threading.Thread(target=self.run, args=(host, port))
        thread.daemon = True
        thread.start()
