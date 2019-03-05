#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from typing import Any
from typing import Callable
from typing import Dict
from typing import Optional

def cash_it(funk: Callable): ...

class Jasm:
    file_path: str = ...
    def __init__(self, path: str) -> None: ...
    def __call__(self, funk: Callable): ...
    @staticmethod
    def read(fpath: str): ...
    @staticmethod
    def write(fpath: str, obj: Dict) -> None: ...

def cprof(funk: Callable): ...

class tictoc(object):
    runs: Any = ...
    def __init__(self, runs: int = ...) -> None: ...
    args: Any = ...
    def __call__(self, time_funk: Callable, printing: bool = ...): ...
    @staticmethod
    def ftime(t1: float, t2: Optional[float] = ...): ...
