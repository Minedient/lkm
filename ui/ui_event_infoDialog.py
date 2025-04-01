# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'event_infoDialogwmeygp.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_EventInfoInputDialog(object):
    def setupUi(self, EventInfoInputDialog):
        if not EventInfoInputDialog.objectName():
            EventInfoInputDialog.setObjectName(u"EventInfoInputDialog")
        EventInfoInputDialog.resize(640, 480)
        self.verticalLayout = QVBoxLayout(EventInfoInputDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(EventInfoInputDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(28)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.line = QFrame(EventInfoInputDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(EventInfoInputDialog)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Microsoft JhengHei UI"])
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.eventLineEdit = QLineEdit(EventInfoInputDialog)
        self.eventLineEdit.setObjectName(u"eventLineEdit")
        font2 = QFont()
        font2.setPointSize(12)
        self.eventLineEdit.setFont(font2)

        self.horizontalLayout.addWidget(self.eventLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(EventInfoInputDialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.plainTextEdit = QPlainTextEdit(EventInfoInputDialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout_2.addWidget(self.plainTextEdit)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(EventInfoInputDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(EventInfoInputDialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(EventInfoInputDialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(EventInfoInputDialog)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.buttonBox = QDialogButtonBox(EventInfoInputDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(EventInfoInputDialog)
        self.buttonBox.accepted.connect(EventInfoInputDialog.accept)
        self.buttonBox.rejected.connect(EventInfoInputDialog.reject)

        QMetaObject.connectSlotsByName(EventInfoInputDialog)
    # setupUi

    def retranslateUi(self, EventInfoInputDialog):
        EventInfoInputDialog.setWindowTitle(QCoreApplication.translate("EventInfoInputDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("EventInfoInputDialog", u"\u6d3b\u52d5\u8cc7\u6599\u8f38\u5165\u5de5\u5177", None))
        self.label_2.setText(QCoreApplication.translate("EventInfoInputDialog", u"\u6d3b\u52d5\u540d\u7a31", None))
        self.label_3.setText(QCoreApplication.translate("EventInfoInputDialog", u"\u6ce8\u610f\u4e8b\u9805!", None))
        self.label_4.setText(QCoreApplication.translate("EventInfoInputDialog", u"\u6bcf\u4e00\u884c\u53ea\u80fd\u8f38\u5165\u4e00\u500b\u5b78\u751f\u7684\u540d\u5b57", None))
        self.label_5.setText(QCoreApplication.translate("EventInfoInputDialog", u" \u7a0b\u5f0f\u6703\u7121\u8996\u4e0d\u5b58\u5728\u7684\u540d\u5b57", None))
        self.label_6.setText(QCoreApplication.translate("EventInfoInputDialog", u"\u8a18\u5f97\u8f38\u5165\u6d3b\u52d5\u540d\u7a31", None))
    # retranslateUi

