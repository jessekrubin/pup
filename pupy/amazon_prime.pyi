#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Jesse K. Rubin ~ Pretty Useful Python
from collections import MutableSequence
from typing import Any, List

def prime_gen(plim: int = ..., kprimes: List[int] = ...): ...
def prime_factorization_gen(n: int) -> None: ...
def prime_factors_gen(n: int): ...
def is_prime(number: int): ...

class OctopusPrime(MutableSequence):
    max_loaded: int = ...
    def __init__(self, plim: int = ...) -> None: 
        self._list = None
        ...
    def __len__(self) -> int: ...
    def __delitem__(self, key) -> None: ...
    def __getitem__(self, key) -> Any: ...
    def __setitem__(self, key): ...
    def _transform(self, n: int = ...) -> None: ...
    def primes_below(self, upper_bound: int): ...
    def primes_between(self, lower_bound: int, upper_bound: int): ...
    def insert(self, key): ...

