def detect_node_type(key, first_data, second_data):
    first_keys = set(first_data.keys())
    second_keys = set(second_data.keys())

    if (key in first_keys) and (key not in second_keys):
        return 'removed'
    elif (key not in first_keys) and (key in second_keys):
        return 'added'
    elif (type(first_data[key]) is dict) and (type(second_data[key]) is dict):
        return 'complex'
    elif first_data[key] == second_data[key]:
        return 'unchanged'
    elif first_data[key] != second_data[key]:
        return 'updated'


def build_diff_ast(first_data, second_data):
    keys = []

    for key in first_data:
        if key not in keys:
            keys.append(key)

    for key in second_data:
        if key not in keys:
            keys.append(key)

    ast = []

    for key in keys:
        node_type = detect_node_type(key, first_data, second_data)
        if node_type == 'complex':
            children = build_diff_ast(first_data[key], second_data[key])
            node = {'type': node_type, 'key': key, 'children': children}
        if node_type == 'removed':
            value = first_data[key]
            node = {'type': node_type, 'key': key, 'value': value}
        elif node_type == 'added':
            value = second_data[key]
            node = {'type': node_type, 'key': key, 'value': value}
        elif node_type == 'unchanged':
            value = first_data[key]
            node = {'type': node_type, 'key': key, 'value': value}
        elif node_type == 'updated':
            old_value = first_data[key]
            new_value = second_data[key]
            node = {
                'type': node_type,
                'key': key,
                'old_value': old_value,
                'new_value': new_value
            }
        ast.append(node)
    return ast
