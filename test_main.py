from unittest import TestCase
from main import SnakeAndLadder

class TestSnakeAndLadder(TestCase):
    def setUp(self) -> None:
        self._game = SnakeAndLadder()

    def test_init(self):
        self.assertEqual(self._game._position, 0)

    def test_diceRoll(self):
        res = self._game._diceRoll()
        self.assertTrue(res in range(1, 7))

    def test_move(self):
        # normal scenario
        self._game._position = 40
        dummyRollValue = 6
        self._game._move(dummyRollValue)
        self.assertLogs("Current position on board: 40")
        self.assertLogs("Moving 4 steps..", level='info')
        self.assertLogs("New position on board: 44", level='info')
        # when roll value moves you beyond 100
        self._game._position = 95
        dummyRollValue = 6
        self._game._move(dummyRollValue)
        self.assertLogs("Current position on board: 95")
        self.assertLogs(f"Sorry, you need 5 or less to move..", level='info')

    def test_play(self):
        self.assertIsInstance(self._game.play(), str)