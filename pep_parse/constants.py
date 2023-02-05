import re
from pathlib import Path

PATTERN_PEP = r'^PEP (?P<number>\d+) – (?P<name>.+)$'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
BASE_DIR = Path(__file__).parent
