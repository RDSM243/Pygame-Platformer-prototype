import pygame, globals

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, tile_width, tile_height):
        super().__init__()
        self.image = pygame.Surface((tile_width, tile_height))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)
    def update(self, delta:float, x_shift):
        self.rect.x += x_shift