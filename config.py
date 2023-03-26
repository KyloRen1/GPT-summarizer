from pathlib import Path

OPENAI_KEY_API = None  # enter yor OPENAI key here
MAX_TOKENS = 3000

# Directories
BASE_DIR = Path(__file__).parent.absolute()
CACHE_DIR = Path(BASE_DIR, "cache")

CACHE_DIR.mkdir(parents=True, exist_ok=True)
