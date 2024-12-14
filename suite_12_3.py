import unittest
import tests_12_2

rt_Test = unittest.TestSuite()
rt_Test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.RunnerTest))
rt_Test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(rt_Test)