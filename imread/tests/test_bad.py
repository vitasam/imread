from nose.tools import raises
from imread import imread
from . import file_path


BAD_FILES = [
    'bad-files/LSM/00r/00r01.lsm',
    'bad-files/LSM/00r/00r03.lsm',
    'bad-files/LSM/00r/00r02.lsm',
    'bad-files/LSM/00r/00r00.lsm',

    'bad-files/LSM/01r/01r00.lsm',
    'bad-files/LSM/01r/01r01.lsm',
    'bad-files/LSM/01r/01r02.lsm',

    'bad-files/LSM/02r/02r00.lsm',
    'bad-files/LSM/02r/02r01.lsm',
    'bad-files/LSM/02r/02r02.lsm',

    'bad-files/LSM/03w/03w01.lsm',
    'bad-files/LSM/03w/03w00.lsm',
    'bad-files/LSM/03w/03w02.lsm',
    'bad-files/LSM/03w/03w03.lsm',

    'bad-files/TIFF/00r00.tiff',
]
def test_read():
    @raises(RuntimeError)
    def read1(fname):
        imread(file_path(fname))
        assert False
    for fname in BAD_FILES:
        read1(fname)