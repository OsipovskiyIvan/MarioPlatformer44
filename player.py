import pygame as pg
import pyganim
import os

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.35
ANIMATION_DELAY = 0.1
ICON_DIR = os.path.dirname(__file__)

ANIMATION_RIGHT = [
    ('%s/mario/r1.png' % ICON_DIR),
    ('%s/mario/r2.png' % ICON_DIR),
    ('%s/mario/r3.png' % ICON_DIR),
    ('%s/mario/r4.png' % ICON_DIR),
    ('%s/mario/r5.png' % ICON_DIR),
]
ANIMATION_JUMP_LEFT = [('%s/mario/jl.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP_RIGHT = [('%s/mario/jr.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP = [('%s/mario/j.png' % ICON_DIR, 0.1)]
ANIMATION_STAY = [('%s/mario/0.png' % ICON_DIR, 0.1)]