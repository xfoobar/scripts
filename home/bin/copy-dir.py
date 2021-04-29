#!/usr/bin/env python3
import sys
from common import eprint
from pathlib import Path
import argparse
import pathlib


def args_init():
    parser = argparse.ArgumentParser(description='just copy directory')
    parser.add_argument('src_dir', type=str, help='source directory')
    parser.add_argument('des_dir', type=str, help='destination directory')
    parser.add_argument('-g', '--ignore', action='store_true',
                        help='ignore existing directories')
    args = parser.parse_args()
    return args


def copy_dir(src_dir: str, des_dir: str,ignore_exist:bool=False):
    src_path=Path(src_dir).resolve()
    des_path=Path(des_dir).resolve()
    for f in src_path.iterdir():
        if f.is_dir():
            new_dir=des_path.joinpath(f.name)
            new_dir.mkdir(exist_ok=ignore_exist)
            copy_dir(str(f),str(new_dir),ignore_exist)


def main():
    args = args_init()
    src_dir = Path(args.src_dir)
    des_dir = Path(args.des_dir)
    ignore_exist=args.ignore
    if not src_dir.is_dir():
        eprint(f'No such directory:{src_dir}')
        sys.exit(1)
    if not des_dir.is_dir():
        eprint(f'No such directory:{des_dir}')
        sys.exit(1)
    copy_dir(src_dir=src_dir,des_dir=des_dir,ignore_exist=ignore_exist)



if __name__ == '__main__':
    main()
