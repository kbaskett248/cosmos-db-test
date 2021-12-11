from enum import Enum
import logging


class Source(Enum):
    TIMER = "TIMER"
    HTTP = "HTTP"


def process_trigger(source: Source, message_template: str, *args, **kwargs) -> str:
    message = f"{source}: {message_template}".format(*args, **kwargs)
    logging.info(message)
    return message
