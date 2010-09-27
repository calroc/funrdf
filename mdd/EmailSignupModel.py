"""
PyModel model for an email signup process, based on the WebModel.py sample.
"""

### Model

INACTIVE = 'Inactive'
RUNNING = 'Running'
ERR = 'Error'

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
  global pendingEmails, activeEmails

  if address in pendingEmails:
    pendingEmails.remove(address)
    activeEmails.add(address)
    return 'activate'

  pendingEmails.add(address)
  return 'pending'

def RecvEnabled(address, body):
  return (
    mode == RUNNING
    and ((
      body == SIGNUP and
      address not in activeEmails and
      address not in pendingEmails
      )
    or (
      body == CONFIRM and
      address not in activeEmails and
      address in pendingEmails
      ))
    )

def Err(address, body):
  global pendingEmails, activeEmails, mode
  pendingEmails.discard(address)
  activeEmails.discard(address)
  mode = ERR

def ErrEnabled(address, body):
  return (
    mode == RUNNING
    and (
      ( body == SIGNUP and (
          address in pendingEmails or
          address in activeEmails
          )
        )
      or (
        body == CONFIRM and
        address not in pendingEmails
        )
      )
    )


def Report():
  global pendingEmails, activeEmails, mode
  if pendingEmails or activeEmails:
    mode = RUNNING
  else:
    mode = INACTIVE

def ReportEnabled():
  return mode == ERR





### Metadata

state = ('mode', 'pendingEmails', 'activeEmails')

actions = (Initialize, Recv, Err, Report)

enablers = {
  Initialize: (InitializeEnabled,),
  Recv: (RecvEnabled,),
  Err: (ErrEnabled,),
  Report: (ReportEnabled,),
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
  Err: {
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
