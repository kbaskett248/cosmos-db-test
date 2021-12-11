import datetime
import logging

import azure.functions as func
from HttpTrigger import MESSAGE_TEMPLATE

from shared import Source, process_trigger


MESSAGE_TEMPLATE = "Processed timer trigger at {current_time}"


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = (
        datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    )

    kwargs = {
        "current_time": utc_timestamp,
        "past_due": mytimer.past_due,
    }

    template = MESSAGE_TEMPLATE
    if mytimer.past_due:
        template += "; It is past due."

    process_trigger(Source.TIMER, template, **kwargs)
