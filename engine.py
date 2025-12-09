import chess.engine # to load engine
import chess # to load chess module
import sys # to get the minimum possible integer value
import random # to get a random move
class Engine(): # define a class
    def play(self, fen, depth, cp_loss, engine_path): # and a function
        self.board = chess.Board(fen=fen) # set the fen to the input fen
        self.engine = chess.engine.SimpleEngine.popen_uci(engine_path) # load engine at engine_path
        self.moves = [] # list of possible moves
        self.best_moves = [] # list of 'good moves'
        self.max_score = -sys.maxsize # set max_score to lowest possible integer value
        for move in self.board.legal_moves: # iterate through all legal moves
            self.board.push(move) # push move to board
            if self.board.is_game_over(can_claim_draw=True) == False: # if stalemate and checkmate are not on the board
                self.score = -self.engine.analyse(self.board, chess.engine.Limit(depth=depth))["score"].pov(self.board.turn).score(mate_score=100000) # analyze a position to the depth specified
            elif self.board.is_stalemate() or self.board.is_insufficient_material() or self.board.can_claim_draw(): # if stalemate is on the board
                self.score = 0
            elif self.board.is_checkmate(): # if checkmate is on the board
                self.score = 100000 # set the score to 100k
            self.max_score = max(self.score, self.max_score) # set max_score to the greater of score and max_score
            self.moves.append([move, self.score]) # append to list of possible moves
            self.board.pop() # pop move from board
        self.engine.quit() # quit engine
        for move in self.moves: # iterate through all legal moves again
            if move[1]+cp_loss >= self.max_score: # check if move is good enough
                self.best_moves.append(move[0]) # if so, append to list of 'good moves'
        return random.choice(self.best_moves) # get a random move