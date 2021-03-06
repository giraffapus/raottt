#!/usr/bin/env python

"""
Simple harness that will run the TTT game. Can do any of Human vs Human,
Human vs Computer, or Computer vs Computer.

Usage: play.py [--blue=<b>] [--red=<r>] [--games=<n>] [--show]

Options:
    --blue=<b>      Blue player type (Human or Computer) [default: Computer]
    --red=<r>       Red plater type (Human or Computer) [default: Computer]
    --games=<n>     Number of games to play [default: 1]
    --show          Show boards between games [default: false]
"""

from __future__ import absolute_import
from __future__ import print_function
from docopt import docopt
from raottt.game import opponent
from raottt.game.game import Game
from raottt.player.computer import ComputerPlayer
from raottt.player.human import HumanPlayer
from raottt.util import Color


def toggle(item1, item2):
    """Returns a generator that will contnually toggle between the two items"""
    while True:
        yield item1
        yield item2


def run_game(player1, player2, max_rounds, show=True):
    """Run a game between player1 and player2 for max_rounds and then return
    the game state"""
    game = Game.new('Blue')
    player_toggle = toggle(player1, player2)
    if show:
        game.show()
        print()

    for _ in xrange(max_rounds):
        if game.game_over():
            break

        player = player_toggle.next()
        game.make_move(player)
        game.validate()

        print(Color.me(player.color, "{}'s Score: {}".format(
            player.name, player.score)))

        # print('Player Score (%s): %s' % (player.name, player.score))

        if show:
            game.show()
            print()

    return game


def main():
    """main"""
    args = docopt(__doc__)

    if args['--blue'] == 'Human':
        blue = HumanPlayer('Blue', opponent)
    elif args['--blue'] == 'Computer':
        blue = ComputerPlayer('Blue', opponent)
    else:
        print('Invalid argument --blue={}'.format(args['--blue']))
        print('Valid options are: Human or Computer')
        return

    if args['--red'] == 'Human':
        red = HumanPlayer('Red', opponent)
    elif args['--red'] == 'Computer':
        red = ComputerPlayer('Red', opponent)
    else:
        print('Invalid argument --red={}'.format(args['--red']))
        print('Valid options are: Human or Computer')
        return

    for _ in xrange(int(args["--games"])):
        game = run_game(blue, red, 999, args['--show'])
        print(Color.me(game.game_over(), '{} wins in {} moves!!!'.format(
            game.game_over(), game.score_tracker['num_moves'])))


if __name__ == '__main__':
    main()
