"""
PyModel model for an email signup process, based on the WebModel.py sample.
"""

# Actions and enabling conditions


def GET():
  pass

def GETEnabled():
  return True


### Metadata

state = ()

actions = (GET,)

enablers = {
  GET: (GETEnabled,),
  }

