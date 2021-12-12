import logging

import azure.functions as func

from shared import Source, process_trigger


def main(req: func.HttpRequest):
    logging.info("Python HTTP trigger function processed a request.")

    params = {}
    try:
        params = req.get_json()
    except ValueError:
        params = req.params

    kwargs = {}

    for k in ("recipient", "subject", "message_template"):
        try:
            kwargs[k] = params[k]
        except KeyError:
            pass

    message = process_trigger(Source.HTTP, **kwargs)

    return func.HttpResponse(message)
