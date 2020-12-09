import UI.addEditCoffeeForm
from PyQt5.QtWidgets import QDialog

from base import get_base_data, get_base


class AddEditCoffee(QDialog):
    def __init__(self, id_: int, variety: int, degree_roasting: int, condition: int,
                 description: str, price: int, volume: int, flags: bool = True) -> None:
        super().__init__()
        self.id_ = id_
        self.ui = UI.addEditCoffeeForm.Ui_Form()
        self.ui.setupUi(self)
        for i in get_base_data("""SELECT title FROM varietys"""):
            self.ui.variety.addItem(i[0])
        for i in get_base_data("""SELECT title FROM degree_roasting"""):
            self.ui.degree_roasting.addItem(i[0])
        for i in get_base_data("""SELECT title FROM conditions"""):
            self.ui.condition.addItem(i[0])
        if flags:
            self.setWindowTitle('Добавление')
            self.ui.button_condition.setText('Создать')
            self.ui.button_condition.clicked.connect(self.addBase)
        else:
            self.setWindowTitle('Изменение')
            self.ui.button_condition.setText('Сохранить')
            self.ui.button_condition.clicked.connect(self.editBase)
            #
            self.ui.variety.setCurrentIndex(variety - 1)
            self.ui.degree_roasting.setCurrentIndex(degree_roasting - 1)
            self.ui.condition.setCurrentIndex(condition - 1)
            self.ui.description.setText(description)
            self.ui.price.setValue(price)
            self.ui.volume.setValue(volume)
        self.ui.cancel.clicked.connect(self.close)

    def addBase(self):
        with get_base('data/coffee.sqlite', True) as base:
            base.execute("""INSERT INTO coffee (id, variety, degree_roasting, condition, description, price, volume)
                                VALUES ((SELECT id FROM coffee ORDER BY id DESC LIMIT 1) + 1, ?, ?, ?, ?, ?, ?)""",
                         (self.ui.variety.currentIndex() + 1,
                          self.ui.degree_roasting.currentIndex() + 1,
                          self.ui.condition.currentIndex() + 1,
                          self.ui.description.toPlainText(),
                          self.ui.price.value(),
                          self.ui.volume.value()
                          ))
        self.accept()

    def editBase(self):
        with get_base('data/coffee.sqlite', True) as base:
            base.execute("""UPDATE coffee SET variety = ?, degree_roasting = ?, 
            condition = ?, description = ?, price = ?, volume = ? WHERE id = ?""",
                         (self.ui.variety.currentIndex() + 1,
                          self.ui.degree_roasting.currentIndex() + 1,
                          self.ui.condition.currentIndex() + 1,
                          self.ui.description.toPlainText(),
                          self.ui.price.value(),
                          self.ui.volume.value(),
                          self.id_)
                         )
        self.accept()
