import entity
from components.position_component import PositionComponent
from components.velocity_component import VelocityComponent

class SoldierEntity(entity.Entity):
    def __init__(self) -> None:
        super().__init__()
        position = PositionComponent()
        velocity = VelocityComponent()
        velocity.vx = 1.1
        velocity.vy = -0.5
        self.components = [position, velocity]
