import json
import re


def validate_input(mssg) -> bool:  # validate  user input (int | float)
    pattern = re.compile(r'^-?\d+(\.\d+)?$')
    if pattern.fullmatch(mssg):
        return True
    return False


class FileHandler:  # context manager's class
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename. self.mode)
        return self.file

    def __exit__(self, ext_type, exc_value, traceback):
        self.file.close()


def read_data(filename):  # for reading recorded data
    try:
        with FileHandler(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def write_data(filename, data):  # for recording updated data
    try:
        with FileHandler(filename, 'w') as f:
            return json.dump(data, f, indent=4)
    except FileNotFoundError:
        return {}
