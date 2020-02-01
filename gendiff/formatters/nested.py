INDENT_LENGTH = 4


def stringify(data, depth):
    if type(data) is bool:
        return str(data).lower()
    if type(data) is not dict:
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
        if node['type'] == 'complex':
            children = render_iter(node['children'], depth + 1)
            nodes_representation.append(
                f"{indentation}    {node['key']}: {children}"
            )
        if node['type'] == 'removed':
            value = stringify(node['value'], depth + 1)
            nodes_representation.append(
                f"{indentation}  - {node['key']}: {value}"
            )
        elif node['type'] == 'added':
            value = stringify(node['value'], depth + 1)
            nodes_representation.append(
                f"{indentation}  + {node['key']}: {value}"
            )
        elif node['type'] == 'unchanged':
            value = stringify(node['value'], depth + 1)
            nodes_representation.append(
                f"{indentation}    {node['key']}: {value}"
            )
        elif node['type'] == 'updated':
            old_value = stringify(node['old_value'], depth + 1)
            nodes_representation.append(
                f"{indentation}  - {node['key']}: {old_value}"
            )
            new_value = stringify(node['new_value'], depth + 1)
            nodes_representation.append(
                f"{indentation}  + {node['key']}: {new_value}"
            )
    content = '\n'.join(nodes_representation)
    result = f"{'{'}\n{content}\n{indentation}{'}'}"
    return result


def render_nested_diff(diff_data):
    return render_iter(diff_data)
