from enum import Enum
import logging


class Source(Enum):
    """Simple enum to define the source that we're triggering."""

    TIMER = "TIMER"
    HTTP = "HTTP"


def process_trigger(source: Source, message_template: str, *args, **kwargs) -> str:
    """Process a trigger from various sources.

    Args:
        source (Source): The source of the trigger being processed.
        message_template (str): A format-compatible template string to log and return.
            The string is formatted using args and kwargs.
        *args: Arguments used to format message_template
        **kwargs: Keyword arguments used to format message_template

    Returns:
        str: The formatted message template
    """
    message = f"{source}: {message_template}".format(*args, **kwargs)
    logging.info(message)
    return message
