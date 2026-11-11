"""A small default material evaluator; callers may inject any Evaluator-compatible object."""
import chess
from typing import Protocol

PIECE_VALUES = {chess.PAWN: 100, chess.KNIGHT: 320, chess.BISHOP: 330,
                chess.ROOK: 500, chess.QUEEN: 900, chess.KING: 0}
MATE_SCORE = 100_000


class Evaluator(Protocol):
    """Structural evaluator contract shared with the game layer."""

    def evaluate(self, board: chess.Board, ply: int = 0) -> int:
        ...


class MaterialEvaluator(Evaluator):
    """Returns centipawns from White's point of view."""
    def evaluate(self, board: chess.Board, ply: int = 0) -> int:
        outcome = board.outcome(claim_draw=True)
        if outcome:
            if outcome.winner is None:
                return 0
            score = MATE_SCORE - ply
            return score if outcome.winner == chess.WHITE else -score
        score = 0
        for piece_type, value in PIECE_VALUES.items():
            score += value * (len(board.pieces(piece_type, chess.WHITE)) -
                              len(board.pieces(piece_type, chess.BLACK)))
        return score


DEFAULT_EVALUATOR = MaterialEvaluator()
