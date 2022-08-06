#!/usr/local/bin/python3.10

from src.logger import logger
from src.uci import start_uci_comunication


if __name__ == '__main__':
    logger.info('Starting bot...')
    start_uci_comunication()
    logger.info('Bot stopped!')

