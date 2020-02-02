from os import path
from gendiff import generate_diff


def test_json_diff():
    with open(path.abspath('tests/fixtures/diff_1'), 'r') as f:
        expected_result = f.read()
        actual_result = generate_diff(
            path.abspath('tests/fixtures/json_1.json'),
            path.abspath('tests/fixtures/json_2.json')
        )
        assert actual_result == expected_result


def test_yaml_diff():
    with open(path.abspath('tests/fixtures/diff_1'), 'r') as f:
        expected_result = f.read()
        actual_result = generate_diff(
            path.abspath('tests/fixtures/yaml_1.yml'),
            path.abspath('tests/fixtures/yaml_2.yml')
        )
        assert actual_result == expected_result


def test_complex_json_diff():
    with open(path.abspath('tests/fixtures/diff_2'), 'r') as f:
        expected_result = f.read()
        actual_result = generate_diff(
            path.abspath('tests/fixtures/json_complex_1.json'),
            path.abspath('tests/fixtures/json_complex_2.json')
        )
        assert actual_result == expected_result


def test_complex_yaml_diff():
    with open(path.abspath('tests/fixtures/diff_2'), 'r') as f:
        expected_result = f.read()
        actual_result = generate_diff(
            path.abspath('tests/fixtures/yaml_complex_1.yml'),
            path.abspath('tests/fixtures/yaml_complex_2.yml')
        )
        assert actual_result == expected_result


def test_plain_formated_diff():
    with open(path.abspath('tests/fixtures/diff_3'), 'r') as f:
        expected_result = f.read()
        actual_result = generate_diff(
            path.abspath('tests/fixtures/yaml_complex_1.yml'),
            path.abspath('tests/fixtures/yaml_complex_2.yml'),
            'plain'
        )
        assert actual_result == expected_result


def test_json_formated_diff():
    with open(path.abspath('tests/fixtures/diff_4'), 'r') as f:
        expected_result = f.read()
        actual_result = generate_diff(
            path.abspath('tests/fixtures/yaml_complex_1.yml'),
            path.abspath('tests/fixtures/yaml_complex_2.yml'),
            'json'
        )
        assert actual_result == expected_result
