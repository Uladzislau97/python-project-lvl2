import json


parse_by_ext = {
    '.json': json.load
}


def parse(file_descriptor, ext):
    try:
        return parse_by_ext[ext](file_descriptor)
    except KeyError:
        raise ValueError('File extension can be .json, .yaml or .ini')
