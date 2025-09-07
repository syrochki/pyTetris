from view import UIView

from pyglet import app
from pyglet.window import key


class Game:
    def __init__(self) -> None:
        self.view = UIView()

        self.view.window.event(self.view.on_draw)
        self.view.window.event(self.on_key_press)

    def on_key_press(self, symbol: int, modifiers: int) -> None:

        if symbol == key.A:
            print("A")
        elif symbol == key.W:
            print("W")
        elif symbol == key.S:
            print("S")
        elif symbol == key.D:
            print("D")

        if modifiers & key.MOD_CTRL:
            print("MOD_CTRL")
        elif modifiers & key.MOD_SHIFT:
            print("MOD_SHIFT")

    def run(self) -> None:
        """Метод запуска игры"""
        self.view.setup_ui()
        app.run()
