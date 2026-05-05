# utils.py
from pathlib import Path
import sys

def resource_path(*paths):
    try:
        base_path = Path(sys._MEIPASS)  # når pakket
    except AttributeError:
        base_path = Path(__file__).parent  # når udvikling
    return str(base_path.joinpath(*paths))
