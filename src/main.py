import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from obj import Pong
import draw

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
                
def init_gui(w,h):
    pygame.init()
    dis = pygame.display.set_mode((w*100,h*100))
    pygame.display.set_caption('Pong Game by Cienfuegos')
    clk = pygame.time.Clock()

    return dis, clk

def main():
    # Map size
    w,h = 8,7

    # Training data
    train = True
    max_gen= 1000
    time = 200
    winners = []

    gen = 0
    while True:
        gen += 1
        game = Pong(w,h)
        # game.ball.traj.x = 0
        # game.ball.traj.y = 1
        # game.paddles[1].move(game, -3)

        if not train: dis, clk = init_gui(w,h)
        
        game_over = False
        
        while not game_over:
            game_over = game.ball.update_pos(game)
            if train:
                time -= 1
                game_over = time <= 0
            else:
                game_over |= key_handler(game)
                draw.draw(dis, game)
                pygame.display.update()
                clk.tick(8)
        
        if not train:
            while not key_handler(game): 
                draw.draw_end_game(dis, game)
                pygame.display.update()
            pygame.quit()
        
        winner = game.get_winner()
        winners.append(winner)
        print("Game " + str(gen) + ": Player " + str(winner) + " wins")
            
        if not train or gen >= max_gen: quit()
        
    
if __name__ == "__main__":
    main()