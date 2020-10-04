import unittest

from Detemination import determine


class MyTestCase(unittest.TestCase):

    def test_something(self):
        alphabet = ["a", "b", "c"]
        start_machine = [[(1, "c"), (2, "a")],
                         [(1, "b")],
                         [(1, "c"), (3, "c")],
                         [(3, "c")]]
        end_machine = {"0": [("2", "a"), ("1", "c")],
                       "1": [("1", "b")],
                       "2": [("13", "c")],
                       "13": [("1", "b"), ("3", "c")],
                       "3": [("3", "c")]}
        self.assertEqual(determine(alphabet, start_machine), end_machine)


if __name__ == '__main__':
    unittest.main()
