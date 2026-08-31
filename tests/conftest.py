import sys
from pathlib import Path

# Garante que o pytest encontre os módulos dentro de src/, independente de onde o comando pytest for executado.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))