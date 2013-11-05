VERSION = (0, 0, '1b')

def get_version():
    '.'.join([str(v) for v in VERSION])

__version__ = get_version()