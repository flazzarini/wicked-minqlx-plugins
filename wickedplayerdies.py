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
            "sound/wickedgamesounds/badtaste_bastard.ogg",
            "sound/wickedgamesounds/badtaste_mamie.ogg",
            "sound/wickedgamesounds/fright-wicked_punished.ogg",
            "sound/wickedgamesounds/mk-toasty.ogg",
            "sound/wickedgamesounds/ms-okay.ogg",
            "sound/wickedgamesounds/os-mmhyahh.ogg",
            "sound/wickedgamesounds/os-mondays.ogg",
            "sound/wickedgamesounds/os-ohyahh.ogg",
            "sound/wickedgamesounds/os-uhyahh.ogg",
            "sound/wickedgamesounds/os-yahh.ogg",
            "sound/wickedgamesounds/pf-big_kahuna_burger.ogg",
            "sound/wickedgamesounds/pf-break_concentration.ogg",
            "sound/wickedgamesounds/pf-dead_as_dead.ogg",
            "sound/wickedgamesounds/pf-gourmet_shit.ogg",
            "sound/wickedgamesounds/pf-tasty_burger.ogg",
            "sound/wickedgamesounds/quake-gib1.ogg",
            "sound/wickedgamesounds/quake-gib2.ogg",
            "sound/wickedgamesounds/sw-ootanee.ogg",
            "sound/wickedgamesounds/wickedquake-death1.ogg",
            "sound/wickedgamesounds/wickedquake-death2.ogg",
            "sound/wickedgamesounds/wickedquake-death3.ogg",
            "sound/wickedgamesounds/wickedquake-death4.ogg",
            "sound/wickedgamesounds/wickedquake-death5.ogg",
            "sound/wickedgamesounds/wickedquake-death6.ogg",
            "sound/wickedgamesounds/wickedquake-death7.ogg",
            "sound/wickedgamesounds/wickedquake-death8.ogg",
            "sound/wickedgamesounds/wickedquake-gib1.ogg",
            "sound/wickedgamesounds/wickedquake-gib2.ogg",
            "sound/wickedgamesounds/wickedquake-gib3.ogg",
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
