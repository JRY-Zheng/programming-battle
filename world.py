from entity import Entity
from system import System
from component import Component

class World:
    # define a variable outside instance function
    # so that the variable is singleton
    # something like static variable
    entities:list[Entity] = []
    components:list[Component] = []
    systems:list[System] = []