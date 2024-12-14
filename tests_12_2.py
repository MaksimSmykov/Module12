import unit_tests_methods as utm
import runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner1 = runner.Runner('Максим')
        for _ in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner2 = runner.Runner('Сергей')
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = runner.Runner('Максим')
        runner2 = runner.Runner('Сергей')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        tournament1 = utm.Tournament(90, self.runner1, self.runner3)
        all_results = tournament1.start()
        self.assertEqual(all_results[max(all_results)], self.runner3)
        TournamentTest.all_results[1] = all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        tournament2 = utm.Tournament(90, self.runner2, self.runner3)
        all_results = tournament2.start()
        self.assertEqual(all_results[max(all_results)], self.runner3)
        TournamentTest.all_results[2] = all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        tournament3 = utm.Tournament(90, self.runner1, self.runner2, self.runner3)
        all_results = tournament3.start()
        self.assertEqual(all_results[max(all_results)], self.runner3)
        TournamentTest.all_results[3] = all_results


if __name__ == '__main__':
    unittest.main()