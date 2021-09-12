#!/usr/bin/env python3

import flask
from flask import url_for

import oblique_strategies

API_PATH = "/api/v1"

app = flask.Flask(__name__)


def get_strategy(ed=None):
    if ed is None:
        return oblique_strategies.get_random_strat()
    elif ed < 1 or ed > len(oblique_strategies.STRATEGIES):
        flask.abort(404)
    else:
        return oblique_strategies.get_random_strat(ed)


def get_strategy_html(ed=None):
    strategy, edition = get_strategy(ed)
    return flask.render_template("strategy.html", strategy=strategy)


@app.route("/")
def show_random_strat():
    html = get_strategy_html()
    return html


@app.route("/<int:ed>")
def show_random_strat_from_edition(ed):
    html = get_strategy_html(ed)
    return html


@app.route(API_PATH + "/")
def get_random_strat():
    strategy, edition = get_strategy()
    return {"strategy": strategy, "edition": edition}


@app.route(API_PATH + "/<int:ed>")
def get_random_strat_from_edition(ed):
    strategy, edition = get_strategy(ed)
    return {"strategy": strategy, "edition": edition}


# Get any strategy: curl -L http://127.0.0.1:5000/api/v1 -X GET
# Get a strategy from first edition: curl http://127.0.0.1:5000/api/v1/1 -X GET
if __name__ == "__main__":
    app.run(debug=True)
