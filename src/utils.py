import json


def load_operation(filename):
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
        operations_list = json.loads(read_file)

    return operations_list
