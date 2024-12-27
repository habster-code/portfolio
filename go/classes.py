import pygame as pg
import numpy as np
import itertools
import networkx as nx


board_color = 'gray'
screen_size = 1000
margin = 125
point_size = 41

def make_board(size):
    points = []
    for i in range(0, size):
        for j in range(0, size):
            points.append(Point('point.png', [point_size*j + margin, point_size*i + margin], [i,j]))
    return (points)

def close_breathe(board, group):
    for x, y in group:
        if x > 0 and board[x - 1, y] == 0:
            return False
        if y > 0 and board[x, y - 1] == 0:
            return False
        if x < board.shape[0] - 1 and board[x + 1, y] == 0:
            return False
        if y < board.shape[0] - 1 and board[x, y + 1] == 0:
            return False
    return True

def get_stone_groups(board, color):
    size = board.shape[0]
    if color == 'black':
        color_code = 1
    else:
        color_code = 2
    xs, ys = np.where(board == color_code)
    graph = nx.grid_graph(dim = [size, size])
    stones = set(zip(xs, ys))
    all_spaces = set(itertools.product(range(size), range(size)))
    stones_to_remove = all_spaces - stones
    graph.remove_nodes_from(stones_to_remove)
    return nx.connected_components(graph)

class Point():
    def __init__(self, img, pos, coords):
        self.img = pg.image.load(img)
        self.rect = self.img.get_rect()
        self.pos = pos
        self.coords = coords
        self.rect.move_ip(pos[0], pos[1])
    def draw(self, screen):
        screen.blit(self.img, self.rect)

class Stone():
    def __init__(self, img, pos):
        self.img = pg.image.load(img)
        self.rect = self.img.get_rect()
        self.pos = pos
        self.rect.move_ip(pos[0], pos[1])
    def draw(self, screen):
        screen.blit(self.img, self.rect)

class Game:
    def __init__(self, size):
        self.board = np.zeros((size, size))
        self.size = size
        self.black_turn = True
        self.prisoners = {'black' : 0, 'white' : 0}
        self.points = make_board(self.size)
        pg.init()
        screen = pg.display.set_mode((screen_size, screen_size))
        self.screen = screen
        self.font = pg.font.SysFont('arial', 30)

    def fill_screen(self):
        self.screen.fill(board_color)
        for point in self.points:
            point.draw(self.screen)
        border = pg.image.load('border.png')
        border_rect = border.get_rect()
        border_rect.move_ip(105, 105)
        self.screen.blit(border, border_rect)
        pg.display.flip()

    def handle_click(self, click):
        click_point = False
        for point in self.points:
            if point.rect.collidepoint(click.pos):
                if self.board[point.coords[0], point.coords[1]] == 0:
                    col, row = point.coords
                    click_point = True
                    break
        if click_point == False:
            return
        if self.black_turn:
            self.board[col, row] = 1  
        else:
            self.board[col, row] = 2

        if self.black_turn:
            self_color = 'black'
            other_color = 'white'
        else:
            self_color = 'white'
            other_color = 'black'

        capture_happened = False
        for group in list(get_stone_groups(self.board, other_color)):
            if close_breathe(self.board, group):
                capture_happened = True
                for i, j in group:
                    self.board[i, j] = 0
                self.prisoners[self_color] += len(group)

        if capture_happened == False:
            group = None
            for group in get_stone_groups(self.board, self_color):
                if (col, row) in group:
                    break
            if close_breathe(self.board, group):
                self.board[col, row] = 0
                return

        self.black_turn = not self.black_turn
        self.draw()

    def draw(self):
        self.fill_screen()
        for row, col in zip(*np.where(self.board == 1)):
            stone = Stone('black.png', [self.points[row*self.size + col].pos[0], self.points[row*self.size + col].pos[1]])
            stone.draw(self.screen)
        for row, col in zip(*np.where(self.board == 2)):
            stone = Stone('white.png', [self.points[row*self.size + col].pos[0], self.points[row*self.size + col].pos[1]])
            stone.draw(self.screen)

        score_txt = (
            f"Black's Prisoners: {self.prisoners['black']}"
            + f"     White's Prisoners: {self.prisoners['white']}"
        )
        txt = self.font.render(score_txt, True, (0,0,0))
        self.screen.blit(txt, (margin, screen_size - margin + 30))
        turn_txt = (
            f"{'Black' if self.black_turn else 'White'} to move. "
            + "Click to place stone."
        )
        txt = self.font.render(turn_txt, True, (0,0,0))
        self.screen.blit(txt, (margin, 20))

        pg.display.flip()

    def update(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_click(event)
            if event.type == pg.QUIT:
                return False
        return True