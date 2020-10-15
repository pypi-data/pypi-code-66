#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import logging
import re
import warnings
from collections import namedtuple
from enum import Enum
from pathlib import Path
from sys import exit
from typing import Iterable, Optional, Union, List, overload, Match, Mapping, Generator
from docopt import docopt, DocoptExit
from myminions import (
    docopt_parsable,
    load_yaml_file_content,
    update_yaml_file_content,
    get_piped_command_line_arguments,
)


# create LOGGER with this namespace's name
_logger = logging.getLogger("marktask")
_logger.setLevel(logging.ERROR)
# create console handler and set level to debug
writes_logs_onto_console = logging.StreamHandler()
# add formatter to ch
writes_logs_onto_console.setFormatter(
    logging.Formatter(
        "%(asctime)s - %(name)s - %(module)s - %(funcName)s "
        "- %(lineno)s - %(levelname)s - %(message)s"
    )
)


__version__ = "0.0a4"
__all__ = [
    "filter_marker_files_by_states",
    "get_target_path_of_marker",
    "is_a_marker_filename",
    "iter_all_marker_files",
    "iter_marker_files_with_state",
    "iter_target_paths_with_task_states",
    "load_task_file",
    "mark_task",
    "mark_tasks",
    "propose_task_filepath",
    "state_of_tasks_are",
    "Task",
    "TASK_FILE_EXTENTION",
    "TaskStates",
    "writes_logs_onto_console",
]

COMMAND_MARK_SHORT = "m"
COMMAND_MARK_LONG = "mark"
COMMAND_MARK_OPTION_D = "-d"
COMMAND_LIST_SHORT = "l"
COMMAND_LIST_LONG = "list"
DEFAULT_TASK_FILE_NAME = ".marktask.yml"
TASK_FILE_EXTENTION = DEFAULT_TASK_FILE_NAME
ALLOWED_TASK_NAME_PATTERN = re.compile("^[a-zA-Z_][0-9a-zA-Z_]*$")
ALLOWED_TASK_STATE_PATTERN = re.compile("^[0-9a-zA-Z_]*$")
TASK_PATTERN = re.compile("^([a-zA-Z_][0-9a-zA-Z_]+):([a-zA-Z_][0-9a-zA-Z_]+)$")
TASK_REPRESENTATION_DELIMITER = ","

APath = Union[str, Path]


def _get_default(container_dict: dict, key: str, default_value):
    try:
        return container_dict[key]
    except KeyError:
        return default_value


def _print_paths(a_bunch_of_paths: Iterable[Path]):
    if a_bunch_of_paths is None:
        return None
    for path in a_bunch_of_paths:
        sys.stdout.write("{}\n".format(path))


def _use_root_folder_of_file(provided_path: Path) -> Path:
    if provided_path.is_file():
        return provided_path.parent
    return provided_path


def _yield_root_folder_of_file(
    provided_paths: Iterable[Path],
) -> Generator[Path, None, None]:
    for provided_path in provided_paths:
        yield _use_root_folder_of_file(provided_path)


def _split_task_representations(task_representation: str) -> List[str]:
    """
    Splits multiple task representations within a single string into
    a list of task representations.

    Examples:
        >>> _split_task_representations("key1:val1,key2:val2")
        ['key1:val1', 'key2:val2']
        >>> _split_task_representations("key1:val1,")
        ['key1:val1']

    Args:
        task_representation(str):
            A single or multiple task representations.

    Returns:
        List[str]
    """
    try:
        return [
            key_value_pair
            for key_value_pair in task_representation.split(
                TASK_REPRESENTATION_DELIMITER
            )
            if key_value_pair
        ]
    except AttributeError:
        raise TypeError(
            "`task_representation` expects string, but got '{}' instead."
            "".format(type(task_representation))
        )


def _get_ingoing_paths(sys_argv_input: Optional[List[str]]) -> List[Path]:
    """
    Converts ingoing paths from the command line arguments to resolved
    `pathlib.Paths`. If no ingoing path is specified, the current working
    directory path is returned.

    Args:
        sys_argv_input:

    Returns:
        List[Path]:
            Resolved paths with the received order.
    """
    assert sys_argv_input is None or isinstance(
        sys_argv_input, List
    ), "The ingoing path needs to be a string, or 'None'."

    no_path_was_supplied = len(sys_argv_input) == 0
    if no_path_was_supplied:
        return [Path().cwd()]

    no_path_supplied_by_commandline = sys_argv_input is None or not sys_argv_input
    if no_path_supplied_by_commandline:
        return [Path().cwd()]
    return [Path(path).resolve() for path in sys_argv_input if path != ""]


def _get_ingoing_paths(sys_argv_input: Optional[List[str]]) -> List[Path]:
    """
    Converts ingoing paths from the command line arguments to resolved
    `pathlib.Paths`. If no ingoing path is specified, the current working
    directory path is returned.

    Args:
        sys_argv_input:

    Returns:
        Un
    """
    assert sys_argv_input is None or isinstance(
        sys_argv_input, List
    ), "The ingoing path needs to be a string, or 'None'."

    no_path_supplied_by_commandline = sys_argv_input is None or not sys_argv_input
    if no_path_supplied_by_commandline:
        return [Path().cwd()]
    return [Path(path) for path in sys_argv_input if path is not None]


class TaskStates(Enum):
    PREPARED = "prepared"
    DONE = "done"

    @overload
    @classmethod
    def to_task_state(cls, state_value: str) -> "TaskStates":
        pass

    @overload
    @classmethod
    def to_task_state(cls, state: "TaskStates") -> "TaskStates":
        pass

    @classmethod
    def to_task_state(cls, state_or_value: Union[str, "TaskStates"]) -> "TaskStates":
        """
        Examples:
            >>> TaskStates.to_task_state("prepared")
            <TaskStates.PREPARED: 'prepared'>
            >>> TaskStates.to_task_state(TaskStates.DONE)
            <TaskStates.DONE: 'done'>

        Args:
            state_or_value(str, TaskStates):
                Either a string value of TaskStates or a TaskStates item itself.

        Returns:
            TaskStates:
                Equivalent item of TaskStates for *state_or_value*
        """
        if isinstance(state_or_value, cls):
            return state_or_value

        for state in cls:
            if state.value == state_or_value:
                return state
        raise ValueError("'{}' is not in {}".format(state_or_value, cls.__name__))


class Task(Mapping):
    NAME = "task_name"
    STATE = "task_state"
    """

    Examples:
        >>> sample_task = Task("name", "state")
        >>> str(sample_task)
        'name:state'
        >>> list(sample_task)
        ['task_name', 'task_state']
        >>> dict(sample_task)
        {'task_name': 'name', 'task_state': 'state'}

    """

    @overload
    def __init__(self, task_name: str, task_state: TaskStates):
        pass

    @overload
    def __init__(self, task_name: str, task_state: str):
        pass

    def __init__(self, task_name: str, task_state: Union[str, TaskStates]):
        if not self.allowed_name(task_name):
            raise ValueError("'{}' is not allowed for a task name.".format(task_name))
        if not self.allowed_state(task_state):
            raise ValueError("'{}' is not allowed for a task state.".format(task_state))
        self._values = {"task_name": task_name, "task_state": task_state}

    def __iter__(self) -> str:
        return iter(self._values)

    def __next__(self) -> str:
        return next(self._values)

    def __len__(self) -> int:
        return len(self._values)

    def __getitem__(self, key: str) -> str:
        return self._values[key]

    @property
    def name(self) -> str:
        return self._values[Task.NAME]

    @property
    def state(self) -> str:
        return self._values[Task.STATE]

    @staticmethod
    def allowed_name(name_to_check: str) -> bool:
        """
        Examples:
            >>> Task.allowed_name("start_with_a_char")
            True
            >>> Task.allowed_name("_underscores_are_allowed")
            True
            >>> Task.allowed_name("a")
            True
            >>> Task.allowed_name("whitespaces are not allowed")
            False
            >>> Task.allowed_name("1_leading_numbers_are_disallowed")
            False
            >>> Task.allowed_name("Special_chars +-.;, etc. are_disallowed")
            False

        Args:
            name_to_check(str):
                A potential name valid for ALLOWED_TASK_NAME_PATTERN.

        Returns:
            bool
        """
        return ALLOWED_TASK_NAME_PATTERN.match(name_to_check) is not None

    @staticmethod
    def allowed_state(state_to_check: Union[str, TaskStates]) -> bool:
        """
        Examples:
            >>> Task.allowed_state(TaskStates.DONE)
            True
            >>> Task.allowed_state("start_with_a_char")
            True
            >>> Task.allowed_state("_underscores_are_allowed")
            True
            >>> Task.allowed_state("a")
            True
            >>> Task.allowed_state("1_leading_numbers_are_allowed")
            True
            >>> Task.allowed_state("whitespaces are not allowed")
            False
            >>> Task.allowed_state("Special_chars +-.;, etc. are_disallowed")
            False

        Args:
            state_to_check:
                A potential state valid for ALLOWED_TASK_STATE_PATTERN.

        Returns:
            bool
        """
        if isinstance(state_to_check, TaskStates):
            return True
        return ALLOWED_TASK_STATE_PATTERN.match(state_to_check) is not None

    @classmethod
    def is_a_task_representation(cls, task_representation: str):
        """
        Examples:
            >>> Task.is_a_task_representation("name:value")
            True
            >>> Task.is_a_task_representation("{name:value}")
            False
            >>> Task.is_a_task_representation("name-1:value")
            False
            >>> Task.is_a_task_representation("name:a value")
            False


        Args:
            task_representation:

        Returns:

        """
        representation_match = TASK_PATTERN.match(task_representation)
        return cls._is_a_task_representation(representation_match)

    @classmethod
    def _is_a_task_representation(cls, representation_match: Optional[Match]) -> bool:
        return representation_match is not None

    @classmethod
    def parse(cls, task_representation: str) -> Optional["Task"]:
        """
        Examples:
            >>> Task.parse("name:value")
            name:value
            >>> print(Task.parse("1_not_allowed_name:and value"))
            None

        Args:
            task_representation:

        Returns:

        """
        matched_representation = TASK_PATTERN.match(task_representation)
        if not cls._is_a_task_representation(matched_representation):
            return None
        name = matched_representation.group(1)
        state = matched_representation.group(2)
        return Task(task_name=name, task_state=state)

    def __repr__(self):
        return "{}:{}".format(self.name, self.state)


"""
Examples:
    >>> from isisysdic import ProjectTaskFile
    >>> from tempfile import TemporaryDirectory
    >>> from pathlib import Path
    >>> with TemporaryDirectory() as temp_dir:
    ...     print(
    ...         "Calculation was done?",
    ...         ProjectTaskFile.state_of_tasks_are(
    ...             temp_dir, ProjectTaskFile.CALCULATION_DONE
    ...         )
    ...     )
    ...     ProjectTaskFile.mark_task(temp_dir, ProjectTaskFile.CALCULATION_DONE)
    ...     print(
    ...         "Calculation was done?",
    ...         ProjectTaskFile.state_of_tasks_are(
    ...             temp_dir, ProjectTaskFile.CALCULATION_DONE
    ...         )
    ...     )
    Calculation was done? False
    Calculation was done? True

"""


def is_a_marker_filename(filepath: str) -> bool:
    """
    Examples:
        >>> is_a_marker_filename(DEFAULT_TASK_FILE_NAME)
        True
        >>> is_a_marker_filename("/" + DEFAULT_TASK_FILE_NAME)
        True
        >>> is_a_marker_filename(DEFAULT_TASK_FILE_NAME + "something")
        False

    Args:
        filepath:

    Returns:

    """
    cut_right_count = len(DEFAULT_TASK_FILE_NAME)
    file_ending_is_default_name = filepath[-cut_right_count:] == DEFAULT_TASK_FILE_NAME
    return file_ending_is_default_name


def propose_task_filepath(path_to_mark: Path) -> Path:
    """
    Proposes the name and location of the task file. This method will be the
    entry point for a customization of the task file name.

    Examples:
        >>> from myminions import strip_for_doctest
        >>> from tempfile import TemporaryDirectory
        >>> from pathlib import Path
        >>> with TemporaryDirectory() as temp_dir:
        ...     a_test_folder = Path(temp_dir, "a_folder")
        ...     a_test_folder.mkdir()
        ...     task_filepath_for_folder = propose_task_filepath(a_test_folder)
        ...     strip_for_doctest(temp_dir, task_filepath_for_folder)
        ...     a_test_file = Path(temp_dir, "a_file.txt")
        ...     a_test_file.touch()
        ...     task_filepath_for_file = propose_task_filepath(a_test_file)
        ...     strip_for_doctest(temp_dir, task_filepath_for_file)
        ...     a_test_marker_file = Path(temp_dir, "marker"+DEFAULT_TASK_FILE_NAME)
        ...     a_test_marker_file.touch()
        ...     test_marker_file = propose_task_filepath(a_test_marker_file)
        ...     strip_for_doctest(temp_dir, test_marker_file)
        '... /a_folder/.marktask.yml'
        '... /a_file.txt.marktask.yml'
        '... /marker.marktask.yml'
        >>> propose_task_filepath("not/existing")
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
            raise FileExistsError("Non existent paths cannot be marked.")
        FileExistsError: 'not/existing' does not exist. Non existent paths cannot be marked.

    Args:
        path_to_mark(Path):
            Path in which the task file will be contained.

    Raises:
        FileExistsError:
            If the given *path to mark* does not exists.

    Returns:
        Path:
            Path of the mark file.
    """
    assert path_to_mark is not None, "folder_path cannot be 'None'."
    path_to_mark = Path(path_to_mark)
    if not path_to_mark.exists():
        raise FileExistsError(
            "'{}' does not exist. Non existent paths cannot be marked."
            "".format(path_to_mark)
        )
    if is_a_marker_filename(str(path_to_mark)):
        return Path(path_to_mark)
    if path_to_mark.is_file():
        return Path(str(path_to_mark) + DEFAULT_TASK_FILE_NAME)
    return path_to_mark.joinpath(DEFAULT_TASK_FILE_NAME)


def iter_all_marker_files(root_path: Path, recursive: bool = True):
    """
    Iterates through all located marker files within a path tree.

    Args:
        root_path(Path):
            Root of the path tree to walk through.

        recursive(bool):
            States whether the whole tree is searched or only the root path.

    Returns:
        Path:
            Path of a marker file.
    """
    if recursive:
        yield from root_path.rglob("*" + DEFAULT_TASK_FILE_NAME)
    else:
        yield from root_path.glob("*" + DEFAULT_TASK_FILE_NAME)


def filter_marker_files_by_states(
    marker_file_paths: Iterable[APath], requested_tasks: List[Task]
) -> Generator[Path, None, None]:
    """
    Filters marker files by comparing their content with the requested tasks.

    Args:
        marker_file_paths(Iterable[APath]):
            Path of marker files.

        requested_tasks(List[Task]):
            Task states which the filtered marker files should have.

    Yields:
        Path:
            Path of the marker files which have equal path states than the
            *requested states*.
    """
    for filepath_to_check in marker_file_paths:
        if state_of_tasks_are(
            marker_filepath=filepath_to_check, requested_tasks=requested_tasks
        ):
            yield filepath_to_check


def iter_marker_files_with_state(
    root_paths: List[Path], requested_task_states: List[Task], recursive: bool = True
) -> Generator[Path, None, None]:
    """
    Iterates through all marker files, which have equal task states than
    the requested task states.

    Args:
        root_paths:
        requested_task_states:
        recursive:

    Yields:
        Path:
            Paths of marker files, which have equal task states than
            the requested tasks.
    """
    for root_path_to_list in root_paths:
        marker_file_paths = iter_all_marker_files(
            root_path=root_path_to_list, recursive=recursive
        )
        yield from filter_marker_files_by_states(
            marker_file_paths=marker_file_paths, requested_tasks=requested_task_states
        )


def get_target_path_of_marker(marker_filepath: Path) -> Path:
    """
    Resolves the marked file or folder depending on the marker's filepath.

    Args:
        marker_filepath(Path):
            The file path of the marker file.

    Returns:
        File or folder path of the marked target.
    """
    cutting_right = len(DEFAULT_TASK_FILE_NAME)
    cutted_resolved = str(marker_filepath.resolve())[:-cutting_right]
    return Path(cutted_resolved)


def iter_target_paths_with_task_states(
    root_paths: List[Path], requested_task_states: Task, recursive: bool = True
) -> Generator[Path, None, None]:
    """
    Iterates through all marked file paths, which marked state (by marker files)
    are equal to the requested tasks.

    Args:
        root_paths(List[Path]):
            Root paths through which to walk.

        requested_task_states(List[Task]):
            Requested task states, which the marker files must have.

        recursive(bool):
            States whether the root paths should be walked through or the search
            just takes place within the root paths.

    Yields:
        Path:
            Paths of files, which marker files have equal task states than
            the requested tasks.
    """
    for marker_filepath in iter_marker_files_with_state(
        root_paths=root_paths,
        requested_task_states=requested_task_states,
        recursive=recursive,
    ):
        yield get_target_path_of_marker(marker_filepath=marker_filepath)


def iter_target_path_with_states():
    pass


def load_task_file(marker_filepath: APath) -> dict:
    assert marker_filepath is not None, "marker_filepath cannot be 'None'."
    task_file_path = propose_task_filepath(path_to_mark=marker_filepath)
    return load_yaml_file_content(filepath=task_file_path, default={})


def mark_tasks(paths_to_mark: List[APath], tasks_to_mark: Iterable[Task]):
    assert isinstance(paths_to_mark, list)
    paths_to_mark = set(paths_to_mark)
    for path_to_mark in paths_to_mark:
        mark_task(path_to_mark=path_to_mark, tasks_to_mark=tasks_to_mark)


def _task_states_to_dict(task_states: List[Task]) -> dict:
    requested_task_states = {}
    for task in task_states:
        assert isinstance(task, Task), "'task_state' needs to be a task."
        requested_task_states[task.name] = task.state
    return requested_task_states


def mark_task(path_to_mark: APath, tasks_to_mark: Iterable[Task]):
    """

    Args:
        path_to_mark(APath):
        tasks_to_mark(Iterable[Task]):
    """
    performed_task_states = _task_states_to_dict(tasks_to_mark)
    task_filepath = propose_task_filepath(path_to_mark=path_to_mark)
    update_yaml_file_content(filepath=task_filepath, new_content=performed_task_states)


def _state_of_task_is(marked_tasks: dict, requested_task: Task) -> bool:
    """
    Examples:
        >>> sample_tasks = {"task1": "done", "task2": "prep"}
        >>> _state_of_task_is(sample_tasks, Task("task1", "done"))
        True
        >>> _state_of_task_is(sample_tasks, Task("task1", "prep"))
        False
        >>> _state_of_task_is(sample_tasks, Task("task2", "done"))
        False
        >>> _state_of_task_is(sample_tasks, Task("task2", "prep"))
        True

    Args:
        marked_tasks(dict):
            The marked task states which are compared against the
            *requested task*.

        requested_task(Task):
            The targeted task state, which should be within *marked tasks*.

    Returns:
        bool:
            True if the *requested task*'s state is within the *marked tasks*.
    """
    task_was_not_marked = requested_task.name not in marked_tasks
    if task_was_not_marked:
        return False

    saved_task_is_different = requested_task.state != marked_tasks[requested_task.name]
    if saved_task_is_different:
        return False
    return True


def _state_of_tasks_are(marked_tasks: dict, requested_tasks: List[Task]) -> bool:
    """
    Examples:
        >>> sample_tasks = {"t1": "done", "t2": "prep"}
        >>> _state_of_tasks_are(sample_tasks, [Task("t1", "done")])
        True
        >>> _state_of_tasks_are(sample_tasks, [Task("t1", "prep")])
        False
        >>> _state_of_tasks_are(sample_tasks, [Task("t2", "done")])
        False
        >>> _state_of_tasks_are(sample_tasks, [Task("t2", "prep")])
        True
        >>> _state_of_tasks_are(sample_tasks, [Task("t1", "done"), Task("t2", "prep")])
        True
        >>> _state_of_tasks_are(sample_tasks, [Task("t1", "done"), Task("t2", "done")])
        False
        >>> _state_of_tasks_are(sample_tasks, [Task("t1", "prep"), Task("t2", "prep")])
        False

    Args:
        marked_tasks(dict):
            The marked task states which are compared against the
            *requested task*.

        requested_tasks(List[Task]):
            The targeted task's with state, which should be within *marked tasks*.

    Returns:
        bool:
            True if the *requested task*'s state is within the *marked tasks*.
    """
    for task_to_check in requested_tasks:
        marked_task_is_not_like_requested_all_fail = not _state_of_task_is(
            marked_tasks=marked_tasks, requested_task=task_to_check
        )
        if marked_task_is_not_like_requested_all_fail:
            return False
    return True


def state_of_tasks_are_for(target_path: APath, requested_tasks: List[Task]) -> bool:
    """
    Checks on base of the local task file, if the specified task was performed
    for the *target path*.

    Args:
        target_path(APath):
            The path of a folder or file, which local marker file should be
            looked up.

        requested_tasks(List[Task]):
            The state(s) which should be within the marker file.

    Returns:
        bool
    """
    assert target_path is not None, "folder_path cannot be 'None'."
    marker_filepath = propose_task_filepath(path_to_mark=target_path)
    return state_of_tasks_are(
        marker_filepath=marker_filepath, requested_tasks=requested_tasks
    )


def state_of_tasks_are(marker_filepath: APath, requested_tasks: List[Task]) -> bool:
    """
    Checks on base of the local task file, if the specified task was performed.

    Args:
        marker_filepath(APath):
            The path of the marker file.

        requested_tasks(List[Task]):
            The state(s) which should be within the marker file.

    Returns:
        bool
    """
    assert marker_filepath is not None, "folder_path cannot be 'None'."
    marked_tasks = load_task_file(marker_filepath=marker_filepath)

    return _state_of_tasks_are(
        marked_tasks=marked_tasks, requested_tasks=requested_tasks
    )


def _check_task_representations_and_exit_on_false(task_representations: List[str]):
    for representation in task_representations:
        if not Task.is_a_task_representation(task_representation=representation):
            sys.stderr.write(
                "'{}' is not a valid task representation." "\n".format(representation)
            )
            sys.exit(1)


@docopt_parsable
def command_list(args):
    """
    USAGE:
        marktask (l|list) [-dr] <state> [<work-paths>...]

    Lists existing measurement or calibration z3d-project files.

    OPTIONS:
        -r, --recursive      Toggles recursive behaviour.
        -d, --directory     This option will force the root folder path of file paths
                            within work-paths.
    ARGUMENTS:
        state       The state is a key-value-pair representation as 'key:value'.
                    Multiple states can be defined by delimiting states with commas
                    like 'name1:state1,name2:state2'

        root-path    Root path in which the calibration should be created, if found.
    """
    work_paths = _get_ingoing_paths(args["<work-paths>"])
    recursive = args["--recursive"]
    task_representations = _split_task_representations(args["<state>"])
    use_root_folders_of_files = args["--directory"]

    _check_task_representations_and_exit_on_false(task_representations)

    requested_tasks = [
        Task.parse(representation) for representation in task_representations
    ]

    if use_root_folders_of_files:
        lists_marker_file_generator = iter_target_paths_with_task_states(
            root_paths=work_paths,
            requested_task_states=requested_tasks,
            recursive=recursive,
        )
        return _yield_root_folder_of_file(lists_marker_file_generator)
    else:
        return iter_target_paths_with_task_states(
            root_paths=work_paths,
            requested_task_states=requested_tasks,
            recursive=recursive,
        )


@docopt_parsable
def command_mark(args):
    """
    USAGE:
        marktask (m|mark) [-d] <state> <work-paths>...

    Creates new measurement or calibration folders based on the image file names.
    The folders doesn't need to contain an ISISYS z3d-file.

    OPTIONS:
        -d, --directory     This option will force the root folder path of file paths
                            within work-paths.

    ARGUMENTS:
        state       The state is a key-value-pair representation as 'key:value'.
                    Multiple states can be defined by delimiting states with commas
                    like 'name1:state1,name2:state2'

        root-path   Root path in which the calibration should be created, if found.
    """
    work_paths = _get_ingoing_paths(args["<work-paths>"])
    task_representations_to_mark = _split_task_representations(args["<state>"])
    use_root_folders_of_files = args["--directory"]

    _check_task_representations_and_exit_on_false(task_representations_to_mark)

    if use_root_folders_of_files:
        work_paths = [_use_root_folder_of_file(path) for path in work_paths]

    tasks_to_mark = [
        Task.parse(representation) for representation in task_representations_to_mark
    ]

    mark_tasks(paths_to_mark=work_paths, tasks_to_mark=tasks_to_mark)


def main(args):
    """
    USAGE:
        marktask [-h|--help] [--version] <command> [<args>...]

    The most commonly use of marktask commands are:
        m, mark
        l, list

    See 'marktask help <command>' for more information on a specific command.

    """
    try:
        args = docopt(
            main.__doc__,
            argv=args,
            version="masktask version " + __version__,
            options_first=True,
        )
    except DocoptExit:
        exit(main.__doc__)

    mark_commands = ["m", "mark"]
    list_commands = ["l", "list"]

    argv = [args["<command>"]] + args["<args>"]
    command = args["<command>"]
    if command in mark_commands:
        optional_upload_generator = command_mark(argv)
    elif command in list_commands:
        optional_upload_generator = command_list(argv)
    else:
        exit("'{}' is not a marktask command. See 'marktask help'.".format(command))

    _print_paths(optional_upload_generator)


if __name__ == "__main__":
    import sys
    sys_argv_and_pipe_content = get_piped_command_line_arguments(sys.argv[1:])
    main(sys_argv_and_pipe_content)
