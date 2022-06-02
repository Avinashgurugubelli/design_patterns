"""
    refer: https://realpython.com/factory-method-python/
"""

from abc import ABC, abstractmethod

class IRoom(ABC):
    def __init__(self) -> None:
        self.name= None

class MagicMazeRoom(IRoom):
    def __init__(self) -> None:
        self.name = 'MagicMazeRoom'

class OrdinaryMazeRoom(IRoom):
    def __init__(self) -> None:
        self.name = 'OrdinaryMazeRoom'

class IMazeGame(ABC):
    room: IRoom = None
    def move(self):
        pass
    def turn(self):
        pass
    def start(self):
        pass
    def exit(self):
        pass
    def halt(self):
        pass

    @abstractmethod
    def create_room(self):
        pass

class MagicMageGame(IMazeGame):

    def create_room(self):
        self.room = MagicMazeRoom()
        print(f'{self.room.name} created')

class OrdinaryMageGame(IMazeGame):

    def create_room(self):
        self.room = OrdinaryMazeRoom()
        print(f'{self.room.name} created')

class GameStarter:

    def start(self, game: IMazeGame):
        game.create_room()



if __name__ == "__main__":
    game = GameStarter()
    game.start(MagicMageGame())
    game.start(OrdinaryMageGame())




