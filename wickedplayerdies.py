# minqlx plugin
# Copyright (C) 2015 Mino <mino@minomino.org>

import minqlx
from random import choice


class wickedplayerdies(minqlx.Plugin):
    """
    Whenever a player dies this plugin takes care of playing a random sound.

    In order for this plugin to work please make sure you have the following
    sound packs (steam workshop items) installed

        - 1733859113 (Westcoastcrew Sound Pack)
    """
    def __init__(self):
        super().__init__()
        self.add_hook("death", self.handle_death)

        self.death_sounds = [
          'sound/westcoastcrew/diemothafuckas.ogg',
          'sound/westcoastcrew/diemotherfucker.ogg',
          'sound/westcoastcrew/anotherbitesdust.ogg',
          'sound/westcoastcrew/anotheronebitesthedust.ogg',
          'sound/westcoastcrew/anotheronegone.ogg',
          'sound/westcoastcrew/boomshakalaka.ogg',
          'sound/westcoastcrew/psygib.ogg',
        ]

    def handle_death(self, player, msg, channel):
        """
        Plays a random sound when someone dies
        """
        sound_to_play = choice(self.death_sounds)
        self.play_sound(sound_to_play)

    def play_sound(self, path):
        for p in self.players():
            if self.db.get_flag(p, "essentials:sounds_enabled", default=True):
                super().play_sound(path, p)
