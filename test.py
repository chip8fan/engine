import chess.engine
engine = chess.engine.SimpleEngine.popen_uci("/Users/me/Downloads/chess/bin/lc0/lc0")
board = chess.Board()
print(engine.analyse(board, chess.engine.Limit(time=1), multipv=len(board.legal_moves)))
engine.quit()