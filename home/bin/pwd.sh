#!/usr/bin/env python3
import sys
from pathlib import Path


if __name__ == '__main__':
    path=Path(sys.argv[0]).resolve().parent
    print(path)
