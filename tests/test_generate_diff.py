from os import path

from gendiff import generate_diff
from gendiff import format


def compare(filepath1, filepath2, expected_result_filepath,
            renderer=format.default):
    with open(path.abspath(expected_result_filepath), 'r') as f:
        expected_result = f.read()
        actual_result = generate_diff(
            path.abspath(filepath1),
            path.abspath(filepath2),
            renderer
        )
        assert actual_result == expected_result


def test_json_diff():
    compare(
        'tests/fixtures/json_1.json',
        'tests/fixtures/json_2.json',
        'tests/fixtures/diff_1'
    )


def test_yaml_diff():
    compare(
        'tests/fixtures/yaml_1.yml',
        'tests/fixtures/yaml_2.yml',
        'tests/fixtures/diff_1'
    )


def test_complex_json_diff():
    compare(
        'tests/fixtures/json_complex_1.json',
        'tests/fixtures/json_complex_2.json',
        'tests/fixtures/diff_2'
    )


def test_complex_yaml_diff():
    compare(
        'tests/fixtures/yaml_complex_1.yml',
        'tests/fixtures/yaml_complex_2.yml',
        'tests/fixtures/diff_2'
    )


def test_plain_formated_diff():
    compare(
        'tests/fixtures/yaml_complex_1.yml',
        'tests/fixtures/yaml_complex_2.yml',
        'tests/fixtures/diff_3',
        renderer=format.plain
    )


def test_json_formated_diff():
    compare(
        'tests/fixtures/yaml_complex_1.yml',
        'tests/fixtures/yaml_complex_2.yml',
        'tests/fixtures/diff_4',
        renderer=format.json
    )
