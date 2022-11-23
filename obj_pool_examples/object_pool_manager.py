from typing import List


class PoolManager():
    def __init__(self, pool):
        self.pool = pool

    def __enter__(self):
        self.obj = self.pool.acquire()
        return self.obj

    def __exit__(self, type, value, traceback):
        self.pool.release(self.obj)


class Reusable:
    def test(self):
        print(f"Using object {id(self)}")
