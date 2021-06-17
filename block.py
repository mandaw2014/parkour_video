from ursina import *

# Normal block class
class NormalBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            collider = "box",
            scale = (3, 0.8, 3),
            color = "#AFFF3C",
            texture = "white_cube",
            position = position,
            rotation = rotation
        )

# Jump block class
class JumpBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            collider = "box",
            scale = (3, 0.8, 3),
            color = "#FF8B00",
            position = position,
            rotation = rotation,
            texture = "white_cube"
        )

# Speed block classs
class SpeedBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0)):
        super().__init__(
            model = "cube",
            collider = "box",
            scale = (3, 0.5, 8),
            color = "#53FFF5",
            position = position,
            rotation = rotation,
            texture = "white_cube"
        )