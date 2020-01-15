import json


parse_by_ext = {
    '.json': json.load
}


def parse(content, ext):
    try:
        return parse_by_ext[ext](content)
    except KeyError:
        raise ValueError('File extension can be .json, .yaml or .ini')
