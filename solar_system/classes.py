import pygame as pg


class The_Star(pg.sprite.Sprite):
    def __init__(self, img, center):
        self._imgorig = pg.image.load(img)
        self._img = self._imgorig
        self._rect = self._img.get_rect()
        self._rect.center = center
    
    def move(self, screen):
        screen.blit(self._img, self._rect)

class The_Planet(The_Star):
    def __init__(self, img, center, speed, speed_resize, orbit, name):
        super().__init__(img, center)
        self._speed = speed
        self._speed_resize = speed_resize
        self._orbit = orbit
        self._counter = 0
        self._name = name
        self._in_front_of = True
        self._behind = False
        self._right = False
        self._left = False
    
    def move(self, screen):
        if self._rect.left >= self._orbit + 600:
            self._in_front_of = False
            self._right = True
        elif self._rect.left <= 600 and self._right:
            self._right = False
            self._behind = True
        elif self._rect.right <= 600 - self._orbit:
            self._behind = False
            self._left = True
        elif self._rect.right >= 600 and self._left:
            self._left = False
            self._in_front_of= True
            self._counter += 1
        if self._in_front_of:
            self._rect.move_ip(self._speed, 0)
            self._img = pg.transform.smoothscale(self._imgorig, (self._img.get_size()[0] - self._speed_resize, self._img.get_size()[1] - self._speed_resize))
            super().move(screen)
        elif self._right:
            self._rect.move_ip(-self._speed, 0)
            self._img = pg.transform.smoothscale(self._imgorig, (self._img.get_size()[0] - self._speed_resize, self._img.get_size()[1] - self._speed_resize))
            super().move(screen)
        elif self._behind:
            self._rect.move_ip(-self._speed, 0)
            self._img = pg.transform.smoothscale(self._imgorig, (self._img.get_size()[0] + self._speed_resize, self._img.get_size()[1] + self._speed_resize))
            super().move(screen)
        elif self._left:
            self._rect.move_ip(self._speed, 0)
            self._img = pg.transform.smoothscale(self._imgorig, (self._img.get_size()[0] + self._speed_resize, self._img.get_size()[1] + self._speed_resize))
            super().move(screen)
            
            