from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            hb1 = ent1.get_hitbox()
            hb2 = ent2.get_hitbox()
            if (hb1.right >= hb2.left and
                    hb1.left <= hb2.right and
                    hb1.bottom >= hb2.top and
                    hb1.top <= hb2.bottom):
                
                if isinstance(ent1, Enemy) and isinstance(ent2, Player):
                    if ent1.damage_cooldown == 0:
                        ent2.health -= ent1.damage
                        ent2.last_dmg = ent1.name
                        ent1.damage_cooldown = 60
                elif isinstance(ent2, Enemy) and isinstance(ent1, Player):
                    if ent2.damage_cooldown == 0:
                        ent1.health -= ent2.damage
                        ent1.last_dmg = ent2.name
                        ent2.damage_cooldown = 60
                else:
                    ent1.health -= ent2.damage
                    ent2.health -= ent1.damage
                    ent1.last_dmg = ent2.name
                    ent2.last_dmg = ent1.name

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list[:]:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    if hasattr(ent, 'state') and ent.state == 'Dead':
                        if ent.animation_index == len(ent.animation_frames) - 1:
                            entity_list.remove(ent)
                elif isinstance(ent, Player):
                    if ent.state == 'Dead':
                        if ent.animation_index == len(ent.animation_frames) - 1:
                            entity_list.remove(ent)
                else:
                    entity_list.remove(ent)
