import datetime
import logging

import azure.functions as func


OPERATIONS = ["-", "+", "*", "/"]


def main(mytimer: func.TimerRequest, doc: func.Out[func.Document]) -> None:
    utc_time = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)

    operation = OPERATIONS[utc_time.second % len(OPERATIONS)]

    doc.set(
        func.Document.from_dict(
            {"num1": utc_time.hour, "num2": utc_time.minute, "operation": operation}
        )
    )

    logging.info("Added document to db: %s", doc)
