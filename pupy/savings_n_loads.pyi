# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python

from pupy._typing import JASM
from typing import Union

def safepath(path_str: str) -> str: ...
def lbytes(filepath: str) -> None: ...
def sstring(filepath: str, string: str) -> None: ...
def savings(filepath: str, string: str) -> None: ...
def sstr(filepath: str, string: str) -> None: ...
def lstring(filepath: str) -> str: ...
def lstr(filepath: str) -> str: ...
def sjson(filepath: str, data: JASM, minify: bool = ...) -> None: ...
def save_jasm(filepath: str, data: JASM, minify: bool = ...) -> None: ...
def sjasm(filepath: str, data: JASM, minify: bool = ...) -> None: ...
def ljson(filepath: str) -> JASM: ...
def load_jasm(filepath: str) -> JASM: ...
def ljasm(filepath: str) -> JASM: ...
def touch(filepath: str) -> None: ...
def shebang(filepath: str) -> Union[None, str]: ...
def stoml(filepath: str, data: JASM) -> None: ...
def ltoml(filepath: str) -> JASM: ...
def spak(filepath: str, data: JASM) -> None: ...
def lpak(filepath: str, raw: bool = ...) -> JASM: ...
def syaml(filepath: str, data: JASM) -> None: ...
def lyaml(filepath: str) -> JASM: ...
