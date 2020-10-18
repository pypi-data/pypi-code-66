import datetime
import os
from typing import Optional


class Logger:

    def __init__(
            self, file_path: Optional[str] = None,
            encoding: str = "utf-8",
            print_to_console: bool = True) -> None:
        """
        Initialises the Logger, also creates the file if file_path is provided.

        Args:
            file_path:
                absolute or relative path
            encoding:
                name of encoding of the logger file as string (not used, if
                file_path is not provided)
            print_to_console:
                a flag that determines whether to output messages to the console
                or not
        """
        if file_path and not os.path.exists(file_path):
            open(file_path, "w")
        self.file_path = file_path
        self.encoding = encoding
        self.print_to_console = print_to_console

    def log(self, log_type: str, message: str) -> None:
        """
        Appends the message to a file (if file_path is provided) and prints it
        in the console (if print_to_console is True).

        Args:
            log_type:
                type of the record. Does not affect anything except it is stated
                in the record after the date and time when the record were made
            message:
                a string to be written to the file or/and printed to the console
        """
        if self.file_path:
            with open(self.file_path, "a", encoding=self.encoding) as f:
                f.write(
                    f"[{datetime.datetime.now()}] [{log_type}] - {message}\n"
                )
        if self.print_to_console:
            print(message)

    def debug(self, message: str) -> None:
        """
        A shortcut for the log method of this class. log_type is set to DEBUG.

        Args:
            message:
                a string to be written to the file or/and printed to the console
        """
        self.log("DEBUG", message)

    def info(self, message: str) -> None:
        """
        A shortcut for the log method of this class. log_type is set to INFO.

        Args:
            message:
                a string to be written to the file or/and printed to the console
        """
        self.log("INFO", message)

    def warning(self, message: str) -> None:
        """
        A shortcut for the log method of this class. log_type is set to WARNING.

        Args:
            message:
                a string to be written to the file or/and printed to the console
        """
        self.log("WARNING", message)

    def error(self, message: str) -> None:
        """
        A shortcut for the log method of this class. log_type is set to ERROR.

        Args:
            message:
                a string to be written to the file or/and printed to the console
        """
        self.log("ERROR", message)

    def critical(self, message: str) -> None:
        """
        A shortcut for the log method of this class. log_type is set to
        CRITICAL.

        Args:
            message:
                a string to be written to the file or/and printed to the console
        """
        self.log("CRITICAL", message)
