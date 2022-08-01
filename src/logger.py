
import logging 
from src.settings import LOG_FILE, LOG_LEVEL

logging.basicConfig(filename=LOG_FILE)

logger = logging.getLogger('engine')
logger.setLevel(LOG_LEVEL)

def send_uci_msg(msg):
    logger.info(f'sending UCI message: {msg}')
    print(msg, flush=True)
