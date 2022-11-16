import random

def not_quite_right(numOfSticks: int) -> int:
    """
    Takes number of sticks from board and returns number of sticks that shoudl be added back to the board.
    Has 30% chances that 1-to-4 sticks are added back to the total number of sticks in play.
    Cannot return more than 20 sticks on the board.

    Args:
        numOfSticks: int
    
    Returns:
        int
    """
    if numOfSticks == 1:
        return "you lose"
    else:
        if random.random() <= .3:
            numOfSticks += random.randrange(1, 5)
            if numOfSticks > 20:
                numOfSticks -= (numOfSticks - 20)
    return numOfSticks

def display_board(numOfSticks: int) -> None:
    """
    Displays number of sticks on the board

    Args:
        numOfSticks: int
    
    Returns:
        none
    """
    for row in range(6):
        for (stick) in range(numOfSticks):
            if row == 5:
                print(stick+1, end="  ")
            else:
                if stick+1 >= 10:
                    print("|", end="   ")
                else:
                    print("|", end="  ")
        print()

def get_sticks_to_take(currentPlayer: int=None, numOfSticks: int=None) -> int:
    """
    Takes in current player and number of sticks on the board and then returns the number of sticks to be taken by the player.
    Should handle cases where player takes too few or too many sticks.

    Args:
        currentPlayer: int,
    
        numOfSticks: int

    Returns:
        int
    """
    isWithinSelection = False

    while not isWithinSelection:
        try:
            playerSticks = int(input("Select a number of sticks between 1-3 >> "))
            if 3 >= playerSticks >= 1:
                isWithinSelection = True
            else:
                print("Your selection must be between 1 and 3")
                continue
        except (ValueError, TypeError):
            print("You must enter numerical values")
            continue
    return playerSticks


def display_summary(
    currentPlayer: int,
    playersNumOfSticks: int,
    addedNumOfSticks: int,
    remainingNumOfSticks: int
) -> None:
    """
    Takes the four paramets and displays the following formatted string:
    "Player <currentPlayer> took <taken>, pictsie shenanigans added <added> back, leaving <remaining>"

    Args:
        currentPlayer: int,
        playersNumOfSticks: int,
        addedNumOfSticks: int,
        remainingNumOfSticks: int
    
    Returns:
        None
    """
    print("Player {0} took {1}, pictsie shenanigans added {2} back, leaving {3} sticks".format(
        currentPlayer,
        playersNumOfSticks,
        addedNumOfSticks,
        remainingNumOfSticks
    ))

def main():
    """
    Main logic of the program
    """
    baseNumofSticksOnBoard = 20
    player_switch = {True: 1, False: 2}
    player_state = True

    while baseNumofSticksOnBoard >= 1:
        current_player = player_switch[player_state]
        display_board(baseNumofSticksOnBoard)
        selectedSticks = get_sticks_to_take()
        baseNumofSticksOnBoard -= selectedSticks
        display_summary(
            currentPlayer=current_player,
            playersNumOfSticks=selectedSticks,
            addedNumOfSticks=not_quite_right(baseNumofSticksOnBoard),
            remainingNumOfSticks=baseNumofSticksOnBoard
        )
        player_state = not player_state
    else:
        print("Sorry, player {} lost".format(current_player))

main()