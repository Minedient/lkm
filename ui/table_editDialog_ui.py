# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table_editDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QGroupBox, QHBoxLayout, QHeaderView,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_TableEditDialog(object):
    def setupUi(self, TableEditDialog):
        if not TableEditDialog.objectName():
            TableEditDialog.setObjectName(u"TableEditDialog")
        TableEditDialog.resize(640, 480)
        self.verticalLayout = QVBoxLayout(TableEditDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(TableEditDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout = QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.studentInfoTable = QTableWidget(self.tab)
        self.studentInfoTable.setObjectName(u"studentInfoTable")
        self.studentInfoTable.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.studentInfoTable.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.studentInfoTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.horizontalLayout.addWidget(self.studentInfoTable)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")

        self.horizontalLayout.addWidget(self.groupBox)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.eventInfoTable = QTableWidget(self.tab_2)
        self.eventInfoTable.setObjectName(u"eventInfoTable")
        self.eventInfoTable.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked)
        self.eventInfoTable.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.eventInfoTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.horizontalLayout_2.addWidget(self.eventInfoTable)

        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")

        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(TableEditDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Discard|QDialogButtonBox.StandardButton.Reset)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(TableEditDialog)
        self.buttonBox.accepted.connect(TableEditDialog.accept)
        self.buttonBox.rejected.connect(TableEditDialog.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TableEditDialog)
    # setupUi

    def retranslateUi(self, TableEditDialog):
        TableEditDialog.setWindowTitle(QCoreApplication.translate("TableEditDialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("TableEditDialog", u"\u4f7f\u7528\u8aaa\u660e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("TableEditDialog", u"\u5b78\u751f\u8cc7\u6599", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TableEditDialog", u"GroupBox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("TableEditDialog", u"\u6d3b\u52d5\u8cc7\u6599", None))
    # retranslateUi

