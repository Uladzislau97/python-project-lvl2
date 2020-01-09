#!/usr/bin/env python3
import argparse
from gendiff import generate_diff
from os import path


def main():
    parser = argparse.ArgumentParser(
        description='Generate diff.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', dest='format', help='set format of output'
    )

    args = parser.parse_args()
    first_file_path = path.abspath(args.first_file)
    second_file_path = path.abspath(args.second_file)
    diff = generate_diff(first_file_path, second_file_path, args.format)
    print(diff)


if __name__ == '__main__':
    main()
