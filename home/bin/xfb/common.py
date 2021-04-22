import sys
from pathlib import Path

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def get_pwd():
    path=Path(sys.argv[0]).resolve().parent
    return str(path)

