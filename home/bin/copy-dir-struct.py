#!/usr/bin/env python3
import sys
from common import eprint,get_path
from pathlib import Path


def init():
    if len(sys.argv)-1!=2:
        eprint('Invalid number of arguments')
        sys.exit(1)
    sdir = Path(sys.argv[1])
    tdir = Path(sys.argv[2])
    if not sdir.is_dir():
        eprint(f'No such directory:{sdir}')
        sys.exit(2)
    if not tdir.is_dir():
        eprint(f'No such directory:{tdir}')
        sys.exit(2)

def copy_struct(sdir:str,tdir:str):
    try:
        t_path=Path(tdir)
        d=path.iterdir()
        for f in d:
            if f.is_dir():
                print_files(f,err,wildcard)
    except Exception as e:
        eprint(f'Error:{e} path:{path}')
        err=True


def test():
    test_dir=Path('.').resolve()
    test_dir
    print(get_path())

if __name__ == '__main__':
    test()
    # init()
    # main()