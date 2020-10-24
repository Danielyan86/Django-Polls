import time
import unittest

from selenium import webdriver


class Polls(unittest.TestCase):

    def test_index(self):
        url = "http://127.0.0.1:8000/"
        d = webdriver.Chrome()
        # 输入URL
        d.get(url)
        time.sleep(1)
        self.assertEqual(d.title, "")
        d.close()


if __name__ == '__main__':
    unittest.main()
