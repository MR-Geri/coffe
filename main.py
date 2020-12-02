import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *

from base import get_all_base, get_base_data
from card import WidgetCoffeeCard
from form_add_coffee import AddEditCoffee


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('main.ui', self)
        # ID, название сорта, степень обжарки, молотый/в зернах, описание вкуса, цена, объем упаковки
        self.update_()
        self.menuBar = self.menuBar()
        action = QAction('Добавить', self)
        action.triggered.connect(self.add_coffee)
        self.menuBar.addAction(action)

    def update_(self):
        layout = QGridLayout()
        self.cards = QListWidget()
        layout.addWidget(self.cards)
        data = get_all_base()
        if data:
            for line in data:
                card = WidgetCoffeeCard(*line)
                card.button_edit.clicked.connect(lambda state, id_=line[0]: self.edit_coffee(id_))
                #
                list_card = QListWidgetItem(self.cards)
                list_card.setSizeHint(card.sizeHint())
                self.cards.addItem(list_card)
                self.cards.setItemWidget(list_card, card)
        self.gridLayout.addLayout(layout, 0, 0)

    def edit_coffee(self, id_: int) -> None:
        dialog = AddEditCoffee(*get_base_data("""SELECT * FROM coffee WHERE id = ?""", (id_,))[0], False)
        if dialog.exec_() == QDialog.Accepted:
            self.update_()
        dialog.deleteLater()

    def add_coffee(self):
        dialog = AddEditCoffee(-1, 1, 1, 1, '', 1, 1)
        if dialog.exec_() == QDialog.Accepted:
            self.update_()
        dialog.deleteLater()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
