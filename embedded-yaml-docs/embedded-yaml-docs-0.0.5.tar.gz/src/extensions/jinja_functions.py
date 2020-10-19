class JinjaFunctions():
    """

    """


    @staticmethod
    def postindent_spaces(s: str, indent: int) -> str:
        """
        Indents the specified string with X amount of spaces, at the end.

        Parameters:
            s (str): The string to post indent with spaces.
            indent (int): Number of spaces to indent the string with.

        Returns:
            The indented string.
        """
        return f"{{:<{indent}}}".format(s)


    @staticmethod
    def preindent_spaces(s: str, indent: int) -> str:
        """
        Indents the specified string with X amount of spaces, at the start.

        Parameters:
            s (str): The string to pre indent with spaces.
            indent (int): Number of spaces to indent the string with.

        Returns:
            The indented string.
        """
        return f"{{:>{indent}}}".format(s)


    @staticmethod
    def align_multiline(block: str, indent: int, newline: bool):
        """
        Aligns a multi-line string by adding the relevant newlines and indentation.

        Parameters:
            block (str): The string block to indent.
            indent (int): Number of spaces to indent the string block by.
            newline (bool): True or False if the string block should start with a newline.

        Returns:
            A block string that has the lines aligned correctly.
        """
        # Variable to save the result.
        result = ''

        # Add a newline to the start of the string.
        if newline:
            result += '\n'

        # Indent each of the lines to match.
        for line in block.split('\n'):
            result += JinjaFunctions.preindent_spaces(line, indent) + '\n'

        return result