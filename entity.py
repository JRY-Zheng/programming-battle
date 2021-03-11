from component import Component

class Entity:
    def __init__(self) -> None:
        self.components:list[Component] = []

    def get_component(self, type:type) -> Component:
        for component in self.components:
            if isinstance(component, type):
                return component
        return None