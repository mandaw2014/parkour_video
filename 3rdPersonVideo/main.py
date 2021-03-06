from ursina import *
from block import *
from player import ThirdPersonController

app = Ursina()

normalJump = 0.5
normalSpeed = 6

player = ThirdPersonController("cube", (0, 10, 0), "box", color = color.orange)
player.jump_height = normalJump
player.SPEED = normalSpeed

light = PointLight(parent = camera, color = color.white, position = (0, 10, -1.5))
AmbientLight(color = color.rgba(100, 100, 100, 0.1))

startBlock = Entity(model = "cube", scale = (10, 1, 10), collider = "box", texture = "white_cube", color = "#CACACA")

block_1_1 = NormalBlock(position = (0, 1, 10))
block_1_2 = NormalBlock(position = (0, 2, 17))
block_1_3 = JumpBlock(position = (0, -20, 25))
block_1_4 = NormalBlock(position = (0, 0, 32))
block_1_5 = SpeedBlock(position = (0, 0, 42))

endBlock = Entity(model = "cube", scale = (10, 1, 10), collider = "box", texture = "white_cube", color = "#CACACA", position = (0, 0, 55))

Sky()

def update():
    if player.y <= -50:
        player.position = (0, 10, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump

    if held_keys["g"]:
        player.position = (0, 10, 0)

    hit = raycast(player.position, player.down, distance = 2, ignore = [player, ])

    if hit.entity == block_1_3:
        player.jump_height = 1
    else:
        player.jump_height = normalJump

    if hit.entity == block_1_5:
        player.SPEED = 15

app.run()