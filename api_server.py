"""
REST Api server built on flask.
"""

# pylint: disable=R0201
# pylint: disable=C0103
# pylint: disable=W0232
# pylint: disable=F0401

from __future__ import print_function
from flask import Flask, request, make_response
from flask.ext.restful import Resource, Api
from raottt.game import opponent
from raottt.game.library import Library
from raottt.player.player import Bench
from raottt.player.rest import RESTPlayer
import json
import uuid


library = Library()
bench = Bench()
app = Flask(__name__, static_url_path='')
api = Api(app)


class Game(Resource):
    """
    Interacts with the game library

    GET /game/ will return a new game that can be played by the user
    PUT /game/ugid will apply a move to the given game
    """
    def get(self, uid):
        """doc string"""
        upid = uid
        player = bench[upid]
        game = library.checkout(player)
        return make_response(json.dumps(game.dump()))

    def put(self, uid):
        """doc string"""
        token = request.form['token']
        print("PUT game called with game id {} and token {}".format(
            uid, token))
        return make_response(json.dumps({'success': True}))


class Player(Resource):
    """
    Tracks stats for users

    GET  /player/puid will return the stats for the given player
    POST /player/ will create a new player
    """
    def get(self, uid):
        """Return the user's stats"""
        player = bench[uid]
        print("Looking up stats for {}".format(player.name))
        return make_response(json.dumps({'name': player.name}))

    def post(self):
        """Create a new user"""
        player = RESTPlayer('Blue', opponent)
        print('Created new player called {}'.format(player.name))
        bench.register(player)
        return make_response(json.dumps({'token': player.upid}))


api.add_resource(Game, '/game/', '/game/<string:uid>/')
api.add_resource(Player, '/player/', '/player/<string:uid>/')


@app.route('/')
def root():
    """Route to serve the statc index.html page"""
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
