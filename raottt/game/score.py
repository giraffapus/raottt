"""
Implments the rules to calculate how much to update the user's score by after
a move.

+1 for every move
+1 if move improved the value of the board for your color
+2 if you change from being behind to ahead
+3 if a chain you helped with wins  (??)
+5 if you make the winning move

-4 if the game is lost on the next move
-1 if a chain you helped with looses
-1 if you lower the value of the board
-1 if you change from being ahead to behind


The Game object should keep a tupe of the previous person to make a move
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

def update_score_post_move(game, player):
    """doc string"""
    player.score += calulate_incremental_score(game, player.color, player.name)


def calulate_incremental_score(game, color, name):
    """doc string"""
    score = 1  # +1 point for making a move

    prev_score = game.prev_score[color]
    new_score = game.board.value(color)
    print("score ({}): {} -> {}".format(name, prev_score, new_score))

    if new_score > prev_score:
        score += 1
    elif new_score < prev_score:
        score -= 1

    prev_score_ratio = game.prev_score_ratio[color]
    new_score_ratio = game.board.value_ratio(color)
    #print("ratio ({}): {} -> {}".format(name, prev_score_ratio, new_score_ratio))

    if prev_score_ratio < 0.50 and new_score_ratio > 0.50:
        score += 2
    elif prev_score_ratio > 0.50 and new_score_ratio < 0.50:
        score -= 1

    if game.game_over() == color:
        score += 5

    return score


