import system
from world import World
from components.position_component import PositionComponent
from components.velocity_component import VelocityComponent

class UpdatePositionSystem(system.System):
    def tick(self, delta_time:float):
        for entity in World.entities:
            position_component:PositionComponent = entity.get_component(PositionComponent)
            velocity_component:VelocityComponent =  entity.get_component(VelocityComponent)
            if (position_component is not None and velocity_component is not None):
                position_component.x += delta_time*velocity_component.vx
                position_component.y += delta_time*velocity_component.vy