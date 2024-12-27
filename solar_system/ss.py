import pygame as pg
from classes import The_Star, The_Planet

pg.init()

screen = pg.display.set_mode((1200, 600))
bg = pg.image.load('solar system/cosmos.png')

the_Sun = The_Star('solar system/sun.png', (600, 250))
the_Mercury = The_Planet('solar system/mercury.png', (600, 250), 576, 1, 200, 'Mercury')
the_Venus = The_Planet('solar system/venus.png', (600, 250), 420, 1, 300, 'Venus')
the_Earth = The_Planet('solar system/earth.png', (600, 250), 366, 1, 400, 'Earth')
the_Mars = The_Planet('solar system/mars.png', (600, 250), 288, 1, 500, 'Mars')
the_Jupiter = The_Planet('solar system/jupiter.png', (600, 250), 156, 8, 600, 'Jupiter')
the_Saturn = The_Planet('solar system/saturn.png', (600, 250), 120, 6, 700, 'Saturn')
the_Uranus = The_Planet('solar system/uranus.png', (600, 250), 84, 1, 800, 'Uranus')
the_Neptune = The_Planet('solar system/neptune.png', (600, 250), 60, 1, 900, 'Neptune')

heavenly_bodies = [the_Sun, the_Mercury, the_Venus, the_Earth, the_Mars, the_Jupiter, the_Saturn, the_Uranus, the_Neptune]
planets = [the_Mercury, the_Venus, the_Earth, the_Mars, the_Jupiter, the_Saturn, the_Uranus, the_Neptune]
f_year = pg.font.SysFont('Arial', 24)
sel_planet = 0
text = f_year.render('Name: ' + planets[sel_planet]._name +  '   Year: ' + str(planets[sel_planet]._counter), False, 'white')

time = 0
running = True
while running:
    pg.display.flip()

    if time == 60:
        text = f_year.render('Name: ' + planets[sel_planet]._name +  '   Year: ' + str(planets[sel_planet]._counter), False, 'white')
        screen.blit(bg, (0,0))
        screen.blit(text, (5, 550))
        for i in range(81):
            for j in range(len(heavenly_bodies)-1):
                if heavenly_bodies[j] == the_Sun:
                    if heavenly_bodies[j] == the_Sun and (heavenly_bodies[j+1]._behind or heavenly_bodies[j+1]._right):
                        heavenly_bodies[j], heavenly_bodies[j+1] = heavenly_bodies[j+1], heavenly_bodies[j]

                elif heavenly_bodies[j+1] == the_Sun:
                    if (heavenly_bodies[j]._in_front_of or heavenly_bodies[j]._left) and heavenly_bodies[j+1] == the_Sun:
                        heavenly_bodies[j], heavenly_bodies[j+1] = heavenly_bodies[j+1], heavenly_bodies[j]

                else:
                    if heavenly_bodies[j]._in_front_of and heavenly_bodies[j+1]._right:
                        heavenly_bodies[j], heavenly_bodies[j+1] = heavenly_bodies[j+1], heavenly_bodies[j]

                    elif heavenly_bodies[j]._left and heavenly_bodies[j+1]._behind:
                        heavenly_bodies[j], heavenly_bodies[j+1] = heavenly_bodies[j+1], heavenly_bodies[j]

                    elif (heavenly_bodies[j]._in_front_of and heavenly_bodies[j+1]._in_front_of) \
                        or (heavenly_bodies[j]._left and heavenly_bodies[j+1]._left):
                        if planets.index(heavenly_bodies[j]) > planets.index(heavenly_bodies[j+1]):
                            heavenly_bodies[j], heavenly_bodies[j+1] = heavenly_bodies[j+1], heavenly_bodies[j]

                    elif (heavenly_bodies[j]._right and heavenly_bodies[j+1]._right) \
                        or (heavenly_bodies[j]._behind and heavenly_bodies[j+1]._behind):
                        if planets.index(heavenly_bodies[j]) < planets.index(heavenly_bodies[j+1]):
                            heavenly_bodies[j], heavenly_bodies[j+1] = heavenly_bodies[j+1], heavenly_bodies[j]
        for body in heavenly_bodies:
            body.move(screen)
        time = 0
    else: time += 1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
