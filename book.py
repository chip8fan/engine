import chess
import chess.engine
import copy
import sys
class bookGenerator():
    def spawn_engine(self, engine_path):
        self.engine = chess.engine.SimpleEngine.popen_uci(engine_path)
    def quit_engine(self):
        self.engine.quit()
    def make_pgn(self, move_stack, file_path):
        self.moves = copy.deepcopy(move_stack)
        self.chess_board = chess.Board()
        self.move_count = 1
        self.pgn_string = ""
        for move in self.moves:
            if self.chess_board.turn == chess.WHITE:
                self.pgn_string = self.pgn_string + f"{self.move_count}. {self.chess_board.san(move)}"
            elif self.chess_board.turn == chess.BLACK:
                self.pgn_string = self.pgn_string + f" {self.chess_board.san(move)} "
                self.move_count += 1
            self.chess_board.push(move)
        print(self.pgn_string, file=open(file_path, "a"))
    def perft(self, depth, move_stack, root_depth, max_advantage, engine_time_limit, file_path):
        self.nodes = 0
        if depth == 0:
            return 1
        elif depth == root_depth:
            file = open(file_path, "w")
            file.close()
        self.board = chess.Board()
        for move in move_stack:
            self.board.push(move)
        for move in self.board.legal_moves:
            self.board.push(move)
            score = abs(self.engine.analyse(self.board, chess.engine.Limit(time=engine_time_limit))["score"].pov(self.board.turn).score(mate_score=sys.maxsize))
            if score <= max_advantage:
                self.make_pgn(self.board.move_stack, file_path)
                self.nodes += self.perft(depth-1, self.board.move_stack, root_depth, max_advantage, engine_time_limit, file_path)
            self.board.pop()
        return self.nodes