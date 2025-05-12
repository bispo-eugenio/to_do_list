#Import
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QListWidgetItem
from PySide6.QtGui import QIcon, QPixmap
from constants import IMAG_ADD, IMAG_UPD, IMAG_DEL, SMALL_SIZE, BIG_SIZE
from components.display import Display
from components.widget_list import ListItem
from utils import is_empty
from constants import G_PRIMARY_COLOR, G_SECONDARY_COLOR, G_TERTIARY_COLOR



#==================LayoutButton==================

class LayoutVButton(QVBoxLayout):
    def __init__(self,  parent: QWidget | None = None, display: Display | None = None,
                 list_item: ListItem | None = None):
        #Atributos e Heranças
        super().__init__(parent)
        self._display = display
        self._list_item = list_item
        self._add_button = ApplyButton(display= self._display, list_item= self._list_item)
        self._upd_button = UpdateButton()
        self._del_button = DeleteButton()

        #Adicionando os botões no LayoutVButton
        self.addWidget(self._add_button)
        self.addWidget(self._upd_button)
        self.addWidget(self._del_button)


#==================Buttons==================
#-> ADICIONAR
class ApplyButton(QPushButton):
    def __init__(self, parent: QWidget | None = None, display: Display | None = None,
                 list_item: ListItem | None = None, *args, **kwargs):
        #Atributos e Heranças
        super().__init__(parent, *args, **kwargs)
        self._display = display
        self._list_item = list_item
        self._icon = QIcon(str(IMAG_ADD))
        #Configurações
        self.config_apply_button()
        self.config_style()
        self.clicked.connect(self.add_item_button)

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
    def add_item_button(self) -> None:
        item = QListWidgetItem()
        text = self._display.text()
        if not is_empty(text):
            item.setText(text)
            self._list_item.insertItem(self._list_item.count, item)
            self._list_item.count += 1
        return

#-> DELETAR
class DeleteButton(QPushButton):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._icon = QIcon(str(IMAG_DEL))
        self.config_del_button(self._icon)

    def config_del_button(self, icon: QIcon | QPixmap) -> None:
        self.setText("Deletar")
        self.setIcon(icon)
        self.setFixedHeight(SMALL_SIZE)
        self.setFixedWidth(BIG_SIZE)
        return

    #Falta Funcionalidade de Apagar e Lógica para apagar

#-> ATUALIZAR
class UpdateButton(QPushButton):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._icon = QIcon(str(IMAG_UPD))
        self.config_upd_button(self._icon)

    def config_upd_button(self, icon: QIcon | QPixmap) -> None:
        self.setText("Atualizar")
        self.setIcon(icon)
        self.setFixedHeight(SMALL_SIZE)
        self.setFixedWidth(BIG_SIZE)
        return
    #Falta Funcionalidade de Atualizar e Lógica