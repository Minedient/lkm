# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QMdiArea, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame_2, 1, 1, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.manualStudentInfoButton = QPushButton(self.frame)
        self.manualStudentInfoButton.setObjectName(u"manualStudentInfoButton")

        self.gridLayout_2.addWidget(self.manualStudentInfoButton, 1, 1, 1, 1)

        self.studentParticipatesByEventButton = QPushButton(self.frame)
        self.studentParticipatesByEventButton.setObjectName(u"studentParticipatesByEventButton")

        self.gridLayout_2.addWidget(self.studentParticipatesByEventButton, 7, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Microsoft JhengHei UI"])
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 2)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 4, 0, 1, 2)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 6, 0, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 7, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.studentEventTableWithCategoryAndNameButton = QPushButton(self.frame)
        self.studentEventTableWithCategoryAndNameButton.setObjectName(u"studentEventTableWithCategoryAndNameButton")

        self.gridLayout_2.addWidget(self.studentEventTableWithCategoryAndNameButton, 9, 1, 1, 1)

        self.studentParticipatesButton = QPushButton(self.frame)
        self.studentParticipatesButton.setObjectName(u"studentParticipatesButton")

        self.gridLayout_2.addWidget(self.studentParticipatesButton, 6, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 10, 0, 1, 1)

        self.manualEventInfoButton = QPushButton(self.frame)
        self.manualEventInfoButton.setObjectName(u"manualEventInfoButton")

        self.gridLayout_2.addWidget(self.manualEventInfoButton, 2, 1, 1, 1)

        self.studentEventTableWithCategoryButton = QPushButton(self.frame)
        self.studentEventTableWithCategoryButton.setObjectName(u"studentEventTableWithCategoryButton")

        self.gridLayout_2.addWidget(self.studentEventTableWithCategoryButton, 8, 1, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 9, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 8, 0, 1, 1)

        self.manualEditInfoButton = QPushButton(self.frame)
        self.manualEditInfoButton.setObjectName(u"manualEditInfoButton")

        self.gridLayout_2.addWidget(self.manualEditInfoButton, 3, 1, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 2, 1)

        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(5)
        sizePolicy3.setVerticalStretch(9)
        sizePolicy3.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.mdiArea, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 33))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuAbout.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.manualStudentInfoButton.setText(QCoreApplication.translate("MainWindow", u"Click", None))
        self.studentParticipatesByEventButton.setText(QCoreApplication.translate("MainWindow", u"Click", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u624b\u8f38\u5165\u8cc7\u6599", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5b78\u751f\u53c3\u8207\u6b21\u6578", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5b78\u751f\u53c3\u8207\u6d3b\u52d5\u540d\u7a31", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5b78\u751f\u8cc7\u6599", None))
        self.studentEventTableWithCategoryAndNameButton.setText(QCoreApplication.translate("MainWindow", u"Click", None))
        self.studentParticipatesButton.setText(QCoreApplication.translate("MainWindow", u"Click", None))
        self.manualEventInfoButton.setText(QCoreApplication.translate("MainWindow", u"Click", None))
        self.studentEventTableWithCategoryButton.setText(QCoreApplication.translate("MainWindow", u"Click", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u6d3b\u52d5\u51fa\u5e2d\u5b78\u751f\u59d3\u540d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8cc7\u6599\u8655\u7406", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6d3b\u52d5\u8cc7\u6599", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6d3b\u52d5\u51fa\u5e2d\u4eba\u6578", None))
        self.manualEditInfoButton.setText(QCoreApplication.translate("MainWindow", u"Click", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6539\u8cc7\u6599", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

