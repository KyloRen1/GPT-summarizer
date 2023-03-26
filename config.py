from pathlib import Path

OPENAI_KEY_API = None  # enter yor OPENAI key here
MODEL_MAX_TOKENS = 3000 # maximum model input (minus 1000 for generation)
TOKE_WORD_COEF = 0.75  # on evarage 100 tokens is ±75 words.

# Directories
BASE_DIR = Path(__file__).parent.absolute()
CACHE_DIR = Path(BASE_DIR, "cache")

CACHE_DIR.mkdir(parents=True, exist_ok=True)
