from PySide6.QtWidgets import QWidget, QLineEdit


class Display(QLineEdit):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
    def config_style(self):
        ...
