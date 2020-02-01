import json
import yaml


def yaml_loader(file_descriptor):
    return yaml.load(file_descriptor, Loader=yaml.Loader)


parse_by_ext = {
    '.json': json.load,
    '.yml': yaml_loader
}


def parse(file_descriptor, ext):
    try:
        return parse_by_ext[ext](file_descriptor)
    except KeyError:
        raise ValueError('File extension can be .json or .yml')
