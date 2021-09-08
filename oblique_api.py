#!/usr/bin/env python3

import flask
import oblique_strategies

API_PATH = "/api/v1"

app = flask.Flask(__name__)


@app.route(API_PATH + "/strategy/")
@app.route(API_PATH + "/strategy")
def get_random_strat():
    strategy, edition = oblique_strategies.get_random_strat()
    return flask.jsonify({"strategy": strategy, "edition": edition})


@app.route(API_PATH + "/strategy/ed/<int:ed>")
def get_random_strat_from_edition(ed):
    if ed < 1 or ed > len(oblique_strategies.STRATEGIES):
        flask.abort(404)
    strategy,edition = oblique_strategies.get_random_strat(ed)
    return {"strategy": strategy, "edition": edition}


# Get any strategy: curl http://127.0.0.1:5000/api/v1/strategy -X GET
# Get a strategy from first edition: curl http://127.0.0.1:5000/api/v1/strategy/ed/1 -X GET
if __name__ == "__main__":
    app.run(debug=True)
