class Recorder:
    def __init__(self, file_name):
        self.file_name = file_name
        self._write_line("# Experiment Record")

    def _write(self, s):
        with open(self.file_name, "a") as f:
            f.write(s)

    def _write_line(self, s):
        with open(self.file_name, "a") as f:
            f.write(s + "\n")

    def begin_meta(self):
        s = "## Meta\n" + \
            "| key | value |\n" + \
            "| :-: |  :-:  |\n"
        self._write(s)

    def begin_data(self):
        s = "## Data"
        self._write_line(s)

    def write_meta(self, key, value):
        s = f"| {key} | {str(value)} |"
        self._write_line(s)

    def write_header(self, *args):
        length = len(args)
        args = map(str, args)
        s = " | ".join(args)
        s = "| " + s + " |"
        s2 = "| :-: " * length + "|"
        self._write_line(s)
        self._write_line(s2)

    def write_data(self, *args):
        args = map(str, args)
        s = " | ".join(args)
        s = "| " + s + " |"
        self._write_line(s)