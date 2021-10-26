from entity import Entity
import pygame, globals

class Player(Entity):
    def __init__(self, pos=(0, 0), imagePath="", sprite_width=32, sprite_height=32, sprite_scale=1):
        Entity.__init__(self, pos, imagePath, sprite_width, sprite_height, sprite_scale)
        self.move_speed = 300
        self.jump_speed = -1000
        self.is_on_light = True
        pygame.mouse.set_pos(pos[0]+(sprite_width/2)*sprite_scale, pos[1]+(sprite_height/2)*sprite_scale)

    def init(self):
        self.spriteSheet.add_animation("idle", [0, 1, 2, 3, 4, 5], 80)
        self.spriteSheet.add_animation("walk", [6, 7, 8, 9], 60)
        self.spriteSheet.add_animation("jump", [10, 11], 100, True)
        self.spriteSheet.add_animation("falling", [8], 80, True)

    def update(self, delta):
        self.motion.x = (globals.pressed_keys[pygame.K_d] - globals.pressed_keys[pygame.K_a])
        self.true_pos[0] = int(self.motion.x * self.move_speed * (delta))
        
        if self.is_on_floor:
            if globals.pressed_keys[pygame.K_SPACE]:
                self.jump(delta)

        Entity.update(self, delta)
        if not self.is_on_floor:
                if self.motion.y > 1:
                    self.image = self.spriteSheet.play("falling")
                else:
                    self.image = self.spriteSheet.play("jump")
        else:
            if self.motion.x != 0:
                self.image = self.spriteSheet.play("walk")
                if self.motion.x < 0:
                    self.spriteSheet.flip_h = True
                elif self.motion.x > 0:
                    self.spriteSheet.flip_h = False
            else:
                self.image = self.spriteSheet.play("idle")

        if not self.is_on_light:
            print("Is not on circle")

    def draw(self):
        globals.screen.blit(pygame.transform.flip(self.image, self.spriteSheet.flip_h, self.spriteSheet.flip_v), self.rect)

    def jump(self, delta):
        self.motion.y = self.jump_speed*delta
