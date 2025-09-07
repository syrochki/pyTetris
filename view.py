from constructor import UIConstructor

from pyglet.window import Window


class UIView:
    def __init__(self) -> None:
        self.window = Window(width=1920, height=1800, caption="Tetris!")  # type: ignore
        self.ui = UIConstructor(window=self.window)

    def setup_ui(self) -> None:
        center_x = self.window.width // 2
        center_y = self.window.height // 2

        self.ui.create_label(
            text="Привет#1!", x=center_x, y=center_y, color=(153, 255, 255)
        )
        self.ui.create_label(
            text="Привет#2!", x=center_x, y=center_y - 50, color=(255, 0, 0)
        )

    def on_draw(self) -> None:
        """Отрисовка окна с интерфейсом"""
        self.window.clear()
        self.ui.draw_all_objects()
