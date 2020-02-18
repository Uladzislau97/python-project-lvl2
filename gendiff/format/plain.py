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
        node_type = node['type']
        node_key = node['key']
        name = '.'.join(parents + [node_key])

        if node_type == node_types.COMPLEX:
            new_parents = parents + [node_key]
            content = render_iter(node['children'], new_parents)
        elif node_type == node_types.ADDED:
            value = stringify(node['value'])
            content = f"Property '{name}' was added with value: {value}"
        elif node_type == node_types.REMOVED:
            content = f"Property '{name}' was removed"
        elif node_type == node_types.UPDATED:
            old_value = stringify(node['old_value'])
            new_value = stringify(node['new_value'])
            content = f"Property '{name}' was updated. " + \
                f"From {old_value} to {new_value}"
        else:
            continue

        nodes_representation.append(content)

    return '\n'.join(nodes_representation)


def format(diff_data):
    return render_iter(diff_data)
