#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENEMY_ANIMATION, GROUND_Y
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, size: tuple = None):
        super().__init__(name, position, size)
        self.state = 'Walk'
        self.update_image(ENEMY_ANIMATION[self.name][self.state])
        self.rect.bottom = GROUND_Y
        self.damage_cooldown = 0
        self.last_attack = 2

    def move(self, player_rect=None, global_scroll: float = 0):
        if self.health <= 0:
            if global_scroll > 0:
                self.rect.centerx -= global_scroll
            if self.state != 'Dead':
                self.state = 'Dead'
                self.animation_index = 0
                self.animation_timer = 0
                self.update_image(ENEMY_ANIMATION[self.name][self.state])
            if self.animation_index < len(self.animation_frames) - 1:
                self.animate()
            return

        moving = True
        
        if global_scroll > 0:
            self.rect.centerx -= global_scroll
        if self.name == 'Enemy3':
            self.rect.centerx -= ENTITY_SPEED[self.name]
        elif player_rect is not None:
            dist = self.rect.centerx - player_rect.centerx
            if abs(dist) <= 40:
                moving = False
                if self.state not in ['Attack1', 'Attack2']:
                    self.last_attack = 1 if self.last_attack == 2 else 2
                    self.state = f'Attack{self.last_attack}'
                    self.update_image(ENEMY_ANIMATION[self.name][self.state])
                elif self.animation_index == len(self.animation_frames) - 1:
                    self.state = 'Walk'
            elif dist > 0:
                self.rect.centerx -= ENTITY_SPEED[self.name]
            else:
                self.rect.centerx += ENTITY_SPEED[self.name]
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if moving:
            if self.state != 'Walk':
                self.state = 'Walk'
                self.update_image(ENEMY_ANIMATION[self.name][self.state])
                
        if self.damage_cooldown > 0:
            self.damage_cooldown -= 1
                
        self.animate()

    def shoot(self):
        return None

    def get_hitbox(self):
        hitbox = self.rect.copy()
        hitbox.width = int(self.rect.width * 0.7)
        hitbox.left = self.rect.left + int(self.rect.width * 0.15)
        hitbox.height = int(self.rect.height * 0.85)
        hitbox.top = self.rect.top + int(self.rect.height * 0.15)
        return hitbox
