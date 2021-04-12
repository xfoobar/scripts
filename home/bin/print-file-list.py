#!/usr/bin/env python3
import sys
from common import eprint
from pathlib import Path



def init():
    if not len(sys.argv)-1 in (1,2):
        eprint('Invalid number of arguments')
        sys.exit(1)
    tdir = Path(sys.argv[1])
    if not tdir.is_dir():
        eprint(f'No such directory:{tdir}')
        sys.exit(2)

def print_files(path:Path,err:bool,wildcard:str=None):
    try:
        if wildcard:
            d=path.rglob(wildcard)
        else:
            d=path.iterdir()
        for f in d:
            if f.is_dir():
                print_files(f,err,wildcard)
            else:
                print(f)
    except Exception as e:
        eprint(f'Error:{e} path:{path}')
        err=True


def main():
    err=False
    tdir = Path(sys.argv[1])
    if len(sys.argv)-1==2:
        wc=sys.argv[2]
    else:
        wc=None
    print_files(tdir,err,wc)
    print(tdir,err,wc)
    if err:
        sys.exit(3)

if __name__ == '__main__':
    init()
    main()