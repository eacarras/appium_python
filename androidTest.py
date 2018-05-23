__author__ = 'eacarras'
import unittest
from appium import webdriver
import os


class AndroidTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        platform_n = input("Input the name of the platform that will be tested: ").lower()
        if platform_n == "android":
            desired_caps["platformName"] = os.environ["Name_android"]
            desired_caps["platformVersion"] = os.environ["Version_android"]
            desired_caps["deviceName"] = os.environ["device_android"]
        else:
            desired_caps["platformName"] = os.environ["Name_ios"]
            desired_caps["platformVersion"] = os.environ["Version_ios"]
            desired_caps["deviceName"] = os.environ["device_ios"]

        desired_caps["browserName"] = "Chrome"

        self.driver = webdriver.Remote("http://localhost:4723/wb/hub", desired_caps)

    # Compile the test
    def tearDown(self):
        self.driver.quit()

    def simpleSmokeTest(self):
        self.driver.get("http://m.youtube.com")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
