from poodle import Object, schedule
from typing import Set

# Define the Position class
class Position(Object):
    def __str__(self):
        if not hasattr(self, "locname"):
            return "unknown"
        return self.locname

# Define the HasHeight class
class HasHeight(Object):
    height: int

# Define the HasPosition class
class HasPosition(Object):
    at: Position

# Define the Monkey class
class Monkey(HasHeight, HasPosition):
    pass

# Define the PalmTree class
class PalmTree(HasHeight, HasPosition):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = 2

# Define the Box class
class Box(HasHeight, HasPosition):
    pass

# Define the Banana class
class Banana(HasHeight, HasPosition):
    owner: Monkey
    attached: PalmTree

# Define the World class
class World(Object):
    locations: Set[Position]

# Create positions in the world
p1 = Position()
p1.locname = "Position A"
p2 = Position()
p2.locname = "Position B"
p3 = Position()
p3.locname = "Position C"

# Initialize the world and add positions
w = World()
w.locations.add(p1)
w.locations.add(p2)
w.locations.add(p3)

# Create a monkey, box, and palm tree
m = Monkey()
m.height = 0  # ground
m.at = p1

box = Box()
box.height = 2
box.at = p2

p = PalmTree()
p.at = p3

b = Banana()
b.attached = p

# Define actions
def go(monkey: Monkey, where: Position):
    assert where in w.locations
    assert monkey.height < 1, "Monkey can only move while on the ground"
    monkey.at = where
    return f"Monkey moved to {where}"

def push(monkey: Monkey, box: Box, where: Position):
    assert monkey.at == box.at
    assert where in w.locations
    assert monkey.height < 1, "Monkey can only move the box while on the ground"
    monkey.at = where
    box.at = where
    return f"Monkey moved box to {where}"

def climb_up(monkey: Monkey, box: Box):
    assert monkey.at == box.at
    monkey.height += box.height
    return "Monkey climbs the box"

def grasp(monkey: Monkey, banana: Banana):
    assert monkey.height == banana.height
    assert monkey.at == banana.at
    banana.owner = monkey
    return "Monkey takes the banana"

def infer_owner_at(palmtree: PalmTree, banana: Banana):
    assert banana.attached == palmtree
    banana.at = palmtree.at
    return "Remembered that if banana is on palm tree, its location is where palm tree is"

def infer_banana_height(palmtree: PalmTree, banana: Banana):
    assert banana.attached == palmtree
    banana.height = palmtree.height
    return "Remembered that if banana is on the tree, its height equals tree's height"

# Execute the sequence using the schedule function
print('\n'.join(x() for x in schedule(
    [go, push, climb_up, grasp, infer_banana_height, infer_owner_at],
    [w, p1, p2, p3, m, box, p, b],
    goal=lambda: b.owner == m
)))
