# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python

from pupy._typing import Flint
from typing import Any, Iterator, List, Optional

def nbytes(num: Flint) -> str: ...
def filesize(filepath: str) -> str: ...
def nseconds(t1: float, t2: Optional[float]=...) -> str: ...
def term_table(strings: List[str], row_wise: bool=..., filler: str=...) -> Iterator[Any]: ...