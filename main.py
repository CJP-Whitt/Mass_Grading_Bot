# **********************************************************************************************************
# Mass Grading Bot - (For google classroom)
# Version 1.0 (4/18/20)
# Created by Carson Whitt
#
# This program is a mass grader used for google classroom in giving the same grade to all students on a given
# assignment. Uses PyQt5, Selenium, and Chrome Driver.
# **********************************************************************************************************

import sys
from massGradingBotApp import *

app = QApplication(sys.argv)
gui = mgbApp()
sys.exit(app.exec_())
