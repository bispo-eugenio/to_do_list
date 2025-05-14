from PySide6.QtWidgets import QApplication
from sys import argv
from components.main_window import MainWindow
from components.buttons import LayoutVButton
from components.display import Display
from components.widget_list import ListItem


if __name__ == "__main__":
    #Variáveis
    app = QApplication(argv)
    display = Display()
    window = MainWindow()
    task_list_widget = ListItem()
    #Configurações
    app.setStyle("Fusion")
    buttons_layout = LayoutVButton(display=display, list_item=task_list_widget)
    window.grid_add_widget(task_list_widget)
    window.grid_add_widget(display, 1, 0)
    window.grid_add_layout(buttons_layout, 0, 1)
    #Execuções
    window.show()
    app.exec()