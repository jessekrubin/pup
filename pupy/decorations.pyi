# Stubs for pupy.decorations (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def cash_it(funk: Any): ...

class Jasm:
    file_path: Any = ...
    def __init__(self, path: Any) -> None: ...
    def __call__(self, funk: Any): ...
    @staticmethod
    def read(fpath: Any): ...
    @staticmethod
    def write(fpath: Any, obj: Any) -> None: ...

def cprof(funk: Any): ...

class tictoc:
    runs: Any = ...
    def __init__(self, runs: int = ...) -> None: ...
    def __str__(self, t_total: Any, funk: Any, args_string: Any): ...
    args: Any = ...
    def __call__(self, time_funk: Any, printing: bool = ...): ...
    @staticmethod
    def ftime(t1: Any, t2: Optional[Any] = ...): ...
