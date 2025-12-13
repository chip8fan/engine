import book
import os
import sys
import chess.engine
engine_path = sys.argv[1]
initial_depth = 1
max_eval = 50
time_limit = 1
book_path = f"{engine_path.split("/")[-1]}.bin"
while True:
    file_path = f"{engine_path.split("/")[-1]}-{initial_depth}ply.pgn"
    engine = chess.engine.SimpleEngine.popen_uci(engine_path)
    book.perft(initial_depth, [], initial_depth, max_eval, time_limit, file_path, engine)
    engine.quit()
    initial_depth += 1
    if os.path.isfile(book_path):
        os.remove(book_path)
    os.system(f"jja make --min-games 1 --output {book_path} {file_path}")