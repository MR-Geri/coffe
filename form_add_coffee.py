from PyQt5 import uic
from PyQt5.QtWidgets import QDialog

from base import get_base_data, get_base


class AddEditCoffee(QDialog):
    def __init__(self, id_: int, variety: int, degree_roasting: int, condition: int,
                 description: str, price: int, volume: int, flags: bool = True) -> None:
        super().__init__()
        self.id_ = id_
        uic.loadUi('addEditCoffeeForm.ui', self)
        for i in get_base_data("""SELECT title FROM varietys"""):
            self.variety.addItem(i[0])
        for i in get_base_data("""SELECT title FROM degree_roasting"""):
            self.degree_roasting.addItem(i[0])
        for i in get_base_data("""SELECT title FROM conditions"""):
            self.condition.addItem(i[0])
        if flags:
            self.setWindowTitle('Добавление')
            self.button_condition.setText('Создать')
            self.button_condition.clicked.connect(self.addBase)
        else:
            self.setWindowTitle('Изменение')
            self.button_condition.setText('Сохранить')
            self.button_condition.clicked.connect(self.editBase)
            #
            self.variety.setCurrentIndex(variety - 1)
            self.degree_roasting.setCurrentIndex(degree_roasting - 1)
            self.condition.setCurrentIndex(condition - 1)
            self.description.setText(description)
            self.price.setValue(price)
            self.volume.setValue(volume)
        self.cancel.clicked.connect(self.close)

    def addBase(self):
        with get_base('coffee.sqlite', True) as base:
            base.execute("""INSERT INTO coffee (id, variety, degree_roasting, condition, description, price, volume)
                                VALUES ((SELECT id FROM coffee ORDER BY id DESC LIMIT 1) + 1, ?, ?, ?, ?, ?, ?)""",
                         (self.variety.currentIndex() + 1,
                          self.degree_roasting.currentIndex() + 1,
                          self.condition.currentIndex() + 1,
                          self.description.toPlainText(),
                          self.price.value(),
                          self.volume.value()
                          ))
        self.accept()

    def editBase(self):
        with get_base('coffee.sqlite', True) as base:
            base.execute("""UPDATE coffee SET variety = ?, degree_roasting = ?, 
            condition = ?, description = ?, price = ?, volume = ? WHERE id = ?""",
                         (self.variety.currentIndex() + 1,
                          self.degree_roasting.currentIndex() + 1,
                          self.condition.currentIndex() + 1,
                          self.description.toPlainText(),
                          self.price.value(),
                          self.volume.value(),
                          self.id_)
                         )
        self.accept()
