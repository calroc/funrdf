from models import URIref, Fact

uKey = URIref.keyOfURI

s = uKey('http://umbel.org/umbel/ac/Action')
p = uKey('http://www.w3.org/2004/02/skos/core#narrowerTransitive')

results = Fact.query(s, p).fetch(5)

for f in results:
    print f.object_.value

##f = results[0]
##print f, f.key()
##print "%s" % f.subject.key().name(), f.predicate.value, f.object_.value












def treeSubset(triples, subject, predicate, res=None):
    '''
    Return a set of triples that are the tree from subject and linked by
    the predicate relation.
    '''
    if res is None:
        res = set()

    # Find all objects of the subject, predicate relation.
    more = set(
        (s, p, o)
        for s, p, o in triples
        if s == subject and p == predicate
        )

    for spo in more:
        if spo not in res:
            res.add(spo)
            treeSubset(triples, spo[2], predicate, res)

    return res


















def subsets(triples, subject, predicate, res=None, seen=None):
    '''
    Return a set of triples that are the tree from subject and linked by
    the predicate relation.
    '''
    if res is None: res = dict()
    if seen is None: seen = set()

    seen.add(subject)

    # Find all objects of the subject, predicate relation.
    more = set(
        o
        for s, p, o in triples
        if s == subject and p == predicate
        ) - seen

    d = res[subject] = int(bool(more)) or {}

    for o in more:
        if o not in res:
            subsets(triples, o, predicate, d, seen)

    return res






























from google.appengine.ext.db import Key
from models import URIref, Fact
uKey = URIref.keyOfURI

a = uKey('http://umbel.org/umbel/ac/Action')
n = uKey('http://www.w3.org/2004/02/skos/core#narrowerTransitive')

q = Fact.all().filter('subject =', a).filter('predicate =', n)
results = q.fetch(5)

f = results[0]
print f.subject.value, f.predicate.value, f.object_.value

































import hashlib
from google.appengine.api import users
from google.appengine.ext.db import Key
from util.homepage import html
from models import knowFact

key_name = hashlib.md5('http://umbel.org/umbel/ac/Action').hexdigest()
acti = URIref.get_by_key_name(key_name)

k = Key.from_path('URIref', key_name)
print k

print acti, acti.value

q = URIref.all() # keys_only=True)
q.filter('value =', 'http://umbel.org/umbel/ac/Action')
results = q.fetch(5)
action = results[0]

print action, action.value

print action == acti

q = Fact.all()
q.filter("subject =", k)
results = q.fetch(5)

f = results[0]
print f.subject.value, f.predicate.value, f.object_.value

























from models import (
    Fact,
    URIref,
    )

for obj in (
    'http://umbel.org/umbel/ac/Communicating',
    "http://umbel.org/umbel/ac/ControllingSomething",
    "http://umbel.org/umbel/ac/ControversialAction",
    "http://umbel.org/umbel/ac/CoordinatedBodyMovement",
    "http://umbel.org/umbel/ac/CreatingAnArtifact",
    ):
    Fact.know(
    'http://umbel.org/umbel/ac/Action',
    'http://www.w3.org/2004/02/skos/core#narrowerTransitive',
    obj,
    )

q = URIref.all()
q.filter('value =', 'http://umbel.org/umbel/ac/Action')
results = q.fetch(5)

print results


# Say hello to the current user
#user = users.get_current_user()
#if user:
#  nickname = user.nickname()
#else:
#  nickname = "guest"
#print "Hello, " + nickname

#print html[:30]

#print dir()

