# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remapper.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RemapperWindow(object):
    def setupUi(self, RemapperWindow):
        RemapperWindow.setObjectName("RemapperWindow")
        RemapperWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(RemapperWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.remap_table = QtWidgets.QTableWidget(self.centralwidget)
        self.remap_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.remap_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.remap_table.setObjectName("remap_table")
        self.remap_table.setColumnCount(2)
        self.remap_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.remap_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.remap_table.setHorizontalHeaderItem(1, item)
        self.remap_table.horizontalHeader().setStretchLastSection(True)
        self.remap_table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.remap_table)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout_2.addWidget(self.add_button)
        self.remove_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_button.setObjectName("remove_button")
        self.horizontalLayout_2.addWidget(self.remove_button)
        self.start_stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_stop_button.setObjectName("start_stop_button")
        self.horizontalLayout_2.addWidget(self.start_stop_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        RemapperWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RemapperWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 36))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        RemapperWindow.setMenuBar(self.menubar)
        self.action_open = QtWidgets.QAction(RemapperWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(RemapperWindow)
        self.action_save.setObjectName("action_save")
        self.action_exit = QtWidgets.QAction(RemapperWindow)
        self.action_exit.setObjectName("action_exit")
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_save)
        self.menuFile.addAction(self.action_exit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(RemapperWindow)
        QtCore.QMetaObject.connectSlotsByName(RemapperWindow)

    def retranslateUi(self, RemapperWindow):
        _translate = QtCore.QCoreApplication.translate
        RemapperWindow.setWindowTitle(_translate("RemapperWindow", "MainWindow"))
        item = self.remap_table.horizontalHeaderItem(0)
        item.setText(_translate("RemapperWindow", "remap"))
        item = self.remap_table.horizontalHeaderItem(1)
        item.setText(_translate("RemapperWindow", "status"))
        self.add_button.setText(_translate("RemapperWindow", "Add"))
        self.remove_button.setText(_translate("RemapperWindow", "Remove"))
        self.start_stop_button.setText(_translate("RemapperWindow", "Start/Stop"))
        self.menuFile.setTitle(_translate("RemapperWindow", "File"))
        self.menuAbout.setTitle(_translate("RemapperWindow", "About"))
        self.action_open.setText(_translate("RemapperWindow", "Open"))
        self.action_save.setText(_translate("RemapperWindow", "Save"))
        self.action_exit.setText(_translate("RemapperWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RemapperWindow = QtWidgets.QMainWindow()
    ui = Ui_RemapperWindow()
    ui.setupUi(RemapperWindow)
    RemapperWindow.show()
    sys.exit(app.exec_())