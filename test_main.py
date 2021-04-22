from unittest import mock, TestCase
from main import SnakeAndLadder


class TestSnakeAndLadder(TestCase):

    def setUp(self):
        self._game = SnakeAndLadder()

    def test_init(self):
        self.assertEqual(self._game._snakes, {14: 7})
        self.assertEqual(self._game._position, 0)
        self.assertEqual(self._game._greenSnakes, {12: 5})
        self.assertFalse(self._game._isBitByGreen)
        self.assertIsNone(self._game._isCrookedDice)

    def test_diceRoll_normal_dice(self):
        res = self._game._diceRoll()
        self.assertTrue(res in range(1, 7))

    @mock.patch('main.SnakeAndLadder._getUserInput', return_value=True)
    def test_diceRoll_crooked_dice(self, userInput):
        self._game.play()
        res = self._game._diceRoll()
        self.assertTrue(res in [2, 4, 6])

    def test_snakeCheck_with_snake(self):
        # dummy values
        self._game._position = 14
        # function call
        self._game._snakeCheck()
        # check
        self.assertEqual(self._game._position, 7)
        self.assertLogs("Oh wait!! You got bit by a snake!", level='info')
        self.assertLogs("New position on board: 7", level='info')

    def test_snakeCheck_without_snake(self):
        self._game._position = 13
        self._game._snakeCheck()
        # check to ensure current position remains unchanged as we don't have a snake at 13
        self.assertEqual(self._game._position, 13)

    def test_move_normal_scenario(self):
        # dummy values
        self._game._position = 40
        dummyRollValue = 6
        # function call
        self._game._move(dummyRollValue)
        # check
        self.assertLogs("Current position on board: 40", level='info')
        self.assertLogs("Moving 6 steps..", level='info')
        self.assertLogs("New position on board: 46", level='info')

    def test_move_when_you_go_beyond_100(self):
        # dummy values
        self._game._position = 95
        dummyRollValue = 6
        # function call
        self._game._move(dummyRollValue)
        # check
        self.assertLogs("Current position on board: 95", level='info')
        self.assertLogs(f"Sorry, you need 5 or less to move..", level='info')

    @mock.patch("main.SnakeAndLadder._getUserInput", return_value=False)
    def test_play_normal_dice(self, userInput):
        self.assertIsInstance(self._game.play(), str)

    @mock.patch("main.SnakeAndLadder._getUserInput", return_value=True)
    def test_play_crooked_dice(self, userInput):
        self.assertIsInstance(self._game.play(), str)