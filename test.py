# -*- coding: utf-8 -*-
# @Author: Siqi Wang
# @Date:   2022-05-10 21:46:37
# @Last Modified by:   Siqi Wang
# @Last Modified time: 2022-05-22 00:21:46


def announce_highest(who, last_score=0, running_high=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 9)
    9 point(s)! The most yet for Player 1
    >>> f3 = f2(20, 9)
    >>> f4 = f3(20, 30)
    21 point(s)! The most yet for Player 1
    >>> f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
    >>> f6 = f5(21, 47)
    >>> f7 = f6(21, 77)
    30 point(s)! The most yet for Player 1
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    # BEGIN PROBLEM 7
    # TODO compare the current score with the last score
    # TODO print <return> point(s)! The most yet for Player <who>

    "*** YOUR CODE HERE ***"
    def high(score0, score1):
        if who == 0:
            if (score0 - last_score) > running_high:
                print((score0 - last_score),
                      'point(s)! The most yet for Player', who)
                return announce_highest(0, score0, (score0 - last_score))
            else:
                return announce_highest(0, score0, running_high)

        else:
            if (score1 - last_score) > running_high:
                print((score1 - last_score),
                      'point(s)! The most yet for Player', who)
                return announce_highest(1, score1, (score1 - last_score))
            else:
                return announce_highest(1, score1, running_high)

    return high
    # END PROBLEM 7
