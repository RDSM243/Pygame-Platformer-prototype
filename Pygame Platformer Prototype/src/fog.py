import globals, world_data, math
import pygame as pg

class Fog():
    def __init__(self) -> None:
        self.fog = pg.Surface((globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT))
        self.fog.fill(world_data.BACKGROUND_COLOR)
        self.light_mask = pg.image.load('../res/images/light.png').convert_alpha()
        self.fill_img(self.light_mask, (94, 233, 233))
        self.light_mask = pg.transform.scale(self.light_mask, world_data.LIGHT_RADIUS)
        self.light_rect = self.light_mask.get_rect()
        pass

    def draw(self):
        # draw the light mask (gradient) onto fog image
        self.fog.fill("black")
        self.light_rect.center = globals.MOUSE_POS
        self.fog.blit(self.light_mask, self.light_rect)
        globals.screen.blit(self.fog, (0, 0), special_flags=pg.BLEND_MULT)
        # pg.draw.circle(globals.screen, (255,0,0), (self.light_rect.center[0]+1, self.light_rect.center[1]-2), int(globals.LIGHT_RADIUS[0]/2)-20, 1)

    #paint every pixel from the image
    def fill_img(self, surface, color):
        w = surface.get_width()
        h = surface.get_height()
        r, g, b = color
        for x in range(w):
            for y in range(h):
                a = surface.get_at((x, y))[3]
                surface.set_at((x, y), pg.Color(r, g, b, a))