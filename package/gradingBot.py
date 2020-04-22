import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from package.HiddenChromeService import HiddenChromeWebDriver
from package.utils import is_frozen, frozen_temp_path


sleep_time = 3

chrome_driver_str = 'chromedriver.exe'

if is_frozen:
    basedir = frozen_temp_path
    driver_dir = os.path.join(basedir, 'driver')
else:
    basedir = os.path.dirname(os.path.abspath(__file__))
    driver_dir = os.path.join(basedir, '..\\driver')


class gradingBot:
    def __init__(self):
        chromedriver = open(os.path.join(driver_dir, chrome_driver_str))
        print(chromedriver.name)
        self.driver = HiddenChromeWebDriver(chromedriver.name)
        # self.driver = webdriver.Chrome(chromedriver.name)
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







