from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout, QLayout


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        #Atributos e Heranças
        super().__init__(parent, *args, **kwargs)
        self.central_widgets = QWidget()
        self._grid_layout = QGridLayout()

        #Processos
        self.config_main("To-do")

    #Configura a Main Window
    def config_main(self, title: str) -> None:
        #Título da aplicação
        self.setWindowTitle(title)
        #Central --recebe-> layout e MainWindow --recebe-> central_widgets
        self.central_widgets.setLayout(self._grid_layout)
        self.setCentralWidget(self.central_widgets)
        return

    #Adiciona um widget no layout_h_box
    def grid_add_widget(self, widget: QWidget, row: int = 0, column: int = 0) -> None:
        self._grid_layout.addWidget(widget, row, column)
        return

    #Adiciona um layout dentro do layout_h_box
    def grid_add_layout(self, layout: QLayout, row: int = 0, column: int = 0) -> None:
        self._grid_layout.addLayout(layout, row, column)
        return