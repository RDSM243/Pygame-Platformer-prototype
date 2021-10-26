import pygame as pg
from entityManager import EntityManager
from tile import Tile
from tilemap import TileMap
import globals, world_data, json, time

class App(object):
    def __init__(self):
        globals.screen = pg.display.get_surface()
        self.screen_rect = globals.screen.get_rect()
        self.clock = pg.time.Clock()
        self.done = False
        globals.pressed_keys = pg.key.get_pressed()

    def init(self):
        self.entityManager = EntityManager()
        self.tileMap = TileMap()
        self.loadLevel(1)
        self.entityManager.init()

    def loadLevel(self, level_path:str = ''):
        if level_path != '':
            self.level_data = json.load(open(level_path, 'r'))
            self.entityManager.set_player((self.level_data['player']['pos_x'], self.level_data['player']['pos_y']), self.level_data['player']['image_path'], self.level_data['player']['image_width'], self.level_data['player']['image_height'], self.level_data['player']['scale'])
            self.entityManager.set_fairy((self.level_data['fairy']['pos_x'], self.level_data['fairy']['pos_y']), self.level_data['fairy']['image_path'], self.level_data['fairy']['image_width'], self.level_data['fairy']['image_height'], self.level_data['fairy']['scale'])
            self.tileMap.loadMap(self.level_data['tilemap_data'], 32, 32)
        else:
            print("ERROR: Cannot Load the level.")
    
    def loadLevel(self, level_number:int = -1):
        if level_number != -1:
            self.level_data = json.load(open('../res/levels/level' + str(level_number) + '.json', 'r'))
            self.entityManager.set_player((self.level_data['player']['pos_x'], self.level_data['player']['pos_y']), self.level_data['player']['image_path'], self.level_data['player']['image_width'], self.level_data['player']['image_height'], self.level_data['player']['scale'])
            self.entityManager.set_fairy((self.level_data['fairy']['pos_x'], self.level_data['fairy']['pos_y']), self.level_data['fairy']['image_path'], self.level_data['fairy']['image_width'], self.level_data['fairy']['image_height'], self.level_data['fairy']['scale'])
            self.tileMap.loadMap(self.level_data['tilemap_data'], 32, 32)
        else:
            print("ERROR: Cannot Load the level.")

    def input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type in (pg.KEYDOWN, pg.KEYUP):
                globals.pressed_keys = pg.key.get_pressed()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_f:
                        world_data.DRAW_FOG = not world_data.DRAW_FOG
        if globals.pressed_keys[pg.K_ESCAPE]:
            self.done = True

    def update(self, delta):
        if globals.PRINT_FPS: print("FPS: " + str(self.clock.get_fps()))
        globals.MOUSE_POS = pg.mouse.get_pos()
        self.tileMap.update(delta)
        self.entityManager.update(delta)
        pass
        
    def draw(self):
        globals.screen.fill(world_data.BACKGROUND_COLOR)
        self.tileMap.draw()
        self.entityManager.draw()
        pg.display.flip()

    def main_loop(self):
        self.init()
        prev_time = time.time()
        delta = 0
        while not self.done:
            self.clock.tick(globals.TARGET_FPS)
            now = time.time()
            delta = now - prev_time
            prev_time = now
            self.input()
            self.update(delta)
            self.draw()