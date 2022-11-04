import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("jump.png").convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio_jump.mp3')
        self.jump_sound.set_volume(0.2)
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self) -> None:
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == 'Fly':
            fly_1 = pygame.image.load("Fly1.png").convert_alpha()
            fly_2 = pygame.image.load("Fly2.png").convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load("snail1.png").convert_alpha()
            snail_2 = pygame.image.load("snail2.png").convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()
    def destroy(self):
       if self.rect.x <= -100:
           self.kill()

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render(f' score: {int(current_time / 1000)}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True

SCREEN_SIZE = (800, 400)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

test_font = pygame.font.Font("Pixeltype.ttf", 50)
game_active = True
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('music.wav')
bg_music.play()

obstacle_group = pygame.sprite.Group()
player = pygame.sprite.GroupSingle()
player.add(Player())

sky_surface = pygame.image.load("../python stuff/Sky.png").convert()
ground_surface = pygame.image.load("ground.png").convert()

player_stand = pygame.image.load("player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Pixel Runner', False, (111, 96, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 320))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEMOTION:
                if event.type == pygame.KEYDOWN:
                    print("hii")
        else:
            if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()
        if game_active:
            if event.type == obstacle_timer and game_active:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
            if event.type == snail_animation_timer:
             print("hii")
            if event.type == fly_animation_timer:
                print("hii2")

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()
        # Player
        player.draw(screen)
        obstacle_group.draw(screen)
        obstacle_group.update()
        player.update()

        # collision
        game_active = collision_sprite()
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_message, game_message_rect)
        screen.blit(game_name, game_name_rect)
        player_gravity = 0
        score_message = test_font.render(f'Your score: {int(score / 1000)} ', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 360))
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)


    pygame.display.update()
    clock.tick(60)
