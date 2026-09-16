# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: MilestoneMap
import sys

ANSI_ENABLED = os.environ.get('MILESTONEMAP_DISABLE_ANSI', '0') != '1'

if ANSI_ENABLED:
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    MAGENTA = '\033[35m'
    def colorize(text, color):
        return f'{color}{text}{RESET}'
    def bold(text):
        return f'{BOLD}{text}{RESET}'
    def dim(text):
        return f'{DIM}{text}{RESET}'
else:
    BOLD = DIM = RESET = RED = GREEN = YELLOW = BLUE = CYAN = WHITE = MAGENTA = ''
    def colorize(text, color):
        return text
    def bold(text):
        return text
    def dim(text):
        return text
