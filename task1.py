import logging
"""logging.basicConfig(level=logging.INFO)
logging.debug('This will get logged')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')"""

logging.basicConfig(filename='app.log',filemode='a',format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')