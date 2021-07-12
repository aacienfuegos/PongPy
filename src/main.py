import math, random, time
import pygame

from colors import bcolors, rgb

from obj import Map, Ball, Paddle
from dynamic import Position, Trajectory

class Pong:
    def __init__(self, w,h):
        self.map = Map(w, h)

        center = math.floor((w-1)/2)

        init_ball_pos = Position(center, 1)
        init_vel = Trajectory(random.randint(-1, 1), 1)
        self.ball = Ball(init_ball_pos, init_vel)
        
        paddle_len = 3
        init_paddle_pos = [Position(center, 0), Position(center, h-1)]
        self.paddles = [Paddle(paddle_len, init_paddle_pos[0]),
                        Paddle(paddle_len, init_paddle_pos[1])]
        
def print_status(game):
    map = [[" " for col in range(game.map.w)] for row in range(game.map.h)]
    
    ball_out = game.ball.pos.y < 0 or game.ball.pos.y >= game.map.h or game.ball.pos.x < 0 or game.ball.pos.x >= game.map.w
    if(not ball_out):
        map[game.ball.pos.y][game.ball.pos.x] = bcolors.OKGREEN + "o" + bcolors.ENDC
    
    for paddle in game.paddles:
        aux = math.floor(paddle.len/2)
        for i in range(-aux, aux+1):
            if(paddle.pos.x + i < 0 or paddle.pos.x + i >= game.map.w): continue
            map[paddle.pos.y][paddle.pos.x + i] = bcolors.OKBLUE + "□" + bcolors.ENDC

    for row in map:
        row.insert(0, "|")
        row.append("|")

    h_line = ["-" for col in range(len(map[0]))]
    h_line[0], h_line[-1] = "+","+"
    map.insert(0, h_line)   
    map.append(h_line)
    
    for i in range(len(map)):
        out = ""
        for col in map[i]:
            out += col
        print(out)

def key_handler(game):
    game_over = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_over = True
            elif event.key == pygame.K_LEFT:
                game.paddles[1].move(game, -1)
            elif event.key == pygame.K_RIGHT:
                game.paddles[1].move(game, 1)
    return game_over
                
def draw(dis, game):
    scale = 100

    dis.fill(rgb.WHITE)

    ball_out = game.ball.pos.y < 0 or game.ball.pos.y >= game.map.h or game.ball.pos.x < 0 or game.ball.pos.x >= game.map.w
    if(not ball_out):
        pygame.draw.circle(dis, rgb.RED, (game.ball.pos.x*scale + scale/2, game.ball.pos.y*scale + scale/2), scale/2)

    for paddle in game.paddles:
        aux = math.floor(paddle.len/2)
        for i in range(-aux, aux+1):
            if(paddle.pos.x + i < 0 or paddle.pos.x + i >= game.map.w): continue
            pygame.draw.rect(dis, rgb.BLUE, [(paddle.pos.x + i)*scale, paddle.pos.y*scale, scale, scale])

def draw_end_game(dis, game):        
    font = pygame.font.Font('freesansbold.ttf', 32)
    msg = ''
    if(game.ball.pos.y < 0):
        msg = 'You Win'
    elif(game.ball.pos.y >= game.map.h): 
        msg = 'You Lose'
    text = font.render(msg, True, rgb.GREEN, rgb.BLUE)
    text_rect = text.get_rect()
    w, h = dis.get_size()
    text_rect.center = (w // 2, h // 2)
    dis.blit(text, text_rect)    


def main():
    pygame.init()
    w,h = 8,7
    dis = pygame.display.set_mode((w*100,h*100))
    pygame.display.set_caption('Pong Game by Cienfuegos')
    clock = pygame.time.Clock()
    
    game_over = False

    game = Pong(w,h)
    game.ball.traj.x = 0
    game.ball.traj.y = 1
    # game.paddles[0].move(game, -3)
    
    while not game_over:
        game_over = key_handler(game)
        game_over |= game.ball.update_pos(game)
        draw(dis, game)
        pygame.display.update()
        clock.tick(8)
    
    while not key_handler(game): 
        draw_end_game(dis, game)
        pygame.display.update()
    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main()