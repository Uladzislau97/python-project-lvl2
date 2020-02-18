import json


def sorted_diff_data(data):
    result = []
    for node in sorted(data, key=lambda node: node['key']):
        if 'children' in node:
            result.append(
                {**node, 'children': sorted_diff_data(node['children'])}
            )
        else:
            result.append(node)
    return result


def format(data):
    return json.dumps(sorted_diff_data(data), indent=4)
