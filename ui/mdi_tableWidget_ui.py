# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mdi_tableWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MDITableWidget(object):
    def setupUi(self, MDITableWidget):
        if not MDITableWidget.objectName():
            MDITableWidget.setObjectName(u"MDITableWidget")
        MDITableWidget.resize(320, 240)
        self.verticalLayout = QVBoxLayout(MDITableWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(MDITableWidget)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.tableWidget)

        self.controlPanel = QFrame(MDITableWidget)
        self.controlPanel.setObjectName(u"controlPanel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.controlPanel.sizePolicy().hasHeightForWidth())
        self.controlPanel.setSizePolicy(sizePolicy1)
        self.controlPanel.setMaximumSize(QSize(16777215, 16777215))
        self.controlPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.controlPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.controlPanel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label = QLabel(self.controlPanel)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.controlPanel)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.controlPanel)


        self.retranslateUi(MDITableWidget)

        QMetaObject.connectSlotsByName(MDITableWidget)
    # setupUi

    def retranslateUi(self, MDITableWidget):
        MDITableWidget.setWindowTitle(QCoreApplication.translate("MDITableWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("MDITableWidget", u"Save to CSV", None))
        self.pushButton.setText(QCoreApplication.translate("MDITableWidget", u"Click", None))
    # retranslateUi

