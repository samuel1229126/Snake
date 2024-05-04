import pygame
from pygame.sprite import Sprite
from random import randint as rdt
class Apple(Sprite):
    """管理苹果的类"""
    def __init__(self,ai):
        super().__init__()
        self.screen=ai.screen
        self.screen_rect=ai.screen.get_rect()
        self.image=pygame.image.load("pic/apple.bmp")
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
        
    def blitapple(self,x,y):
        self.rect.x=x
        self.rect.y = y
        self.screen.blit(self.image,self.rect)
