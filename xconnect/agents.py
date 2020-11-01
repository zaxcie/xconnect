from random import choice

import numpy as np

from xconnect.game import get_valid_moves
from xconnect.one_step_lookahead import score_move

def agent_random(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]

    return choice(valid_moves)

def agent_middle(obs, config):
    return config.columns//2

def agent_leftmost(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]

    return valid_moves[0]

def onestep_lookahead_agent(obs, config):
    # Get list of valid moves
    valid_moves = get_valid_moves(obs, config)

    grid = np.asarray(obs.board).reshape(config.rows, config.columns)
    scores = dict(zip(valid_moves, [score_move(grid, col, obs.mark, config) for col in valid_moves]))
    max_cols = [key for key in scores.keys() if scores[key] == max(scores.values())]


    return choice(max_cols)
