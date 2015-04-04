"""
Implments the rules to calculate how much to update the user's score by after
a move.

+1 for every move
+1 if move improved the value of the board for your color
+2 if you change from being behind to ahead
+2 if a chain you helped with wins  (??)
+5 if you make the winning move

-4 if the game is lost on the next move
-1 if a chain you helped with looses
-1 if you lower the value of the board
-1 if you change from being ahead to behind


The Game object should keep a tuple of the previous person to make a move
(Player, Score, Ratio) then we can compare in the post_move_score_update if the
current move (that has just completed) improved or worsened things.

Also, if the game ends at this point then we can modify the score of the
previous person who made it happen ...

Questions:
Shoulds we keep track of ALL the people who have participated in the
game (and the number of turns they took - and possibly the ration of imprcements
and decreases??)? That way, when a game ends, we can allocation a number of
point to the winning team (the older the game the more points) and hand them out
to the people who partiipated ...

How should I be notifying you about a score change that happened becuse of a
subsequent move?? Go all out and do smily and frowney faces? "BigGorillaMonkey
just won a game where you made the previous move .. Oh shame on you ..." or
"Great News! BigGorillaMonkey just made the winning move for team Red in a
game that you helped. He was standing on the shoulders of giants. Yours
Shoulders (among others). Great stuff. Have +X points"

"""


from __future__ import print_function
from ..game import opponent


def empty_score_tracker():
    """blah"""
    return {'teams': {'red': {}, 'blue': {}},
            'previous': {'red': (0, 0, 0), 'blue': (0, 0, 0)}}


def post_move_score_update(tracker, new_score, new_ratio, winner, color, upid):
    """blah"""
    _, prev_score, _ = tracker['previous'][color][-1]
    _, _, prev_ratio = tracker['previous'][opponent(color)][-1]

    # Record the fact that this upid participated in the game
    tracker['teams'][color][upid] = tracker['teams'][color].get(upid, 0) + 1
    tracker['previous'][color].append((upid, new_score, new_ratio))

    # Calculate the score this player will get based on the rules:
    # +1 for every move
    # +1 if move improved the value of the board for your color
    # -1 if you lower the value of the board for your color
    # +2 if you change your color from being behind to ahead
    # -1 if you change your color from being ahead to behind
    # +3 if you make the winning move
    score = 1
    if new_score > prev_score:
        score += 1
    elif new_score < prev_score:
        score -= 1

    if prev_ratio < 0.50 and new_ratio > 0.50:
        score += 2
    elif prev_ratio > 0.50 and new_ratio < 0.50:
        score -= 1

    if winner == color:
        score += 3

    return score, tracker


"""
class ScoreKeeper(object):
    def __init__(self, ugid):
        self.ugid = ugid
        self.teams = {'red': {}, 'blue': {}}
        self.previous = {'red': (0, 0, 0), 'blue': (0, 0, 0)}

    def calculate_move_score(self, new_score, new_ratio, winner, color, upid):
        """doc string"""
        _, prev_score, _ = self.previous[color][-1]
        _, _, prev_ratio = self.previous[opponent(color)][-1]

        # Record the fact that this upid participated in the game
        self.teams[color][upid] = self.teams[color].get(upid, 0) + 1
        self.previous[color].append((upid, new_score, new_ratio))

        # Calculate the score this player will get based on the rules:
        # +1 for every move
        # +1 if move improved the value of the board for your color
        # -1 if you lower the value of the board for your color
        # +2 if you change your color from being behind to ahead
        # -1 if you change your color from being ahead to behind
        # +3 if you make the winning move
        score = 1
        if new_score > prev_score:
            score += 1
        elif new_score < prev_score:
            score -= 1

        if prev_ratio < 0.50 and new_ratio > 0.50:
            score += 2
        elif prev_ratio > 0.50 and new_ratio < 0.50:
            score -= 1

        if winner == color:
            score += 3

        return score

    def calculate_game_score(self, winning_color):
        """doc srting"""
        game_points = len(self.previous['red']) + len(self.previous['blue'])
        winning_factor = 2
        loosing_factor = -1

        winners = {}
        for upid, _, _ in self.previous[winning_color][1:]:
            winners[upid] = winners.get(upid, 0) + 1
        for upid in winners:
            add_points(upid, winners[upid] * winning_factor)

        loosers = {}
        for upid, _, _ in self.previous[opponent(winning_color)][1:]:
            loosers[upid] = loosers.get(upid, 0) + 1
        for upid in loosers:
            add_points(upid, loosers[upid] * loosing_factor)
"""

def add_points(upid, points):
    """Adds points to the given user's profile"""
    pass


def update_score_post_move(game, player):
    """blah"""
    pass

#     """doc string"""
#     player.score += calulate_incremental_score(game, player.color, player.name)


# def calulate_incremental_score(game, color, name):
#     """doc string"""
#     score = 1  # +1 point for making a move

#     prev_player, prev_score, prev_ratio = game.prev_states[-1]

#     new_score = game.board.value(color)

#     if new_score > prev_score:
#         score += 1
#     elif new_score < prev_score:
#         score -= 1

#     new_ratio = game.board.value_ratio(color)
#     #print("ratio ({}): {} -> {}".format(name, prev_score_ratio, new_score_ratio))

#     if prev_ratio < 0.50 and new_ratio > 0.50:
#         score += 2
#     elif prev_ratio > 0.50 and new_ratio < 0.50:
#         score -= 1

#     if game.game_over() == color:
#         score += 5
#         # Leave a message for the other player telling them the sad news ...
#         # and subtract points from their score



#     return score


