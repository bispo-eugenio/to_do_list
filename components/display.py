from PySide6.QtWidgets import QWidget, QLineEdit
from PySide6.QtCore import QTimer, Signal, Slot
from PySide6.QtGui import QKeyEvent, Qt
from constants import MARGIN_TEXT, BACKGROUN_LINE_EDIT_OR_LIST, BORDER_LINE_EDIT_OR_LIST
from utils import is_empty

class Display(QLineEdit):
    add_pressed = Signal()
    upd_pressed = Signal()
    del_input_pressed = Signal()
    espace_pressed = Signal()
    letter_or_number_pressed = Signal(str)
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config_style()
        #Garante o foco após a execução da aplicação
        """Explicação
        -> O Qtimer consegue colocar temporizadores para poder agendar uma ação durante a execução. Ele serve
        propriamente para poder acionar ações repetidas ou atrasar execução, como necesse caso, que estou usando o 
        QTimer.singleShot para poder executar a ação set.focus() após a execução do programa.
        """
        QTimer.singleShot(0, self.setFocus)
        self.config_line_edit()
        self.letter_or_number_pressed.connect(self.insert_text)
        self.del_input_pressed.connect(self.del_text)
        self.espace_pressed.connect(self._espace)

    def config_style(self):
        self.setStyleSheet(f"""
                        QLineEdit{{
                            color: #fff;
                            background: "{BACKGROUN_LINE_EDIT_OR_LIST}";
                            border: 2px solid "{BORDER_LINE_EDIT_OR_LIST}";
                            font-family: arial;
                            font-size: 14px
                        }}
                        """)
    def config_line_edit(self):
        self.setPlaceholderText("Adicione um item na lista...")
        margin_text:list[int] = [MARGIN_TEXT for _ in range(4)]
        self.setTextMargins(*margin_text) #type: ignore
        return
    #Usando sobrecarga de métodos para realizar o polimofismo em tempo de execução para manipula as teclas
    def keyPressEvent(self, event:QKeyEvent):
        key = event.key()
        text = event.text()
        KEY = Qt.Key
        is_add = key == KEY.Key_Return
        is_update = key == KEY.Key_F2
        is_delete_input = key == KEY.Key_Backspace
        is_espace = key == KEY.Key_Space

        if is_add:
            self.add_pressed.emit()
            return event.ignore()
        elif is_delete_input:
            self.del_input_pressed.emit()
        elif is_espace:
            self.espace_pressed.emit()
            return event.ignore()
        elif is_empty(text):
            return event.ignore()
        elif text.isalnum():
            self.letter_or_number_pressed.emit(text)
            return event.ignore()
    @Slot(str)
    def insert_text(self, text:str):
        if not is_empty(text):
            self.insert(text)
        return
    @Slot()
    def del_text(self):
        text = self.text()
        if not is_empty(text):
            text = list(text)
            text.pop()
            self.setText("".join(text))
        return
    @Slot()
    def _espace(self):
        self.insert(" ")
        return