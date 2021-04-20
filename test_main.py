from unittest import TestCase
from main import SnakeAndLadder


class TestSnakeAndLadder(TestCase):

    def setUp(self) -> None:
        self._game = SnakeAndLadder()

    def test_init(self):
        self.assertEqual(self._game._position, 0)
        self.assertEqual(self._game._snakes, {14: 7})

    def test_diceRoll(self):
        res = self._game._diceRoll()
        self.assertTrue(res in range(1, 7))

    def test_snakeCheck(self):
        # dummy values
        self._game._position = 14
        self._game._snakeCheck()
        self.assertEqual(self._game._position, 7)
        self.assertLogs("Oh wait!! You got bit by a snake!", level='info')
        self.assertLogs("New position on board: 7", level='info')

    def test_move(self):
        # normal scenario
        ## dummy values
        self._game._position = 40
        dummyRollValue = 6
        ## function call
        self._game._move(dummyRollValue)
        ## check
        self.assertLogs("Current position on board: 40", level='info')
        self.assertLogs("Moving 4 steps..", level='info')
        self.assertLogs("New position on board: 44", level='info')

        # when roll value moves you beyond 100
        ## dummy values
        self._game._position = 95
        dummyRollValue = 6
        # function call
        self._game._move(dummyRollValue)
        # check
        self.assertLogs("Current position on board: 95", level='info')
        self.assertLogs(f"Sorry, you need 5 or less to move..", level='info')

    def test_play(self):
        self.assertIsInstance(self._game.play(), str)