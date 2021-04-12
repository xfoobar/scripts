#!/usr/bin/env python3
import sys
from common import eprint
from pathlib import Path



def init():
    if len(sys.argv)-1!=1:
        eprint('One path is required')
        sys.exit(1)
    tdir = Path(sys.argv[1])
    if not tdir.is_dir():
        eprint(f'No such directory:{tdir}')
        sys.exit(2)

def print_files(path:Path,err:bool):
    try:
        for f in path.iterdir():
            if f.is_dir():
                print_files(f,err)
            else:
                print(f)
    except Exception as e:
        eprint(f'Error:{e} path:{path}')
        err=True



if __name__ == '__main__':
    err=False
    tdir = Path(sys.argv[1])
    print_files(tdir,err)
    if err:
        sys.exit(3)