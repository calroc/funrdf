import hashlib


class KeyNameCollisionError(ValueError):
    pass


def key_name_of(uri):
    return hashlib.md5(uri).hexdigest()
