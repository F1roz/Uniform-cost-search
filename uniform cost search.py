import math

adjList = {
    'A': (('B', 3), ('J', 4), ('G', 1)),
    'B': (('A', 3), ('D', 10)),
    'C': (('H', 3)),
    'D': (('B', 10), ('J', 3), ('H', 11)),
    'E': (('F', 2), ('G', 14), ('I', 1)),
    'F': (('G', 8), ('E', 2), ('I', 2), ('H', 4)),
    'G': (('A', 1), ('E', 14), ('F', 8), ('J', 6)),
    'H': (('D', 11), ('F', 4), ('I', 6), ('C', 3)),
    'I': (('E', 1), ('F', 2), ('H', 6)),
    'J': (('A', 4), ('G', 6), ('D', 3)),
}

start = 'A'
goal = 'C'
frontier = {'A': 0}
explored = {}
parent = {}
ans = []


def dequeue():
    minValue = math.inf
    minNode = ''
    for key in frontier.keys():
        if frontier[key] < minValue:
            minValue = frontier[key]
            minNode = key
    del frontier[minNode]
    return (minNode, minValue)


while True:
    if not frontier:
        break
    node, weight = dequeue()
    if node == goal:
        break
    explored[node] = weight
    for child in adjList[node]:
        cn, cw = child
        if cn in frontier.keys():
            if cw + weight < frontier[cn]:
                frontier[cn] = cw + weight
                parent[cn] = node

        if cn not in explored.keys():
            if cn not in frontier.keys():
                frontier[cn] = cw + weight
                parent[cn] = node

key = goal
while True:
    if key == start:
        break
    r = parent[key]
    key = r
    ans.append(r)

ans.reverse()
ans.append(goal)

print(ans)
