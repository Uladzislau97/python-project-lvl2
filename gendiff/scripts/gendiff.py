#!/usr/bin/env python3
from os import path

import argparse

from gendiff import generate_diff
from gendiff import format


def formatter(name):
    if name == format.JSON:
        return format.json
    elif name == format.PLAIN:
        return format.plain
    elif name == format.DEFAULT:
        return format.default
    raise argparse.ArgumentTypeError(
        'Unknown formatter: "{}". Use one of this: {}'.format(
            name,
            ', '.join(format.FORMATTERS),
        )
    )


def main():
    parser = argparse.ArgumentParser(
        description='Generate diff.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        type=formatter,
        default=format.DEFAULT
    )

    args = parser.parse_args()
    first_file_path = path.abspath(args.first_file)
    second_file_path = path.abspath(args.second_file)
    diff = generate_diff(first_file_path, second_file_path, args.format)
    print(diff)


if __name__ == '__main__':
    main()
