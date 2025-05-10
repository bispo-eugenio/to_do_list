#Import
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PySide6.QtGui import QIcon, QPixmap
from constants import IMAG_ADD, IMAG_UPD, IMAG_DEL, SMALL_SIZE, BIG_SIZE


#==================LayoutButton==================

class LayoutVButton(QVBoxLayout):
    def __init__(self,  parent: QWidget | None = None):
        #Atributos e Heranças
        super().__init__(parent)
        self._add_button = ApplyButton()
        self._upd_button = UpdateButton()
        self._del_button = DeleteButton()

        #Adicionando os botões no LayoutVButton
        self.addWidget(self._add_button)
        self.addWidget(self._upd_button)
        self.addWidget(self._del_button)


#==================Buttons==================
#-> ADICIONAR
class ApplyButton(QPushButton):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._icon = QIcon(str(IMAG_ADD))
        self.config_apply_button(self._icon)


    def config_apply_button(self, icon: QIcon | QPixmap) -> None:
        self.setText("Adicionar")
        self.setIcon(icon)
        self.setFixedHeight(SMALL_SIZE)
        self.setFixedWidth(BIG_SIZE)
        return
    # Falta Funcionalidade de Adicionar

#-> DELETAR
class DeleteButton(QPushButton):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._icon = QIcon(str(IMAG_DEL))
        self.config_del_button(self._icon)

    def config_del_button(self, icon: QIcon | QPixmap) -> None:
        self.setText("Deletar")
        self.setIcon(self._icon)
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