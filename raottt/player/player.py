"""
Player - Implments Human and AI Modified TTT Players

The HumanPlayer reads commands from stdin.
The ComputerPlayer uses a basic min/max algo to select the next move.
"""

from __future__ import absolute_import
from ..util import Color
import names
import uuid


class Bench(object):
    """Implements the player bench which is used to track all know players"""
    def __init__(self):
        self.players = {}

    def __getitem__(self, upid):
        return self.players.get(upid, None)

    def register(self, player):
        """Register a new player"""
        self.players[player.upid] = player


class Player(object):
    """Implementation of a TTT Player. See the specific implmentations below"""
    def __init__(self, color, opponent, name=None, upid=None,):
        self.color = color
        self.opponent = opponent
        self.name = name or names.get_first_name()
        self.upid = upid or uuid.uuid4().hex

    @classmethod
    def load(cls, data):
        """Loads the Player state from a python dict"""
        return cls(data['color'], data['upid'])

    def __str__(self):
        """Return string representation of the player"""
        return '%s %s' % (self.name, Color.me(self.color, self.upid))

    def dump(self):
        """Dumps the Player state as a python dict"""
        return {'color': self.color, 'upid': self.upid}

    def get_move(self, board):
        """Returns the user's move"""
        raise NotImplementedError
