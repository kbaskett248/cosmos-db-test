import logging

import azure.functions as func

from shared import Source, process_trigger


MESSAGE_TEMPLATE = "Hello, {name}. This HTTP triggered function executed successfully."


def main(req: func.HttpRequest):
    logging.info("Python HTTP trigger function processed a request.")

    params = {}
    try:
        params = req.get_json()
    except ValueError:
        params = req.params

    kwargs = {"name": params.get("name", "friend")}

    message = process_trigger(Source.HTTP, MESSAGE_TEMPLATE, **kwargs)

    return func.HttpResponse(message)
