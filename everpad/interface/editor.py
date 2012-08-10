# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created: Fri Aug 10 15:21:51 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Editor(object):
    def setupUi(self, Editor):
        Editor.setObjectName("Editor")
        Editor.resize(351, 333)
        self.centralwidget = QtGui.QWidget(Editor)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content = QtGui.QTextEdit(self.centralwidget)
        self.content.setObjectName("content")
        self.verticalLayout.addWidget(self.content)
        self.options = QtGui.QHBoxLayout()
        self.options.setObjectName("options")
        self.notebook = QtGui.QComboBox(self.centralwidget)
        self.notebook.setObjectName("notebook")
        self.options.addWidget(self.notebook)
        self.tags = QtGui.QLineEdit(self.centralwidget)
        self.tags.setObjectName("tags")
        self.options.addWidget(self.tags)
        self.verticalLayout.addLayout(self.options)
        Editor.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Editor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 25))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtGui.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        Editor.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(Editor)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        Editor.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        Editor.insertToolBarBreak(self.toolBar)
        self.actionSave = QtGui.QAction(Editor)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_and_close = QtGui.QAction(Editor)
        self.actionSave_and_close.setObjectName("actionSave_and_close")
        self.actionDelete = QtGui.QAction(Editor)
        self.actionDelete.setObjectName("actionDelete")
        self.actionClose = QtGui.QAction(Editor)
        self.actionClose.setObjectName("actionClose")
        self.actionCut = QtGui.QAction(Editor)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtGui.QAction(Editor)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(Editor)
        self.actionPaste.setObjectName("actionPaste")
        self.menuFIle.addAction(self.actionSave)
        self.menuFIle.addAction(self.actionSave_and_close)
        self.menuFIle.addAction(self.actionDelete)
        self.menuFIle.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(Editor)
        QtCore.QMetaObject.connectSlotsByName(Editor)

    def retranslateUi(self, Editor):
        Editor.setWindowTitle(QtGui.QApplication.translate("Editor", "Everpad", None, QtGui.QApplication.UnicodeUTF8))
        self.notebook.setToolTip(QtGui.QApplication.translate("Editor", "Select notebook", None, QtGui.QApplication.UnicodeUTF8))
        self.tags.setToolTip(QtGui.QApplication.translate("Editor", "Note tags", None, QtGui.QApplication.UnicodeUTF8))
        self.tags.setPlaceholderText(QtGui.QApplication.translate("Editor", "Commas separated tags", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFIle.setTitle(QtGui.QApplication.translate("Editor", "Note", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("Editor", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("Editor", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("Editor", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_and_close.setText(QtGui.QApplication.translate("Editor", "Save and close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("Editor", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("Editor", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("Editor", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("Editor", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("Editor", "Paste", None, QtGui.QApplication.UnicodeUTF8))

