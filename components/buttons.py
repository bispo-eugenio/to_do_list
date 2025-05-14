#Import
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QListWidgetItem
from PySide6.QtGui import QIcon
from constants import IMAG_ADD, IMAG_UPD, IMAG_DEL, SMALL_SIZE, BIG_SIZE
from components.display import Display
from components.widget_list import ListItem
from utils import is_empty
from constants import (G_PRIMARY_COLOR, G_SECONDARY_COLOR, G_TERTIARY_COLOR,
                       B_PRIMARY_COLOR, B_SECONDARY_COLOR, B_TERTIARY_COLOR,
                       R_PRIMARY_COLOR, R_SECONDARY_COLOR, R_TERTIARY_COLOR)

#==================LayoutButton==================

class LayoutVButton(QVBoxLayout):
    def __init__(self,  parent: QWidget | None = None, display: Display | None = None,
                 list_item: ListItem | None = None) -> None:
        #Atributos e Heranças
        super().__init__(parent)
        self._display = display
        self._list_item = list_item
        self._add_button = ApplyButton(display= self._display, list_item= self._list_item)
        self._upd_button = UpdateButton(display= self._display, list_item= self._list_item)
        self._del_button = DeleteButton(display= self._display, list_item= self._list_item)

        #Adicionando os botões no LayoutVButton
        self.addWidget(self._add_button)
        self.addWidget(self._upd_button)
        self.addWidget(self._del_button)


#==================Buttons==================

#-> ADICIONAR ITEM
class ApplyButton(QPushButton):
    def __init__(self, parent: QWidget | None = None, display: Display | None = None,
                 list_item: ListItem | None = None, *args, **kwargs) -> None:
        #Atributos e Heranças
        super().__init__(parent, *args, **kwargs)
        self._display = display
        self._list_item = list_item
        self._icon = QIcon(str(IMAG_ADD))
        #Configurações
        self.config_apply_button()
        self.config_style()
        self.clicked.connect(self.add_item)

    #Configuração do botão
    def config_apply_button(self) -> None:
        self.setText("Adicionar")
        self.setIcon(self._icon)
        self.setFixedHeight(SMALL_SIZE)
        self.setFixedWidth(BIG_SIZE)
        return

    #Estilo do botão
    def config_style(self) -> None:
        self.setStyleSheet(f"""
                QPushButton{{
                    color: #fff;
                    background: {G_PRIMARY_COLOR};
                    border-radius: 4px;
                    font-family: arial;
                    font-size: 12px
                }}
                QPushButton:hover{{
                    color: #fff;
                    background: {G_SECONDARY_COLOR};
                }}
                QPushButton:pressed{{
                    color: #fff;
                    background: {G_TERTIARY_COLOR};
                }}
                """)
        return

    #Adiciona item na lista
    def add_item(self) -> None:
        item = QListWidgetItem()
        text = self._display.text()
        if not is_empty(text):
            item.setText(text)
            self._list_item.insertItem(self._list_item.count_item, item)
            self._list_item.count_item += 1
            print(self._list_item.count_item)
        return

#-> DELETAR ITEM
class DeleteButton(QPushButton):
    def __init__(self, parent: QWidget | None = None, display: Display | None = None,
                 list_item: ListItem | None = None, *args, **kwargs) -> None:
        #Atributos e Heranças
        super().__init__(parent, *args, **kwargs)
        self._display = display
        self._list_item = list_item
        self._icon = QIcon(str(IMAG_DEL))
        #Cofigurações
        self.config_del_button()
        self.config_style()
        self.clicked.connect(self.del_item) #-> Falta slot()

    def config_del_button(self) -> None:
        self.setText("Deletar")
        self.setIcon(self._icon)
        self.setFixedHeight(SMALL_SIZE)
        self.setFixedWidth(BIG_SIZE)
        return

    #Estilo do botão
    def config_style(self) -> None:
        self.setStyleSheet(f"""
                QPushButton{{
                    color: #fff;
                    background: {R_PRIMARY_COLOR};
                    border-radius: 4px;
                    font-family: arial;
                    font-size: 12px
                }}
                QPushButton:hover{{
                    color: #fff;
                    background: {R_SECONDARY_COLOR};
                }}
                QPushButton:pressed{{
                    color: #fff;
                    background: {R_TERTIARY_COLOR};
                }}
                """)
        return
    def del_item(self) -> None:
        current_row = self._list_item.currentRow()
        if current_row >= 0:
            self._list_item.takeItem(current_row)
            self._list_item.count_item -= 1
        return

#-> ATUALIZAR ITEM
class UpdateButton(QPushButton):
    def __init__(self, parent: QWidget | None = None, display: Display | None = None,
                 list_item: ListItem | None = None, *args, **kwargs) -> None:
        #Atributos e Heranças
        super().__init__(parent, *args, **kwargs)
        self._display = display
        self._list_item = list_item
        self._icon = QIcon(str(IMAG_UPD))
        #Configurações
        self.config_upd_button()
        self.config_style()
        self.clicked.connect(self.upd_item)


    def config_upd_button(self) -> None:
        self.setText("Atualizar")
        self.setIcon(self._icon)
        self.setFixedHeight(SMALL_SIZE)
        self.setFixedWidth(BIG_SIZE)
        return

    #Estilo do botão
    def config_style(self) -> None:
        self.setStyleSheet(f"""
                QPushButton{{
                    color: #fff;
                    background: {B_PRIMARY_COLOR};
                    border-radius: 4px;
                    font-family: arial;
                    font-size: 12px
                }}
                QPushButton:hover{{
                    color: #fff;
                    background: {B_SECONDARY_COLOR};
                }}
                QPushButton:pressed{{
                    color: #fff;
                    background: {B_TERTIARY_COLOR};
                }}
                """)
        return

    def upd_item(self) -> None:
        #Variáveis
        item = QListWidgetItem()
        text = self._display.text()
        item.setText(text)
        current_row = self._list_item.currentRow()
        #Se o display estiver vazio não funciona
        if not is_empty(text):
            #Limpa caso a seleção seja o primeiro row/linha
            if self._list_item.count_item == 1:
                self._list_item.clear()
                self._list_item.insertItem(current_row, item)
            #Caso seja outros items
            if self._list_item.selectedItems():
                self._list_item.takeItem(current_row)
                self._list_item.insertItem(current_row, item)
        return