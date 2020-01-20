import os
from .parse import parse
from .builder import build_diff_ast
from .formatters import render_diff


def get_file_data(filepath):
    _, ext = os.path.splitext(filepath)
    with open(filepath, 'r') as f:
        return parse(f, ext)


def generate_diff(path_to_file1, path_to_file2, format=None):
    file1_data = get_file_data(path_to_file1)
    file2_data = get_file_data(path_to_file2)
    diff_data = build_diff_ast(file1_data, file2_data)
    return render_diff(diff_data, format)
