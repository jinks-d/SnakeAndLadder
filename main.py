import logging
import time
from random import randrange


logger = logging.getLogger(__name__)


# adding below as PyCharm does not print anything having level less than warning with logging
logger.info = print


class SnakeAndLadder(object):

    def __init__(self):
        self._position = 0
        self._snakes = {14: 7}

    def _move(self, rollValue = 0) -> None:
        logger.info(f"Current position on board: {self._position}")
        # when you move beyond 100
        if self._position + rollValue > 100:
            logger.info(f"Sorry, you need {100 - self._position} or less to move..")
            return
        # move
        logger.info(f"Moving {rollValue} steps..")
        time.sleep(1)
        self._position += rollValue
        logger.info(f"New position on board: {self._position}")
        # check if you landed on a snake
        self._snakeCheck()

    def _snakeCheck(self) -> None:
        if self._position in self._snakes:
            logger.info("Oh wait!! You got bit by a snake!")
            self._position = self._snakes[self._position]
            logger.info(f"New position on board: {self._position}")

    @staticmethod
    def _diceRoll() -> int:
        val = randrange(1, 7)
        logger.info(f"Dice roll value: {val}")
        return val

    def play(self) -> str:
        for i in range(10):
            logger.info(f"Rolling dice for turn *{i+1}*")
            time.sleep(1)
            # roll
            rollValue = self._diceRoll()
            # move
            self._move(rollValue)
            # check
            if self._position == 100:
                return "You Won!!"
        return f"Final position after 10 turns: {self._position}"


def main():
    res = SnakeAndLadder().play()
    logger.info(f"Result: {res}")
    logger.info("Thanks for playing. Visit again..! :)")


main()
