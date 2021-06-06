# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"#pipelinePreview, #pipelineWidgets, #resultPreview, #pipelineWidgets::pane {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-radius: .5em;\n"
"}\n"
"\n"
"#pipelineWidgets::pane {\n"
"	border-top-left-radius: 0;\n"
"}")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.centralSplitter = QSplitter(self.centralwidget)
        self.centralSplitter.setObjectName(u"centralSplitter")
        self.centralSplitter.setChildrenCollapsible(False)
        self.pipelineWidgets = QTabWidget(self.centralSplitter)
        self.pipelineWidgets.setObjectName(u"pipelineWidgets")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pipelineWidgets.sizePolicy().hasHeightForWidth())
        self.pipelineWidgets.setSizePolicy(sizePolicy)
        self.pipelineWidgets.setMinimumSize(QSize(200, 0))
        self.pipelineWidgets.setStyleSheet(u"QTabBar::tab {\n"
"	border-top-left-radius: .25em;\n"
"	border-top-right-radius: .25em;\n"
"	min-width: 8ex;\n"
"	padding: 3px 5px 3px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"	margin-top: 5px;\n"
"	\n"
"	background-color: rgb(248, 248, 248);\n"
"	color: rgb(93, 109, 109);\n"
"}")
        self.allTab = QWidget()
        self.allTab.setObjectName(u"allTab")
        self.pipelineWidgets.addTab(self.allTab, "")
        self.imageProcessingTab = QWidget()
        self.imageProcessingTab.setObjectName(u"imageProcessingTab")
        self.pipelineWidgets.addTab(self.imageProcessingTab, "")
        self.centralSplitter.addWidget(self.pipelineWidgets)
        self.previewsFrame = QFrame(self.centralSplitter)
        self.previewsFrame.setObjectName(u"previewsFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.previewsFrame.sizePolicy().hasHeightForWidth())
        self.previewsFrame.setSizePolicy(sizePolicy1)
        self.previewsFrame.setMinimumSize(QSize(400, 0))
        self.verticalLayout = QVBoxLayout(self.previewsFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.previewsSplitter = QSplitter(self.previewsFrame)
        self.previewsSplitter.setObjectName(u"previewsSplitter")
        self.previewsSplitter.setOrientation(Qt.Vertical)
        self.previewsSplitter.setChildrenCollapsible(False)
        self.resultPreview = QFrame(self.previewsSplitter)
        self.resultPreview.setObjectName(u"resultPreview")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.resultPreview.sizePolicy().hasHeightForWidth())
        self.resultPreview.setSizePolicy(sizePolicy2)
        self.resultPreview.setMinimumSize(QSize(0, 150))
        self.resultPreview.setFrameShape(QFrame.StyledPanel)
        self.resultPreview.setFrameShadow(QFrame.Raised)
        self.previewsSplitter.addWidget(self.resultPreview)
        self.pipelinePreview = QFrame(self.previewsSplitter)
        self.pipelinePreview.setObjectName(u"pipelinePreview")
        sizePolicy2.setHeightForWidth(self.pipelinePreview.sizePolicy().hasHeightForWidth())
        self.pipelinePreview.setSizePolicy(sizePolicy2)
        self.pipelinePreview.setMinimumSize(QSize(0, 150))
        self.pipelinePreview.setAcceptDrops(True)
        self.pipelinePreview.setFrameShape(QFrame.StyledPanel)
        self.pipelinePreview.setFrameShadow(QFrame.Raised)
        self.previewsSplitter.addWidget(self.pipelinePreview)

        self.verticalLayout.addWidget(self.previewsSplitter)

        self.centralSplitter.addWidget(self.previewsFrame)

        self.centralSplitter.setSizes([1000, 5000])

        self.gridLayout.addWidget(self.centralSplitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)

        self.pipelineWidgets.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PipelineCV", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.pipelineWidgets.setTabText(self.pipelineWidgets.indexOf(self.allTab), QCoreApplication.translate("MainWindow", u"All", None))
        self.pipelineWidgets.setTabText(self.pipelineWidgets.indexOf(self.imageProcessingTab), QCoreApplication.translate("MainWindow", u"Image Processing", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

