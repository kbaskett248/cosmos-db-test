import logging

import azure.functions as func


OPERATIONS = {
    "-": lambda x, y: x - y,
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def main(documents: func.DocumentList):
    if not documents:
        return "No documents"

    for document in documents:
        logging.info("Document: %s", document["id"])
        for key, value in document.items():
            logging.info("    %s: %s", key, value)

        try:
            num1 = document["num1"]
            num2 = document["num2"]
            operation = document["operation"]
        except KeyError:
            logging.error("Missing one or more required fields")
            continue

        try:
            operator = OPERATIONS[operation]
        except KeyError:
            logging.error("Unhandled operation %s", operation)
            continue

        result = operator(num1, num2)

        logging.info(
            "%s: %s %s %s = %s",
            document["id"],
            num1,
            operation,
            num2,
            result,
        )
