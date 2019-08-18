import enum


class Status(enum.Enum):
    """
    Enum representing the Status of a position on a goban
    """
    WHITE = 1
    BLACK = 2
    EMPTY = 3
    OUT = 4


class Goban(object):
    def __init__(self, goban):
        self.goban = goban
        self.stonesList = []
        self.eject = False

    def get_status(self, x, y):
        """
        Get the status of a given position

        Args:
            x: the x coordinate
            y: the y coordinate

        Returns:
            a Status
        """
        if not self.goban or x < 0 or y < 0 or y >= len(self.goban) or x >= len(self.goban[0]):
            return Status.OUT
        elif self.goban[y][x] == '.':
            return Status.EMPTY
        elif self.goban[y][x] == 'o':
            return Status.WHITE
        elif self.goban[y][x] == '#':
            return Status.BLACK

    def is_taken(self, x, y):
        # I'm using a reccursion in order to check all the possibilities

        stone = {'x': x, 'y': y} # Current stone coordinates
        color = self.get_status(x, y) # Set color of the stone for comparaison
        stonesList = self.stonesList 

        # Here we get the status of the stones arround
        rightStone = self.get_status(x + 1, y)
        downStone = self.get_status(x, y + 1)
        leftStone = self.get_status(x - 1, y)
        upStone = self.get_status(x, y - 1)
        
        # print('stone', stone)
        # print('stonesList', stonesList)
        # print('leftStone', leftStone, 'rightStone', rightStone, upStone, 'upStone', 'downStone', downStone)

        # If we have ONE empty slot then we need to get out of each reccursion until we completly out.
        if self.eject == True:  
            return False

        # Here we check if we already checked this stone
        if stone in stonesList: 
            return True # If all the stones have been checked we eject the reccursion with True (form surrounded).
        else:
            stonesList.append(stone)


        if Status.EMPTY in (leftStone, rightStone, upStone, downStone):
            self.eject = True # If we find an empty slot, we can eject.
            return False

        # Here we check every direction around the stone.
        elif rightStone == color:
            return self.is_taken(x + 1, y)

        elif downStone == color:

            return self.is_taken(x, y + 1)
        elif leftStone == color:

            return self.is_taken(x - 1, y)
        elif upStone == color:

            return self.is_taken(x, y - 1)
        else:
            return True # For simples cases
