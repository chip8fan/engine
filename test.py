import chess.engine
import sys
import random
engine = chess.engine.SimpleEngine.popen_uci("")
board = chess.Board()
board.push(chess.Move.from_uci("e2e4"))
moves = [[move['score'].relative.score(mate_score=sys.maxsize), move['pv'][0]] for move in engine.analyse(board, chess.engine.Limit(time=30), multipv=len(list(board.legal_moves)))]
engine.quit()
print(moves)
max_score = max([move[0] for move in moves])
moves = [move[1] for move in moves if move[0]+100 >= max_score]
print(moves)
print(random.choice(moves))