import pygame, tile, globals, world_data

from tile import *

class TileMap:
    def __init__(self):
        self.xOffset = 0
        self.tiles = pygame.sprite.Group()

    def loadMap(self, tilemap_data, tile_width=32, tile_height=32):
        for line in range(len(tilemap_data)):
            for column in range(len(tilemap_data[line])):
                if tilemap_data[line][column] != 0:
                    self.tiles.add(Tile((column*tile_width, line*tile_height), tile_width, tile_height))
        world_data.tiles = self.tiles
    
    def update(self, delta):
        self.tiles.update(delta, self.xOffset)
        
    def draw(self):
        self.tiles.draw(globals.screen)