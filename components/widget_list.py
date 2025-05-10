from PySide6.QtWidgets import QListWidget, QWidget

class ListItem(QListWidget):

    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
    def config_list(self):
        ...