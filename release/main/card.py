from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QTextBrowser


class WidgetCoffeeCard(QWidget):
    def __init__(self, id_: int, variety: str, degree_roasting: str, condition: str,
                 description: str, price: int, volume: int) -> None:
        super().__init__()
        self.id_ = id_
        # ["ID", "Название",  "Степень обжарки", "Состояние", "Вкус", "Цена", 'Объем']
        self.label_variety = QLabel(f'Название сорта: {variety}')
        self.label_degree_roasting = QLabel(f'Степень обжарки: {degree_roasting}')
        self.label_condition = QLabel(f'Состояние: {condition}')
        self.label_description = QLabel(f'Описание: {description}')
        self.label_price = QLabel(f'Цена: {price}')
        self.label_volume = QLabel(f'Объем: {volume}')
        #
        self.label_variety.setFont(QFont('MS Shell Dlg 2', 20))
        self.label_degree_roasting.setFont(QFont('MS Shell Dlg 2', 20))
        self.label_condition.setFont(QFont('MS Shell Dlg 2', 20))
        self.label_description.setFont(QFont('MS Shell Dlg 2', 20))
        self.label_price.setFont(QFont('MS Shell Dlg 2', 20))
        self.label_volume.setFont(QFont('MS Shell Dlg 2', 20))
        #
        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.label_variety, 1, 0)
        self.gridLayout.addWidget(self.label_degree_roasting, 2, 0)
        self.gridLayout.addWidget(self.label_condition, 3, 0)
        self.gridLayout.addWidget(self.label_description, 4, 0)
        self.gridLayout.addWidget(self.label_price, 5, 0)
        self.gridLayout.addWidget(self.label_volume, 6, 0)
        #
        self.button_edit = QPushButton('Изменить')
        self.button_edit.setFont(QFont('MS Shell Dlg 2', 20))
        #
        self.gridLayout.addWidget(self.button_edit, 7, 0)
        #
        self.setLayout(self.gridLayout)
