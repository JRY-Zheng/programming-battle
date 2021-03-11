import component

class PositionComponent(component.Component):
    def __init__(self) -> None:
        super().__init__()
        self.x = 0
        self.y = 0