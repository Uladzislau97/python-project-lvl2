import json

from gendiff.formatters.nested import render_nested_diff
from gendiff.formatters.plain import render_plain_diff


render_by_format = {
    'nested': render_nested_diff,
    'plain': render_plain_diff,
    'json': json.dumps
}


def render_diff(diff_data, format):
    try:
        if format is None:
            format = 'nested'
        return render_by_format[format](diff_data)
    except KeyError:
        raise ValueError('Diff format can be nested, plain or json')
