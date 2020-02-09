#!/usr/bin/env python3
from os import path

import argparse
import json

from gendiff import generate_diff
from gendiff.formatters.nested import render_nested_diff
from gendiff.formatters.plain import render_plain_diff


render_by_format = {
    'nested': render_nested_diff,
    'plain': render_plain_diff,
    'json': json.dumps
}


def renderer(format):
    try:
        if format is None:
            format = 'nested'
        return render_by_format[format]
    except KeyError:
        raise ValueError('Diff format can be nested, plain or json')


def main():
    parser = argparse.ArgumentParser(
        description='Generate diff.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', dest='format',
        help='set format of output', type=renderer
    )

    args = parser.parse_args()
    first_file_path = path.abspath(args.first_file)
    second_file_path = path.abspath(args.second_file)
    diff = generate_diff(first_file_path, second_file_path, renderer)
    print(diff)


if __name__ == '__main__':
    main()
