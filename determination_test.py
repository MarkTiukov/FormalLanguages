import unittest

from Detemination import determine, makeTotal

alphabet = ["a", "b", "c"]
nka_machine = [[(1, "c"), (2, "a")],
               [(1, "b")],
               [(1, "c"), (3, "c")],
               [(3, "c")]]
dka_machine = {"0": [("2", "a"), ("1", "c")],
               "1": [("1", "b")],
               "2": [("1#3", "c")],
               "1#3": [("1", "b"), ("3", "c")],
               "3": [("3", "c")]}
pdka_machine = {"0": [("2", "a"), ("1", "c"), ("5", "b")],
                "1": [("1", "b"), ("5", "a"), ("5", "c")],
                "2": [("1#3", "c"), ("5", "a"), ("5", "b")],
                "1#3": [("1", "b"), ("3", "c"), ("5", "a")],
                "3": [("3", "c"), ("5", "a"), ("5", "b")],
                "5": [("5", "a"), ("5", "b"), ("5", "c")]}
nka_final_states = {"1", "3"}
dka_final_states = {"1", "3", "1#3"}


class MyTestCase(unittest.TestCase):
    global alphabet, nka_machine, dka_machine

    def test_determination(self):
        self.assertEqual(determine(alphabet, nka_machine, nka_final_states)[0], dka_machine)
        self.assertEqual(determine(alphabet, nka_machine, nka_final_states)[1], dka_final_states)

    def test_making_total(self):
        self.assertEqual(makeTotal(dka_machine, alphabet), pdka_machine)


if __name__ == '__main__':
    unittest.main()
