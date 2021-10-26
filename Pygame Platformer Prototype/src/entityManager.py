from pygame import event
from fairy import Fairy
import globals, world_data, pygame
from entity import Entity
from player import Player
from fog import Fog

class EntityManager:
    def __init__(self):
        self.player = None
        self.fairy = None
        self.enemies = []
        self.fog = Fog()
    
    def init(self):
        for enemy in self.enemies:
            enemy.init()
        if self.player != None:
            self.player.init()
        if self.fairy != None:
            self.fairy.init()

    def update(self, delta):
        for enemy in self.enemies:
            enemy.update(delta)
        if self.player != None:
            self.player.update(delta)
        if self.fairy != None:
            self.fairy.update(delta)
        self.player.is_on_light = world_data.circle_collision(self.player.rect.left, self.player.rect.top, self.player.rect.width, self.player.rect.height, self.fog.light_rect.center[0]-10, self.fog.light_rect.center[1]-20, (world_data.LIGHT_RADIUS[0]/2)-25)
    
    def draw(self):
        for enemy in self.enemies:
            enemy.draw()
        if self.player != None:
            self.player.draw()
        if self.fairy != None:
            self.fairy.draw()
        if world_data.DRAW_FOG: self.fog.draw() 

    
    def add_enemy(self):
        pass

    def set_player(self, pos=(0,0), image_path="", sprite_width=32, sprite_height=32, sprite_scale=1):
        self.player = Player(pos, image_path, sprite_width, sprite_height, sprite_scale)
    
    def set_fairy(self, pos=(0,0), image_path="", sprite_width=32, sprite_height=32, sprite_scale=1):
        self.fairy = Fairy(pos, image_path, sprite_width, sprite_height, sprite_scale)
        