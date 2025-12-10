import chess.engine
import chess
import sys
import random
class Engine():
    def play(self, fen, max_time, cp_loss, engine_path):
        self.board = chess.Board(fen=fen)
        self.engine = chess.engine.SimpleEngine.popen_uci(engine_path)
        self.moves = []
        self.best_moves = []
        self.max_score = -sys.maxsize
        max_time /= len(list(self.board.legal_moves))
        max_time = max(max_time, 0.1)
        for move in self.board.legal_moves:
            self.board.push(move)
            if self.board.is_game_over(claim_draw=True) == False:
                self.score = -self.engine.analyse(self.board, chess.engine.Limit(time=max_time))["score"].pov(self.board.turn).score(mate_score=sys.maxsize)
            elif self.board.is_checkmate():
                self.score = sys.maxsize
            else:
                self.score = 0
            self.max_score = max(self.score, self.max_score)
            self.moves.append([move, self.score])
            self.board.pop()
        self.engine.quit()
        for move in self.moves:
            if move[1]+cp_loss >= self.max_score:
                self.best_moves.append(move[0])
        return random.choice(self.best_moves)
