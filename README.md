# AutoLeague for League Play
[DomNomNom's Autoleague](https://github.com/DomNomNom/AutoLeague) modified to play [RLBot](http://rlbot.org/)'s Official League Play.

# How to use:

Recommended: Use [Bakkesmod](https://bakkesmod.com/) and have 'Automatically save all replays' enabled.

Installation:
- To install, clone this repo and run `pip install -e .` in the directory containing `setup.py`.
- This should give you access to the `autoleagueplay` command line tool. Try `autoleague --help`.

Usage:
```
autoleagueplay (odd | even) <path/to/current/ladder.txt>  | Plays an odd or even week from the given ladder
autoleagueplay fetch <week_num> <league_dir>              | Fetches the given ladder from the Google Sheets
autoleagueplay (-h | --help)                              | Show commands and options
autoleagueplay --version                                  | Show version
```

Options:
```
--replays=R          What to do with the replays of the match. Valid values are 'save', and 'calculated_gg'. [default: calculated_gg]
--list               Instead of playing the matches, the list of matches is printed.
--results            Like --list but also shows the result of matches that has been played.
-h --help            Show this screen.
--version            Show version.
```


The ladder is described by a text file, e.g. `ladder.txt`.
This should contain the bot names separated by newlines (it can be copy-pasted directly from the sheet).
A `bots/` directory with all the bots and their files must be located next to the ladder file.

When running the script you point it to the ladder file and give it either `odd` or `even` as argument to set what type of week it should play:
- Odd: Overclocked, Circuit, Transitor, ect plays.
- Even: Quantum, Processor, Abacus, etc plays.

Results are stored in a matches directory next to the ladder file. Each match will get a json file with all the relevant data, and they are named something like `quantum_reliefbot_vs_atlas_result.json`.
When all results are found, a new ladder `ladder_new.txt` is created next to the original ladder file.

### Advanced Usage:

#### Match Config
Change `autoleague/default_match_config.cfg` for other game modes and mutators.

#### Psyonix Bots
AutoLeaguePlay can handle Psyonix bots, but their names must be: `Psyonix Allstar`, `Psyonix Pro`, and `Psyonix Rookie`.
You don't have to give them config files in the `bots/` directory. AutoLeaguePlay has its own config files for Psyonix bots.
If you really want to give them different names, change them [there](https://github.com/NicEastvillage/AutoLeague/blob/master/autoleagueplay/psyonix_allstar.cfg).

#### Fetching ladder from Google Sheets
You can fetch the ladder from the Google Sheets with the `autopleagueplay fetch <week_num> <league_dir>` command.
Before you can use this you must get a `credentials.json` file which you can get by enabling [Google Sheets API](https://developers.google.com/sheets/api/quickstart/python) and then download the client configurations.
Put the `credentials.json ` in `autopleagueplay/cred/`. Next time you run the command, Google wants your permission, and then it should work.

#### Current Match and Overlay
AutoLeaguePlay creates a `current_match.json` next to the ladder file whenever a match is about to begin.
This file contains the division, and the paths to the bots currently playing. E.g.:

```json
{
    "division": 0,
    "blue_config_path": "C:\\User\\RLBot\\League\\bots\\Self-driving car\\self-driving-car.cfg",
    "orange_config_path": "C:\\User\\RLBot\\League\\bots\\Beast from the East\\beastbot.cfg"
}
```

The information in the file can be used for an overlay.
When the new ladder is complete the `current_match.json` is removed.