from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
import pygame
import random

class ObstacleManager:

    def __init__(self):
        self.obstacles = []
    
    
    def update(self, game):

        if len(self.obstacles) == 0:
            index = random.randint(0, 2)
            if index == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif index == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif index == 2:
                self.obstacles.append(Bird(BIRD))
            
                
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break
            
                
    def draw(self, screen):
            for obstacle in self.obstacles:
                obstacle.draw(screen) 
       

