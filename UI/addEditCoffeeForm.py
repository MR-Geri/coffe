from PyQt5.QtCore import QCoreApplication, QMetaObject, Qt, QRect, QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLabel, QComboBox, QTextEdit, QSpinBox, QGridLayout, QWidget


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(551, 700)
        Form.setMinimumSize(QSize(551, 700))
        Form.setMaximumSize(QSize(551, 700))
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 551, 701))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.volume = QSpinBox(self.gridLayoutWidget)
        self.volume.setObjectName(u"volume")
        font = QFont()
        font.setPointSize(20)
        self.volume.setFont(font)
        self.volume.setAlignment(Qt.AlignCenter)
        self.volume.setMaximum(10000000)

        self.gridLayout.addWidget(self.volume, 13, 0, 1, 2)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 12, 0, 1, 2)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 6, 0, 3, 2)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 10, 0, 1, 2)

        self.degree_roasting = QComboBox(self.gridLayoutWidget)
        self.degree_roasting.setObjectName(u"degree_roasting")
        self.degree_roasting.setFont(font)

        self.gridLayout.addWidget(self.degree_roasting, 3, 0, 1, 2)

        self.price = QSpinBox(self.gridLayoutWidget)
        self.price.setObjectName(u"price")
        self.price.setFont(font)
        self.price.setAlignment(Qt.AlignCenter)
        self.price.setMaximum(10000000)

        self.gridLayout.addWidget(self.price, 11, 0, 1, 2)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.variety = QComboBox(self.gridLayoutWidget)
        self.variety.setObjectName(u"variety")
        self.variety.setFont(font)

        self.gridLayout.addWidget(self.variety, 1, 0, 1, 2)

        self.description = QTextEdit(self.gridLayoutWidget)
        self.description.setObjectName(u"description")
        self.description.setFont(font)

        self.gridLayout.addWidget(self.description, 9, 0, 1, 2)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.condition = QComboBox(self.gridLayoutWidget)
        self.condition.setObjectName(u"condition")
        self.condition.setFont(font)

        self.gridLayout.addWidget(self.condition, 5, 0, 1, 2)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 2)

        self.button_condition = QPushButton(self.gridLayoutWidget)
        self.button_condition.setObjectName(u"button_condition")
        self.button_condition.setFont(font)

        self.gridLayout.addWidget(self.button_condition, 14, 0, 1, 1)

        self.cancel = QPushButton(self.gridLayoutWidget)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setFont(font)

        self.gridLayout.addWidget(self.cancel, 14, 1, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u044a\u0435\u043c", None))
        self.label_4.setText(QCoreApplication.translate("Form",
                                                        u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u043a\u0443\u0441\u0430",
                                                        None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Form",
                                                        u"\u0421\u0442\u0435\u043f\u0435\u043d\u044c \u043e\u0431\u0436\u0430\u0440\u043a\u0438",
                                                        None))
        self.label.setText(QCoreApplication.translate("Form",
                                                      u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u043e\u0440\u0442\u0430",
                                                      None))
        self.label_3.setText(
            QCoreApplication.translate("Form", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None))
        self.button_condition.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.cancel.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
