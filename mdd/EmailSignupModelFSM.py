
# pma EmailSignupModel
# 12 states, 15 transitions, 12 accepting states, 2 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def Initialize(): pass
def Recv(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'EmailSignupModel': {'activeEmails': [], 'mode': 'Inactive', 'pendingEmails': []}},
  1 : {'EmailSignupModel': {'activeEmails': [], 'mode': 'Running', 'pendingEmails': []}},
  2 : {'EmailSignupModel': {'activeEmails': [], 'mode': 'Running', 'pendingEmails': ['OleBrumm']}},
  3 : {'EmailSignupModel': {'activeEmails': [], 'mode': 'Running', 'pendingEmails': ['VinniPuhh']}},
  4 : {'EmailSignupModel': {'activeEmails': ['OleBrumm'], 'mode': 'Running', 'pendingEmails': []}},
  5 : {'EmailSignupModel': {'activeEmails': [], 'mode': 'Running', 'pendingEmails': ['OleBrumm', 'VinniPuhh']}},
  6 : {'EmailSignupModel': {'activeEmails': ['VinniPuhh'], 'mode': 'Running', 'pendingEmails': []}},
  7 : {'EmailSignupModel': {'activeEmails': [], 'mode': 'Running', 'pendingEmails': ['VinniPuhh', 'OleBrumm']}},
  8 : {'EmailSignupModel': {'activeEmails': ['OleBrumm'], 'mode': 'Running', 'pendingEmails': ['VinniPuhh']}},
  9 : {'EmailSignupModel': {'activeEmails': ['VinniPuhh'], 'mode': 'Running', 'pendingEmails': ['OleBrumm']}},
  10 : {'EmailSignupModel': {'activeEmails': ['OleBrumm', 'VinniPuhh'], 'mode': 'Running', 'pendingEmails': []}},
  11 : {'EmailSignupModel': {'activeEmails': ['VinniPuhh', 'OleBrumm'], 'mode': 'Running', 'pendingEmails': []}},
}

# initial state, accepting states, frontier states, deadend states

initial = 0
accepting = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
frontier = []
finished = [10, 11]
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Initialize, (), None), 1),
  (1, (Recv, ('OleBrumm',), 'pending'), 2),
  (1, (Recv, ('VinniPuhh',), 'pending'), 3),
  (2, (Recv, ('OleBrumm',), 'activate'), 4),
  (2, (Recv, ('VinniPuhh',), 'pending'), 5),
  (3, (Recv, ('VinniPuhh',), 'activate'), 6),
  (3, (Recv, ('OleBrumm',), 'pending'), 7),
  (4, (Recv, ('VinniPuhh',), 'pending'), 8),
  (5, (Recv, ('OleBrumm',), 'activate'), 8),
  (5, (Recv, ('VinniPuhh',), 'activate'), 9),
  (6, (Recv, ('OleBrumm',), 'pending'), 9),
  (7, (Recv, ('OleBrumm',), 'activate'), 8),
  (7, (Recv, ('VinniPuhh',), 'activate'), 9),
  (8, (Recv, ('VinniPuhh',), 'activate'), 10),
  (9, (Recv, ('OleBrumm',), 'activate'), 11),
)
