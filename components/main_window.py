from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        #Atributos e Heranças
        super().__init__(parent, *args, **kwargs)
        self.central_widgets = QWidget()
        self.layout_h_box = QGridLayout()

        #Processos
        self.config_main("To-do", self.central_widgets, self.layout_h_box)

    def config_main(self, title: str, central_widgets: QWidget, layout: QGridLayout) -> None:
        #Título da aplicação
        self.setWindowTitle(title)
        #Central --recebe-> layout e MainWindow --recebe-> central_widgets
        central_widgets.setLayout(layout)
        self.setCentralWidget(central_widgets)
        return

