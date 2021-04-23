import sys,os
from pathlib import Path
import subprocess
from typing import Iterable,List,NoReturn,Any,AnyStr,Dict
import time
from dataclasses import dataclass,field
import enum
from functools import total_ordering
from copy import copy,deepcopy


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

class ValueType(enum.Enum):
    string=enum.auto()
    number=enum.auto()
    empty=enum.auto()

@total_ordering
@dataclass(eq=False)
class Argument:
    name:str = field(compare=True)
    optional:bool = False
    repeatable:bool = False
    conflict:Iterable=None
    value_type:ValueType = ValueType.string
    value:str = None
    comment:str = None

    def __eq__(self,other):
        if type(other) is str:
            return self.name == other
        else:
            return self.name == other.name
    
    def __lt__(self,other):
        if type(other) is str:
            return self.name < other
        else:
            return self.name < other.name
    def __hash__(self):
        return self.name.__hash__()


def args_check(args:[str],define:[Argument])->Dict[str,List]:
    for d in define:
        props=(d.name,d.optional,d.repeatable,d.value_type)
        for p in props:
            if p is None:
                raise AttributeError(f'Some filed is empty:{d}')
    args=args[1:]
    length=len(args)
    params={}
    i=0
    while i<length:
        arg=args[i]
        if arg in define:
            df = define[define.index(arg)]
            if df not in params.keys():
                params[df.name]=[]
            value=None
            if df.value_type != ValueType.empty:
                i+=1
                if i<length:
                    value=args[i]
            p = copy(df)
            p.value=value
            params[df].append(p)
            i+=1
        else:
            raise ValueError(f'Invalid argument:{arg}')
        i+=1
    # optional check
    require_df=set([d.name for d in define if not d.optional])
    require=set([p for p in params.keys() if not params[])
    print(require_df)
    print(require)
    rq=require_df-require
    for r in rq:
        raise SyntaxError(f'Missing argument {r}')
    # repeatable check
    for df in define:
        if df.name in params.keys() and not df.repeatable and len(params[df.name])>1:
            raise SyntaxError(f'Argument {df} is not repeatable')
    # conflict check
    for c in params.keys():
        c= define[define.index(c)]
        if c.conflict:
            for p in params.keys():
                if p in c.conflict:
                    raise SyntaxError(f'{c} and {p} conflicted')
    # value check
    for k in params.keys():
        k= define[define.index(k)]
        if k.ValueType == ValueType.empty:
            for p in params[k.name]:
                value=p.value
                if value:
                    raise SyntaxError(f'Invalid value {k}:{value}')
        if k.value_type in  (ValueType.string,ValueType.number):
            for p in params[k.name]:
                value=p.value
                if not value:
                    raise SyntaxError(f'Invalid value {k}:')
                if k.value_type == ValueType.number and not value.isdigit():
                    raise SyntaxError(f'Invalid value {k}:{value}')
    return params



if __name__ == '__main__':
    
    define=[]
    define.append(
        Argument('--name',
        optional=False,
        repeatable=False,
        conflict=['--filename','--file'],
        value_type=ValueType.string,
        comment='Name')
    )
    define.append(
        Argument('--help',
        optional=True,
        repeatable=False,
        conflict=[],
        value_type=ValueType.empty,
        comment='Help')
    )
    define.append(
        Argument('--filename',
        optional=True,
        repeatable=False,
        conflict=['--name','--file'],
        value_type=ValueType.string,
        comment='FileName')
    )
    define.append(
        Argument('--file',
        optional=True,
        repeatable=False,
        conflict=['--name','--filename'],
        value_type=ValueType.string,
        comment='File')
    )
    define.append(
        Argument('--i',
        optional=True,
        repeatable=True,
        conflict=[],
        value_type=ValueType.number,
        comment='input')
    )
    args=['fo.py','--name','aa']
    r=args_check(args,define)
    print(r)
