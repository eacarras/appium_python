__author__ = 'eacarras'
import unittest
from appium import webdriver


class AndroidTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6.0.1"
        desired_caps["deviceName"] = "Galaxy"
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
