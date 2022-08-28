#!/usr/local/bin/python3.10

from src.logger import logger
from src.uci import start_uci_comunication_with_pool_of_process


if __name__ == '__main__':
    logger.info('Starting bot...')
    start_uci_comunication_with_pool_of_process()
    logger.info('Bot stopped!')

