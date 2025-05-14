from PySide6.QtWidgets import QListWidget, QWidget

class ListItem(QListWidget):

    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.count_item = 0

    def config_list(self):
        ...