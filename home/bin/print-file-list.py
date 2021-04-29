#!/usr/bin/env python3
import sys
from common import eprint
from pathlib import Path
import argparse



def args_init():
    parser = argparse.ArgumentParser(description='print file list')
    parser.add_argument('path', type=str,help='target directory')
    parser.add_argument('-f','--filter', type=str,required=False,help='file filter')
    args = parser.parse_args()
    return args

def print_files(path:Path,err:bool,file_filter:str=None):
    try:
        if file_filter:
            d=path.rglob(file_filter)
        else:
            d=path.iterdir()
        for f in d:
            if f.is_dir():
                print_files(f,err,file_filter)
            else:
                print(f)
    except Exception as e:
        eprint(f'Error:{e} path:{path}')
        err=True


def main():
    err=False
    args=args_init()
    tdir=Path(args.path)
    file_filter=args.filter
    print_files(tdir,err,file_filter)
    if err:
        sys.exit(1)

if __name__ == '__main__':
    main()