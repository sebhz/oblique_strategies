#!/usr/bin/env python3

import flask
import random
import oblique_strategies

API_PATH = "/api/v1"

app = flask.Flask(__name__)


@app.route(API_PATH + "/strategy/")
@app.route(API_PATH + "/strategy")
def get_random_strat():
    edition = random.randint(0, len(oblique_strategies.STRATEGIES) - 1)
    strategy = oblique_strategies.get_random_strat(edition)
    return flask.jsonify({"strategy": strategy, "edition": edition + 1})


@app.route(API_PATH + "/strategy/ed/<int:ed>")
def get_random_strat_from_edition(ed):
    if ed < 1 or ed > len(oblique_strategies.STRATEGIES):
        flask.abort(404)
    strategy = oblique_strategies.get_random_strat(ed - 1)
    return {"strategy": strategy, "edition": ed}


# Get any strategy: curl http://127.0.0.1:5000/api/v1/strategy -X GET
# Get a strategy from first edition: curl http://127.0.0.1:5000/api/v1/strategy/ed/1 -X GET
if __name__ == "__main__":
    app.run(debug=True)
