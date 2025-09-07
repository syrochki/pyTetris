from typing import Literal, Any

from pyglet.window import Window
from pyglet.text import Label


class UIConstructor:
    def __init__(self, window: Window) -> None:
        self.window = window
        self.labels: list[Label] = []

    def create_label(
        self,
        *,
        text: str,
        x: float,
        y: float,
        **kwargs: Any,
    ) -> Label:

        default_label_params: dict[str, Any] = {
            "z": 1,
            "anchor_x": "center",
            "anchor_y": "center",
            "font_name": "Cooper",
            "font_size": 24,
        }

        default_label_params.update(kwargs)

        label = Label(text, x, y, **default_label_params)
        self.labels.append(label)
        return label

    def draw_all_objects(self) -> None:
        for object in self.labels:
            object.draw()
