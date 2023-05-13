import json
import yaml


def deserialize(path):
    with open(path, "r") as file:
        if path.endswith('.json'):
            return json.load(file)
        if path.endswith('.yml') or path.endswith('.yaml'):
            return yaml.safe_load(file)
