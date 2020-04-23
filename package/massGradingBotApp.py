import time

from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from package.gradingBot import *
from resources.strings import *

class mgbApp(QMainWindow):
    def __init__(self, resource_dir):
        super().__init__()
        self.logo_pic = open(os.path.join(resource_dir, 'mgb_logo.png'))
        self.ex_pic = open(os.path.join(resource_dir, 'grade_example.png'))
        print(self.logo_pic.name)
        print(self.ex_pic.name)
        self.create_view_init_UI()
        self.resize(400, 300), self.center(), self.setWindowTitle('Mass Grading Bot'), self.setWindowIcon(
            QIcon(self.logo_pic.name))

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.initial_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
        self.show()

    def create_view_init_UI(self):
        self.initial_widget = QWidget()
        self.initial_layout = QVBoxLayout()
        hbox = QHBoxLayout()

        hello_lbl = QLabel("Hello!", self)
        hello_lbl.setWordWrap(True)
        hello_lbl.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))

        lbl = QLabel(intro_msg1, self)
        lbl.setWordWrap(True)
        lbl.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Normal))
        self.nxt_btn = QPushButton("Next")
        self.initial_layout.setSpacing(0)
        self.initial_layout.addWidget(hello_lbl)
        self.initial_layout.addWidget(lbl)
        self.initial_layout.addStretch(1)

        hbox.addStretch(1)
        hbox.addWidget(self.nxt_btn)
        hbox.addStretch(1)
        self.initial_layout.addLayout(hbox)

        self.initial_widget.setLayout(self.initial_layout)
        self.nxt_btn.clicked.connect(self.login)

    def create_view_login_UI(self):
        self.login_widget = QWidget()
        self.login_layout = QVBoxLayout()
        hbox = QHBoxLayout()

        lbl = QLabel(login_msg1, self)
        lbl.setWordWrap(True)
        lbl.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Normal))
        self.login_nxt_btn = QPushButton("Next")
        self.login_layout.addWidget(lbl)
        self.login_layout.addStretch(1)

        hbox.addStretch(1)
        hbox.addWidget(self.login_nxt_btn)
        hbox.addStretch(1)
        self.login_layout.addLayout(hbox)

        self.login_widget.setLayout(self.login_layout)
        self.login_nxt_btn.clicked.connect(self.grade)

    def create_view_grade_UI(self):
        self.grade_widget = QWidget()
        self.grade_layout = QVBoxLayout()
        self.grade_layout.setSpacing(10)

        pic_label = QLabel(self)
        pic = QPixmap(self.ex_pic.name)
        pic_label.setPixmap(pic)

        lbl = QLabel(grade_msg1, self)
        lbl.setWordWrap(True)
        lbl.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.grade_btn = QPushButton("Grade")
        self.grade_layout.addWidget(lbl)
        self.grade_layout.addWidget(pic_label)
        lbl1 = QLabel(grade_msg2, self)
        lbl1.setWordWrap(True)
        lbl1.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.grade_layout.addWidget(lbl1)
        self.text_grade = QLineEdit(self)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.text_grade)
        hbox1.addStretch(1)
        self.grade_layout.addLayout(hbox1)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.grade_btn)
        hbox.addStretch(1)
        self.grade_layout.addLayout(hbox)

        self.error_label = QLabel(self)
        self.error_label.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Normal))
        self.grade_layout.addWidget(self.error_label)

        self.grade_widget.setLayout(self.grade_layout)
        self.grade_btn.clicked.connect(self.grade_click)

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
        if not gradeValue.isnumeric():
            self.error_label.setText("Non-valid input...retry")
            return
        if gradeValue == '':
            self.error(2)
            return
        if int(gradeValue) <= 0:
            self.error(1)
            return
        elif int(gradeValue) > 0:
            self.error_label.setText("Grading...")
        else:
            self.error_label.setText("Non-valid input...retry")
            return

        try:
            self.bot.gradeclass(gradeValue)
        except:
            self.error(3)
            return
        self.error_label.setText("Gave everyone " + gradeValue + " for the current assignment."
                                                                 "\nYou may now grade another class or close the Mass "
                                                                 "Grading Application...")

    # Function for handling errors during the grading process. Specifically the actual grading related operations.
    def error(self, error_state):
        if error_state == 1:
            self.error_label.setText(error_msg1)
        if error_state == 2:
            self.error_label.setText(error_msg2)
        if error_state == 3:
            self.error_label.setText(error_msg3)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

