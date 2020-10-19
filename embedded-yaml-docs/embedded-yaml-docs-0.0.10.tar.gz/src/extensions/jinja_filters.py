from jinja2.filters import prepare_select_or_reject, contextfilter


class JinjaFilters:
    """
    Collection of custom Jinja Filters.
    """


    @staticmethod
    def __select_or_reject_attr_if_present_key(args, kwargs, modfunc, lookup_attr):
        """
        Processes the select or reject filter only if the attribute exists.

        Parameters:
            args (list): The arguments to process.
            args[0] (any): The context of the Template.
            args[1] (any): The collection.
            args[2] (str): The attribute to use in the collection.
            args[3+] (str): Parameters for the Test function.
            modefunc (lambda): Function to use for the collection, used for inversing.
            lookup_attr (bool): Flag for if a particular attribute in the item should be used.

        Returns:
            List of items that either match the test function or do not contain the
            specified attribute.
        """
        seq, func = prepare_select_or_reject(args, kwargs, modfunc, lookup_attr)
        if seq:
            for item in seq:
                if args[2] in item.keys():
                    if func(item):
                        yield item
                else:
                    yield item


    @staticmethod
    def __select_or_reject_key(args, kwargs, inverse):
        """
        Selects or rejects the item only if it contains the key.

        Parameters:
            args (list): The arguments to process.
            args[0] (any): The context of the Template.
            args[1] (any): The collection.
            args[2] (str): The attribute to use in the collection.
            args[3+] (str): Parameters for the Test function.
            inverse (lambda): Whether to inverse the result or not.

        Returns:
            List of items that either does or doesn't contain the specified key.
        """
        if args[1]:
            for item in args[1]:
                if inverse:
                    if args[2] not in item.keys():
                        yield item
                else:
                    if args[2] in item.keys():
                        yield item


    @staticmethod
    @contextfilter
    def rejectattr_ifkey(*args, **kwargs):
        """
        Iterates through the collection and only rejects the item if the attribute
        both exists and it matches the supplied test.

        Parameters:
            args (any): The arguments to process.
            args[0] (any): The context of the Template.
            args[1] (any): The collection.
            args[2] (str): The attribute to use in the collection.
            args[3+] (any): Parameters for the Test function.

        Returns:
            List of items that do not match the test function or do not contain the
            specified attribute.
        """
        return JinjaFilters.__select_or_reject_attr_if_present_key(
            args,
            kwargs,
            lambda x: not x,
            True
        )


    @staticmethod
    @contextfilter
    def selectattr_ifkey(*args, **kwargs):
        """
        Iterates through the collection and only selects the item if the attribute
        both exists and it matches the supplied test.

        Parameters:
            args (any): The arguments to process.
            args[0] (any): The context of the Template.
            args[1] (any): The collection.
            args[2] (str): The attribute to use in the collection.
            args[3+] (any): Parameters for the Test function.

        Returns:
            List of items that match the test function or do not contain the
            specified attribute.
        """
        return JinjaFilters.__select_or_reject_attr_if_present_key(
            args,
            kwargs,
            lambda x: x,
            True
        )


    @staticmethod
    @contextfilter
    def rejectkey(*args, **kwargs):
        """
        Iterates through the collection and rejects the item it it contains the specified key.

        For use if the `selectattr()` function is returning false positives due to its truthiness
        behaviour.

        Parameters:
            args (list): The arguments to process.
            args[0] (any): The context of the Template.
            args[1] (any): The collection.
            args[2] (str): Key to select.

        Returns:
            List of items that either does not contain the specified key.
        """
        return JinjaFilters.__select_or_reject_key(
            args,
            kwargs,
            True
        )


    @staticmethod
    @contextfilter
    def selectkey(*args, **kwargs):
        """
        Iterates through the collection and selects the item it it contains the specified key.

        For use if the `selectattr()` function is returning false positives due to its truthiness
        behaviour.

        Parameters:
            args (list): The arguments to process.
            args[0] (any): The context of the Template.
            args[1] (any): The collection.
            args[2] (str): Key to select.

        Returns:
            List of items that contain the specified key.
        """
        return JinjaFilters.__select_or_reject_key(
            args,
            kwargs,
            False
        )


    @staticmethod
    def indent(block: str, indent: int, multi: bool) -> str:
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

        # Indent the lines, if multiline then then each line is indented.
        if multi:
            for line in block.split('\n'):
                result += f"{{:>{indent}}}".format(block) + '\n'
        else:
            result = f"{{:>{indent}}}".format(block)

        return result


    @staticmethod
    def postfix(s: str, postfix: str) -> str:
        """
        """
        return s + postfix


    @staticmethod
    def prefix(s: str, prefix: str) -> str:
        """
        """
        return prefix + s