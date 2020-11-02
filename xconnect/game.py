def get_valid_moves(obs, config):
    moves = [col for col in range(config.columns) if obs.board[col] == 0]
    return moves
