import logging
from typing import Tuple


class Game:
    def __init__(self, title: str, release_year: int, dat_filename: str = None, dir_filename: str = None,
                 dir_descriptor_size: int = None):
        self.title = title
        self.release_year = release_year
        self.dir_filename = dir_filename
        self.dat_filename = dat_filename
        self.dir_descriptor_size = dir_descriptor_size


class Configuration:
    def __init__(self, game: Game, ignore_warnings: bool, parse_sections: Tuple[str, ...] = None, debug=False):
        self.game = game
        self.ignore_warnings = ignore_warnings  # If False, warnings stop program execution
        self.parse_sections = () if parse_sections is None else parse_sections
        logging.basicConfig(format='%(message)s', level=logging.DEBUG if debug else logging.WARNING)
        self.debug = debug


CROC_1_PS1 = Game("Croc 1 PS1", 1997, 'CROCFILE.1', 'CROCFILE.DIR', 24)
CROC_2_PS1 = Game("Croc 2 PS1", 1999, 'CROCII.DAT', 'CROCII.DIR', 20)
CROC_2_DEMO_PS1 = Game("Croc 2 Demo PS1", 1999, 'CROCII.DAT', 'CROCII.DIR', 20)
CROC_2_DEMO_PS1_DUMMY = Game("Croc 2 Demo PS1 (Dummy)", 1999, 'DUMMY.DAT', None, None)
HARRY_POTTER_1_PS1 = Game("Harry Potter 1 PS1", 2001, 'POTTER.DAT', 'POTTER.DIR', 20)
HARRY_POTTER_2_PS1 = Game("Harry Potter 2 PS1", 2002, 'POTTER.DAT', 'POTTER.DIR', 20)

SUPPORTED_GAMES = \
    (CROC_1_PS1, CROC_2_PS1, CROC_2_DEMO_PS1, CROC_2_DEMO_PS1_DUMMY, HARRY_POTTER_1_PS1, HARRY_POTTER_2_PS1)
# Croc 1 parsing is not supported, but it can be extracted
PARSABLE_GAMES = (CROC_2_PS1, CROC_2_DEMO_PS1, CROC_2_DEMO_PS1_DUMMY, HARRY_POTTER_1_PS1, HARRY_POTTER_2_PS1)
EXTRACTABLE_GAMES = SUPPORTED_GAMES

PARSABLE_SECTIONS = ('XSPT', 'XSPS', 'XSPD', ' DNE')

wavefront_header = "# Generated by ps1_brender tools: https://github.com/OverSurge/PS1-BRender-Reverse\n"
wav_header = b"Generated by ps1_brender tools: https://github.com/OverSurge/PS1-BRender-Reverse"
