#!/usr/bin/env python3

from SimpleTgProxy import SimpleTgProxy
from BotConnector import BotConnector

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    import os

    api_key = os.getenv('API_KEY')

    listener_host = os.getenv('LISTENER_HOST')
    listener_port = os.getenv('LISTENER_PORT')

    receiver_chat_id = os.getenv('RECEIVER_CHAT_ID')

    logger.debug(
        "Starting with args:\nAPI_KEY={}\nLISTENER_HOST={}\nLISTENER_PORT={}\nRECEIVER_CHAT_ID={}"
        .format(api_key, listener_host, listener_port, receiver_chat_id)
    )

    bot = BotConnector(api_key=api_key, chat_id=receiver_chat_id)

    tg_proxy = SimpleTgProxy(bot=bot)
    tg_proxy.run_async(listener_host, listener_port)
