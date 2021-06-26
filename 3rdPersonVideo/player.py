from ursina import *
import math

class ThirdPersonController(Entity):
    def __init__(self, model, position, collider, scale = (1, 1, 1), SPEED = 3,velocity = (0, 0, 0), jump_height = 1, gravity = 1, **kwargs):
        super().__init__(
            model = model,
            position = position,
            collider = collider,
            scale = scale
        )
        
        camera.parent = self
        camera.position = (0, 11, -15)
        camera.rotation = (30, 0, 0)
        self.velocity_x, self.velocity_y, self.velocity_z = velocity
        self.SPEED = SPEED
        self.jump_height = jump_height
        self.jump_count = 0
        self.gravity = gravity
        self.jump_height = 0.3
        self.slope = 40

        for key, value in kwargs.items():
            try:
                setattr(self, key, value)
            except:
                print(key,value)

    def update(self):
        y_movement = self.velocity_y

        direction = (0, 1, 0)
        if y_movement < 0:
            direction = (0, -1, 0)

        yRay = boxcast(origin = self.world_position, direction = direction, distance = self.scale_y / 2 + abs(y_movement), ignore = [self, ])
        if yRay.hit:
            self.velocity_y = 0
        else:
            self.velocity_y -= self.gravity * time.dt

        if y_movement != 0:
            direction = (0, 1, 0)
            if y_movement < 0:
                direction = (0, -1, 0)
                
            yRay = boxcast(origin = self.world_position, direction = direction,distance = self.scale_y / 2 + abs(y_movement), ignore = [self, ])

            move = True
            if yRay.hit:
                move = False
                self.jump_count = 0
                
            if move:
                self.y += y_movement

        SPEED = time.dt * self.SPEED

        z_movement = round((held_keys["w"] * SPEED + -held_keys["s"] * SPEED) * math.cos(math.radians(self.rotation_y)), 5) + round((held_keys["d"] * SPEED + -held_keys["a"] * SPEED) * math.cos(math.radians(self.rotation_y + 90)), 5)
        x_movement = round((held_keys["w"] * SPEED + -held_keys["s"] * SPEED) * math.sin(math.radians(self.rotation_y)), 5) + round((held_keys["d"] * SPEED + -held_keys["a"] * SPEED) * math.sin(math.radians(self.rotation_y + 90)), 5)
        
        if x_movement != 0:
            direction = (1, 0, 0)
            if x_movement < 0:
                direction = (-1, 0, 0)

            xRay = boxcast(origin = self.world_position, direction = direction, distance = self.scale_x / 2 + abs(x_movement), ignore = [self, ])

            move = True
            if xRay.hit:
                move = False
            if move:
                self.x += x_movement
            else:
                BottomXRay = raycast(origin = self.world_position + (self.scale_x / 2 * direction[0], -self.scale_y / 2, 0), direction = direction, distance = abs(x_movement), ignore = [self, ])
                
                if BottomXRay.hit:
                    TopXRay = raycast(origin = self.world_position + (self.scale_x / 2 * direction[0], -self.scale_y / 2 + 0.1, 0), distance = max(x_movement, self.scale_x), direction = direction, ignore = [self, ])
                    
                    if TopXRay.hit:
                        if TopXRay.distance - BottomXRay.distance + 0.00001 >= 0.1 / math.tan(math.radians(self.slope)):
                            self.x += x_movement
                            HeightRay = raycast(origin = self.world_position + (self.scale_x / 2 * direction[0], self.scale_y / 2, 0), direction = (0, -1, 0), distance = self.scale_y, ignore = [self, ])
                            if HeightRay.hit:
                                self.y += round(self.scale_y - HeightRay.distance + 0.000005, 5)
                    else:
                        self.x += x_movement
                        HeightRay = raycast(origin = self.world_position + (self.scale_x / 2 * direction[0], self.scale_y / 2, 0), direction = (0, -1, 0), distance = self.scale_y, ignore = [self, ])
                        if HeightRay.hit:
                            self.y += round(self.scale_y - HeightRay.distance + 0.000005, 5)

        if z_movement != 0:
            direction = (0, 0, 1)
            if z_movement < 0:
                direction = (0, 0, -1)
            zRay = boxcast(origin = self.world_position, direction = direction, distance = self.scale_z / 2 + abs(z_movement), ignore = [self, ])

            move = True
            if zRay.hit:
                move = False
            if move:
                self.z += z_movement
            else:
                BottomZRay = raycast(origin = self.world_position + (0, -self.scale_y / 2, self.scale_z / 2 * direction[2]), direction = direction, distance = abs(z_movement), ignore = [self, ])
                
                if BottomZRay.hit:
                    TopZRay = raycast(origin = self.world_position + (0, -self.scale_y / 2 + 0.1, self.scale_z / 2 * direction[2]), distance = max(z_movement, self.scale_z), direction = direction, ignore = [self, ])
                    
                    if TopZRay.hit:
                        if TopZRay.distance - BottomZRay.distance + 0.00001 >= 0.1 / math.tan(math.radians(self.slope)):
                            self.z += z_movement
                            HeightRay = raycast(origin = self.world_position + (0, self.scale_y / 2, self.scale_z / 2 * direction[2]), direction = (0, -1, 0), distance = self.scale_y, ignore = [self, ])
                            
                            if HeightRay.hit:
                                self.y += round(self.scale_y - HeightRay.distance + 0.000005, 5)
                    else:
                        self.z += z_movement
                        HeightRay = raycast(origin = self.world_position + (0, self.scale_y / 2, self.scale_z / 2 * direction[2]), direction = (0, -1, 0), distance = self.scale_y, ignore = [self, ])
                        
                        if HeightRay.hit :
                            self.y += round(self.scale_y - HeightRay.distance + 0.000005, 5)
        
        if mouse.right:
            self.rotation_x -= mouse.velocity[1] * 150
            self.rotation_y += mouse.velocity[0] * 150

    def input(self, key):
        if key == "space":
            if self.jump_count < self.jump_height:
                self.velocity_y = self.jump_height
                self.jump_count += 1
