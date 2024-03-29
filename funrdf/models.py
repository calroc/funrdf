import pickle, uuid
from google.appengine.ext import db
from util import key_name_of, KeyNameCollisionError


class StateStorage(db.Model):
    data = db.BlobProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    whose = db.UserProperty()

    @classmethod
    def fetch(class_, user, uuid):
        key_name = class_._makeKey(user, uuid)
        key = db.Key.from_path(class_.__name__, key_name)
        state = db.get(key)
        if state:
            return pickle.loads(state.data.decode('zlib'))

    @classmethod
    def store(class_, user, state):
        u = uuid.uuid4().hex
        key_name = class_._makeKey(user, u)
        state = pickle.dumps(state).encode('zlib')
        stored_state = class_.get_or_insert(
            key_name,
            data=state,
            whose=user,
            )
        if stored_state.data != state:
            raise KeyNameCollisionError(
                'key_name collision for: %s'
                % (key_name,)
                )
        return u

    @classmethod
    def _makeKey(class_, user, uuid):
        user_id = user.user_id()
        return user_id + uuid


class URIref(db.Model):
    value = db.StringProperty(required=True)

    @classmethod
    def internURI(class_, uri):
        '''
        Return the URIref object for the given URI (prevents duplicate
        URIs from being stored in the datastore.)
        '''
        URI = class_.get_or_insert(key_name_of(uri), value=uri)
        if URI.value != uri:
            raise KeyNameCollisionError(
                'md5 sum collision: %s  <==> %s' %
                (URI.value, uri)
                )
        return URI

    @classmethod
    def keyOfURI(class_, uri):
        '''
        Return the computed Key object for an URI without checking the
        datastore for the existance of that URI in the URIrefs.
        '''
        return db.Key.from_path('URIref', key_name_of(uri))


class Fact(db.Model):
    subject = db.ReferenceProperty(URIref, collection_name='subject_set')
    predicate = db.ReferenceProperty(URIref, collection_name='predicate_set')
    object_ = db.ReferenceProperty(URIref, collection_name='object_set')

    @classmethod
    def know(class_, subject, predicate, object_):
        s = URIref.internURI(subject).key()
        p = URIref.internURI(predicate).key()
        o = URIref.internURI(object_).key()
        key_name = key_name_of(''.join(k.name() for k in (s, p, o)))
        class_.get_or_insert(key_name, subject=s, predicate=p, object_=o)

    @classmethod
    def query(class_, subject=None, predicate=None, object_=None):
        q = class_.all()
        if subject is not None:
            q = q.filter('subject =', subject)
        if predicate is not None:
            q = q.filter('predicate =', predicate)
        if object_ is not None:
            q = q.filter('object_ =', object_)
        return q

