import logging
import os

import azure.functions as func
import httpx


ENDPOINT = os.environ["ENDPOINT"]


def main(documents: func.DocumentList):
    if not documents:
        return "No documents"

    for document in documents:
        logging.info("Document: %s", document["id"])

        for key, value in document.items():
            logging.debug("    %s: %s", key, value)

        logging.info("Making request to %s", ENDPOINT)
        httpx.post(ENDPOINT, json=dict(document.items()))
