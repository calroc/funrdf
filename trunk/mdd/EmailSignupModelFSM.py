
# pma EmailSignupModel
# 5 states, 8 transitions, 5 accepting states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def Initialize(): pass
def Report(): pass
def Recv(): pass
def Err(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Inactive', 'pendingEmails': set([])}},
  1 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Running', 'pendingEmails': set([])}},
  2 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Error', 'pendingEmails': set([])}},
  3 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Running', 'pendingEmails': set(['VinniPuhh'])}},
  4 : {'EmailSignupModel': {'activeEmails': set(['VinniPuhh']), 'mode': 'Running', 'pendingEmails': set([])}},
}

# initial state, accepting states, frontier states, deadend states

initial = 0
accepting = [0, 1, 2, 3, 4]
frontier = []
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Initialize, (), None), 1),
  (1, (Err, ('VinniPuhh', 'confirm'), None), 2),
  (1, (Recv, ('VinniPuhh', 'sign up'), 'pending'), 3),
  (2, (Report, (), None), 0),
  (3, (Err, ('VinniPuhh', 'sign up'), None), 2),
  (3, (Recv, ('VinniPuhh', 'confirm'), 'activate'), 4),
  (4, (Err, ('VinniPuhh', 'sign up'), None), 2),
  (4, (Err, ('VinniPuhh', 'confirm'), None), 2),
)
