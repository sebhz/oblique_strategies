#!/usr/bin/env python3

import argparse
import random
import oblique_strategies

parser = argparse.ArgumentParser()
parser.add_argument(
    "-e",
    "--edition",
    help="Edition to chose from.",
    type=int,
    choices=list(range(1, 6)),
)
parser.add_argument(
    "-a", "--all", help="Display all editions.", action="store_true", default=False
)
parser.add_argument(
    "-s",
    "--show-edition",
    help="Show strategy edition(s).",
    action="store_true",
    default=False,
)

_args = parser.parse_args()


if _args.all:
    if _args.edition is None:
        all_strats = oblique_strategies.get_all_strats()
        for strat in sorted(all_strats.keys()):
            print(strat, all_strats[strat] if _args.show_edition else "")
    else:
        for strat in oblique_strategies.STRATEGIES[_args.edition - 1]:
            print(strat, "[" + str(_args.edition) + "]" if _args.show_edition else "")
else:
    strat, edition = oblique_strategies.get_random_strat(_args.edition)
    print(strat, "[" + str(edition) + "]" if _args.show_edition else "")
