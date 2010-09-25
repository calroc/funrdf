"""
PyModel model for an email signup process, based on the WebModel.py sample.
"""

### Model

INACTIVE = 'Inactive'
RUNNING = 'Running'

# State, with initial values

mode = INACTIVE  # can't call it 'state', that has special meaning
pendingEmails = []
activeEmails = []


# Actions and enabling conditions


def Initialize():
  global mode
  mode = RUNNING

def InitializeEnabled():
  return mode == INACTIVE


def Recv(address):
  global pendingEmails

  if address in pendingEmails:
    pendingEmails.remove(address)
    activeEmails.append(address)
    return 'activate'

  pendingEmails.append(address)
  return 'pending'

def RecvEnabled(address):
  return mode == RUNNING and address not in activeEmails


### Metadata

state = ('mode', 'pendingEmails', 'activeEmails')

actions = (Initialize, Recv)

enablers = {
  Initialize: (InitializeEnabled,),
  Recv: (RecvEnabled,),
  }

# cleanup = (Logout,)

# default domains

users = ['VinniPuhh']

domains = {
  Recv: {'address':users},
  }

# needed for multiple test runs in one session

def Reset():
  global mode, pendingEmails, activeEmails
  mode = INACTIVE
  del pendingEmails[:]
  del activeEmails[:]
