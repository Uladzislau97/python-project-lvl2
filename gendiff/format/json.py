import json


def format(diff_data):
    return json.dumps(diff_data, indent=4)
