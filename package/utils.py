# These variables are set by pyinstaller if running from a frozen
import sys
is_frozen = getattr(sys, 'frozen', False)
frozen_temp_path = getattr(sys, '_MEIPASS', '')