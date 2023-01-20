import unittest
import settings


class MyTestCase(unittest.TestCase):
    def test_get_level(self):
        self.level = settings.get_level()

        self.assertEqual(settings.get_level(), 2)  # add assertion here


if __name__ == '__main__':
    unittest.main()
