import datetime
import azure.functions as func

from shared import Source, process_trigger


def main(mytimer: func.TimerRequest) -> None:
    process_trigger(Source.TIMER)
