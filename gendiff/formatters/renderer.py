INDENT_LENGTH = 4


def render_diff(diff_data, format):
    indentation = ' ' * INDENT_LENGTH
    nodes_representation = []
    for node in diff_data:
        if node['type'] == 'removed':
            nodes_representation.append(
                f"{indentation}  - {node['key']}: ${node['value']}"
            )
        elif node['type'] == 'added':
            nodes_representation.append(
                f"{indentation}  + {node['key']}: ${node['value']}"
            )
        elif node['type'] == 'unchanged':
            nodes_representation.append(
                f"{indentation}    {node['key']}: ${node['value']}"
            )
        elif node['type'] == 'updated':
            nodes_representation.append(
                f"{indentation}  - {node['key']}: ${node['old_value']}"
            )
            nodes_representation.append(
                f"{indentation}  + {node['key']}: ${node['new_value']}"
            )
    content = '\n'.join(nodes_representation)
    result = f"{'{'}\n{content}\n{'}'}"
    return result
