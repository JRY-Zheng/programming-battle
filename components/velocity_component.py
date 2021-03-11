import component

class VelocityComponent(component.Component):
    def __init__(self) -> None:
        super().__init__()
        self.vx = 0
        self.vy = 0
