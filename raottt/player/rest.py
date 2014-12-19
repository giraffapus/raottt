"""
REST (Swift App) player
"""


from __future__ import absolute_import
from player import Player


class RESTPlayer(Player):
    """Implements a REST player (Api)"""
    def __init__(self, color, opponent, name=None, upid=None):
        """Initializes the RESTPlayer"""
        super(RESTPlayer, self).__init__(color, opponent, name, upid)
        self.move = None

    def queue_move(self, move):
        """Set the move in the user so that if can be pulled out again using
        get_move"""
        self.move = move

    def get_move(self, board):
        """Returns the move that was queued"""
        return self.move

    # def game_state(game, player, hint='Your turn ...'):
    #     """Adapts the game and player state to the format expected by the
    #     swift code"""
    #     board_squares = game.board.dump()
    #     possible_moves = [s for (s, _) in game.board.available_moves(player)]
    #     for i, square in enumerate(board_squares):
    #         square['position'] = i+1
    #         if i in possible_moves:
    #             square['movable'] = True
    #         else:
    #             square['movable'] = False

    #     return json.dumps(
    #         {'pieces': board_squares,
    #          'moveNumber': game.moves_performed + 1,
    #          'nextPlayer': game.next_player,
    #          'hint': hint,
    #          'ugid': game.ugid})
