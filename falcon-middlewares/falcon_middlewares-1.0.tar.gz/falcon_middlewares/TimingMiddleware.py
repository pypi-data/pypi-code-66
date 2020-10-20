import datetime


class TimingMiddleware:
    def __init__(self, logger):
        self.__logger = logger

    def process_resource(self, req, resp, resource, params):  # noqa: F841
        resp.set_header(
            "ReceptionTimestamp", str(datetime.datetime.now().timestamp())
        )

    def process_response(
        self, req, resp, resource, req_succeeded
    ):  # noqa: F841
        reception_header = resp.get_header("ReceptionTimestamp")
        if reception_header:
            reception_timestamp = float(reception_header)
            now = datetime.datetime.now().timestamp()
            execution_time = now - reception_timestamp
            resp.set_header("ExecutionTime", execution_time)
            self.__logger.info(
                f"Endpoint {resource.__class__.__name__}(success={req_succeeded})={execution_time}s"
            )
