from __future__ import annotations

import libcst as cst
from collections.abc import Sequence
from argparse import ArgumentParser

from pyspark_formatter.window_formatter import PysparkWindowTransformer
from pyspark_formatter.join_formatter import JoinTransformer
from pyspark_formatter.unnecessary_col_formatter import UncessecaryColTransformer


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

    transformers = [
        PysparkWindowTransformer(),
        JoinTransformer(),
        UncessecaryColTransformer(),
    ]

    for filename in args.filenames:
        with open(filename) as f:
            file_content = f.read()
        
        try:
            module = cst.parse_module(file_content)
        except:
            print(f"Couldn't parse {filename}.")
            continue

        formatted_module = module
        for transformer in transformers:
            formatted_module = formatted_module.visit(transformer)

        if formatted_module.deep_equals(module):
            continue

        with open(filename, "w") as f:
            f.write(formatted_module.code)
        exit_code = 1

    return exit_code
