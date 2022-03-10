vertex = ['a','b','c','d','e','f','i','g','h','k']
edge = {'a': ['c', 'd', 'e'], 'c': ['f'], 'b': [], 'd': ['f', 'i'], 'e': ['k', 'g'], 'f': ['b'], 'g': ['b', 'h'],
        'k': [], 'h': ['b'], 'i': ['b', 'g']}
# print(edge)

fringe = []
initial_state = 'a'
goal_state = 'b'


def expand_tree(current_state):
    fringe.extend(edge[current_state])


def tree_search():
    fringe.append(initial_state)
    while True:
        if len(fringe)==0:
            print('Goal not found')
            return
        print(fringe,end='')
        current_state = fringe.pop(0)
        print(' -> ', current_state)
        # print(fringe)
        if current_state==goal_state:
            print('Goal found: ', current_state)
            return
        expand_tree(current_state)


tree_search()
