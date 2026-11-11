"""Cấu hình chung toàn dự án."""
import os
from pathlib import Path

MATE = 100_000                      # điểm chiếu hết
INF = 10 ** 9
DEFAULT_DEPTH = 3
MAX_MINIMAX_DEPTH = 3               # Minimax thuần quá chậm ở độ sâu >3 (Python)
MAX_ALPHABETA_DEPTH = 5

# Đường dẫn Stockfish: đặt biến môi trường STOCKFISH_PATH hoặc sửa ở đây
_DEFAULT_STOCKFISH = (Path(__file__).resolve().parents[2] / "stockfish-windows-x86-64-universal" /
                      "stockfish" / "stockfish-windows-x86-64-universal.exe")
STOCKFISH_PATH = os.environ.get("STOCKFISH_PATH", str(_DEFAULT_STOCKFISH))
STOCKFISH_ANALYSIS_DEPTH = 15

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
