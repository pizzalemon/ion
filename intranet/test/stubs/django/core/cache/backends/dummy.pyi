# Stubs for django.core.cache.backends.dummy (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.cache.backends.base import BaseCache

class DummyCache(BaseCache):
    def __init__(self, host, *args, **kwargs): ...
    def add(self, key, value, timeout=..., version=None): ...
    def get(self, key, default=None, version=None): ...
    def set(self, key, value, timeout=..., version=None): ...
    def delete(self, key, version=None): ...
    def get_many(self, keys, version=None): ...
    def has_key(self, key, version=None): ...
    def set_many(self, data, timeout=..., version=None): ...
    def delete_many(self, keys, version=None): ...
    def clear(self): ...
