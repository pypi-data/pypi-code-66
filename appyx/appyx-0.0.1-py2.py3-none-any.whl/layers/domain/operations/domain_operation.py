from appyx.layers.domain.exceptions.early_return import EarlyReturnException
from appyx.layers.domain.result import Result


class DomainOperation:
    """
    Models an operation from the Domain.
    Answers a Result after executing the operation.
    Can delegate the return from execute() to private methods.

    Subclasses should implement _execute_logic(), calling _return() if they need to return from execute().

    Note: _save_model is a crutch that couples us to Django. Further iterations will remove this coupling.
    """
    def __init__(self) -> None:
        super().__init__()
        self._result = Result()

    def execute(self):
        self._result = Result()

        try:
            self._execute_logic()
        except EarlyReturnException:
            pass

        return self._result

    def _return(self):
        raise EarlyReturnException()

    def _execute_logic(self):
        raise NotImplementedError("Subclass responsibility")

    def _save_model(self, model):
        model.full_clean()
        model.save()
        return model
