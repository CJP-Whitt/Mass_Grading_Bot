from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from gradingBot import *
from strings import *

class mgbApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.create_view_init_UI()
        self.resize(400, 300), self.center(), self.setWindowTitle('Mass Grading Bot'), self.setWindowIcon(QIcon('mgb_logo.png'))

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.initial_widget)

        self.central_widget = QWidget()
        self.statusBar = QStatusBar()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
        self.setStatusBar(self.statusBar)
        self.show()

    def create_view_init_UI(self):
        self.initial_widget = QWidget()
        self.initial_layout = QVBoxLayout()
        hbox = QHBoxLayout()

        lbl = QLabel(intro_msg1, self)
        lbl.setWordWrap(True)
        lbl.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        nxt_btn = QPushButton("Next")
        self.initial_layout.setSpacing(0)
        self.initial_layout.addWidget(lbl)
        self.initial_layout.addStretch(1)

        hbox.addStretch(1)
        hbox.addWidget(nxt_btn)
        hbox.addStretch(1)
        self.initial_layout.addLayout(hbox)

        self.initial_widget.setLayout(self.initial_layout)
        nxt_btn.clicked.connect(self.login)

    def create_view_login_UI(self):
        self.login_widget = QWidget()
        self.login_layout = QVBoxLayout()
        hbox = QHBoxLayout()

        lbl = QLabel(login_msg1, self)
        lbl.setWordWrap(True)
        lbl.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        nxt_btn = QPushButton("Next")
        self.login_layout.addWidget(lbl)
        self.login_layout.addStretch(1)

        hbox.addStretch(1)
        hbox.addWidget(nxt_btn)
        hbox.addStretch(1)
        self.login_layout.addLayout(hbox)

        self.login_widget.setLayout(self.login_layout)
        nxt_btn.clicked.connect(self.grade)

    def create_view_grade_UI(self):
        self.grade_widget = QWidget()
        self.grade_layout = QVBoxLayout()
        self.grade_layout.setSpacing(10)

        pic_label = QLabel(self)
        pic = QPixmap('grade_example.png')
        pic_label.setPixmap(pic)

        lbl = QLabel(grade_msg1, self)
        lbl.setWordWrap(True)
        lbl.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        grade_btn = QPushButton("Grade")
        self.grade_layout.addWidget(lbl)
        self.grade_layout.addWidget(pic_label)
        lbl1 = QLabel(grade_msg2, self)
        lbl1.setWordWrap(True)
        lbl1.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.grade_layout.addWidget(lbl1)
        self.text_grade = QLineEdit(self)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.text_grade)
        hbox1.addStretch(1)
        self.grade_layout.addLayout(hbox1)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(grade_btn)
        hbox.addStretch(1)
        self.grade_layout.addLayout(hbox)

        self.grade_widget.setLayout(self.grade_layout)
        grade_btn.clicked.connect(self.grade_click)

    def login(self):
        self.bot = gradingBot()
        self.bot.login()
        self.create_view_login_UI()
        self.stacked_layout.addWidget(self.login_widget)
        self.stacked_layout.setCurrentIndex(1)
        self.show()
        self.activateWindow()
        self.raise_()

    def grade(self, grade):
        self.create_view_grade_UI()
        self.stacked_layout.addWidget(self.grade_widget)
        self.stacked_layout.setCurrentIndex(2)
        self.center()
        self.show()
        self.activateWindow()
        self.raise_()

    def grade_click(self):
        gradeValue = self.text_grade.text()
        if gradeValue == '':
            self.error(2)
            return
        if int(gradeValue) <= 0:
            self.error(1)
            return
        elif int(gradeValue) > 0:
            self.statusBar.showMessage("Grading...")

        try:
            self.bot.gradeclass(gradeValue)
        except:
            self.error(3)
            return
        self.statusBar.showMessage("Gave everyone " + gradeValue + " for the current assignment. ")

    # Function for handling errors during the grading process. Specifically the actual grading related oeprations.
    def error(self, error_state):
        if error_state == 1:
            self.statusBar.clearMessage()
            self.statusBar.showMessage("Invalid grade input. Input a number grater than zero and hit the grade "
                                       "button...")
        if error_state == 2:
            self.statusBar.clearMessage()
            self.statusBar.showMessage("Missing grade input. Input a grade value and hit grade button...")
        if error_state == 3:
            self.statusBar.clearMessage()
            self.statusBar.showMessage("No assignment grading page detected. Make sure you are on page as in image "
                                       "above and retry...")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())