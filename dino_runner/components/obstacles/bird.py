from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image_list):
        self.type = 0
        super().__init__(image_list, self.type)
        self.rect.y = 250
        self.anim_time = 0.0
        
        

    def update(self, game_speed, obstacles):
        super().update(game_speed, obstacles)
       
        self.anim_time += game_speed / 1000.0
        if self.anim_time > 0.2:
            self.anim_time = 0.0

    def draw(self, screen):
        if self.anim_time < 0.1:
            self.type = 0
        else:
            self.type = 1

        screen.blit(self.image_list[self.type], self.rect)
