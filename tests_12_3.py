import runner
import runner_and_tournament
import unittest
import random


def generate_random_name():
    name = ""
    vowels = 'ауеыоэёяию'
    consonants = 'бвгджзйклмнпрстфхцчшщь'

    for i in range(2):
        name += random.choice(consonants)
        name += random.choice(vowels)

    name = name.capitalize()
    return name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_1 = runner.Runner(generate_random_name())
        for i in range(10):
            runner.Runner.walk(runner_1)
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_1 = runner.Runner(generate_random_name())
        for i in range(10):
            runner.Runner.run(runner_1)
        self.assertEqual(runner_1.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = runner.Runner(generate_random_name())
        runner_2 = runner.Runner(generate_random_name())

        methods = [runner.Runner.run, runner.Runner.walk]

        for i in range(10):
            random.choice(methods)(runner_1)
            random.choice(methods)(runner_2)
        self.assertNotEqual(runner_1.distance, runner_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()

    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner_3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        race = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3)
        results = race.start()
        formatted_results = {place: runner.name for place, runner in results.items()}
        self.__class__.all_results['test_1'] = formatted_results
        participants = list(race.participants)
        last_participant = participants[-1]
        self.assertTrue(results[len(participants)] == last_participant.name)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        race = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        results = race.start()
        formatted_results = {place: runner.name for place, runner in results.items()}
        self.__class__.all_results['test_2'] = formatted_results
        participants = list(race.participants)
        last_participant = participants[-1]
        self.assertTrue(results[len(participants)] == last_participant.name)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        race = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = race.start()
        formatted_results = {place: runner.name for place, runner in results.items()}
        self.__class__.all_results['test_3'] = formatted_results
        participants = list(race.participants)
        last_participant = participants[-1]
        self.assertTrue(results[len(participants)] == last_participant.name)


if __name__ == '__main__':
    unittest.main()
