# -*- coding: utf-8 -*-
# Pretty ~ Useful ~ Python

from os import chdir
from os import getcwd
from typing import Any
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

class LIN:
    @staticmethod
    def rsync_args(
        src: Any,
        dest: Any,
        delete: bool = ...,
        mkdirs: bool = ...,
        exclude: Any = ...,
        include: Any = ...,
        dry_run: bool = ...,
    ): ...
    @staticmethod
    def rsync(
        src: Any,
        dest: Any,
        delete: bool = ...,
        exclude: Any = ...,
        include: Any = ...,
        dry_run: bool = ...,
    ): ...
    @staticmethod
    def link_dir(linkpath: Any, targetpath: Any) -> None: ...
    @staticmethod
    def link_dirs(link_target_tuples: Any) -> None: ...
    @staticmethod
    def link_file(linkpath: str, targetpath: str) -> None: ...
    @staticmethod
    def link_files(link_target_tuples: Any) -> None: ...
    @staticmethod
    def unlink_dir(link: Any) -> None: ...
    @staticmethod
    def unlink_dirs(links: Any) -> None: ...
    @staticmethod
    def unlink_file(link: Any) -> None: ...
    @staticmethod
    def unlink_files(links: Any) -> None: ...
    sync: Any = ...

class WIN:
    @staticmethod
    def robocopy_args(
        src: Any,
        dest: Any,
        delete: bool = ...,
        exclude_files: Any = ...,
        exclude_dirs: Any = ...,
        dry_run: bool = ...,
    ): ...
    @staticmethod
    def robocopy(
        src: Any,
        dest: Any,
        delete: bool = ...,
        exclude_files: Any = ...,
        exclude_dirs: Any = ...,
        dry_run: bool = ...,
    ): ...
    @staticmethod
    def link_dir(link: Any, target: Any) -> None: ...
    @staticmethod
    def link_dirs(link_target_tuples: Any): ...
    @staticmethod
    def link_file(link: Any, target: Any) -> None: ...
    @staticmethod
    def link_files(link_target_tuples: Any): ...
    @staticmethod
    def unlink_dir(link: Any) -> None: ...
    @staticmethod
    def unlink_dirs(links: Any) -> None: ...
    @staticmethod
    def unlink_file(link: Any) -> None: ...
    @staticmethod
    def unlink_files(links: Any) -> None: ...
    sync: Any = ...

class DirTree:
    path: Any = ...
    parent: Any = ...
    is_last: Any = ...
    depth: Any = ...
    def __init__(self, path: str, parent_path: str, is_last: bool) -> Any: ...
    @classmethod
    def make_tree(
        cls,
        root: Any,
        parent: Optional[Any] = ...,
        is_last: bool = ...,
        criteria: Optional[Any] = ...,
    ): ...
    @property
    def displayname(self): ...
    def displayable(self): ...

pwd = getcwd
cd = chdir

def tree(dirpath: Any, criteria: Optional[Any] = ...): ...
def mv(src: Any, dst: Any) -> None: ...
def cp(
    src: Any, dst: Any, r: bool = ..., symlinks: bool = ..., ignore: Optional[Any] = ...
) -> None: ...
def ls(dirpath: str = ..., abs: bool = ...) -> List[str]: ...
def ls_files(dirpath: str = ..., abs: bool = ...) -> List[str]: ...
def ls_dirs(dirpath: str = ..., abs: bool = ...) -> List[str]: ...
def ls_files_dirs(
    dirpath: str = ..., abs: bool = ...
) -> Tuple[List[str], List[str]]: ...
def rm(f_arg: Any, *args: Any) -> None: ...
def basename(path_str: str) -> str: ...
def dirname(fdpath: str) -> str: ...
def export(key: str, val: Union[None, str] = ...) -> None: ...

path2name = basename
parent_dirpath = dirname
link_dir: Any
link_dirs: Any
link_file: Any
link_files: Any
unlink_dir: Any
unlink_dirs: Any
unlink_file: Any
unlink_files: Any
sync: Any
echo = print
