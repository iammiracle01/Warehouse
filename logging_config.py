import os
import logging
import logging.config


if not os.path.exists('logs'):
    os.makedirs('logs')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'controller_file': {
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': 'logs/controller.log',
            'mode': 'a',
        },
        'service_file': {
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': 'logs/service.log',
            'mode': 'a',
        },
    },
    'loggers': {
        'controller_logger': {
            'handlers': ['console', 'controller_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'service_logger': {
            'handlers': ['console', 'service_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

logging.config.dictConfig(LOGGING)
