import math, random, time

from colors import bcolors

from obj import Map, Ball, Paddle
from dynamic import Position, Trajectory

class Pong:
    def __init__(self):
        w,h = 7,7
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

        

def main():
    game = Pong()
    game.ball.traj.x = 0
    game.ball.traj.y = 1
    game.paddles[1].move(game, -1)
    
    for t in range(20):
        print_status(game)
        # game.paddles[0].move(game, -1)
        # game.paddles[1].move(game, 1)
        game.ball.update_pos(game)
        time.sleep(0.5)

if __name__ == "__main__":
    main()