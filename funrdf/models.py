import hashlib
from google.appengine.ext import db


class URIref(db.Model):
    value = db.StringProperty(required=True)


class Fact(db.Model):
    subject = db.ReferenceProperty(URIref, collection_name='subject_set')
    predicate = db.ReferenceProperty(URIref, collection_name='predicate_set')
    object_ = db.ReferenceProperty(URIref, collection_name='object_set')


def knowFact(subject, predicate, object_):
    fact = Fact()
    fact.subject = internURI(subject).key()
    fact.predicate = internURI(predicate).key()
    fact.object_ = internURI(object_).key()
    fact.put()


def internURI(uri):
    key_name = hashlib.md5(uri).hexdigest()
    URI = URIref.get_or_insert(key_name, value=uri)
    if URI.value != uri:
        raise ValueError('md5 sum collision: %s  <==> %s' % (
            URI.value, uri
            ))
    return URI
