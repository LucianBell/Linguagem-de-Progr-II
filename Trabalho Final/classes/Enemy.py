from abc import ABC, abstractmethod


class Enemy(ABC):
    @abstractmethod
    def update_enemy(self):
        pass

    @abstractmethod
    def draw_enemy(self):
        pass
