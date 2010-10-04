import hashlib


class KeyNameCollisionError(ValueError):
    pass


def key_name_of(uri):
    return hashlib.md5(uri).hexdigest()


# Support for JSON encoding of data that includes Xerblin words.
from types import FunctionType
from django.utils.simplejson import JSONEncoder, dumps


class XerblinWordEncoder(JSONEncoder):
    def default(self, obj):
        if (
            isinstance(obj, FunctionType)
            and obj.__module__ in ('xerblin.library', 'xerblin.base')
            ):
            return dict(__xerblin_word__=obj.__name__)
        return JSONEncoder.default(self, obj)


jsonDumps = lambda obj: dumps(obj, cls=XerblinWordEncoder)
