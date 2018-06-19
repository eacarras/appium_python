__author__ = 'eacarras'
__name__ = '__main__'
import unittest
from appium import webdriver
import os
from time import sleep


class AndroidTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps["platformName"] = os.environ[""]
        desired_caps["platformVersion"] = os.environ[""]
        desired_caps["deviceName"] = os.environ[""]

        desired_caps["browserName"] = "Chrome"

        self.driver = webdriver.Remote("http://localhost:4723/wb/hub", desired_caps)

    # Here you put all the smoke/regression/bvt test
    def simpleSmokeTest(self):
        self.driver.get("http://m.youtube.com")
        
    # Compile the test
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
