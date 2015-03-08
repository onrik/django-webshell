VERSION = (0, 0, '3b')

def get_version():
    return '.'.join([str(v) for v in VERSION])

__version__ = get_version()
