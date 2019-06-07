# -*- coding: utf-8 -*-

from os import path
from os import sep

from pupy import dirs_gen
from pupy import files_gen
import pupy.utils

PWD = path.split(path.realpath(__file__))[0]

def test_mkdirs():
    dirs = [('something',), ('something', 'else')]
    expected = [path.join(*route) for route in dirs]
    with pupy.utils.linked_tmp_dir(mkdirs=dirs) as tmpdir:
        dirs = sorted(dirpath for dirpath in (tmp_subdir.replace(tmpdir, '').strip(sep) for tmp_subdir in dirs_gen(
            tmpdir)) if dirpath != '')
        assert set(dirs) == set(expected)
    assert all(not path.exists(d) for d in dirs)

def test_linkin():
    tdata = [['dummy_dir', 'a_file.txt'],
             ['dummy_dir', 'b_file.txt'],
             ['dummy_dir', 'a_dir', 'c_file.txt'],
             ['dummy_dir', 'a_dir', 'a_a_dir', 'd_file.txt'],
             ['dummy_dir', 'b_dir', 'e_file.txt'],
             ['dummy_dir', 'b_dir', 'f_file.txt']]
    lnfiles = [(path.join(*route), path.join(PWD, *route)) for route in tdata]
    with pupy.utils.linked_tmp_dir(prefix='D:\\pupy', lnfiles=lnfiles) as tmpdir:
        linkedfiles = sorted(dirpath for dirpath in (tmp_subdir.replace(tmpdir, '').strip(sep)
                                                     for tmp_subdir in files_gen(tmpdir)) if dirpath != '')
    lnfiles_links = [link for link, target in lnfiles]
    assert set(lnfiles_links) == set(linkedfiles)

if __name__ == "__main__":
    pass