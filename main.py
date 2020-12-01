import sqlite3
import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *

from card import WidgetCoffeeCard
from form_add_coffee import AddEditCoffee


def get_base() -> list:
    con = sqlite3.connect('data.sqlite')
    sql = con.cursor()
    result = sql.execute("""SELECT cof.id, v.title, d.title, c.title, cof.description, cof.price, cof.volume FROM 
    coffee cof, conditions c, degree_roasting d, varietys v 
    WHERE cof.variety = v.id AND cof.condition = c.id AND cof.degree_roasting = d.id""").fetchall()
    con.close()
    return result


class MyWidget(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('main.ui', self)
        # ID, название сорта, степень обжарки, молотый/в зернах, описание вкуса, цена, объем упаковки
        data = get_base()
        self.cards = QListWidget()
        self.gridLayout.addWidget(self.cards)
        if data:
            for line in data:
                card = WidgetCoffeeCard(*line)
                card.button_edit.clicked.connect(lambda state,  data=line: self.click(data))
                #
                list_card = QListWidgetItem(self.cards)
                list_card.setSizeHint(card.sizeHint())
                self.cards.addItem(list_card)
                self.cards.setItemWidget(list_card, card)

    def click(self, data: list) -> None:
        dialog = AddEditCoffee()
        dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
