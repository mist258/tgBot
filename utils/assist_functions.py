import re


def validate_input(mssg) -> bool:  # validate  user input (int | float)
    pattern = re.compile(r'^-?\d+(\.\d+)?$')
    if pattern.fullmatch(mssg):
        return True
    return False


class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        pass

    def __exit__(self, ext_type, exc_value, traceback):
        self.file.close()

