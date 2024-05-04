import pygame
class Snake:
    """管理蛇的类"""
    def __init__(self,ai):
        self.screen=ai.screen
        self.screen_rect=ai.screen.get_rect()

        self.image=pygame.image.load("pic/snake.bmp")
        self.rect=self.image.get_rect()
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        self.rect.midbottom=self.screen_rect.midbottom

    def update(self):
        if self.moving_right==True:
            self.rect.x+=1
        elif self.moving_left==True:
            self.rect.x-=1
        elif self.moving_up==True:
            self.rect.y-=1
        elif self.moving_down==True:
            self.rect.y+=1
    def blitsnake(self):
        self.screen.blit(self.image,self.rect)
