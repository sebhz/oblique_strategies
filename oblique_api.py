#!/usr/bin/env python3

from flask import Flask, abort
from flask_restful import Resource, Api
import random
import oblique_strategies

app = Flask(__name__)
api = Api(app, prefix="/api/v1")


class StratRoot(Resource):
    def get(self):
        edition = random.randint(0, len(oblique_strategies.STRATEGIES) - 1)
        strategy = oblique_strategies.get_random_strat(edition)
        return {"strategy": strategy, "edition": edition + 1}


class StratEdition(Resource):
    def get(self, ed):
        if ed < 1 or ed > len(oblique_strategies.STRATEGIES):
            abort(404)
        strategy = oblique_strategies.get_random_strat(ed - 1)
        return {"strategy": strategy, "edition": ed}


api.add_resource(StratRoot, "/strategy")
api.add_resource(StratEdition, "/strategy/<int:ed>")

# Get any strategy: curl http://127.0.0.1:5000/api/v1/strategy -X GET
# Get a strategy from first edition: curl http://127.0.0.1:5000/api/v1/strategy/1 -X GET
if __name__ == "__main__":
    app.run(debug=False)
