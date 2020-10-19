__all__ = [
    "CustomError"
]


class CustomError(BaseException):
    """Custom Exception(Base)"""
    include_err_name = True

    def prepare_description(self):
        desc = self.__doc__
        if self.include_err_name:
            desc = "{} - {}".format(type(self).__name__, desc)
        return desc

    @staticmethod
    def prepare_args(*args) -> str:
        return ", ".join(
            [
                str(arg)
                for arg in args
            ])

    @staticmethod
    def prepare_kwargs(**kwargs) -> str:
        return ", ".join([
            "{}={}".format(k, v)
            for k, v in kwargs.items()
        ])

    def prepare_err_message(self, *args, **kwargs):
        return "{}{}{}".format(self.prepare_description(),
                               self.prepare_args(*args),
                               self.prepare_kwargs(**kwargs))

    def __init__(self, *args, **kwargs):
        super().__init__(self.prepare_err_message(*args, **kwargs))
