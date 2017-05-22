import json
import os
from os.path import join, exists
import inspect


def json_backend(d):
    if not exists(d):
        os.mkdir(d)

    def wrap(fn):
        mod_name = inspect.getmodule(fn).__name__
        fn_name = fn.__name__
        name = mod_name + "." + fn_name
        fpath = join(d, name)
        return JSONBackend(fpath)
    return wrap


class JSONBackend(object):
    """ a simple json-file-based backend for the memoize decorator.  writes to a
    temp file before atomically moving to the provided file, to prevent
    data corruption """

    def __init__(self, fpath):
        self._data = {}
        if exists(fpath):
            with open(fpath, "r") as h:
                self._data = json.load(h)

        self._fpath = fpath
        self._backup = self._fpath + ".tmp"

    def __setitem__(self, k, v):
        self._data[k] = v
        self._atomic_write()

    def __getitem__(self, k):
        return self._data[k]

    def __contains__(self, k):
        return k in self._data

    def _atomic_write(self):
        with open(self._backup, "w") as h:
            json.dump(self._data, h)

        # atomic move
        os.rename(self._backup, self._fpath)
