import logging.config
from logging_config import LOGGING

from app import create_app
from app.controllers import main


logging.config.dictConfig(LOGGING)
app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
