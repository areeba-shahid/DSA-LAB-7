import copy
from heapq import heappush, heappop

n = 3  # size of the puzzle (3x3)

row = [1, 0, -1, 0]  # movement in the row direction (up, down, left, right)
col = [0, 1, 0, -1]  # movement in the column direction (up, down, left, right)

class priorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, k):
        heappush(self.heap, k)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        return len(self.heap) == 0


class Node:
    def __init__(self, parent, mat, empty_tile_pos, cost, level):
        self.parent = parent
        self.mat = mat
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.level = level

    def __lt__(self, nxt):
        return self.cost < nxt.cost  # For comparing nodes in the priority queue


def calculateCost(mat, final):
    count = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0 and mat[i][j] != final[i][j]:
                count += 1
    return count


def newNode(mat, empty_tile_pos, new_empty_tile_pos, level, parent, final):
    new_mat = copy.deepcopy(mat)
    x1, y1 = empty_tile_pos
    x2, y2 = new_empty_tile_pos
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]  # Swap tiles
    cost = calculateCost(new_mat, final)
    return Node(parent, new_mat, new_empty_tile_pos, cost, level)


def printMatrix(mat):
    for i in range(n):
        for j in range(n):
            print(f"{mat[i][j]} ", end=" ")
        print()


def isSafe(x, y):
    return 0 <= x < n and 0 <= y < n


def printPath(root):
    if root is None:
        return
    printPath(root.parent)
    printMatrix(root.mat)
    print()


def solve(initial, empty_tile_pos, final):
    pq = priorityQueue()
    cost = calculateCost(initial, final)
    root = Node(None, initial, empty_tile_pos, cost, 0)
    pq.push(root)

    while not pq.empty():
        minimum = pq.pop()

        if minimum.cost == 0:  # If the cost is zero, the puzzle is solved
            printPath(minimum)
            return

        for i in range(4):  # For all possible moves (up, down, left, right)
            new_tile_pos = [minimum.empty_tile_pos[0] + row[i], minimum.empty_tile_pos[1] + col[i]]
            if isSafe(new_tile_pos[0], new_tile_pos[1]):
                child = newNode(minimum.mat, minimum.empty_tile_pos, new_tile_pos, minimum.level + 1, minimum, final)
                pq.push(child)


initial = [
    [1, 2, 3],
    [5, 6, 0],
    [7, 8, 4]
]

final = [
    [1, 2, 3],
    [5, 8, 6],
    [0, 7, 4]
]

empty_tile_pos = [1, 2]  # Position of the empty tile (represented by 0)

solve(initial, empty_tile_pos, final)
