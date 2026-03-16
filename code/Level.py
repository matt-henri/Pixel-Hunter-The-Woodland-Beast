#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL, C_BLACK, C_LIGHT_GREEN, C_LIGHT_CYAN
from code.Background import Background
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.enemies_spawned = 0
        self.enemies_killed = 0
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        self.entity_list.append(player)
        self.scrolled_distance = 0
        self.player_dead_time = 0
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self):
        try:
            pygame.mixer_music.load(f'./asset/{self.name}.mp3')
            pygame.mixer_music.set_volume(0.3)
            pygame.mixer_music.play(-1)
        except pygame.error:
            print(f"Warning: Could not load music for {self.name}")
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            
            global_scroll = 0
            parallax_scroll = 0
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    if ent.state != 'Dead':
                        ent.move()
                    else:
                        ent.animate()
                    
                    if hasattr(ent, 'global_scroll'):
                        global_scroll = max(global_scroll, ent.global_scroll)
                    if hasattr(ent, 'step_scroll'):
                        if abs(ent.step_scroll) > abs(parallax_scroll):
                            parallax_scroll = ent.step_scroll

            if global_scroll > 0:
                self.scrolled_distance += global_scroll

            spawn_threshold = 200
            if self.scrolled_distance >= spawn_threshold:
                self.scrolled_distance -= spawn_threshold
                if self.enemies_spawned < 15:
                    if (self.enemies_spawned + 1) % 3 == 0:
                        choice = 'Enemy3'
                    else:
                        choice = 'Enemy1'
                    self.entity_list.append(EntityFactory.get_entity(choice))
                    self.enemies_spawned += 1

            p1_rect = next((p.rect for p in self.entity_list if isinstance(p, Player) and p.name == 'Player1'), None)
            for ent in self.entity_list:
                if isinstance(ent, Enemy):
                    ent.move(player_rect=p1_rect, global_scroll=global_scroll)
                elif isinstance(ent, Background):
                    ent.move(global_scroll=parallax_scroll)
                elif not isinstance(ent, Player): # Shots
                    ent.move()
                
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                
                if ent.name == 'Player1':
                    self.level_text(20, f'Player1 - Vida: {"♥" * ent.health} | Kills: {self.enemies_killed}/15', C_LIGHT_GREEN, (10, 30))
                if ent.name == 'Player2':
                    self.level_text(20, f'Player2 - Vida: {"♥" * ent.health} | Kills: {self.enemies_killed}/15', C_LIGHT_CYAN, (10, 55))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player):
                                if self.enemies_killed < 15:
                                    ent.health = 0
                        
                        if self.enemies_killed >= 15:
                            return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                        if ent.health <= 0 and self.player_dead_time == 0:
                            self.player_dead_time = pygame.time.get_ticks()

                if not found_player:
                    if self.player_dead_time > 0 and pygame.time.get_ticks() - self.player_dead_time > 3000:
                        return False
                    elif self.player_dead_time == 0:
                        self.player_dead_time = pygame.time.get_ticks()

            self.level_text(20, f'{self.name} - Tempo: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            
            enemies_before = sum(1 for e in self.entity_list if isinstance(e, Enemy))
            EntityMediator.verify_health(entity_list=self.entity_list)
            enemies_after = sum(1 for e in self.entity_list if isinstance(e, Enemy))
            self.enemies_killed += (enemies_before - enemies_after)

            if self.enemies_killed >= 15:
                return True

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        if "♥" in text:
            text_font = pygame.font.SysFont(name="Arial", size=text_size)
        shadow_surf: Surface = text_font.render(text, True, C_BLACK).convert_alpha()
        shadow_rect: Rect = shadow_surf.get_rect(left=text_pos[0] + 1, top=text_pos[1] + 1)
        self.window.blit(source=shadow_surf, dest=shadow_rect)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
