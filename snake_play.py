import sys
import pygame
from settings import Settings
from snake import Snake
from apple import Apple
from random import randint as rdt
class Snakeplay:
    """资源总类"""
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        self.bg_color=(255,255,255)
        self.points=0
        self.apple_how=0
        self.apple=pygame.sprite.Group()
        self.screen=pygame.display.set_mode((self.settings.width,self.settings.hidth))
        pygame.display.set_caption("贪吃蛇")
        self.snake=Snake(self)
    def run_game(self):
        self._add_apple()
        while True:            
            self._check_events()
            self.snake.update()
            self._check_bang()
            self._change_screen()
    def _add_apple(self):
        self.apple.empty()
        rand_1_5=rdt(1,5)
        for i in range(rand_1_5):
            new_apple=Apple(self)
            new_apple.x=rdt(100,1100)
            new_apple.y=rdt(100,700)
            self.apple.add(new_apple)
        self.apple_how=rand_1_5
    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    self.snake.moving_right=True
                elif event.key==pygame.K_LEFT:
                    self.snake.moving_left=True
                elif event.key==pygame.K_UP:
                    self.snake.moving_up=True
                elif event.key==pygame.K_DOWN:
                    self.snake.moving_down=True
                    
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    self.snake.moving_right=False
                if event.key==pygame.K_LEFT:
                    self.snake.moving_left=False
                if event.key==pygame.K_UP:
                    self.snake.moving_up=False
                if event.key==pygame.K_DOWN:
                    self.snake.moving_down=False
                    
    def _change_screen(self):
        self.screen.fill(self.bg_color)
        self.snake.blitsnake()
        for aple in self.apple.sprites():
            aple.blitapple(aple.x,aple.y)
        pygame.display.flip()
    def _check_bang(self):
        if pygame.sprite.spritecollideany(self.snake,self.apple):
            self.points=self.points+1
            self.apple_how=self.apple_how-1
            if self.apple_how==0:
                self._add_apple()


ai=Snakeplay()
ai.run_game()
