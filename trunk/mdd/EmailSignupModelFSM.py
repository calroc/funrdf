
# pma EmailSignupModel TwoEmail
# 15 states, 42 transitions, 15 accepting states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def Initialize(): pass
def Report(): pass
def Recv(): pass
def Err(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Inactive', 'pendingEmails': set([])}},
  1 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Running', 'pendingEmails': set([])}},
  2 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Running', 'pendingEmails': set(['OleBrumm'])}},
  3 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Error', 'pendingEmails': set([])}},
  4 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Running', 'pendingEmails': set(['VinniPuhh'])}},
  5 : {'EmailSignupModel': {'activeEmails': set(['OleBrumm']), 'mode': 'Running', 'pendingEmails': set([])}},
  6 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Error', 'pendingEmails': set(['OleBrumm'])}},
  7 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Running', 'pendingEmails': set(['OleBrumm', 'VinniPuhh'])}},
  8 : {'EmailSignupModel': {'activeEmails': set(['VinniPuhh']), 'mode': 'Running', 'pendingEmails': set([])}},
  9 : {'EmailSignupModel': {'activeEmails': set([]), 'mode': 'Error', 'pendingEmails': set(['VinniPuhh'])}},
  10 : {'EmailSignupModel': {'activeEmails': set(['OleBrumm']), 'mode': 'Error', 'pendingEmails': set([])}},
  11 : {'EmailSignupModel': {'activeEmails': set(['OleBrumm']), 'mode': 'Running', 'pendingEmails': set(['VinniPuhh'])}},
  12 : {'EmailSignupModel': {'activeEmails': set(['VinniPuhh']), 'mode': 'Running', 'pendingEmails': set(['OleBrumm'])}},
  13 : {'EmailSignupModel': {'activeEmails': set(['VinniPuhh']), 'mode': 'Error', 'pendingEmails': set([])}},
  14 : {'EmailSignupModel': {'activeEmails': set(['OleBrumm', 'VinniPuhh']), 'mode': 'Running', 'pendingEmails': set([])}},
}

# initial state, accepting states, frontier states, deadend states

initial = 0
accepting = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
frontier = []
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (Initialize, (), None), 1),
  (1, (Recv, ('OleBrumm', 'sign up'), 'pending'), 2),
  (1, (Err, ('VinniPuhh', 'confirm'), None), 3),
  (1, (Recv, ('VinniPuhh', 'sign up'), 'pending'), 4),
  (1, (Err, ('OleBrumm', 'confirm'), None), 3),
  (2, (Err, ('OleBrumm', 'sign up'), None), 3),
  (2, (Recv, ('OleBrumm', 'confirm'), 'activate'), 5),
  (2, (Err, ('VinniPuhh', 'confirm'), None), 6),
  (2, (Recv, ('VinniPuhh', 'sign up'), 'pending'), 7),
  (3, (Report, (), None), 0),
  (4, (Recv, ('OleBrumm', 'sign up'), 'pending'), 7),
  (4, (Err, ('VinniPuhh', 'sign up'), None), 3),
  (4, (Recv, ('VinniPuhh', 'confirm'), 'activate'), 8),
  (4, (Err, ('OleBrumm', 'confirm'), None), 9),
  (5, (Err, ('OleBrumm', 'sign up'), None), 3),
  (5, (Err, ('VinniPuhh', 'confirm'), None), 10),
  (5, (Recv, ('VinniPuhh', 'sign up'), 'pending'), 11),
  (5, (Err, ('OleBrumm', 'confirm'), None), 3),
  (6, (Report, (), None), 2),
  (7, (Err, ('OleBrumm', 'sign up'), None), 9),
  (7, (Recv, ('OleBrumm', 'confirm'), 'activate'), 11),
  (7, (Recv, ('VinniPuhh', 'confirm'), 'activate'), 12),
  (7, (Err, ('VinniPuhh', 'sign up'), None), 6),
  (8, (Recv, ('OleBrumm', 'sign up'), 'pending'), 12),
  (8, (Err, ('VinniPuhh', 'sign up'), None), 3),
  (8, (Err, ('VinniPuhh', 'confirm'), None), 3),
  (8, (Err, ('OleBrumm', 'confirm'), None), 13),
  (9, (Report, (), None), 4),
  (10, (Report, (), None), 5),
  (11, (Err, ('OleBrumm', 'sign up'), None), 9),
  (11, (Err, ('VinniPuhh', 'sign up'), None), 10),
  (11, (Recv, ('VinniPuhh', 'confirm'), 'activate'), 14),
  (11, (Err, ('OleBrumm', 'confirm'), None), 9),
  (12, (Err, ('OleBrumm', 'sign up'), None), 13),
  (12, (Recv, ('OleBrumm', 'confirm'), 'activate'), 14),
  (12, (Err, ('VinniPuhh', 'confirm'), None), 6),
  (12, (Err, ('VinniPuhh', 'sign up'), None), 6),
  (13, (Report, (), None), 8),
  (14, (Err, ('OleBrumm', 'sign up'), None), 13),
  (14, (Err, ('VinniPuhh', 'sign up'), None), 10),
  (14, (Err, ('VinniPuhh', 'confirm'), None), 10),
  (14, (Err, ('OleBrumm', 'confirm'), None), 13),
)
