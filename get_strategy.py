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

if _args.edition:
    edition = _args.edition - 1
else:
    edition = random.randint(0, len(oblique_strategies.STRATEGIES) - 1)

if _args.all:
    if not _args.edition:
        all_strats = oblique_strategies.get_all_strats()
        for strat in sorted(all_strats.keys()):
            print(strat, all_strats[strat] if _args.show_edition else "")
    else:
        for strat in oblique_strategies.STRATEGIES[edition]:
            print(strat, "[" + str(edition + 1) + "]" if _args.show_edition else "")
else:
    print(
        oblique_strategies.get_random_strat(edition),
        "[" + str(edition + 1) + "]" if _args.show_edition else "",
    )
