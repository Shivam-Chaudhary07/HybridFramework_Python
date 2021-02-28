import logging

logging.basicConfig(filename=r'C:\Users\dell\Pictures\Screenshots\test.log', format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logging.debug('debug')
logging.info("Info log")
logging.warning("Warning")
logging.critical("Critical")
logging.error('error')
#logging start from warning, we have to set level before that

