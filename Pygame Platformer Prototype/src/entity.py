import pygame
import globals, world_data
from spritesheet import SpriteSheet 

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0), imagePath="", sprite_width=32, sprite_height=32, sprite_scale=1):
        super().__init__()
        if imagePath != "":
            self.spriteSheet = SpriteSheet(imagePath)
            self.image = self.spriteSheet.get_image(sprite_width, sprite_height, sprite_scale, (0, 0, 0))
        else:
            self.image = pygame.Surface((sprite_width, sprite_height))
            self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.motion = pygame.math.Vector2(0, 0)
        self.is_on_floor = False
        self.true_pos = list(self.rect.center) # Exact float position.
        self.gravity = 50
    
    def update(self, delta):
        self.rect.centerx += self.true_pos[0]
        self.checkHorizontalCollisions()
        self.motion.y += self.gravity*delta
        self.true_pos[1] = self.motion.y
        self.rect.centery += self.true_pos[1]
        self.checkVerticalCollisions()
        pass

    def checkHorizontalCollisions(self):
        for sprite in world_data.tiles.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.motion.x < 0:
                    self.motion.x = 0
                    self.rect.left = sprite.rect.right
                elif self.motion.x > 0:
                    self.motion.x = 0
                    self.rect.right = sprite.rect.left
            
    def checkVerticalCollisions(self):
        self.is_on_floor = False
        for sprite in world_data.tiles.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.motion.y > 0:
                    self.is_on_floor = True
                    self.rect.bottom = sprite.rect.top
                    self.motion.y = 0
                elif self.motion.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.motion.y = 0

    def draw(self):
        globals.screen.blit(self.image, self.rect)