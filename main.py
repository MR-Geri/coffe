import sqlite3
import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *


def get_base():
    con = sqlite3.connect('data.sqlite')
    sql = con.cursor()
    result = sql.execute("""SELECT cof.id, v.title, d.title, c.title, cof.description, cof.price, cof.volume FROM 
    coffee cof, conditions c, degree_roasting d, varietys v 
    WHERE cof.variety = v.id AND cof.condition = c.id AND cof.degree_roasting = d.id""").fetchall()
    con.close()
    return result


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        # ID, название сорта, степень обжарки, молотый/в зернах, описание вкуса, цена, объем упаковки
        self.headers = ["ID", "Название",  "Степень обжарки", "Состояние", "Вкус", "Цена", 'Объем']
        self.table.setColumnCount(len(self.headers))
        self.table.setHorizontalHeaderLabels(self.headers)
        self.table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        data = get_base()
        if data:
            for row, line in enumerate(data):
                self.table.insertRow(row)
                for ind, sell in enumerate(line):
                    self.table.setItem(row, ind, QTableWidgetItem(f'{sell}'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
