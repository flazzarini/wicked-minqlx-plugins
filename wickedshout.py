# minqlx plugin
# Copyright (C) 2015 Mino <mino@minomino.org>

import minqlx

from minqlx.database import Redis


class wickedshout(minqlx.Plugin):
    """
    # TODO add docstring
    """
    database = Redis

    def __init__(self):
        super().__init__()
        self._mapping = None  # Cached variable (set in self.mapping property)

        self.add_command("shout", self.shout)
        self.add_command("shoutlist", self.shoutlist)

    def shout(self, player, msg, channel):
        """
        Handle shout command
        """
        shout_pack = msg[1]
        shout_sound = msg[2]

        sound_path = self.mapping.get(shout_pack, {}).get(shout_sound)

        if not sound_path:
            channel.reply(
                "Shout sound ^2%s^7 for shout_pack ^2%s^7 was not found, "
                "please use ^2!shoutlist^7 to list all available shouts" % (
                    shout_sound, shout_pack))
            return

        channel.reply("Player ^3%s^7 shouts ^2%s %s^7" % (
            player, shout_pack, shout_sound))
        self.play_sound(sound_path)
        return

    def shoutlist(self, player, msg, channel):
        """
        Print Shoutlist to player
        """
        output = []
        for shout_pack in sorted(self.mapping.keys()):
            output.append("^5%s^7\n" % shout_pack)
            output.append("^5%s^7\n" % ("=" * len(shout_pack)))

            shout_sounds = []
            for shout_sound in sorted(self.mapping.get(shout_pack).keys()):
                shout_sounds.append("^6%s^7 " % shout_sound)

                if len("".join(shout_sounds)) >= 120:
                    shout_sounds.append("\n")
            output += shout_sounds
            output.append("\n\n")

        output.append(
            "\n\nExample Usage: ^3\\say !shout wickedq1-badblood 02^7")

        player.tell("".join(output))

    def play_sound(self, path):
        """
        Plays sound stored in `path`
        """
        for p in self.players():
            super().play_sound(path, p)

    @property
    def mapping(self):
        if self._mapping:
            return self._mapping

        self._mapping = {
            'wickedq1-badblood': {
                '01': 'sound/wicked/characters/BadBlood/01.ogg',
                '02': 'sound/wicked/characters/BadBlood/02.ogg',
                '03': 'sound/wicked/characters/BadBlood/03.ogg',
                '04': 'sound/wicked/characters/BadBlood/04.ogg',
                '05': 'sound/wicked/characters/BadBlood/05.ogg',
                '06': 'sound/wicked/characters/BadBlood/06.ogg',
                '07': 'sound/wicked/characters/BadBlood/07.ogg',
                '08': 'sound/wicked/characters/BadBlood/08.ogg',
                '09': 'sound/wicked/characters/BadBlood/09.ogg',
                '10': 'sound/wicked/characters/BadBlood/10.ogg',
                '11': 'sound/wicked/characters/BadBlood/11.ogg',
                '12': 'sound/wicked/characters/BadBlood/12.ogg',
            },
            'wickedq1-buzz': {
                '01': 'sound/wicked/characters/Buzz/01.ogg',
                '02': 'sound/wicked/characters/Buzz/02.ogg',
                '03': 'sound/wicked/characters/Buzz/03.ogg',
                '04': 'sound/wicked/characters/Buzz/04.ogg',
                '05': 'sound/wicked/characters/Buzz/05.ogg',
                '06': 'sound/wicked/characters/Buzz/06.ogg',
                '07': 'sound/wicked/characters/Buzz/07.ogg',
                '08': 'sound/wicked/characters/Buzz/08.ogg',
                '09': 'sound/wicked/characters/Buzz/09.ogg',
                '10': 'sound/wicked/characters/Buzz/10.ogg',
                '11': 'sound/wicked/characters/Buzz/11.ogg',
                '12': 'sound/wicked/characters/Buzz/12.ogg',
            },
            'wickedq1-darthvader': {
                '01': 'sound/wicked/characters/DarthVader/01.ogg',
                '02': 'sound/wicked/characters/DarthVader/02.ogg',
                '03': 'sound/wicked/characters/DarthVader/03.ogg',
                '04': 'sound/wicked/characters/DarthVader/04.ogg',
                '05': 'sound/wicked/characters/DarthVader/05.ogg',
                '06': 'sound/wicked/characters/DarthVader/06.ogg',
                '07': 'sound/wicked/characters/DarthVader/07.ogg',
                '08': 'sound/wicked/characters/DarthVader/08.ogg',
                '09': 'sound/wicked/characters/DarthVader/09.ogg',
                '10': 'sound/wicked/characters/DarthVader/10.ogg',
                '11': 'sound/wicked/characters/DarthVader/11.ogg',
                '12': 'sound/wicked/characters/DarthVader/12.ogg',
            },
            'wickedq1-docholiday': {
                '01': 'sound/wicked/characters/DocHoliday/01.ogg',
                '02': 'sound/wicked/characters/DocHoliday/02.ogg',
                '03': 'sound/wicked/characters/DocHoliday/03.ogg',
                '04': 'sound/wicked/characters/DocHoliday/04.ogg',
                '05': 'sound/wicked/characters/DocHoliday/05.ogg',
                '06': 'sound/wicked/characters/DocHoliday/06.ogg',
                '07': 'sound/wicked/characters/DocHoliday/07.ogg',
                '08': 'sound/wicked/characters/DocHoliday/08.ogg',
                '09': 'sound/wicked/characters/DocHoliday/09.ogg',
                '10': 'sound/wicked/characters/DocHoliday/10.ogg',
                '11': 'sound/wicked/characters/DocHoliday/11.ogg',
                '12': 'sound/wicked/characters/DocHoliday/12.ogg',
            },
            'wickedq1-moses': {
                '01': 'sound/wicked/characters/Moses/01.ogg',
                '02': 'sound/wicked/characters/Moses/02.ogg',
                '03': 'sound/wicked/characters/Moses/03.ogg',
                '04': 'sound/wicked/characters/Moses/04.ogg',
                '05': 'sound/wicked/characters/Moses/05.ogg',
                '06': 'sound/wicked/characters/Moses/06.ogg',
                '07': 'sound/wicked/characters/Moses/07.ogg',
                '08': 'sound/wicked/characters/Moses/08.ogg',
                '09': 'sound/wicked/characters/Moses/09.ogg',
                '10': 'sound/wicked/characters/Moses/10.ogg',
                '11': 'sound/wicked/characters/Moses/11.ogg',
                '12': 'sound/wicked/characters/Moses/12.ogg',
            },
            'wickedq1-peedee': {
                '01': 'sound/wicked/characters/Peedee/01.ogg',
                '02': 'sound/wicked/characters/Peedee/02.ogg',
                '03': 'sound/wicked/characters/Peedee/03.ogg',
                '04': 'sound/wicked/characters/Peedee/04.ogg',
                '05': 'sound/wicked/characters/Peedee/05.ogg',
                '06': 'sound/wicked/characters/Peedee/06.ogg',
                '07': 'sound/wicked/characters/Peedee/07.ogg',
                '08': 'sound/wicked/characters/Peedee/08.ogg',
                '09': 'sound/wicked/characters/Peedee/09.ogg',
                '10': 'sound/wicked/characters/Peedee/10.ogg',
                '11': 'sound/wicked/characters/Peedee/11.ogg',
                '12': 'sound/wicked/characters/Peedee/12.ogg',
            },
            'wickedq1-scavenger': {
                '01': 'sound/wicked/characters/Scavenger/01.ogg',
                '02': 'sound/wicked/characters/Scavenger/02.ogg',
                '03': 'sound/wicked/characters/Scavenger/03.ogg',
                '04': 'sound/wicked/characters/Scavenger/04.ogg',
                '05': 'sound/wicked/characters/Scavenger/05.ogg',
                '06': 'sound/wicked/characters/Scavenger/06.ogg',
                '07': 'sound/wicked/characters/Scavenger/07.ogg',
                '08': 'sound/wicked/characters/Scavenger/08.ogg',
                '09': 'sound/wicked/characters/Scavenger/09.ogg',
                '10': 'sound/wicked/characters/Scavenger/10.ogg',
                '11': 'sound/wicked/characters/Scavenger/11.ogg',
                '12': 'sound/wicked/characters/Scavenger/12.ogg',
            },
            'wickedq1-syndrome': {
                '01': 'sound/wicked/characters/Syndrome/01.ogg',
                '02': 'sound/wicked/characters/Syndrome/02.ogg',
                '03': 'sound/wicked/characters/Syndrome/03.ogg',
                '04': 'sound/wicked/characters/Syndrome/04.ogg',
                '05': 'sound/wicked/characters/Syndrome/05.ogg',
                '06': 'sound/wicked/characters/Syndrome/06.ogg',
                '07': 'sound/wicked/characters/Syndrome/07.ogg',
                '08': 'sound/wicked/characters/Syndrome/08.ogg',
                '09': 'sound/wicked/characters/Syndrome/09.ogg',
                '10': 'sound/wicked/characters/Syndrome/10.ogg',
                '11': 'sound/wicked/characters/Syndrome/11.ogg',
                '12': 'sound/wicked/characters/Syndrome/12.ogg',
            },
            'wickedq1-thelord': {
                '01': 'sound/wicked/characters/TheLord/01.ogg',
                '02': 'sound/wicked/characters/TheLord/02.ogg',
                '03': 'sound/wicked/characters/TheLord/03.ogg',
                '04': 'sound/wicked/characters/TheLord/04.ogg',
                '05': 'sound/wicked/characters/TheLord/05.ogg',
                '06': 'sound/wicked/characters/TheLord/06.ogg',
                '07': 'sound/wicked/characters/TheLord/07.ogg',
                '08': 'sound/wicked/characters/TheLord/08.ogg',
                '09': 'sound/wicked/characters/TheLord/09.ogg',
                '10': 'sound/wicked/characters/TheLord/10.ogg',
                '11': 'sound/wicked/characters/TheLord/11.ogg',
                '12': 'sound/wicked/characters/TheLord/12.ogg',
            },
            'wickedq1-wotan': {
                '01': 'sound/wicked/characters/Wotan/01.ogg',
                '02': 'sound/wicked/characters/Wotan/02.ogg',
                '03': 'sound/wicked/characters/Wotan/03.ogg',
                '04': 'sound/wicked/characters/Wotan/04.ogg',
                '05': 'sound/wicked/characters/Wotan/05.ogg',
                '06': 'sound/wicked/characters/Wotan/06.ogg',
                '07': 'sound/wicked/characters/Wotan/07.ogg',
                '08': 'sound/wicked/characters/Wotan/08.ogg',
                '09': 'sound/wicked/characters/Wotan/09.ogg',
                '10': 'sound/wicked/characters/Wotan/10.ogg',
                '11': 'sound/wicked/characters/Wotan/11.ogg',
                '12': 'sound/wicked/characters/Wotan/12.ogg',
            },
            'officespace': {
                'diemothafuckas': 'sound/westcoastcrew/diemothafuckas.ogg',
            }
        }
        return self._mapping
