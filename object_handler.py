from sprite_object import *
from npc import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/cyber_demon/'
        self.static_sprite_path = 'resources/textures/Spites/stil_sprite/'
        self.anim_sprite_path = 'resources/textures/Spites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_position = {}

        # sprite map
        add_sprite(SpriteObject(game))      # still sprite
        add_sprite(AnimatedSprite(game))    # animated sprite
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.3)))
        add_sprite(AnimatedSprite(game, pos=(1.2, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 3.0)))
        add_sprite(AnimatedSprite(game, pos=(2.5, 3.2)))
        # new type sprite
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'eye/eye.png', pos=(14.7, 7.7)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'dead/dead.png', pos=(14.7, 1.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'Fire_1/Objects2.png', pos=(6.2, 5.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'corps/corps.png', pos=(10.2, 1.2)))

        # npc map
        add_npc(NPC(game, pos=(9.9, 2.4)))
        add_npc(NPC(game, pos=(11.5, 4.5)))
        add_npc(NPC(game, pos=(10.5, 3.5)))

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)