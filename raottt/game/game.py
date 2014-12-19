"""
Implements the modified Tic Tac Toe game.

Keeps track of the current board state as well as the history of the game,
specifically the set of users that have previousely plaed this game, and the
change in board value.
"""

from __future__ import absolute_import
from ..game import COLORS
from ..game import opponent
from ..util import Color
from .board import Board
import uuid


class Game(object):
    """Tracks the current state as well as the history of the game."""
    def __init__(self, first_player):
        self.ugid = uuid.uuid4().hex
        self.players = {k: {} for k in COLORS}
        self.moves_performed = 0
        self.next_color = first_player
        self.prev_player = None
        self.board = None

    @classmethod
    def new(cls, first_player):
        """Returns a new game."""
        game = cls(first_player)
        game.board = Board()
        return game

    @classmethod
    def load(cls, data):
        """Restores (loads) a game from the given state expressed as a dict."""
        game = cls(data['nextPlayer'])
        game.ugid = data['ugid']
        game.board = Board.load(data['board'])
        game.players = data['players']
        game.moves_performed = data['movesPerformed']
        return game

    def dump(self):
        """Returns the game state as a dict."""
        squares = self.board.dump()
        return {'board': squares,
                'players': self.players,
                'moveNumber': self.moves_performed + 1,
                'nextPlayer': self.next_color,
                'ugid': self.ugid}

    def make_move(self, player):
        """Obtains a movr from the passed in player, and then applies that move
        to the game."""
        assert player.color == self.next_color
        move = player.get_move(self.board)
        score_before_move = self.board.value_ratio(player)
        self.board.make_move(player.color, move[0], move[1])

        score_after_move = self.board.value_ratio(player)
        if score_after_move > score_before_move:
            # TODO - inplement scoring logic
            # User added value!
            pass

        # Update players to record this user has taken a turn for this color
        color = player.color
        upid = player.upid
        self.players[color][upid] = self.players[color].get(upid, 0) + 1

        self.moves_performed += 1
        self.board.age(opponent(color))
        self.next_color = opponent(color)
        return move

    def show(self):
        """Prints the board (in pretty colorized ASCII :-) to stdout."""
        print 'Game: %s' % Color.yellow(self.ugid)
        print 'Moves Performed: %s' % Color.yellow(self.moves_performed)
        print 'Board Value: %s/%s' % (Color.blue(self.board.value('Blue')),
                                      Color.red(self.board.value('Red')))
        print 'Next Player: %s' % (Color.me(self.next_color,
                                            self.next_color))

        print 'Value Ratio (%s): %s' % (
            Color.me(self.next_color, self.next_color),
            Color.yellow(self.board.value_ratio(self.next_color)))

        print 'Value Ratio (%s): %s' % (
            Color.me(opponent(self.next_color),
                     opponent(self.next_color)),
            Color.yellow(self.board.value_ratio(
                opponent(self.next_color))))
        self.board.show()

    def game_over(self):
        """Returns the winner if the game is in a winning (won?) state, or
        None if the game is still in play."""
        return self.board.winner()

    def validate(self):
        """Checks to make sure the game is in a valid state."""
        # Check that we have no more than 6 pieces on the board
        pieces = len([p for p in self.board.squares if p.color])
        assert pieces <= 6

        # If we have made 6 or more moves, then there must be 6 pieces
        if self.moves_performed >= 6:
            assert pieces == 6

        # Check that all pieces have a count between 1 and 5
        pieces = len([p for p in self.board.squares if p.count < 1] +
                     [p for p in self.board.squares if p.count > 5])
        assert not pieces

        # Check that we have at most one piece with a count of 1
        pieces = len([p for p in self.board.squares if p.count == 1])
        assert pieces <= 1

        # Make sure the same upid has not played both sides
        players = set(self.players['Red']).intersection(
            set(self.players['Blue']))
        assert not players
