import rt_with_exceptions
import unittest
import logging


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner_walk = rt_with_exceptions.Runner(10, 20)
            for i in range(10):
                runner_walk.walk()
            self.assertEqual(runner_walk.distance, 50)
            logging.info(f'"test_walk" выполнен успешно {runner_walk}')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner_run = rt_with_exceptions.Runner('Run2', -55)
            for i in range(10):
                runner_run.run()
            self.assertEqual(runner_run.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
            return 0

    def test_challenge(self):
        runner_1 = rt_with_exceptions.Runner('Run3')
        runner_2 = rt_with_exceptions.Runner('Run4')
        for i in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log', encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")


