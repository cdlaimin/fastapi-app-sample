import logging
from logging import handlers

sys_log = logging.getLogger()
sys_log.setLevel(level=logging.DEBUG)


def log_init():
    sys_log.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter(
        'process-ID:%(process)d - '
        'Thread-ID:%(thread)d- '
        'TimeStamp:%(asctime)s - '
        'Dir:%(pathname)s:%(lineno)d - '
        'Level:%(levelname)s - '
        'Message:%(message)s'
    )
    sys_log.handlers.clear()
    file_handler = handlers.TimedRotatingFileHandler('./logs/app_logs.log', encoding='utf-8', when='D')
    file_handler.setLevel(level=logging.INFO)
    file_handler.setFormatter(formatter)
    sys_log.addHandler(file_handler)