import pygame as pg
import time

pg.init()
deltaTime = time.time()
class Monke():
    def __init__(self, sprite, hunger, dirtyness, food):
        self._hunger = 0
        self._dirtyness = 0
        self._hunger_max = hunger
        self._dirtyness_max = dirtyness
        self._food = food
        self._monkey = pg.image.load(sprite)
        self.rect = self._monkey.get_rect()
        self._game_over = True
    def starve(self):
        global deltaTime
        if self._hunger >= self._hunger_max:
            self._hunger = self._hunger_max
            self.death_starve()
            self._game_over = False
        elif self._game_over:
            self._hunger += (time.time() - deltaTime)*6
    def poop(self):
        global deltaTime
        if self._dirtyness >= self._dirtyness_max:
            self._dirtyness = self._dirtyness_max
            self.death_poop()
            self.game_over = False
        elif self._game_over:
            self._dirtyness += time.time() - deltaTime
            deltaTime = time.time()
    def feed(self):
        self._hunger -= self._food
        if self._hunger < 0:
            self._hunger = 0
    def power_poop(self):
        self._dirtyness += self._food/2
    def clean(self):
        self._dirtyness = 0
    def death_starve(self):
        screen.fill('grey')
        for i in range(2):
            screen.blit(f_death.render(game_over_starve.split('.')[i], True, 'white'), (10, i*26))
    def death_poop(self):
        screen.fill((127, 94, 0))
        for i in range(2):
            screen.blit(f_death.render(game_over_poop.split('.')[i], True, 'white'), (10, i*26))
    def restart(self):
        global deltaTime
        self._hunger = 0
        self._dirtyness = 0
        deltaTime = time.time()
        self._game_over = True
          
screen = pg.display.set_mode([320, 320])
bg = pg.image.load("back.png")
running = True
Nikita = Monke("monkey.png", 80, 80, 10)
Nikita.rect.move_ip(104, 104)
f = pg.font.SysFont("Arial", 16)
f_death = pg.font.SysFont("Arial", 24)
hunger_text = f.render('Hunger (press F)', True, 'black')
dirty_text = f.render('Dirtyness (press C)', True, 'black')
restart_text = f.render('Press Enter to restart', True, 'black')
game_over_starve = 'Your monkey is gone.You were should look after her.'
game_over_poop = 'You were bombarded with poop.You were should wash monkey.'
def show_game():
    screen.blit(bg, bg.get_rect())
    pg.draw.rect(screen, 'red', (100, 20, Nikita._hunger, 10))
    pg.draw.rect(screen, 'brown', (100, 50, Nikita._dirtyness, 10))
    pg.draw.rect(screen, 'black', (100, 20, 80, 10), 2)
    pg.draw.rect(screen, 'black', (100, 50, 80, 10), 2)
    screen.blit(Nikita._monkey, Nikita.rect)
    screen.blit(hunger_text, (100, 4))
    screen.blit(dirty_text, (100, 34))
    Nikita.starve()
    Nikita.poop()

while running:
    pg.display.flip()
    if Nikita._game_over:
        show_game()
    screen.blit(restart_text, (10, 300))
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_f:
                Nikita.feed()
                Nikita.power_poop()
            if event.key == pg.K_c:
                Nikita.clean()
            if event.key == pg.K_RETURN:
                Nikita.restart()
        if event.type == pg.QUIT:
            running = False
        