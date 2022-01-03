import sys
from datetime import datetime
from importlib import import_module


def parse(filename, parser=str, sep='\n', sample=0) -> tuple:
    """Split the input file into entries separated with 'sep' and apply
    'parse' to each"""
    text = open(filename).read()
    entries = mapt(parser, text.rstrip().split(sep))
    return entries


def mapt(fn, *args) -> tuple:
    """map(fn, *args) and return the results as a tuple."""
    return tuple(map(fn, *args))


def run(func, filename):
    return parse(filename, str)  # func(parse(filename, str))


def run_day(day):
    module = import_module(f"pyt.day{day:02}")

    for i in ('p1', 'p2'):
        if not hasattr(module, i):
            continue
        print(f"==== {i} ====")
        print(run(getattr(module, i), f"input/day{day:02}.txt"))


if __name__ == "__main__":
    day = int(sys.argv[1]) if len(sys.argv) >= 2 else datetime.now().day
    run_day(day)
