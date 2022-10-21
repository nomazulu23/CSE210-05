import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        #self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        cycle1 = cast.get_first_actor("cycle1")
        direction1 = Point(0, 0)
        # left
        if self._keyboard_service.is_key_down('a'):
            direction1 = Point(-constants.CELL_SIZE, 0)
    
        # right
        if self._keyboard_service.is_key_down('d'):
            direction1 = Point(constants.CELL_SIZE, 0)
    
        # up
        if self._keyboard_service.is_key_down('w'):
            direction1 = Point(0, -constants.CELL_SIZE)
    
        # down
        if self._keyboard_service.is_key_down('s'):
            direction1 = Point(0, constants.CELL_SIZE)

        cycle1.turn_head(direction1)

        cycle2 = cast.get_first_actor("cycle2")
        direction2 = Point(0, 0)
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)
    
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)
    
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)
    
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)

        cycle2.turn_head(direction2)
        
       