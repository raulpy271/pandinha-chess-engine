
import logging 

logging.basicConfig(filename='engine.log')

logger = logging.getLogger('engine')
logger.setLevel(logging.DEBUG)

def send_uci_msg(msg):
    logger.info(f'sending UCI message: {msg}')
    print(msg, flush=True)
