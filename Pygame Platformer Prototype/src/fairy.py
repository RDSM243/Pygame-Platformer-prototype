from entity import Entity
import pygame, globals

class Fairy(Entity):
    def __init__(self, pos=(0, 0), imagePath="", sprite_width=32, sprite_height=32, sprite_scale=1):
        Entity.__init__(self, pos, imagePath, sprite_width, sprite_height, sprite_scale)
        pygame.mouse.set_visible(False)
    
    def init(self):
        self.spriteSheet.add_animation("idle", [0, 1, 2, 3], 70)

    def update(self, delta):
        self.image = self.spriteSheet.play("idle")
        self.rect.center = globals.MOUSE_POS

    def draw(self):
        globals.screen.blit(self.image, self.rect)
