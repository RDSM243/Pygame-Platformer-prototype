import pygame
from pygame import transform

class SpriteSheet():
    def __init__(self, image):
        self.sheet = pygame.image.load(image).convert_alpha()
        self.current_frame = 0
        self.animations = {}
        self.init_time = pygame.time.get_ticks()
        self.flip_h = False
        self.flip_v = False
        
    def get_image(self, width, height, scale, color):
        self.frame_width = width
        self.frame_height = height
        self.image_scale = scale
        image = pygame.Surface((width, height))
        image.blit(self.sheet, (0, 0), ((self.current_frame*width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image

    def add_animation(self, name:str, animation_frames=[0], time=80, one_shot=False):
        if type(animation_frames) is list:
            self.animations[name] = [animation_frames, time, one_shot]
        elif type(animation_frames) is int and animation_frames >= 0:
            frames_list = []
            for i in animation_frames:
                frames_list.append(i)
            self.animations[name] = [frames_list, time, one_shot]
        else:
            print('ERROR: Could not create animation' + name + '.')

    def play(self, name:str):
        if name in self.animations.keys():
            current_time = pygame.time.get_ticks()
            if current_time - self.init_time > self.animations[name][1]: # animate every half second
                self.init_time = current_time
                #animating player 
                self.current_frame += 1
                if self.current_frame not in self.animations[name][0]:
                    if self.animations[name][2]:
                        self.current_frame = self.animations[name][0][len(self.animations[name][0])-1]
                    else: 
                        self.current_frame = self.animations[name][0][0] 
    
        else:
            print("ERROR: Animation " + name +  " don't exist.")
        image = self.get_image(self.frame_width, self.frame_height, self.image_scale, (0, 0, 0))   
        return image