import math
from aux import sign

from dynamic import Position, Trajectory

width, height = 7,7

class Ball:
    def __init__(self, init_pos=Position(0,0), init_vel=Trajectory(0,1)):
        self.pos = init_pos
        self.traj = init_vel
        
    def update_pos(self, game):
        final_x = self.pos.x + self.traj.x
        final_y = self.pos.y + self.traj.y

        bool_bounce_wall = final_x < 0 or final_x >= game.map.w
        if(bool_bounce_wall): self.bounce_wall()

        for paddle in game.paddles:
            bool_bounce_paddle = (final_y == paddle.pos.y) and (abs(final_x - paddle.pos.x) <= paddle.len/2)
            if(bool_bounce_paddle):
                self.bounce_paddle(paddle)               
                break

        self.pos.x += self.traj.x
        self.pos.y += self.traj.y
        
    def bounce_wall(self):
        self.traj.x *= -1
        
    def bounce_paddle(self, paddle):
        self.traj.y *= -1
        final_x = self.pos.x + self.traj.x
        paddle_square = final_x - paddle.pos.x
        if (abs(paddle_square) == math.floor(paddle.len/2)):
            self.traj.x = 1*sign(paddle_square)
        else:
            self.traj.x = 0
            
            
        
        
            
        
class Paddle:
    def __init__(self, len=3,  init_pos=Position(0,0)):
        self.len = len
        self.pos = init_pos
        
    def move(self, game, x):
        self.pos.x += x
        if (self.pos.x >= game.map.w):
            self.pos.x = game.map.w
        elif (self.pos.x < -1):
            self.pos.x = -1
        
class Map:
    def __init__(self, w=7,  h=7):
        self.w, self.h = w, h
