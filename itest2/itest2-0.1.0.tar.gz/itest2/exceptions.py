# -*- coding: utf-8 -*-

class ITestException(BaseException):
    """
    Base Test exception.
    """

    def __init__(self, msg=None, stacktrace=None):
        self.msg = msg
        self.stacktrace = stacktrace

    def __str__(self):
        exception_msg = "Message: %s\n" % self.msg
        if self.stacktrace is not None:
            stacktrace = "\n".join(self.stacktrace)
            exception_msg += "Stacktrace:\n%s" % stacktrace
        return exception_msg


class TimeoutException(ITestException):...
class ClientNotFountException(ITestException):...
