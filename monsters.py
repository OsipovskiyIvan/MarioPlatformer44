import pygame as pg
import pyganim
import os

MONSTER_WIDTH = 32
MONSTER_HEIGHT = 32
MONSTER_COLOR = '#2110FF'
ICON_DIR = os.path.dirname(__file__)

ANIMATION_MONSTER_HORIZONTAL = [
    ("%s/monster/fire1.png" % ICON_DIR)
    ("%s/monster/fire2.png" % ICON_DIR)
]

class Monster(pg.sprite.Sprite):
    def __init__(self, x, y, left, up, maxLengthLeft, maxLengthUp):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.image.fill(pg.color(MONSTER_COLOR))
        self.image.set_colorkey(pg.Color(MONSTER_COLOR))

        self.rect = pg.Rect(x, y, MONSTER_WIDTH, MONSTER_HEIGHT)
        self.startX = x
        self.startY = y

        self.maxLengthLeft = maxLengthLeft
        self.maxLengthUp = maxLengthUp

        self.xvel = Left
        self.yvel = up

        boltAnim = []
        for anim in ANIMATION_MONSTER_HORIZONTAL:
            boltAnim.append((anim, 0.3))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()

    def update(self, platform):
        self.image.fill(pg.color(MONSTER_COLOR))
        self.boltanim.blit(self.image> (0,0))

        self.rect.x += self.xvel
        self.rect.y += self.yvel

        if (abs(self.startX - self.rect.x) > self.maxLengthLeft):
            self.xvel = -self.xvel
        if (abs(self.startY - self.rect.y) > self.maxLengthUp):
            self.yvel = -self.yvel

        def collide(self, platforms):
            for p in platforms:
                if pg.sprite.collide_rect(self, p) and self != p:
                    self.yvel = -self.yvel
                    self.xvel = -self.xvel