from PyQt5 import uic
from PyQt5.QtWidgets import QDialog


class AddEditCoffee(QDialog):
    def __init__(self, id_: int, variety: str, degree_roasting: str, condition: str,
                 description: str, price: int, volume: int = -1) -> None:
        super().__init__()
        uic.loadUi('../addEditCoffeeForm.ui', self)
        if volume == -1:
            self.condition.setText('Создать')
            self.condition.clicked.connect()
        else:
            self.condition.setText('Сохранить')
            self.condition.clicked.connect()
        self.cancel.clicked.connect(self.close)

    def addBase(self):
        pass

    def editBase(self):
        pass
