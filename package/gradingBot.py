import sys
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



sleep_time = 3
executable_path = '../driver/chromedriver.exe'

class gradingBot():
    def __init__(self):
        self.driver = webdriver.Chrome(self.resource_path(executable_path))
        self.actions = ActionChains(self.driver)

    def login(self):
        self.driver.get("https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue"
                        "=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&followup=https%3A%2F%2Fclassroom.google.com"
                        "%2F%3Femr%3D0&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

    def gradeclass(self, grade):
        try:
            boxes = self.driver.find_elements_by_class_name("Fk0vXe")
        except:
            raise Exception("Chrome page not detected")

        if len(boxes) == 0:
            raise Exception("Assignment grading page not detected")
        self.actions.send_keys(Keys.BACK_SPACE)
        self.actions.send_keys(Keys.BACK_SPACE)
        self.actions.send_keys(Keys.BACK_SPACE)
        self.actions.send_keys(grade)
        # Testing mode
        # for i in range(0, 2):
        #     boxes[i].click()
        #     self.actions.perform()

        # User Mode
        for i in range(0, len(boxes)):
            boxes[i].click()
            self.actions.perform()

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.dirname(__file__)
        return os.path.join(base_path, relative_path)







