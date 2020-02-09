import os

from gendiff.parsers import parse
from gendiff.builder import build_diff_ast


def get_file_data(filepath):
    _, ext = os.path.splitext(filepath)
    with open(filepath, 'r') as f:
        return parse(f, ext)


def generate_diff(path_to_file1, path_to_file2, render):
    file1_data = get_file_data(path_to_file1)
    file2_data = get_file_data(path_to_file2)
    diff_data = build_diff_ast(file1_data, file2_data)
    return render(diff_data)
