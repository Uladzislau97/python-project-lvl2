from gendiff import node_types


def build_diff_ast(first_data, second_data):
    first_keys = set(first_data.keys())
    second_keys = set(second_data.keys())
    removed_keys = first_keys - second_keys
    added_keys = second_keys - first_keys
    keys = first_keys | second_keys
    ast = []

    for key in keys:
        if key in removed_keys:
            value = first_data[key]
            node = {'type': node_types.REMOVED, 'key': key, 'value': value}
        elif key in added_keys:
            value = second_data[key]
            node = {'type': node_types.ADDED, 'key': key, 'value': value}
        else:
            first_value = first_data[key]
            second_value = second_data[key]

            if (
                isinstance(first_value, dict) and
                isinstance(second_value, dict)
            ):
                children = build_diff_ast(first_value, second_value)
                node = {
                    'type': node_types.COMPLEX,
                    'key': key,
                    'children': children
                }
            elif first_value == second_value:
                node = {
                    'type': node_types.UNCHANGED,
                    'key': key,
                    'value': first_value
                }
            else:
                node = {
                    'type': node_types.UPDATED,
                    'key': key,
                    'old_value': first_value,
                    'value': second_value
                }
        ast.append(node)
    return ast
