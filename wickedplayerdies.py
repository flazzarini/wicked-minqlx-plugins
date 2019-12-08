# minqlx plugin
# Copyright (C) 2015 Mino <mino@minomino.org>

import minqlx
from random import choice


class wickedplayerdies(minqlx.Plugin):
    """
    Whenever a player dies this plugin takes care of playing a random sound.

    In order for this plugin to work please make sure you have the following
    sound packs (steam workshop items) installed

        - 1931426635 (The Wicked Net - Game Sounds)
    """
    def __init__(self):
        super().__init__()
        self.add_hook("death", self.handle_death)

        self.death_sounds = [
            "sound/wicked/gamesounds/badtaste_bastard.ogg",
            "sound/wicked/gamesounds/badtaste_mamie.ogg",
            "sound/wicked/gamesounds/fright-wicked_punished.ogg",
            "sound/wicked/gamesounds/mk-toasty.ogg",
            "sound/wicked/gamesounds/ms-okay.ogg",
            "sound/wicked/gamesounds/os-mmhyahh.ogg",
            "sound/wicked/gamesounds/os-mondays.ogg",
            "sound/wicked/gamesounds/os-ohyahh.ogg",
            "sound/wicked/gamesounds/os-uhyahh.ogg",
            "sound/wicked/gamesounds/os-yahh.ogg",
            "sound/wicked/gamesounds/pf-big_kahuna_burger.ogg",
            "sound/wicked/gamesounds/pf-break_concentration.ogg",
            "sound/wicked/gamesounds/pf-dead_as_dead.ogg",
            "sound/wicked/gamesounds/pf-gourmet_shit.ogg",
            "sound/wicked/gamesounds/pf-tasty_burger.ogg",
            "sound/wicked/gamesounds/quake-gib1.ogg",
            "sound/wicked/gamesounds/quake-gib2.ogg",
            "sound/wicked/gamesounds/sw-ootanee.ogg",
            "sound/wicked/gamesounds/wickedquake-death1.ogg",
            "sound/wicked/gamesounds/wickedquake-death2.ogg",
            "sound/wicked/gamesounds/wickedquake-death3.ogg",
            "sound/wicked/gamesounds/wickedquake-death4.ogg",
            "sound/wicked/gamesounds/wickedquake-death5.ogg",
            "sound/wicked/gamesounds/wickedquake-death6.ogg",
            "sound/wicked/gamesounds/wickedquake-death7.ogg",
            "sound/wicked/gamesounds/wickedquake-death8.ogg",
            "sound/wicked/gamesounds/wickedquake-gib1.ogg",
            "sound/wicked/gamesounds/wickedquake-gib2.ogg",
            "sound/wicked/gamesounds/wickedquake-gib3.ogg",
        ]

    def handle_death(self, player, msg, channel):
        """
        Plays a random sound when someone dies
        """
        sound_to_play = choice(self.death_sounds)
        self.play_sound(sound_to_play)

    def play_sound(self, path):
        for p in self.players():
            super().play_sound(path, p)
