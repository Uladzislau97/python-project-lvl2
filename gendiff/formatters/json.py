import json


def render_json_diff(diff_data):
    return json.dumps(diff_data, indent=4)
