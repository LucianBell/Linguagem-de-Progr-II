class OutOfBounds(Exception):
    def __init__(self, message="Player got out of game boundries."):
        self.message = message
        super().__init__(self.message)


class EnemyLoopError(Exception):
    def __init__(self,
                 message="Enemy loop did not work correctly. Try to restart your game and review enemy's respawn point."):
        self.message = message
        super().__init__(self.message)
