#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image
from PIL import Image

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE


class Entity(ABC):
    def __init__(self, name: str, position: tuple, size: tuple = None):
        self.name = name
        self.size = size
        self.animation_frames = []
        self.animation_index = 0
        self.animation_timer = 0
        self.animation_delay = 5

        self.update_image(name)
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        pass

    def get_hitbox(self):
        return self.rect

    def update_image(self, name: str):
        self.animation_frames = []
        full_path = f'./asset/{name}'
        if not (name.endswith('.png') or name.endswith('.gif')):
            import os
            if os.path.exists(full_path + '.gif'):
                full_path += '.gif'
            else:
                full_path += '.png'
        else:
            full_path = f'./asset/{name}'

        try:
            if full_path.endswith('.gif'):
                self.load_gif(full_path)
                if self.animation_frames:
                    self.surf = self.animation_frames[0]
            else:
                self.surf = pygame.image.load(full_path).convert_alpha()
                if self.surf.get_width() >= self.surf.get_height() * 2:
                    num_frames = self.surf.get_width() // self.surf.get_height()
                    frame_width = self.surf.get_width() // num_frames
                    frame_height = self.surf.get_height()
                    for i in range(num_frames):
                        frame = self.surf.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
                        if self.size:
                            frame = pygame.transform.scale(frame, self.size)
                        self.animation_frames.append(frame)
                    self.surf = self.animation_frames[0]
                else:
                    if self.size:
                        self.surf = pygame.transform.scale(self.surf, self.size)
                    self.animation_frames.append(self.surf)
        except (FileNotFoundError, pygame.error):
            print(f"Warning: Asset {full_path} not found. Using placeholder.")
            self.surf = pygame.Surface((32, 32))
            self.surf.fill((255, 0, 255))

        if hasattr(self, 'rect'):
            old_center = self.rect.center
            self.rect = self.surf.get_rect(center=old_center)

    def load_gif(self, filename):
        pil_image = Image.open(filename)
        if pil_image.n_frames == 1 and pil_image.width >= pil_image.height * 2:
            frame_rgba = pil_image.convert("RGBA")
            mode = frame_rgba.mode
            size = frame_rgba.size
            data = frame_rgba.tobytes()
            sheet_surf = pygame.image.fromstring(data, size, mode).convert_alpha()
            
            num_frames = pil_image.width // pil_image.height
            frame_width = pil_image.width // num_frames
            frame_height = pil_image.height
            for i in range(num_frames):
                frame_surf = sheet_surf.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
                self.animation_frames.append(frame_surf)
            return

        for frame_index in range(pil_image.n_frames):
            pil_image.seek(frame_index)
            frame_rgba = pil_image.convert("RGBA")
            mode = frame_rgba.mode
            size = frame_rgba.size
            data = frame_rgba.tobytes()
            pygame_surface = pygame.image.fromstring(data, size, mode).convert_alpha()
            self.animation_frames.append(pygame_surface)

    def animate(self):
        if len(self.animation_frames) > 1:
            self.animation_timer += 1
            if self.animation_timer >= self.animation_delay:
                self.animation_timer = 0
                self.animation_index = (self.animation_index + 1) % len(self.animation_frames)
                self.surf = self.animation_frames[self.animation_index]
