#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, global_scroll: float = 0):
        if global_scroll != 0:
            self.rect.centerx -= global_scroll * ENTITY_SPEED[self.name] * 0.05
            
            if self.rect.right <= 0:
                self.rect.left += WIN_WIDTH * 2
            elif self.rect.left >= WIN_WIDTH:
                self.rect.right -= WIN_WIDTH * 2
