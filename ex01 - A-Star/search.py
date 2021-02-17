"""
Oria Segal
209338193
"""

import state
import frontier


def search(n):  # searches for the target state of the game
    s = state.create(n)  # creates a new random board
    print(s)
    f = frontier.create(s)  # returns a priority queue that contains s
    while not frontier.is_empty(f):  # while the queue isn't empty
        s = frontier.remove(f)  # getting the first state out of the queue
        if state.is_target(s):  # if this state is the target
            return s  # , numStates, maxStates  # returns the target, the number of states we've done do far
            # and the max. number of states that have been together at the same time
        ns = state.get_next(s)  # saving the sons of this state we're at
        for i in ns:  # running trough the sons to check them too
            frontier.insert(f, i)  # inserts the sons into the frontier- queue
    return 0  # when done


# question 2, 3 and 4

for i in range(10):
#   print(search(3))
#   print(search(4))
    print("")


