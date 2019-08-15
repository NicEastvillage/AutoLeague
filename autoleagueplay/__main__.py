"""AutoLeague

Usage:
    autoleagueplay (odd | even | bubble) <ladder> [--replays=R] [--teamsize=T] [--list|--results]
    autoleagueplay (-h | --help)
    autoleagueplay --version

Options:
    --replays=R                  What to do with the replays of the match. Valid values are 'save', and 'calculated_gg'. [default: calculated_gg]
    --teamsize=T                 How many players per team. [default: 1]
    --list                       Instead of playing the matches, the list of matches is printed.
    --results                    Like --list but also shows the result of matches that has been played.
    -h --help                    Show this screen.
    --version                    Show version.
"""

import sys
from pathlib import Path

from docopt import docopt

from autoleagueplay.bubble_sort import run_bubble_sort
from autoleagueplay.list_matches import list_matches
from autoleagueplay.paths import WorkingDir
from autoleagueplay.replays import ReplayPreference
from autoleagueplay.run_matches import run_league_play
from autoleagueplay.version import __version__


def main():
    arguments = docopt(__doc__, version=__version__)

    ladder_path = Path(arguments['<ladder>'])
    if not ladder_path.exists():
        print(f'\'{ladder_path}\' does not exist.')
        sys.exit(1)

    working_dir = WorkingDir(ladder_path)

    replay_preference = ReplayPreference(arguments['--replays'])
    team_size = int(arguments['--teamsize'])

    if arguments['bubble']:
        run_bubble_sort(working_dir, team_size, replay_preference)
    elif arguments['odd'] or arguments['even']:
        if arguments['--results']:
            list_matches(working_dir, arguments['odd'], True)
        elif arguments['--list']:
            list_matches(working_dir, arguments['odd'], False)
        else:
            run_league_play(working_dir, arguments['odd'], replay_preference, team_size)
    else:
        raise NotImplementedError()


if __name__ == '__main__':
    main()
