from PySide6.QtWidgets import QApplication
from sys import argv
from components.main_window import MainWindow
from components.buttons import LayoutVButton
from components.display import Display
from components.widget_list import ListItem


if __name__ == "__main__":
    #Variáveis
    app = QApplication(argv)
    window = MainWindow()
    display = Display()
    buttons_layout = LayoutVButton()
    list_todo = ListItem()
    #Configurações
    window.layout_h_box.addWidget(list_todo)
    window.layout_h_box.addWidget(display,1,0)
    window.layout_h_box.addLayout(buttons_layout,0,1)
    #Execuções
    window.show()
    app.exec()