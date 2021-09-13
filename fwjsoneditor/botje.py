# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'botje.ui',
# licensing of 'botje.ui' applies.
#
# Created: Fri Oct  5 10:27:29 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_botShotForm(object):
    def setupUi(self, botShotForm):
        botShotForm.setObjectName("botShotForm")
        botShotForm.resize(694, 625)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("boteditor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        botShotForm.setWindowIcon(icon)
        botShotForm.setStyleSheet("QLineEdit{\n"
"border-radius: 4px;\n"
"border: 1px solid grey;\n"
"}\n"
"\n"
"#pushButtonPrevious {\n"
"    background-color: #4CAF50; /* Green */\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#pushButtonNext {\n"
"    background-color: #4CAF50; /* Green */\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#pushButtonEdit {\n"
"    background-color: #4CAF50; /* Green */\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 14px;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(botShotForm)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.shotEditorTitleLabel = QtWidgets.QLabel(botShotForm)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.shotEditorTitleLabel.setFont(font)
        self.shotEditorTitleLabel.setStyleSheet("#shotEditorTitleLabel{\n"
"    padding: 8px;\n"
"    color:  white;\n"
"    border: 1px solid white;\n"
"    background-color: #555555; /* Blue*/\n"
"}\n"
"")
        self.shotEditorTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.shotEditorTitleLabel.setObjectName("shotEditorTitleLabel")
        self.verticalLayout.addWidget(self.shotEditorTitleLabel)
        self.tabWidget = QtWidgets.QTabWidget(botShotForm)
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid black;\n"
"    background: white;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: silver;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.previewTab = QtWidgets.QWidget()
        self.previewTab.setObjectName("previewTab")
        self.previewTreeWidget = QtWidgets.QTreeWidget(self.previewTab)
        self.previewTreeWidget.setGeometry(QtCore.QRect(10, 98, 651, 291))
        self.previewTreeWidget.setObjectName("previewTreeWidget")
        self.label = QtWidgets.QLabel(self.previewTab)
        self.label.setGeometry(QtCore.QRect(10, 35, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.previewVersionLineEdit = QtWidgets.QLineEdit(self.previewTab)
        self.previewVersionLineEdit.setGeometry(QtCore.QRect(10, 59, 251, 31))
        self.previewVersionLineEdit.setObjectName("previewVersionLineEdit")
        self.label_2 = QtWidgets.QLabel(self.previewTab)
        self.label_2.setGeometry(QtCore.QRect(280, 35, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.previewTypeLineEdit = QtWidgets.QLineEdit(self.previewTab)
        self.previewTypeLineEdit.setGeometry(QtCore.QRect(280, 60, 381, 31))
        self.previewTypeLineEdit.setObjectName("previewTypeLineEdit")
        self.label_14 = QtWidgets.QLabel(self.previewTab)
        self.label_14.setGeometry(QtCore.QRect(20, 4, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.previewButton = QtWidgets.QPushButton(self.previewTab)
        self.previewButton.setGeometry(QtCore.QRect(10, 400, 651, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.previewButton.setFont(font)
        self.previewButton.setStyleSheet("#previewButton {\n"
"    background-color: #4CAF50; /* Green */\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 14px;\n"
"    height: 35px;\n"
"}\n"
"\n"
"QPushButton#previewButton:hover {\n"
"    background-color: #008e06;\n"
"}\n"
"\n"
"QPushButton#previewButton:pressed {\n"
"    background-color: #4CAF50;     \n"
"}")
        self.previewButton.setObjectName("previewButton")
        self.tabWidget.addTab(self.previewTab, "")
        self.createTab = QtWidgets.QWidget()
        self.createTab.setObjectName("createTab")
        self.label_3 = QtWidgets.QLabel(self.createTab)
        self.label_3.setGeometry(QtCore.QRect(40, 40, 111, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.createTab)
        self.label_5.setGeometry(QtCore.QRect(40, 160, 61, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.createTab)
        self.label_6.setGeometry(QtCore.QRect(40, 99, 71, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.createDepartmentComboBox = QtWidgets.QComboBox(self.createTab)
        self.createDepartmentComboBox.setGeometry(QtCore.QRect(40, 119, 161, 31))
        self.createDepartmentComboBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.createDepartmentComboBox.setObjectName("createDepartmentComboBox")
        self.createDepartmentComboBox.addItem("")
        self.createDepartmentComboBox.addItem("")
        self.createDepartmentComboBox.addItem("")
        self.createDepartmentComboBox.addItem("")
        self.createRenderLineEdit = QtWidgets.QLineEdit(self.createTab)
        self.createRenderLineEdit.setGeometry(QtCore.QRect(40, 180, 451, 31))
        self.createRenderLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.createRenderLineEdit.setObjectName("createRenderLineEdit")
        self.createTypeLineEdit = QtWidgets.QLineEdit(self.createTab)
        self.createTypeLineEdit.setGeometry(QtCore.QRect(40, 60, 451, 31))
        self.createTypeLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.createTypeLineEdit.setObjectName("createTypeLineEdit")
        self.label_13 = QtWidgets.QLabel(self.createTab)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.createVersionLineEdit = QtWidgets.QLineEdit(self.createTab)
        self.createVersionLineEdit.setGeometry(QtCore.QRect(40, 240, 211, 31))
        self.createVersionLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.createVersionLineEdit.setObjectName("createVersionLineEdit")
        self.label_15 = QtWidgets.QLabel(self.createTab)
        self.label_15.setGeometry(QtCore.QRect(40, 220, 47, 13))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.createPushButton = QtWidgets.QPushButton(self.createTab)
        self.createPushButton.setGeometry(QtCore.QRect(10, 400, 651, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.createPushButton.setFont(font)
        self.createPushButton.setStyleSheet("#createPushButton {\n"
"    background-color: #f4511e; /* Green */\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 14px;\n"
"    height: 35px;\n"
"}\n"
"\n"
"QPushButton#createPushButton:hover {\n"
"    background-color: #f23a01;\n"
"}\n"
"\n"
"QPushButton#createPushButton:pressed {\n"
"    background-color: #f4511e;     \n"
"}")
        self.createPushButton.setObjectName("createPushButton")
        self.tabWidget.addTab(self.createTab, "")
        self.editTab = QtWidgets.QWidget()
        self.editTab.setObjectName("editTab")
        self.label_7 = QtWidgets.QLabel(self.editTab)
        self.label_7.setGeometry(QtCore.QRect(70, 60, 47, 13))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.editTab)
        self.label_8.setGeometry(QtCore.QRect(70, 270, 71, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.editTab)
        self.label_9.setGeometry(QtCore.QRect(70, 130, 71, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.editTab)
        self.label_10.setGeometry(QtCore.QRect(70, 200, 81, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.editTypeLineEdit = QtWidgets.QLineEdit(self.editTab)
        self.editTypeLineEdit.setGeometry(QtCore.QRect(70, 80, 331, 31))
        self.editTypeLineEdit.setObjectName("editTypeLineEdit")
        self.editVersionLineEdit = QtWidgets.QLineEdit(self.editTab)
        self.editVersionLineEdit.setGeometry(QtCore.QRect(70, 290, 331, 31))
        self.editVersionLineEdit.setObjectName("editVersionLineEdit")
        self.editRenderLineEdit = QtWidgets.QLineEdit(self.editTab)
        self.editRenderLineEdit.setGeometry(QtCore.QRect(70, 150, 471, 31))
        self.editRenderLineEdit.setObjectName("editRenderLineEdit")
        self.editDirectoryLineEdit = QtWidgets.QLineEdit(self.editTab)
        self.editDirectoryLineEdit.setGeometry(QtCore.QRect(70, 220, 471, 31))
        self.editDirectoryLineEdit.setObjectName("editDirectoryLineEdit")
        self.editDirectoryPushButton = QtWidgets.QPushButton(self.editTab)
        self.editDirectoryPushButton.setGeometry(QtCore.QRect(550, 220, 61, 31))
        self.editDirectoryPushButton.setObjectName("editDirectoryPushButton")
        self.editEditPushButton = QtWidgets.QPushButton(self.editTab)
        self.editEditPushButton.setGeometry(QtCore.QRect(410, 80, 75, 31))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.editEditPushButton.setFont(font)
        self.editEditPushButton.setObjectName("editEditPushButton")
        self.label_12 = QtWidgets.QLabel(self.editTab)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.editSavePushButton = QtWidgets.QPushButton(self.editTab)
        self.editSavePushButton.setGeometry(QtCore.QRect(10, 400, 651, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.editSavePushButton.setFont(font)
        self.editSavePushButton.setStyleSheet("#editSavePushButton {\n"
"    background-color: #800080; /* Green */\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 14px;\n"
"    height: 35px;\n"
"}\n"
"\n"
"QPushButton#editSavePushButton:hover {\n"
"    background-color: #4d004d;\n"
"}\n"
"\n"
"QPushButton#editSavePushButton:pressed {\n"
"    background-color: #800080;     \n"
"}")
        self.editSavePushButton.setObjectName("editSavePushButton")
        self.tabWidget.addTab(self.editTab, "")
        self.deleteTab = QtWidgets.QWidget()
        self.deleteTab.setObjectName("deleteTab")
        self.label_11 = QtWidgets.QLabel(self.deleteTab)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.deleteTypeLineEdit = QtWidgets.QLineEdit(self.deleteTab)
        self.deleteTypeLineEdit.setGeometry(QtCore.QRect(10, 45, 361, 31))
        self.deleteTypeLineEdit.setObjectName("deleteTypeLineEdit")
        self.deleteDeletePushButton = QtWidgets.QPushButton(self.deleteTab)
        self.deleteDeletePushButton.setGeometry(QtCore.QRect(380, 45, 75, 31))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.deleteDeletePushButton.setFont(font)
        self.deleteDeletePushButton.setObjectName("deleteDeletePushButton")
        self.deleteTreeWidget = QtWidgets.QTreeWidget(self.deleteTab)
        self.deleteTreeWidget.setGeometry(QtCore.QRect(10, 88, 651, 311))
        self.deleteTreeWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.deleteTreeWidget.setObjectName("deleteTreeWidget")
        self.tabWidget.addTab(self.deleteTab, "")
        self.tabSettings = QtWidgets.QWidget()
        self.tabSettings.setObjectName("tabSettings")
        self.label_16 = QtWidgets.QLabel(self.tabSettings)
        self.label_16.setGeometry(QtCore.QRect(10, 20, 141, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tabSettings)
        self.label_17.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.label_17.setObjectName("label_17")
        self.settingsNewFileNameLineEdit = QtWidgets.QLineEdit(self.tabSettings)
        self.settingsNewFileNameLineEdit.setGeometry(QtCore.QRect(140, 50, 391, 31))
        self.settingsNewFileNameLineEdit.setObjectName("settingsNewFileNameLineEdit")
        self.settingsCreatePushButton = QtWidgets.QPushButton(self.tabSettings)
        self.settingsCreatePushButton.setGeometry(QtCore.QRect(10, 400, 651, 41))
        self.settingsCreatePushButton.setStyleSheet("#settingsCreatePushButton {\n"
"    background-color: #ff0000; /* Green */\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    font-size: 14px;\n"
"    height: 35px;\n"
"}\n"
"\n"
"QPushButton#settingsCreatePushButton:hover {\n"
"    background-color: #b30000;\n"
"}\n"
"\n"
"QPushButton#settingsCreatePushButton:pressed {\n"
"    background-color: #ff0000;     \n"
"}")
        self.settingsCreatePushButton.setObjectName("settingsCreatePushButton")
        self.label_18 = QtWidgets.QLabel(self.tabSettings)
        self.label_18.setGeometry(QtCore.QRect(20, 120, 81, 16))
        self.label_18.setObjectName("label_18")
        self.settingsBaseDirectoryLineEdit = QtWidgets.QLineEdit(self.tabSettings)
        self.settingsBaseDirectoryLineEdit.setGeometry(QtCore.QRect(140, 110, 391, 31))
        self.settingsBaseDirectoryLineEdit.setObjectName("settingsBaseDirectoryLineEdit")
        self.settingsDirectoryPushButton = QtWidgets.QPushButton(self.tabSettings)
        self.settingsDirectoryPushButton.setGeometry(QtCore.QRect(540, 110, 51, 31))
        self.settingsDirectoryPushButton.setObjectName("settingsDirectoryPushButton")
        self.tabWidget.addTab(self.tabSettings, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.outputTitleLabel = QtWidgets.QLabel(botShotForm)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.outputTitleLabel.setFont(font)
        self.outputTitleLabel.setObjectName("outputTitleLabel")
        self.verticalLayout.addWidget(self.outputTitleLabel)
        self.finalPreviewOutputLabel = QtWidgets.QLabel(botShotForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.finalPreviewOutputLabel.setFont(font)
        self.finalPreviewOutputLabel.setStyleSheet("#finalPreviewOutputLabel{\n"
"    padding: 8px;\n"
"    color:  white;\n"
"    border: 1px solid white;\n"
"    background-color: #008CBA; /* Blue*/\n"
"}\n"
"")
        self.finalPreviewOutputLabel.setText("")
        self.finalPreviewOutputLabel.setObjectName("finalPreviewOutputLabel")
        self.verticalLayout.addWidget(self.finalPreviewOutputLabel)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(botShotForm)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(botShotForm)
        botShotForm.setTabOrder(self.previewVersionLineEdit, self.previewTypeLineEdit)
        botShotForm.setTabOrder(self.previewTypeLineEdit, self.previewTreeWidget)
        botShotForm.setTabOrder(self.previewTreeWidget, self.previewButton)
        botShotForm.setTabOrder(self.previewButton, self.createTypeLineEdit)
        botShotForm.setTabOrder(self.createTypeLineEdit, self.createDepartmentComboBox)
        botShotForm.setTabOrder(self.createDepartmentComboBox, self.createRenderLineEdit)
        botShotForm.setTabOrder(self.createRenderLineEdit, self.createVersionLineEdit)
        botShotForm.setTabOrder(self.createVersionLineEdit, self.createPushButton)
        botShotForm.setTabOrder(self.createPushButton, self.editTypeLineEdit)
        botShotForm.setTabOrder(self.editTypeLineEdit, self.editEditPushButton)
        botShotForm.setTabOrder(self.editEditPushButton, self.editRenderLineEdit)
        botShotForm.setTabOrder(self.editRenderLineEdit, self.editDirectoryLineEdit)
        botShotForm.setTabOrder(self.editDirectoryLineEdit, self.editDirectoryPushButton)
        botShotForm.setTabOrder(self.editDirectoryPushButton, self.editVersionLineEdit)
        botShotForm.setTabOrder(self.editVersionLineEdit, self.deleteTypeLineEdit)
        botShotForm.setTabOrder(self.deleteTypeLineEdit, self.deleteDeletePushButton)
        botShotForm.setTabOrder(self.deleteDeletePushButton, self.settingsNewFileNameLineEdit)
        botShotForm.setTabOrder(self.settingsNewFileNameLineEdit, self.settingsBaseDirectoryLineEdit)
        botShotForm.setTabOrder(self.settingsBaseDirectoryLineEdit, self.settingsDirectoryPushButton)
        botShotForm.setTabOrder(self.settingsDirectoryPushButton, self.settingsCreatePushButton)
        botShotForm.setTabOrder(self.settingsCreatePushButton, self.tabWidget)

    def retranslateUi(self, botShotForm):
        botShotForm.setWindowTitle(QtWidgets.QApplication.translate("botShotForm", "BOT SHOT Editor", None, -1))
        self.shotEditorTitleLabel.setText(QtWidgets.QApplication.translate("botShotForm", "BOT SHOT Editor", None, -1))
        self.previewTreeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("botShotForm", "Type/Show", None, -1))
        self.previewTreeWidget.headerItem().setText(1, QtWidgets.QApplication.translate("botShotForm", "Department", None, -1))
        self.previewTreeWidget.headerItem().setText(2, QtWidgets.QApplication.translate("botShotForm", "Render", None, -1))
        self.previewTreeWidget.headerItem().setText(3, QtWidgets.QApplication.translate("botShotForm", "Version", None, -1))
        self.previewTreeWidget.headerItem().setText(4, QtWidgets.QApplication.translate("botShotForm", "Output Path", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("botShotForm", "Version", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("botShotForm", "Type/Show", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("botShotForm", "Select/Type a shot to get preview", None, -1))
        self.previewButton.setText(QtWidgets.QApplication.translate("botShotForm", "Preview", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.previewTab), QtWidgets.QApplication.translate("botShotForm", "Preview", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("botShotForm", "Type/Shot Name", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("botShotForm", "Render", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("botShotForm", "Department", None, -1))
        self.createDepartmentComboBox.setItemText(0, QtWidgets.QApplication.translate("botShotForm", "Select a department", None, -1))
        self.createDepartmentComboBox.setItemText(1, QtWidgets.QApplication.translate("botShotForm", "Roto", None, -1))
        self.createDepartmentComboBox.setItemText(2, QtWidgets.QApplication.translate("botShotForm", "Paint", None, -1))
        self.createDepartmentComboBox.setItemText(3, QtWidgets.QApplication.translate("botShotForm", "Comp", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("botShotForm", "Add a New Shot", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("botShotForm", "Version", None, -1))
        self.createPushButton.setText(QtWidgets.QApplication.translate("botShotForm", "Add Shot", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.createTab), QtWidgets.QApplication.translate("botShotForm", "Create", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("botShotForm", "Type", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("botShotForm", "Version", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("botShotForm", "Render", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("botShotForm", "Base Path", None, -1))
        self.editDirectoryPushButton.setText(QtWidgets.QApplication.translate("botShotForm", "...", None, -1))
        self.editEditPushButton.setText(QtWidgets.QApplication.translate("botShotForm", "Edit", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("botShotForm", "Enter the TYPE to edit", None, -1))
        self.editSavePushButton.setText(QtWidgets.QApplication.translate("botShotForm", "Save", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.editTab), QtWidgets.QApplication.translate("botShotForm", "Edit", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("botShotForm", "Enter the TYPE to Delete", None, -1))
        self.deleteDeletePushButton.setText(QtWidgets.QApplication.translate("botShotForm", "Delete", None, -1))
        self.deleteTreeWidget.headerItem().setText(0, QtWidgets.QApplication.translate("botShotForm", "Type/Show", None, -1))
        self.deleteTreeWidget.headerItem().setText(1, QtWidgets.QApplication.translate("botShotForm", "Department", None, -1))
        self.deleteTreeWidget.headerItem().setText(2, QtWidgets.QApplication.translate("botShotForm", "Render", None, -1))
        self.deleteTreeWidget.headerItem().setText(3, QtWidgets.QApplication.translate("botShotForm", "Version", None, -1))
        self.deleteTreeWidget.headerItem().setText(4, QtWidgets.QApplication.translate("botShotForm", "Output Path", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.deleteTab), QtWidgets.QApplication.translate("botShotForm", "Delete", None, -1))
        self.label_16.setText(QtWidgets.QApplication.translate("botShotForm", "Create New Config File", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("botShotForm", "New Data File Name", None, -1))
        self.settingsCreatePushButton.setText(QtWidgets.QApplication.translate("botShotForm", "Create", None, -1))
        self.label_18.setText(QtWidgets.QApplication.translate("botShotForm", "Base Directory", None, -1))
        self.settingsDirectoryPushButton.setText(QtWidgets.QApplication.translate("botShotForm", "...", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings), QtWidgets.QApplication.translate("botShotForm", "Settings", None, -1))
        self.outputTitleLabel.setText(QtWidgets.QApplication.translate("botShotForm", "Output:", None, -1))

