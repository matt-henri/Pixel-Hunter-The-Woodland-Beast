#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_ORANGE, C_WHITE, C_YELLOW, C_BLACK


class Victory:
    def __init__(self, window):
        self.window = window
        try:
            self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        except FileNotFoundError:
            self.surf = pygame.image.load('./asset/7.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        try:
            pygame.mixer_music.load('./asset/Menu.mp3')
            pygame.mixer_music.play(-1)
        except pygame.error:
            pass
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Você Venceu!!", C_YELLOW, ((WIN_WIDTH / 2), WIN_HEIGHT / 2 - 110))
            self.menu_text(30, "A Floresta está Segura!", C_YELLOW, ((WIN_WIDTH / 2), WIN_HEIGHT / 2 - 70))

            self.menu_text(30, "Enter - Para voltar para o Menu", C_WHITE, ((WIN_WIDTH / 2), WIN_HEIGHT - 40))
            
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        # Sombra
        shadow_surf: Surface = text_font.render(text, True, C_BLACK).convert_alpha()
        shadow_rect: Rect = shadow_surf.get_rect(center=(text_center_pos[0] + 2, text_center_pos[1] + 2))
        self.window.blit(source=shadow_surf, dest=shadow_rect)

        # Texto principal
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
