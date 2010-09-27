
# pma EmailSignupModel foo
# 4 states, 7 transitions, 4 accepting states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def Initialize(): pass
def Recv(): pass
def GET(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Inactive', 'pendingEmails': set([])}, 'foo': {}},
  1 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Running', 'pendingEmails': set([])}, 'foo': {}},
  2 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Running', 'pendingEmails': set(['VinniPuhh'])}, 'foo': {}},
  3 : {'EmailSignupModel': {'activeEmails': set(['VinniPuhh']), 'mode': 'Running', 'pendingEmails': set([])}, 'foo': {}},
}

# initial state, accepting states, frontier states, deadend states

initial = 0
accepting = [0, 1, 2, 3]
frontier = []
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Initialize, (), None), 1),
  (0, (GET, (), None), 0),
  (1, (GET, (), None), 1),
  (1, (Recv, ('VinniPuhh',), 'pending'), 2),
  (2, (Recv, ('VinniPuhh',), 'activate'), 3),
  (2, (GET, (), None), 2),
  (3, (GET, (), None), 3),
)
