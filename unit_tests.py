import unit_tests_methods as utm
import unittest

class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.runner1 = utm.Runner('Усэйн', 10)
        self.runner2 = utm.Runner('Андрей', 9)
        self.runner3 = utm.Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
            result = {}
            for key, value in i.items():
                result[key] = value.name
            print(result)

    def test_tournament1(self):
        tournament1 = utm.Tournament(90, self.runner1, self.runner3)
        all_results = tournament1.start()
        self.assertEqual(all_results[max(all_results)], self.runner3)
        TournamentTest.all_results[1] = all_results

    def test_tournament2(self):
        tournament2 = utm.Tournament(90, self.runner2, self.runner3)
        all_results = tournament2.start()
        self.assertEqual(all_results[max(all_results)], self.runner3)
        TournamentTest.all_results[2] = all_results

    def test_tournament3(self):
        tournament3 = utm.Tournament(90, self.runner1, self.runner2, self.runner3)
        all_results = tournament3.start()
        self.assertEqual(all_results[max(all_results)], self.runner3)
        TournamentTest.all_results[3] = all_results


if __name__ == '__main__':
    unittest.main()