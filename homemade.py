import chess
import chess.engine
import chess.polyglot
import sys
import lib.engine_wrapper
import lib.lichess_types
import logging
logger = logging.getLogger(__name__)
engine_name = "stockfish"
engine_path = f"/opt/homebrew/bin/{engine_name}"
book_path = "/Users/me/Downloads/chess/book.bin"
class ExampleEngine(lib.engine_wrapper.MinimalEngine):
    pass
class Engine(ExampleEngine):
    def search(self, board: chess.Board, time_limit: chess.engine.Limit, ponder: bool, draw_offered: bool, root_moves: lib.lichess_types.MOVE) -> chess.engine.PlayResult:
        open(f"/Library/WebServer/Documents/{engine_name}-fen.txt", "w").write(board.fen())
        try:
            with chess.polyglot.open_reader(book_path) as reader:
                move = reader.choice(board)
            open(f"/Library/WebServer/Documents/{engine_name}-eval.txt", "w").write("book")
        except IndexError:
            engine = chess.engine.SimpleEngine.popen_uci(engine_path)
            move = engine.play(board, time_limit, info=chess.engine.INFO_ALL)
            engine.quit()
            open(f"/Library/WebServer/Documents/{engine_name}-eval.txt", "w").write(str(move.info['score'].relative.score(mate_score=sys.maxsize)/100))
        board.push(move.move)
        open(f"/Library/WebServer/Documents/{engine_name}-fen.txt", "w").write(board.fen())
        return chess.engine.PlayResult(move.move, None)