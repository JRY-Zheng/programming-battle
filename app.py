import numpy as np
from world import World
from entities.soldier_entity import SoldierEntity
from systems.update_position_system import UpdatePositionSystem

class Application:
    def run(self):
        soldier:SoldierEntity = SoldierEntity()
        World.entities.append(soldier)
        World.components.extend(soldier.components)
        World.systems.append(UpdatePositionSystem())
        for t in np.arange(0, 10, 0.01):
            for system in World.systems:
                system.tick(0.01)
            
            # hack code:
            print(f'soldier is at pos: {soldier.components[0].x}, {soldier.components[0].y}')



app = Application()
app.run()