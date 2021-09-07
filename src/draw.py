import math, pygame
import colors


def print_status(game):
    map = [[" " for col in range(game.map.w)] for row in range(game.map.h)]

    ball_out = (
        game.ball.pos.y < 0
        or game.ball.pos.y >= game.map.h
        or game.ball.pos.x < 0
        or game.ball.pos.x >= game.map.w
    )
    if not ball_out:
        map[game.ball.pos.y][game.ball.pos.x] = (
            colors.bcolors.OKGREEN + "o" + colors.bcolors.ENDC
        )

    for paddle in game.paddles:
        aux = math.floor(paddle.len / 2)
        for i in range(-aux, aux + 1):
            if paddle.pos.x + i < 0 or paddle.pos.x + i >= game.map.w:
                continue
            map[paddle.pos.y][paddle.pos.x + i] = (
                colors.bcolors.OKBLUE + "□" + colors.bcolors.ENDC
            )

    for row in map:
        row.insert(0, "|")
        row.append("|")

    h_line = ["-" for col in range(len(map[0]))]
    h_line[0], h_line[-1] = "+", "+"
    map.insert(0, h_line)
    map.append(h_line)

    for i in range(len(map)):
        out = ""
        for col in map[i]:
            out += col
        print(out)


def draw(dis, game):
    scale = 100

    dis.fill(colors.rgb.WHITE)

    ball_out = (
        game.ball.pos.y < 0
        or game.ball.pos.y >= game.map.h
        or game.ball.pos.x < 0
        or game.ball.pos.x >= game.map.w
    )
    if not ball_out:
        pygame.draw.circle(
            dis,
            colors.rgb.RED,
            (game.ball.pos.x * scale + scale / 2, game.ball.pos.y * scale + scale / 2),
            scale / 2,
        )

    for paddle in game.paddles:
        aux = math.floor(paddle.len / 2)
        for i in range(-aux, aux + 1):
            if paddle.pos.x + i < 0 or paddle.pos.x + i >= game.map.w:
                continue
            pygame.draw.rect(
                dis,
                colors.rgb.BLUE,
                [(paddle.pos.x + i) * scale, paddle.pos.y * scale, scale, scale],
            )


def draw_end_game(dis, game):
    font = pygame.font.Font("freesansbold.ttf", 32)
    msg = ""
    if game.get_winner():
        msg = "You Win"
    else:
        msg = "You Lose"
    text = font.render(msg, True, colors.rgb.GREEN, colors.rgb.BLUE)
    text_rect = text.get_rect()
    w, h = dis.get_size()
    text_rect.center = (w // 2, h // 2)
    dis.blit(text, text_rect)
