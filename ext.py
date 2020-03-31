import os

EXTENSION_MAP = {
    'py': 'python',
    'md': 'marldown',
    'markown': 'markdown',
}

path, ext = os.path.splitext('/path/to/main.py')


def find_extension(filepath):
    path, ext = os.path.splitext(filepath)
    return EXTENSION_MAP.get(ext.lstrip('.'), 'NONE')
