import chess
import chess.engine
import copy
import sys
def make_pgn(move_stack, file_path):
    moves = copy.deepcopy(move_stack)
    chess_board = chess.Board()
    move_count = 1
    pgn_string = ""
    for move in moves:
        if chess_board.turn == chess.WHITE:
            pgn_string = pgn_string + f"{move_count}. {chess_board.san(move)}"
        elif chess_board.turn == chess.BLACK:
            pgn_string = pgn_string + f" {chess_board.san(move)} "
            move_count += 1
        chess_board.push(move)
    print(pgn_string, file=open(file_path, "a"), end="\n\n")
def perft(depth, move_stack, root_depth, max_advantage, engine_time_limit, file_path, engine):
    nodes = 0
    if depth == 0:
        return 1
    elif depth == root_depth:
        file = open(file_path, "w")
        file.close()
    board = chess.Board()
    for move in move_stack:
        board.push(move)
    for move in board.legal_moves:
        board.push(move)
        score = abs(engine.analyse(board, chess.engine.Limit(time=engine_time_limit))["score"].pov(board.turn).score(mate_score=sys.maxsize))
        if score <= max_advantage:
            make_pgn(board.move_stack, file_path)
            nodes += perft(depth-1, board.move_stack, root_depth, max_advantage, engine_time_limit, file_path, engine)
        board.pop()
    return nodes