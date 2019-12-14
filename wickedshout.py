from collections import namedtuple
from datetime import datetime
from os.path import join
from random import choice
from typing import Optional, List

import minqlx
from minqlx.database import Redis


class Shout(namedtuple('Shout', ['pack', 'alias', 'simplified_path'])):
    PREFIX_PATH = 'sound/wicked'

    @property
    def path(self) -> str:
        if not self.simplified_path.startswith('sound/wicked'):
            return join(self.PREFIX_PATH, self.simplified_path)
        return self.simplified_path


class Shoutdb:
    DB = {}

    def register_shouts(self, shouts: List[Shout]) -> None:
        """
        Loops and delegates to self.register
        """
        for shout in shouts:
            self.register(shout)

    def register(self, shout: Shout) -> None:
        """
        Registers a new Shout to the "database"
        """
        if shout.pack not in self.DB:
            self.DB[shout.pack] = {}

        self.DB[shout.pack.lower()][shout.alias.lower()] = shout

    def get_shout(self, shout_pack: str, shout_alias: str) -> Optional[Shout]:
        """
        Retrieve matching shout from the "database"
        """
        return self.DB.get(shout_pack, {}).get(shout_alias)

    def get_random_shout(self) -> Optional[Shout]:
        """
        Get a random shout, by default return a standard sound
        """
        if not self.DB:
            return Shout('default', 'quakelive',
                         'sound/player/razor/taunt.wav')

        pack = choice(self.get_shout_packs())
        chosen_shout = choice(self.get_shouts_in_pack(pack))
        return chosen_shout

    def get_shout_packs(self) -> List[str]:
        """
        Get a list of available shout packs
        """
        return list(self.DB.keys())

    def get_shouts_in_pack(self, shout_pack: str) -> List[Shout]:
        """
        Returns a list of shouts for a given shout_pack
        """
        if shout_pack not in self.DB:
            return []

        return list(self.DB[shout_pack].values())


class wickedshout(minqlx.Plugin):
    """
    # TODO add docstring
    """
    database = Redis

    def __init__(self):
        super().__init__()
        self.shoutdb = Shoutdb()
        self.register_shouts()

        self.add_command("shout", self.shout)
        self.add_command("shoutlist", self.shoutlist)
        self.add_command("shoutrandom", self.shoutrandom)

    def shout(self, player, msg, channel):
        """
        Handle shout command
        """
        shout_pack = msg[1]
        shout_sound = msg[2]

        shout = self.shoutdb.get_shout(shout_pack, shout_sound)

        if not shout:
            channel.reply(
                "Shout sound ^2%s^7 for shout_pack ^2%s^7 was not found, "
                "please use ^2!shoutlist^7 to list all available shouts" % (
                    shout_sound, shout_pack))
            return

        self.play_sound(channel, player, shout)
        return

    def shoutrandom(self, player, msg, channel):
        """
        Shouts a random shout
        """
        random_shout = self.shoutdb.get_random_shout()
        self.play_sound(channel, player, random_shout)
        return

    def shoutlist(self, player, msg, channel):
        """
        Print Shoutlist to player
        """
        output = []
        for shout_pack in sorted(self.shoutdb.get_shout_packs()):
            output.append("^5%s^7\n" % shout_pack)
            output.append("^5%s^7\n" % ("=" * len(shout_pack)))

            shout_aliases = []
            for shout in sorted(self.shoutdb.get_shouts_in_pack(shout_pack)):
                shout_aliases.append("^6%s^7 " % shout.alias)

                if len("".join(shout_aliases)) >= 120:
                    shout_aliases.append("\n")
            output += shout_aliases
            output.append("\n\n")

        output.append(
            "\n\nExample Usage: ^3\\say !shout wickedq1-badblood 02^7")
        output.append(
            "\n\nShout a random sound: ^3\\say !shoutrandom^7")

        player.tell("".join(output))

    def play_sound(self, channel, player, shout):
        """
        Plays sound stored in `path`
        """
        if not self.player_is_allowed(player):
            player.tell("^1Stop shouting for a few seconds^7")
            return

        channel.reply("Player ^3%s^7 shouts ^2%s %s^7" % (
            player, shout.pack, shout.alias))

        for p in self.players():
            super().play_sound(shout.path, p)

    def player_is_allowed(self, player):
        """
        Verifies if player has shouted in the last 2 seconds
        """
        player_key = "wickedshout_last_%s" % player.steam_id
        if player_key in self.db:
            last_played = float(self.db[player_key])
            now = datetime.now().timestamp()
            if (now - last_played) < 2.0:
                return False

        self.db[player_key] = datetime.now().timestamp()
        return True

    def register_shouts(self):
        """
        Registers shouts in our local instance of `Shoutdb`
        """
        characters = [
            'Badblood', 'Buzz', 'DarthVader',
            'DocHoliday', 'Moses', 'Peedee',
            'TheLord', 'Scavenger', 'Wotan'
        ]
        char_shouts = []
        for character in characters:
            for index in range(1, 13):
                char_shouts.append(
                    Shout(
                        'wickedq1-%s' % character.lower(),
                        '%02d' % index,
                        'characters/%s/%02d.ogg' % (character, index)))

        self.shoutdb.register_shouts(char_shouts)
        self.shoutdb.register_shouts([
            Shout('5thelement', 'omg', 'shouts/5th/omg.ogg'),
            Shout('5thelement', 'pipolei', 'shouts/5th/pipolei.ogg'),
            Shout('5thelement', 'supergreen', 'shouts/5th/super_green.ogg'),

            Shout('aliens', 'gameover', 'shouts/aliens/game_over.ogg'),
            Shout('aliens', 'ready', 'shouts/aliens/ready_to_get_it_on.ogg'),
            Shout('aliens', 'stop', 'shouts/aliens/stop_your_grinnin.ogg'),
            Shout('aliens', 'badass', 'shouts/aliens/ultimate_badass.ogg'),

            Shout('aod', 'arrogance', 'shouts/aod/arrogance.ogg'),
            Shout('aod', 'boomstick', 'shouts/aod/boomstick.ogg'),
            Shout('aod', 'comegetsome', 'shouts/aod/comegetsome.ogg'),
            Shout('aod', 'cometopappa', 'shouts/aod/cometopappa.ogg'),
            Shout('aod', 'fancypants', 'shouts/aod/fancypants.ogg'),
            Shout('aod', 'groovy', 'shouts/aod/groovy.ogg'),
            Shout('aod', 'guywithgun', 'shouts/aod/guywithgun.ogg'),
            Shout('aod', 'killkiss', 'shouts/aod/killkiss.ogg'),
            Shout('aod', 'laughter', 'shouts/aod/laughter.ogg'),
            Shout('aod', 'liveagain', 'shouts/aod/liveagain.ogg'),
            Shout('aod', 'miserable', 'shouts/aod/miserable.ogg'),
            Shout('aod', 'run', 'shouts/aod/run.ogg'),
            Shout('aod', 'shopsmart', 'shouts/aod/shopsmart.ogg'),

            Shout('apo', 'napalm', 'shouts/apo/napalm.ogg'),

            Shout('badtaste', 'bastard', 'shouts/badtaste/bastard.ogg'),
            Shout('badtaste', 'bastards', 'shouts/badtaste/bastards.ogg'),
            Shout('badtaste', 'bornagain', 'shouts/badtaste/bornagain.ogg'),
            Shout('badtaste', 'eatlead', 'shouts/badtaste/eatlead.ogg'),
            Shout('badtaste', 'getya', 'shouts/badtaste/getya.ogg'),
            Shout('badtaste', 'holyshit', 'shouts/badtaste/holyshit.ogg'),
            Shout('badtaste', 'lunch', 'shouts/badtaste/lunch.ogg'),
            Shout('badtaste', 'suckmyspinning', 'shouts/badtaste/suckmyspinning.ogg'),  # noqa

            Shout('braindead', 'devine', 'shouts/braindead/devine_intervention.ogg'),  # noqa
            Shout('braindead', 'forthelord', 'shouts/braindead/i_kick_ass_for_the_lord.ogg'),  # noqa
            Shout('braindead', 'mental', 'shouts/braindead/mental.ogg'),
            Shout('braindead', 'nopudding', 'shouts/braindead/no_pudding.ogg'),
            Shout('braindead', 'partyover', 'shouts/braindead/party_is_over.ogg'),  # noqa
            Shout('braindead', 'whatdoyouwant', 'shouts/braindead/what_do_you_want.ogg'),  # noqa
            Shout('braindead', 'whatingodsname', 'shouts/braindead/what_in_gods_name.ogg'),  # noqa

            Shout('cestarriver', 'bienfait', 'shouts/carriver/bien_fait.ogg'),
            Shout('cestarriver', 'pourrire', 'shouts/carriver/c_est_pour_rire.ogg'),  # noqa
            Shout('cestarriver', 'enmerde', 'shouts/carriver/je_temerde.ogg'),  # noqa

            Shout('frighteners', 'graves', 'shouts/fright/get_back_in_your_graves.ogg'),  # noqa
            Shout('frighteners', 'liestill', 'shouts/fright/lie_still_like_that.ogg'),  # noqa
            Shout('frighteners', 'numberone', 'shouts/fright/number_one.ogg'),
            Shout('frighteners', 'omg', 'shouts/fright/omg.ogg'),
            Shout('frighteners', 'wickedpunished', 'shouts/fright/wicked_punished.ogg'),  # noqa
            Shout('frighteners', 'youngandbeautiful', 'shouts/fright/young_and_beautiful.ogg'),  # noqa

            Shout('officespace', 'cursing', 'shouts/officespace/cursing.ogg'),
            Shout('officespace', 'fuckinga', 'shouts/officespace/fuckinga.ogg'),  # noqa
            Shout('officespace', 'happening', 'shouts/officespace/happening.ogg'),  # noqa
            Shout('officespace', 'mmyahh', 'shouts/officespace/mmhyahh.ogg'),
            Shout('officespace', 'mondays', 'shouts/officespace/mondays.ogg'),
            Shout('officespace', 'ohyahh', 'shouts/officespace/ohyahh.ogg'),
            Shout('officespace', 'terrific', 'shouts/officespace/terrific.ogg'),  # noqa
            Shout('officespace', 'uhyahh', 'shouts/officespace/uhyahh.ogg'),

            Shout('wasabi', 'bordelle', 'shouts/wasabi/bordelle.ogg'),
            Shout('wasabi', 'nonnon', 'shouts/wasabi/nonnon.ogg'),
            Shout('wasabi', 'piercing', 'shouts/wasabi/piercing.ogg'),
            Shout('wasabi', 'voila', 'shouts/wasabi/voila.ogg'),

            Shout('werner', 'lassmich', 'shouts/werner/lass_mich_mol_rann_loa.ogg'),  # noqa
            Shout('werner', 'neeneenee', 'shouts/werner/nee_nee_nee.ogg'),
            Shout('werner', 'russen', 'shouts/werner/russen.ogg'),
        ])
