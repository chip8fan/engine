import book
import os
import sys
engine_path = sys.argv[1]
stockfish = book.bookGenerator()
initial_depth = 1
max_eval = 50
time_limit = 1
book_path = f"{engine_path.split("/")[-1]}.bin"
while True:
    file_path = f"{engine_path.split("/")[-1]}-{initial_depth}ply.pgn"
    stockfish.spawn_engine(engine_path)
    stockfish.perft(initial_depth, [], initial_depth, max_eval, time_limit, file_path)
    stockfish.quit_engine()
    initial_depth += 1
    os.system(f"jja make --min-games 1 --output {book_path} {file_path}")