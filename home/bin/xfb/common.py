import sys,os
from pathlib import Path
import subprocess
from typing import Iterable,List,NoReturn,Any,AnyStr,Dict,Set
import time
from dataclasses import dataclass,field
import enum
from functools import total_ordering
from copy import copy,deepcopy
# import argparse


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def get_pwd():
    path=Path(sys.argv[0]).resolve().parent
    return str(path)

def puts(content):
    print(content, end='')

def eputs(content):
    print(content, end='',file=sys.stderr)


def exe_cmd(args:Iterable,stdin=None,encoding='UTF-8',timeout_sec:float=None)->(int,AnyStr,AnyStr):
    p=subprocess.Popen(args,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE,encoding=encoding)
    stdout,stderr=p.communicate(input=stdin,timeout=timeout_sec)
    return p.returncode,stdout,stderr

def is_number(s:str)->bool:
    if s is None:
        return False
    try:
        float(s)
        return True
    except Exception:
        return False


if __name__ == '__main__':
    pass