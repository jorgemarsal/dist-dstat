import logging
from color import *

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-8s [%(filename)s:%(lineno)s-%(funcName)20s()] DR-1.1 %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/tmp/dist-dstat.log',
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger

dr_logger = logging.getLogger('dist-dstat')
dr_logger.addHandler(console)


def log_error(msg):
    dr_logger.error(to_red(msg))

def log_warning(msg):
    dr_logger.warning(to_yellow(msg))

def log_green(msg):
    dr_logger.info(to_green(msg))

