import logging
import time
from random import randrange


logger = logging.getLogger(__name__)


# adding below as PyCharm does not print anything having level less than warning with logging
logger.info = print


class SnakeAndLadder(object):

    def __init__(self) -> None:
        """

        :return: None
        """
        # initialize
        self._snakes = {14: 7}
        self._position = 0
        self._isCrookedDice = None

    def _move(self, rollValue = 0) -> None:
        """
        Move position on board depending on dice roll value

        :param int rollValue: Value of the rolled dice
        :return: None
        """
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
        """
        Checks if current position has a snake on it or not

        :return: None
        """
        if self._position in self._snakes:
            logger.info("Oh wait!! You got bit by a snake!")
            # reset position to snake's tail
            self._position = self._snakes[self._position]
            logger.info(f"New position on board: {self._position}")

    def _diceRoll(self) -> int:
        """
        Rolls a dice and returns the value

        :return: None
        """
        # generate a random number
        val = randrange(1, 7) if not self._isCrookedDice else randrange(2, 7, 2)
        logger.info(f"Dice roll value: {val}")
        return val

    def play(self) -> str:
        """
        Snake and Ladder game is executed via this method

        :return: None
        """
        # ask which type of dice to be used
        self._isCrookedDice = self._getUserInput()
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

    def _getUserInput(self) -> bool:
        """
        Prompts to the user for a choice of dice

        :return: bool
        """
        print("""
                We have 2 types of dice, a Normal and a Crooked one.
                Enter 1 to choose Normal dice.
                Enter 2 to choose Crooked dice.
            """)
        isCrooked = int(input()) == 2
        logger.info(f"You have chosen a {'Crooked' if isCrooked else 'Normal'} dice..")
        return isCrooked


def main():
    res = SnakeAndLadder().play()
    logger.info(f"Result: {res}")
    logger.info("Thanks for playing. Visit again..! :)")


main()
