import unittest

start_machine = {"0": [("1", "a"), ("3", "b")],
                 "1": [("2", "a"), ("4", "b")],
                 "2": [("0", "a"), ("5", "b")],
                 "3": [("4", "a"), ("6", "b")],
                 "4": [("5", "a"), ("7", "b")],
                 "5": [("3", "a"), ("8", "b")],
                 "6": [("7", "a"), ("0", "b")],
                 "7": [("8", "a"), ("1", "b")],
                 "8": [("6", "a"), ("2", "b")]}

final_states = {"0", "4", "8"}

alphabet = ["a", "b"]

classes = {'0': 0, '1': 1, '3': 2, '2': 2, '4': 0, '6': 1, '5': 1, '7': 2, '8': 0}


class MyTestCase(unittest.TestCase):
    def test_something(self):
        from Minimization import minimize
        self.assertEqual(minimize(start_machine, alphabet, final_states), classes)


if __name__ == '__main__':
    unittest.main()
