PADDING = 20

RED = '\033[1;31m'
GREEN = '\033[0;32m'
CYAN = '\033[1;36m'
BLUE = '\033[1;34m'
YELLOW = '\033[33m'
WHITE = '\033[37m'
GRAY = '\033[0;90m'

REVERSE = '\033[7m'
RESET = '\033[0m'

def change_color(color):
    print(color, end='')
