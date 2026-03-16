#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY, PLAYER_ANIMATION, GROUND_Y
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.state = 'Idle'
        self.vertical_velocity = 0
        self.gravity = 0.5
        self.jump_force = -10
        self.is_jumping = False
        self.step_scroll = 0
        self.update_image(PLAYER_ANIMATION[self.name][self.state])
        self.rect.bottom = GROUND_Y

    def move(self):
        self.global_scroll = 0
        self.step_scroll = 0
        pressed_key = pygame.key.get_pressed()
        moving = False
        
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
            self.step_scroll = -ENTITY_SPEED[self.name]
            moving = True
        if pressed_key[PLAYER_KEY_RIGHT[self.name]]:
            if self.rect.centerx >= WIN_WIDTH / 2:
                self.global_scroll = ENTITY_SPEED[self.name]
            else:
                self.rect.centerx += ENTITY_SPEED[self.name]
            self.step_scroll = ENTITY_SPEED[self.name]
            moving = True
        if self.health <= 0:
            if self.state != 'Dead':
                self.state = 'Dead'
                self.update_image(PLAYER_ANIMATION[self.name][self.state])
            self.animate()
            return

        if pressed_key[PLAYER_KEY_UP[self.name]] and not self.is_jumping:
            self.is_jumping = True
            self.vertical_velocity = self.jump_force
        if self.is_jumping:
            self.rect.centery += self.vertical_velocity
            self.vertical_velocity += self.gravity
            if self.rect.bottom >= GROUND_Y:
                self.rect.bottom = GROUND_Y
                self.is_jumping = False
                self.vertical_velocity = 0
        if self.is_jumping:
            new_state = 'Jump'
        else:
            new_state = 'Walk' if moving else 'Idle'
            
        if self.state != 'Attack' and self.state != new_state:
            self.state = new_state
            self.update_image(PLAYER_ANIMATION[self.name][self.state])
        
        if self.state in ['Walk', 'Jump']:
            self.animate()

    def shoot(self):
        if self.health <= 0:
            return None

        self.shot_delay -= 1
        if self.shot_delay <= 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                if self.state != 'Attack':
                    self.state = 'Attack'
                    self.update_image(PLAYER_ANIMATION[self.name]['Attack'])
                self.animate()
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
            else:
                if self.state == 'Attack':
                    self.state = 'Idle'
                    self.update_image(PLAYER_ANIMATION[self.name]['Idle'])
                return None
            return None
        else:
            if self.state == 'Attack':
                self.animate()
            return None

    def get_hitbox(self):
        hitbox = self.rect.copy()
        hitbox.width = int(self.rect.width * 0.4)
        hitbox.left = self.rect.left + int(self.rect.width * 0.3)
        hitbox.height = int(self.rect.height * 0.7)
        hitbox.top = self.rect.top + int(self.rect.height * 0.3)
        return hitbox
