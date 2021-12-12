import datetime
from enum import Enum
import logging
import os
from typing import Optional

DEFAULT_SUBJECT = os.environ.get("DEFAULT_SUBJECT", "New Event")
DEFAULT_MESSAGE_TEMPLATE = os.environ.get(
    "DEFAULT_MESSAGE_TEMPLATE",
    "A new event was received at {current_time} and is being processed",
)
DEFAULT_RECIPIENT = os.environ.get("DEFAULT_RECIPIENT")


class Source(Enum):
    """Simple enum to define the source that we're triggering."""

    TIMER = "TIMER"
    HTTP = "HTTP"


def process_trigger(
    source: Source,
    subject: str = DEFAULT_SUBJECT,
    recipient: Optional[str] = DEFAULT_RECIPIENT,
    message_template: str = DEFAULT_MESSAGE_TEMPLATE,
) -> str:
    """Process a trigger from various sources.

    Each of the arguments can be defined as environment variables.

    Args:
        source (Source): The source of the trigger being processed.
        recipient (str, optional): A message recipient. Defaults to DEFAULT_RECIPIENT.
        subject (str, optional): A message subject. Defaults to DEFAULT_SUBJECT.
        message_template (str, optional): A format-compatible message template.
            The template is formatted with each of the arguments and the current_time.
            Defaults to DEFAULT_MESSAGE_TEMPLATE.

    Returns:
        str: [description]
    """
    current_time = (
        datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    )
    message = message_template.format(
        current_time=current_time, recipient=recipient, source=source, subject=subject
    )
    logging.info(f"    source:    {source}")
    logging.info(f"    subject:   {subject}")
    logging.info(f"    recipient: {recipient}")
    logging.info(f"    message:   {message}")

    return message
