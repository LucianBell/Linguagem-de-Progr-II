# Exceção para quando o jogador leva o personagem para fora das bordas da tela
class OutOfBounds(Exception):
    def __init__(self, message="Player got out of game boundries."):
        self.message = message
        super().__init__(self.message)


# Exceção para quando o loop do inimigo não é executado corretamente
class EnemyLoopError(Exception):
    def __init__(self,
                 message="Enemy loop did not work correctly. Try to restart your game and review enemy's respawn point."):
        self.message = message
        super().__init__(self.message)


# Exceção para quando o loop do level não é executado corretamente
class ScreenDrawingError(Exception):
    def __init__(self,
                 message="Screen was not loaded correctly. Try to restart your game and review the screen functions."):
        self.message = message
        super().__init__(self.message)
