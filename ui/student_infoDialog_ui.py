# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student_infoDialog.ui'
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
    QFrame, QGridLayout, QGroupBox, QLabel,
    QPlainTextEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_StudentInfoInputDialog(object):
    def setupUi(self, StudentInfoInputDialog):
        if not StudentInfoInputDialog.objectName():
            StudentInfoInputDialog.setObjectName(u"StudentInfoInputDialog")
        StudentInfoInputDialog.resize(640, 514)
        self.gridLayout = QGridLayout(StudentInfoInputDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(StudentInfoInputDialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout.addWidget(self.label_12)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout.addWidget(self.label_13)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout.addWidget(self.label_14)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout.addWidget(self.label_15)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.buttonBox = QDialogButtonBox(self.groupBox)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Discard|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.groupBox, 2, 1, 1, 1)

        self.label = QLabel(StudentInfoInputDialog)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(28)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.line = QFrame(StudentInfoInputDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)

        self.plainTextEdit = QPlainTextEdit(StudentInfoInputDialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(6)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Microsoft JhengHei"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.plainTextEdit.setFont(font2)

        self.gridLayout.addWidget(self.plainTextEdit, 2, 0, 3, 1)


        self.retranslateUi(StudentInfoInputDialog)
        self.buttonBox.accepted.connect(StudentInfoInputDialog.accept)
        self.buttonBox.rejected.connect(StudentInfoInputDialog.reject)

        QMetaObject.connectSlotsByName(StudentInfoInputDialog)
    # setupUi

    def retranslateUi(self, StudentInfoInputDialog):
        StudentInfoInputDialog.setWindowTitle(QCoreApplication.translate("StudentInfoInputDialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("StudentInfoInputDialog", u"Helper", None))
        self.label_2.setText(QCoreApplication.translate("StudentInfoInputDialog", u"\u6ce8\u610f\u4e8b\u9805!", None))
        self.label_3.setText(QCoreApplication.translate("StudentInfoInputDialog", u"\u6bcf\u4e00\u884c\u53ea\u80fd\u8f38\u5165\u4e00\u500b\u5b78\u751f\u7684\u6578\u64da", None))
        self.label_4.setText(QCoreApplication.translate("StudentInfoInputDialog", u"\u540c\u6642\u8acb\u8ddf\u96a8\u4ee5\u4e0b\u683c\u5f0f\u8f38\u5165", None))
        self.label_7.setText(QCoreApplication.translate("StudentInfoInputDialog", u"\u73ed\u5225\uff0c\u73ed\u865f\uff0c\u59d3\u540d\uff0c\u7d93\u6fdf\u4ee3\u865f", None))
        self.label_8.setText(QCoreApplication.translate("StudentInfoInputDialog", u"\u9805\u76ee\u4e2d\u9593\u7528\u82f1\u6587\u9017\u865f(,)\u5206\u9694", None))
        self.label_5.setText(QCoreApplication.translate("StudentInfoInputDialog", u"\u4f8b\u5b50:", None))
        self.label_6.setText(QCoreApplication.translate("StudentInfoInputDialog", u"1A,1,\u9673\u5927\u6587,C", None))
        self.label_9.setText(QCoreApplication.translate("StudentInfoInputDialog", u"1D,24,\u9ec3\u4e00\u5fc3,D", None))
        self.label_10.setText(QCoreApplication.translate("StudentInfoInputDialog", u"\u7d93\u6fdf\u4ee3\u865f", None))
        self.label_11.setText(QCoreApplication.translate("StudentInfoInputDialog", u"C - \u7d9c\u7de9", None))
        self.label_12.setText(QCoreApplication.translate("StudentInfoInputDialog", u"F - \u5168\u514d", None))
        self.label_13.setText(QCoreApplication.translate("StudentInfoInputDialog", u"H - \u534a\u514d", None))
        self.label_14.setText(QCoreApplication.translate("StudentInfoInputDialog", u"D - \u7d93\u6fdf\u56f0\u96e3", None))
        self.label_15.setText(QCoreApplication.translate("StudentInfoInputDialog", u"S - \u7279\u6b8a", None))
        self.label.setText(QCoreApplication.translate("StudentInfoInputDialog", u"\u5b78\u751f\u8cc7\u6599\u8f38\u5165\u5de5\u5177", None))
    # retranslateUi

