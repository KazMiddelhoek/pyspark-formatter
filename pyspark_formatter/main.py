import libcst as cst
from collections.abc import Sequence
from argparse import ArgumentParser

from pyspark_formatter.window_formatter import PysparkWindowTransformer


def run(argv: Sequence[str] | None = None) -> int:
    """Runs the pyspark-formatter.

    Args:
        argv: the CLI-arguments this function is called with. Contain the argument 'filenames',
            a list of all filenames to check.

    Returns:
        0 if all no files are reformatted, otherwise 1.
    """

    parser = ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args(argv)

    exit_code = 0

    for filename in args.filenames:
        with open(filename) as f:
            module = cst.parse_module(f.read())

        formatted_module =module.visit(PysparkWindowTransformer())

        if formatted_module.deep_equals(module):
            continue
        
        with open(filename, "w") as f:
            f.write(formatted_module.code)
        exit_code = 1

    return exit_code
