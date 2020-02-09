from gendiff import node_types


def stringify(data):
    if type(data) is dict:
        return '[complex value]'
    if type(data) is str:
        return f"'{data}'"
    if type(data) is bool:
        return str(data).lower()
    return str(data)


def render_iter(data, parents=[]):
    nodes_representation = []
    for node in data:
        if node['type'] == node_types.COMPLEX:
            new_parents = parents + [node['key']]
            content = render_iter(node['children'], new_parents)
            nodes_representation.append(content)
        elif node['type'] == node_types.ADDED:
            name = '.'.join(parents + [node['key']])
            value = stringify(node['value'])
            content = f"Property '{name}' was added with value: {value}"
            nodes_representation.append(content)
        elif node['type'] == node_types.REMOVED:
            name = '.'.join(parents + [node['key']])
            content = f"Property '{name}' was removed"
            nodes_representation.append(content)
        elif node['type'] == node_types.UPDATED:
            name = '.'.join(parents + [node['key']])
            old_value = stringify(node['old_value'])
            new_value = stringify(node['new_value'])
            content = f"Property '{name}' was updated. " + \
                f"From {old_value} to {new_value}"
            nodes_representation.append(content)
    return '\n'.join(nodes_representation)


def render_plain_diff(diff_data):
    return render_iter(diff_data)
