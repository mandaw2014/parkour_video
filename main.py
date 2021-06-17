from numpy import positive
from numpy.core.shape_base import block
from ursina import *
from block import *
from player import Player

app = Ursina()

normalJump = 0.3
normalSpeed = 2

player = Player("cube", (0, 10, 0), "box", controls = "wasd")
player.jump_height = normalJump
player.SPEED = normalSpeed

light = PointLight(parent = camera, position = (0, 10, -1.5))
light.color = color.white

AmbientLight(color = color.rgba(100, 100, 100, 0.1))

Sky()

startBlock = Entity(model = "cube", color = color.light_gray, collider = "box", scale = (10, 1, 10), texture = "white_cube")

block_1_1 = NormalBlock(position = (0, 1, 10))
block_1_2 = NormalBlock(position = (0, 2, 20))
block_1_3 = JumpBlock(position = (0, -20, 35))
block_1_4 = NormalBlock(position = (0, 0, 50))
block_1_5 = SpeedBlock(position = (0, 0, 61))

endBlock = Entity(model = "cube", color = color.light_gray, collider = "box", scale = (10, 1, 10), texture = "white_cube", position = (0, 0, 80))

def update():
    if player.y <= -50:
        player.position = (0, 10, 0)
        player.jump_height = normalJump
        player.SPEED = normalSpeed

    # Collision
    hit = raycast(player.position, player.down, distance = 2, ignore = [player, ])

    if hit.entity == block_1_3:
        player.jump_height = 1.5
    else:
        player.jump_height = normalJump

    if hit.entity == block_1_5:
        player.SPEED = 5

app.run()