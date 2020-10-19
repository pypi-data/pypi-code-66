import os


class FileDelegate:
    def __init__(self, parent: str):
        self.parent = parent

    def provide(self, file: str):
        """Provide the full path

        Args:
            file (str): destination file

        Returns:
            [str]: full path concat the parent and the file path
        """
        return os.path.join(self.parent, file)
