from gendiff import node_types


INDENT_LENGTH = 4


def stringify(data, depth):
    if type(data) is bool:
        return str(data).lower()
    if not isinstance(data, dict):
        return str(data)
    indentation = ' ' * INDENT_LENGTH * depth
    keys_representation = []
    for key in data:
        value = stringify(data[key], depth + 1)
        keys_representation.append(f"{indentation}    {key}: {value}")
    content = '\n'.join(keys_representation)
    return f"{'{'}\n{content}\n{indentation}{'}'}"


def render_iter(diff_data, depth=0):
    indentation = ' ' * INDENT_LENGTH * depth
    nodes_representation = []
    for node in diff_data:
        node_type = node['type']
        if node_type == node_types.COMPLEX:
            children = render_iter(node['children'], depth + 1)
            node_data = ((' ', children),)
        elif node_type == node_types.REMOVED:
            value = stringify(node['value'], depth + 1)
            node_data = (('-', value),)
        elif node_type == node_types.ADDED:
            value = stringify(node['value'], depth + 1)
            node_data = (('+', value),)
        elif node_type == node_types.UNCHANGED:
            value = stringify(node['value'], depth + 1)
            node_data = ((' ', value),)
        elif node_type == node_types.UPDATED:
            old_value = stringify(node['old_value'], depth + 1)
            new_value = stringify(node['new_value'], depth + 1)
            node_data = (('-', old_value), ('+', new_value))

        for sign, val in node_data:
            nodes_representation.append(
                f"{indentation}  {sign} {node['key']}: {val}"
            )

    content = '\n'.join(nodes_representation)
    result = f"{'{'}\n{content}\n{indentation}{'}'}"
    return result


def format(diff_data):
    return render_iter(diff_data)
