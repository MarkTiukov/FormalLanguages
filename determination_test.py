import unittest

from Detemination import determine


class MyTestCase(unittest.TestCase):

    def test_determination(self):
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
        start_final_states = {"1", "3"}
        end_final_states = {"1", "3", "13"}
        self.assertEqual(determine(alphabet, start_machine, start_final_states)[0], end_machine)
        self.assertEqual(determine(alphabet, start_machine, start_final_states)[1], end_final_states)


if __name__ == '__main__':
    unittest.main()
