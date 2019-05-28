import os
import platform
import logging


def main():
    log_file = None
    if platform.platform().startswith('Windows'):
        log_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
    else:
        log_file = os.path.join(os.getenv('HOME'), 'test.log')
    print('Log file with its location', log_file)

    # log configuration
    logging.basicConfig(
        level = logging.DEBUG,
        format = '%(asctime)s : %(levelname)s : %(message)s',
        filename=log_file,
        filemode='w'
    )

    logging.debug("Hi this is debug")
    logging.info('Hi this is info')
    logging.warning('Hi this is warning')
    #logging.warn('Hi this is war')
    logging.critical('Hi this is critical')
    logging.exception('Hi this is exception')
    logging.error('Hi this error')
    logging.debug("Hi this is debug")

    #print(logging.BASIC_FORMAT)
    #print(logging.getLoggerClass())

if __name__ == '__main__':
    main()


