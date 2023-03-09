import pygame
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.text_utils import TextUtils
from dino_runner.utils.constants import BG, COLORS, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, IMG_DIR
from dino_runner.components.dinosaur import Dinosaur
import os
import pygame.mixer



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.text_utils = TextUtils()
        self.game_running = True
        self.background_color = COLORS["light blue"]
        

        pygame.mixer.init()

        

    def run(self):
        musica_fondo = pygame.mixer.Sound("dino_runner/assets/Audio/musica.wav")
        pygame.mixer.Sound.play(musica_fondo, -1)
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.points = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

        pygame.mixer.Sound.stop(musica_fondo)
        


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill(COLORS["light blue"]) 
        self.draw_background()
        
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score()

        
        pygame.display.update()
        pygame.display.flip()
        


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

 

    def score(self):
        self.points += 1
        text, text_rect = self.text_utils.get_score(self.points)
        self.screen.blit(text, text_rect)

    def show_menu(self, death_count = 0):
        self.game_running = True
        self.screen.fill(self.background_color)  
        self.print_menu_elements(death_count)
        pygame.display.update()
        self.handle_key_events()



    def print_menu_elements(self, death_count=0):
        title, title_rect = self.text_utils.get_centered_message("DINO GAME", height=SCREEN_HEIGHT//7 - 50)
        self.screen.blit(title, title_rect)
        
        text, text_rext = self.text_utils.get_centered_message("Press any key to Start", height=SCREEN_HEIGHT//2 + 150)
        self.screen.blit(text, text_rext)
        if death_count > 0:
            score, score_rect = self.text_utils.get_centered_message(
                "Your Score: " + str(self.points),
                height= SCREEN_HEIGHT//2 + 200)
            self.screen.blit(score, score_rect)
        self.screen.blit(RUNNING[0], (SCREEN_WIDTH//2 - 20, SCREEN_HEIGHT//2 -140))

        Cactus_img = pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png"))
        Cloud_img = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
        BG_img = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
        
        self.screen.blit(Cactus_img, (SCREEN_WIDTH//2 - 300, SCREEN_HEIGHT//2 - 135))
        self.screen.blit(Cactus_img, (SCREEN_WIDTH//2 + 200, SCREEN_HEIGHT//2 - 135))
        self.screen.blit(Cloud_img, (SCREEN_WIDTH//2 - 350, SCREEN_HEIGHT//2 - 250))
        self.screen.blit(Cloud_img, (SCREEN_WIDTH//2 + 300, SCREEN_HEIGHT//2 - 200))
        self.screen.blit(Cloud_img, (SCREEN_WIDTH//2 -400, SCREEN_HEIGHT//2 - 150))
        self.screen.blit(Cloud_img, (SCREEN_WIDTH//2 + 300, SCREEN_HEIGHT//2 - 110))
        self.screen.blit(Cloud_img, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 180))
        self.screen.blit(BG_img, (SCREEN_WIDTH//2 - 600, SCREEN_HEIGHT//2 - 60))
    
        

    def handle_key_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                self.run()

