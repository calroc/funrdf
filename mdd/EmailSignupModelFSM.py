
# pma EmailSignupModel
# 4 states, 3 transitions, 4 accepting states, 1 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def Initialize(): pass
def Recv(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Inactive', 'pendingEmails': set([])}},
  1 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Running', 'pendingEmails': set([])}},
  2 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Running', 'pendingEmails': set(['VinniPuhh'])}},
  3 : {'EmailSignupModel': {'activeEmails': set(['VinniPuhh']), 'mode': 'Running', 'pendingEmails': set([])}},
}

# initial state, accepting states, frontier states, deadend states

initial = 0
accepting = [0, 1, 2, 3]
frontier = []
finished = [3]
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Initialize, (), None), 1),
  (1, (Recv, ('VinniPuhh', 'sign up'), 'pending'), 2),
  (2, (Recv, ('VinniPuhh', 'confirm'), 'activate'), 3),
)
