import chess
import chess.engine
import chess.pgn
import chess.polyglot
import sys
import time
prefix = "/Library/WebServer/Documents/"
engines = {
    "Stockfish 18": "stockfish-18",
    "Arasan 25.3": "arasan-25.3",
    "PlentyChess 7.0.0": "plentychess-7.0.0",
    "Stockfish 16.1": "stockfish-16.1",
    "Arasan 24.0": "arasan-24.0",
    "PlentyChess 3.0.2": "plentychess-3.0.2"
}
player1 = sys.argv[1]
player2 = sys.argv[2]
engine = [chess.engine.SimpleEngine.popen_uci(f"{prefix}{engines[player1]}"), chess.engine.SimpleEngine.popen_uci(f"{prefix}{engines[player2]}")]
games = int(sys.argv[3])
board = int(sys.argv[4])
match = f"round{games}"
node = None
chess_board = chess.Board()
game = chess.pgn.Game()
game.headers["Event"] = "Engine Games"
game.headers["Round"] = f"{games}.{board}"
game.headers["White"] = player1
game.headers["Black"] = player2
game.headers["WhiteTitle"] = "BOT"
game.headers["BlackTitle"] = "BOT"
game.headers["Result"] = "*"
print(game, file=open(f"{match}/game{board}.pgn", "w"), end="\n\n")
white_clock = 60*3
black_clock = 60*3
inc = 2
while chess_board.is_game_over(claim_draw=True) == False:
    start = time.time()
    try:
        with chess.polyglot.open_reader("book.bin") as reader:
            move = reader.weighted_choice(chess_board).move
    except IndexError:
        engine_limit = chess.engine.Limit(white_clock=white_clock, black_clock=black_clock, white_inc=inc, black_inc=inc)
        if chess_board.turn == chess.WHITE:
            move = engine[0].play(chess_board, engine_limit).move
        elif chess_board.turn == chess.BLACK:
            move = engine[1].play(chess_board, engine_limit).move
    if chess_board.turn == chess.WHITE:
        white_clock -= time.time()-start
        if white_clock <= 0:
            game.headers["Result"] = "0-1"
            break
        white_clock += inc
        hour = int(white_clock/3600)
        minute = int(white_clock/60) % 60
        second = white_clock % 60
    elif chess_board.turn == chess.BLACK:
        black_clock -= time.time()-start
        if black_clock <= 0:
            game.headers["Result"] = "1-0"
            break
        black_clock += inc
        hour = int(black_clock/3600)
        minute = int(black_clock/60) % 60
        second = black_clock % 60
    chess_board.push(move)
    if node == None:
        node = game.add_variation(move)
    else:
        node = node.add_variation(move)
    node.comment = f"[%clk {str(int(hour)).zfill(2)}:{str(int(minute)).zfill(2)}:{str(int(second)).zfill(2)}]"
    if game.headers["Result"] == "*":
        game.headers["Result"] = chess_board.result(claim_draw=True)
    print(game, file=open(f"{match}/game{board}.pgn", "w"), end="\n\n")
print(game, file=open(f"{match}/game{board}.pgn", "w"), end="\n\n")
engine[0].quit()
engine[1].quit()
