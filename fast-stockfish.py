import chess
import chess.engine
engine = chess.engine.SimpleEngine.popen_uci("/home/linuxbrew/.linuxbrew/bin/stockfish")
calculated_positions = []
board = chess.Board()
while True:
    line = input().split()
    if line[0] == "uci":
        print(f"id name Fast {engine.id['name']}")
        print("uciok")
    elif line[0] == "isready":
        print("readyok")
    elif line[0] == "position":
        if "fen" in line:
            board = chess.Board(fen=" ".join(line[2:]).split(" moves")[0])
        elif "startpos" in line:
            board = chess.Board()
        if "moves" in line:
            move_list = line[3:]
            for move in move_list:
                board.push_uci(move)
    elif line[0] == "go":
        new_board = board.copy()
        best_move = None
        for move in new_board.legal_moves:
            new_board.push(move)
            if new_board.fen() in calculated_positions:
                best_move = move
            new_board.pop()
            if best_move != None:
                break
        if best_move == None:
            if line[1] == "wtime" and line[3] == "btime" and line[5] == "winc" and line[7] == "binc":
                white_clock = int(line[2])/1000
                black_clock = int(line[4])/1000
                white_inc = int(line[6])/1000
                black_inc = int(line[8])/1000
            calculated_moves = engine.play(board, chess.engine.Limit(white_clock=white_clock, black_clock=black_clock, white_inc=white_inc, black_inc=black_inc), info=chess.engine.INFO_ALL).info['pv']
            best_move = calculated_moves[0]
            for move in calculated_moves:
                new_board.push(move)
                calculated_positions.append(new_board.fen())
        print(f"bestmove {best_move.uci()}")
    elif line[0] == "quit":
        break
    elif line[0] == "ucinewgame":
        pass
    else:
        print(line)
engine.quit()