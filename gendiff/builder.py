def detect_key_type(key, first_data, second_data):
    if (key in first_data) and (key not in second_data):
        return 'removed'
    elif (key not in first_data) and (key in second_data):
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
        key_type = detect_key_type(key, first_data, second_data)
        if key_type == 'complex':
            children = build_diff_ast(first_data[key], second_data[key])
            node = {'type': key_type, 'key': key, 'children': children}
        if key_type == 'removed':
            value = first_data[key]
            node = {'type': key_type, 'key': key, 'value': value}
        elif key_type == 'added':
            value = second_data[key]
            node = {'type': key_type, 'key': key, 'value': value}
        elif key_type == 'unchanged':
            value = first_data[key]
            node = {'type': key_type, 'key': key, 'value': value}
        elif key_type == 'updated':
            old_value = first_data[key]
            new_value = second_data[key]
            node = {
                'type': key_type,
                'key': key,
                'old_value': old_value,
                'new_value': new_value
            }
        ast.append(node)
    return ast
