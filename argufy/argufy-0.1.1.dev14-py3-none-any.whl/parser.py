# -*- coding: utf-8 -*-
# copyright: (c) 2020 by Jesse Johnson.
# license: Apache 2.0, see LICENSE for more details.
'''Argufier is an inspection based CLI parser.'''

import inspect
import sys
from argparse import ArgumentParser, Namespace, _SubParsersAction
from inspect import _ParameterKind
from types import ModuleType
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    TypeVar,
)

# from argparse_color_formatter import ColorHelpFormatter, ColorTextWrapper
from docstring_parser import parse

from .argument import Argument

# Define function as parameters for MyPy
F = TypeVar('F', bound=Callable[..., Any])


class Parser(ArgumentParser):
    '''Provide CLI parser for function.'''

    __exclude_prefixes__ = ('@', '_')

    def __init__(self, *args: str, **kwargs: str) -> None:
        '''Initialize parser.

        Parameters
        ----------
        prog: str
            The name of the program
        usage: str
            The string describing the program usage
        description: str
            Text to display before the argument help
        epilog: str
            Text to display after the argument help
        parents: list
            A list of ArgumentParser objects whose arguments should also
            be included
        formatter_class: Object
            A class for customizing the help output
        prefix_chars: char
            The set of characters that prefix optional arguments
        fromfile_prefix_chars: None
            The set of characters that prefix files from which additional
            arguments should be read
        argument_default: None
            The global default value for arguments
        conflict_handler: Object
            The strategy for resolving conflicting optionals
        add_help: str
            Add a -h/--help option to the parser
        allow_abbrev: bool
            Allows long options to be abbreviated if the abbreviation is
            unambiguous

        '''
        module = self.__get_parent_module()
        if module:
            docstring = parse(module.__doc__)
            if not kwargs.get('description'):
                kwargs['description'] = docstring.short_description

        if module and 'prog' not in kwargs:
            kwargs['prog'] = module.__name__.split('.')[0]

        if 'version' in kwargs:
            self.version = kwargs.pop('version')

        super().__init__(**kwargs)  # type: ignore
        # if not hasattr(self, '_commands'):
        #     self._commands = None

        # if module:
        #     self._load_module(module)

    @staticmethod
    def __get_parent_module() -> Optional[ModuleType]:
        '''Get parent name importing this module.'''
        module = None
        stack = inspect.stack()
        stack_frame = stack[1]
        module = inspect.getmodule(stack_frame[0])
        return module

    @staticmethod
    def __get_args(argument: Argument) -> Dict[Any, Any]:
        '''Retrieve arguments from argument.'''
        return {
            k[len('_Argument__') :]: v  # noqa
            for k, v in vars(argument).items()
            if k.startswith('_Argument__')
        }

    def add_arguments(
        self, obj: Any, parser: Optional[ArgumentParser] = None
    ) -> 'Parser':
        '''Add arguments to parser/subparser.'''
        if not parser:
            parser = self
        docstring = parse(obj.__doc__)
        signature = inspect.signature(obj)
        for arg in signature.parameters:
            description = next(
                (d for d in docstring.params if d.arg_name == arg), None
            )
            argument = Argument(signature.parameters[arg], description)
            arguments = self.__get_args(argument)
            name = arguments.pop('name')
            parser.add_argument(*name, **arguments)
        # if signature.parameters:
        #     print('not empty')
        # else:
        #     print('empty')
        return self

    def add_commands(
        self,
        module: ModuleType,
        exclude_prefix: list = ['@', '_'],
        parser: Optional[ArgumentParser] = None,
    ) -> 'Parser':
        '''Add commands.'''
        module_name = module.__name__.split('.')[-1]
        docstring = parse(module.__doc__)

        if not parser:
            parser = self
        if not any(isinstance(x, _SubParsersAction) for x in parser._actions):
            parser.add_subparsers(dest=module_name)
        command = next(
            (x for x in parser._actions if isinstance(x, _SubParsersAction)),
            None,
        )

        # self._load_module(module, command, exclude_prefix)
        for name, value in inspect.getmembers(module):
            # TODO: Possible singledispatch candidate
            if not name.startswith(self.__exclude_prefixes__):
                if inspect.isclass(value):
                    continue  # pragma: no cover
                elif inspect.isfunction(value):  # or inspect.ismethod(value):
                    # TODO: Turn argumentless function into switch
                    if (
                        module.__name__ == value.__module__
                        and not name.startswith(
                            (', '.join(self.__exclude_prefixes__))
                        )
                    ):
                        if command:
                            cmd = command.add_parser(
                                name.replace('_', '-'),
                                help=parse(value.__doc__).short_description,
                            )
                            cmd.set_defaults(fn=value)
                        # print('command', name, value, cmd)
                        self.add_arguments(value, cmd)
                elif isinstance(value, (float, int, str, list, dict, tuple)):
                    # TODO: Reconcile inspect parameters with dict
                    parameters = inspect.Parameter(
                        name,
                        _ParameterKind.POSITIONAL_OR_KEYWORD,  # type: ignore
                        default=getattr(module, name),
                        annotation=inspect._empty,  # type: ignore
                    )
                    description = next(
                        (d for d in docstring.params if d.arg_name == name),
                        None,
                    )
                    argument = Argument(parameters, description)
                    arguments = self.__get_args(argument)
                    name = arguments.pop('name')
                    parser.add_argument(*name, **arguments)
        return self

    def add_subcommands(
        self,
        module: ModuleType,
        exclude_prefix: list = ['@', '_'],
        parser: Optional[ArgumentParser] = None,
    ) -> 'Parser':
        '''Add subcommands.'''
        module_name = module.__name__.split('.')[-1]
        docstring = parse(module.__doc__)

        if not parser:
            parser = self
        if not any(isinstance(x, _SubParsersAction) for x in parser._actions):
            parser.add_subparsers(dest=module_name)
        command = next(
            (x for x in parser._actions if isinstance(x, _SubParsersAction)),
            None,
        )
        if command:
            subcommand = command.add_parser(
                module_name.replace('_', '-'),
                help=docstring.short_description,
            )
            subcommand.set_defaults(mod=module)
        self.add_commands(module, exclude_prefix, subcommand)
        return self

    def __set_module_arguments(
        self, fn: Callable[[F], F], ns: Namespace
    ) -> Namespace:
        '''Separe module arguments from functions.'''
        if 'mod' in ns:
            mod = vars(ns).pop('mod')
        else:
            mod = None
        signature = inspect.signature(fn)
        # Separate namespace from other variables
        args = [
            {k: vars(ns).pop(k)}
            for k in list(vars(ns).keys()).copy()
            if not signature.parameters.get(k)
        ]
        if mod:
            for arg in args:
                for k, v in arg.items():
                    mod.__dict__[k] = v
        return ns

    def retrieve(
        self, args: Sequence[str] = None, ns: Optional[Namespace] = None,
    ) -> Tuple[List[str], Namespace]:
        '''Retrieve values from CLI.'''
        main_ns, main_args = self.parse_known_args(args, ns)
        if main_args == [] and 'fn' in vars(main_ns):
            return main_args, main_ns
        else:
            # NOTE: default to help message for subcommand
            if 'mod' in vars(main_ns):
                a = []
                a.append(vars(main_ns)['mod'].__name__.split('.')[-1])
                a.append('--help')
                self.parse_args(a)
            return main_args, main_ns

    def dispatch(
        self,
        args: Sequence[str] = sys.argv[1:],
        ns: Optional[Namespace] = None,
    ) -> Optional[Callable[[F], F]]:
        '''Call command with arguments.'''
        if args == []:
            args = ['--help']  # pragma: no cover
        arguments, namespace = self.retrieve(args, ns)
        if 'fn' in namespace:
            fn = vars(namespace).pop('fn')
            namespace = self.__set_module_arguments(fn, namespace)
            return fn(**vars(namespace))
        return None
