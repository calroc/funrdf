"""
PyModel model for an email signup process, based on the WebModel.py sample.
"""

### Model

INACTIVE = 'Inactive'
RUNNING = 'Running'

SIGNUP = 'sign up'
CONFIRM = 'confirm'


# State, with initial values

mode = INACTIVE  # can't call it 'state', that has special meaning
pendingEmails = set()
activeEmails = set()


# Actions and enabling conditions


def Initialize():
  global mode
  mode = RUNNING

def InitializeEnabled():
  return mode == INACTIVE


def Recv(address, body):
  global pendingEmails

  if address in pendingEmails:
    pendingEmails.remove(address)
    activeEmails.add(address)
    return 'activate'

  pendingEmails.add(address)
  return 'pending'

def RecvEnabled(address, body):
  return (
    mode == RUNNING
    and (
      body == SIGNUP and
      address not in activeEmails and
      address not in pendingEmails
      )
    or (
      body == CONFIRM and
      address not in activeEmails and
      address in pendingEmails
      )
    )


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
messages = [SIGNUP, CONFIRM]

domains = {
  Recv: {
    'address': users,
    'body': messages,
    },
  }

# needed for multiple test runs in one session

def Reset():
  global mode, pendingEmails, activeEmails
  mode = INACTIVE
  pendingEmails.clear()
  activeEmails.clear()
