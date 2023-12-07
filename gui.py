# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.view_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.view_btn.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.view_btn.setObjectName("view_btn")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 40, 591, 361))
        self.stackedWidget.setObjectName("stackedWidget")
        self.view_page = QtWidgets.QWidget()
        self.view_page.setObjectName("view_page")
        self.view_lbl = QtWidgets.QLabel(parent=self.view_page)
        self.view_lbl.setGeometry(QtCore.QRect(250, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.view_lbl.setFont(font)
        self.view_lbl.setObjectName("view_lbl")
        self.current_checkings_lbl = QtWidgets.QLabel(parent=self.view_page)
        self.current_checkings_lbl.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.current_checkings_lbl.setObjectName("current_checkings_lbl")
        self.checkings_amount_lbl = QtWidgets.QLabel(parent=self.view_page)
        self.checkings_amount_lbl.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.checkings_amount_lbl.setObjectName("checkings_amount_lbl")
        self.current_savings_lbl = QtWidgets.QLabel(parent=self.view_page)
        self.current_savings_lbl.setGeometry(QtCore.QRect(130, 50, 91, 20))
        self.current_savings_lbl.setObjectName("current_savings_lbl")
        self.savings_amount_lbl = QtWidgets.QLabel(parent=self.view_page)
        self.savings_amount_lbl.setGeometry(QtCore.QRect(130, 70, 47, 14))
        self.savings_amount_lbl.setObjectName("savings_amount_lbl")
        self.current_other_lbl = QtWidgets.QLabel(parent=self.view_page)
        self.current_other_lbl.setGeometry(QtCore.QRect(240, 53, 81, 16))
        self.current_other_lbl.setObjectName("current_other_lbl")
        self.other_amount_lbl = QtWidgets.QLabel(parent=self.view_page)
        self.other_amount_lbl.setGeometry(QtCore.QRect(240, 70, 47, 14))
        self.other_amount_lbl.setObjectName("other_amount_lbl")
        self.set_amount_checking_lnedit = QtWidgets.QLineEdit(parent=self.view_page)
        self.set_amount_checking_lnedit.setGeometry(QtCore.QRect(10, 130, 91, 20))
        self.set_amount_checking_lnedit.setObjectName("set_amount_checking_lnedit")
        self.set_amount_checking_btn = QtWidgets.QPushButton(parent=self.view_page)
        self.set_amount_checking_btn.setGeometry(QtCore.QRect(10, 100, 91, 23))
        self.set_amount_checking_btn.setObjectName("set_amount_checking_btn")
        self.set_amount_saving_btn = QtWidgets.QPushButton(parent=self.view_page)
        self.set_amount_saving_btn.setGeometry(QtCore.QRect(130, 100, 91, 23))
        self.set_amount_saving_btn.setObjectName("set_amount_saving_btn")
        self.set_amount_saving_lnedit = QtWidgets.QLineEdit(parent=self.view_page)
        self.set_amount_saving_lnedit.setGeometry(QtCore.QRect(130, 130, 91, 20))
        self.set_amount_saving_lnedit.setObjectName("set_amount_saving_lnedit")
        self.set_amount_other_btn = QtWidgets.QPushButton(parent=self.view_page)
        self.set_amount_other_btn.setGeometry(QtCore.QRect(240, 100, 91, 23))
        self.set_amount_other_btn.setObjectName("set_amount_other_btn")
        self.set_amount_other_lnedit = QtWidgets.QLineEdit(parent=self.view_page)
        self.set_amount_other_lnedit.setGeometry(QtCore.QRect(240, 130, 91, 20))
        self.set_amount_other_lnedit.setObjectName("set_amount_other_lnedit")
        self.view_warning_lbl = QtWidgets.QLabel(parent=self.view_page)
        self.view_warning_lbl.setGeometry(QtCore.QRect(10, 160, 321, 16))
        self.view_warning_lbl.setObjectName("view_warning_lbl")
        self.stackedWidget.addWidget(self.view_page)
        self.check_day_page = QtWidgets.QWidget()
        self.check_day_page.setObjectName("check_day_page")
        self.check_day_lbl = QtWidgets.QLabel(parent=self.check_day_page)
        self.check_day_lbl.setGeometry(QtCore.QRect(240, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.check_day_lbl.setFont(font)
        self.check_day_lbl.setObjectName("check_day_lbl")
        self.year_lbl_3 = QtWidgets.QLabel(parent=self.check_day_page)
        self.year_lbl_3.setGeometry(QtCore.QRect(400, 60, 31, 16))
        self.year_lbl_3.setObjectName("year_lbl_3")
        self.check_year_lnedit = QtWidgets.QLineEdit(parent=self.check_day_page)
        self.check_year_lnedit.setGeometry(QtCore.QRect(360, 90, 113, 20))
        self.check_year_lnedit.setObjectName("check_year_lnedit")
        self.month_lbl_3 = QtWidgets.QLabel(parent=self.check_day_page)
        self.month_lbl_3.setGeometry(QtCore.QRect(140, 60, 41, 16))
        self.month_lbl_3.setObjectName("month_lbl_3")
        self.check_month_lnedit = QtWidgets.QLineEdit(parent=self.check_day_page)
        self.check_month_lnedit.setGeometry(QtCore.QRect(100, 90, 113, 20))
        self.check_month_lnedit.setObjectName("check_month_lnedit")
        self.check_day_lnedit = QtWidgets.QLineEdit(parent=self.check_day_page)
        self.check_day_lnedit.setGeometry(QtCore.QRect(230, 90, 113, 20))
        self.check_day_lnedit.setObjectName("check_day_lnedit")
        self.day_lbl_3 = QtWidgets.QLabel(parent=self.check_day_page)
        self.day_lbl_3.setGeometry(QtCore.QRect(280, 60, 21, 16))
        self.day_lbl_3.setObjectName("day_lbl_3")
        self.view_day_btn = QtWidgets.QPushButton(parent=self.check_day_page)
        self.view_day_btn.setGeometry(QtCore.QRect(250, 120, 75, 23))
        self.view_day_btn.setObjectName("view_day_btn")
        self.label = QtWidgets.QLabel(parent=self.check_day_page)
        self.label.setGeometry(QtCore.QRect(30, 160, 61, 21))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(parent=self.check_day_page)
        self.label_4.setGeometry(QtCore.QRect(130, 160, 47, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.check_day_page)
        self.label_5.setGeometry(QtCore.QRect(220, 160, 47, 14))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.check_day_page)
        self.label_6.setGeometry(QtCore.QRect(300, 160, 81, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.check_day_page)
        self.label_7.setGeometry(QtCore.QRect(410, 160, 47, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.check_day_page)
        self.label_8.setGeometry(QtCore.QRect(520, 160, 47, 21))
        self.label_8.setObjectName("label_8")
        self.groceries_amount_lbl = QtWidgets.QLabel(parent=self.check_day_page)
        self.groceries_amount_lbl.setGeometry(QtCore.QRect(30, 180, 47, 14))
        self.groceries_amount_lbl.setObjectName("groceries_amount_lbl")
        self.gas_amount_lbl = QtWidgets.QLabel(parent=self.check_day_page)
        self.gas_amount_lbl.setGeometry(QtCore.QRect(120, 180, 47, 14))
        self.gas_amount_lbl.setObjectName("gas_amount_lbl")
        self.fun_amount_lbl = QtWidgets.QLabel(parent=self.check_day_page)
        self.fun_amount_lbl.setGeometry(QtCore.QRect(210, 180, 47, 14))
        self.fun_amount_lbl.setObjectName("fun_amount_lbl")
        self.subscriptions_amount_lbl = QtWidgets.QLabel(parent=self.check_day_page)
        self.subscriptions_amount_lbl.setGeometry(QtCore.QRect(310, 180, 47, 14))
        self.subscriptions_amount_lbl.setObjectName("subscriptions_amount_lbl")
        self.savings_amount_lbl_2 = QtWidgets.QLabel(parent=self.check_day_page)
        self.savings_amount_lbl_2.setGeometry(QtCore.QRect(410, 180, 47, 14))
        self.savings_amount_lbl_2.setObjectName("savings_amount_lbl_2")
        self.income_amount_lbl = QtWidgets.QLabel(parent=self.check_day_page)
        self.income_amount_lbl.setGeometry(QtCore.QRect(520, 180, 47, 14))
        self.income_amount_lbl.setObjectName("income_amount_lbl")
        self.check_day_warning_lbl = QtWidgets.QLabel(parent=self.check_day_page)
        self.check_day_warning_lbl.setGeometry(QtCore.QRect(140, 40, 271, 20))
        self.check_day_warning_lbl.setObjectName("check_day_warning_lbl")
        self.label_3 = QtWidgets.QLabel(parent=self.check_day_page)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 91, 16))
        self.label_3.setObjectName("label_3")
        self.tot_exp_lbl = QtWidgets.QLabel(parent=self.check_day_page)
        self.tot_exp_lbl.setGeometry(QtCore.QRect(30, 240, 81, 16))
        self.tot_exp_lbl.setObjectName("tot_exp_lbl")
        self.label_10 = QtWidgets.QLabel(parent=self.check_day_page)
        self.label_10.setGeometry(QtCore.QRect(150, 220, 101, 16))
        self.label_10.setObjectName("label_10")
        self.revenue_for_day_lbl = QtWidgets.QLabel(parent=self.check_day_page)
        self.revenue_for_day_lbl.setGeometry(QtCore.QRect(150, 240, 71, 16))
        self.revenue_for_day_lbl.setObjectName("revenue_for_day_lbl")
        self.stackedWidget.addWidget(self.check_day_page)
        self.add_page = QtWidgets.QWidget()
        self.add_page.setObjectName("add_page")
        self.label_2 = QtWidgets.QLabel(parent=self.add_page)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.month_lnedit = QtWidgets.QLineEdit(parent=self.add_page)
        self.month_lnedit.setGeometry(QtCore.QRect(40, 80, 113, 20))
        self.month_lnedit.setObjectName("month_lnedit")
        self.day_lnedit = QtWidgets.QLineEdit(parent=self.add_page)
        self.day_lnedit.setGeometry(QtCore.QRect(170, 80, 113, 20))
        self.day_lnedit.setObjectName("day_lnedit")
        self.year_lnedit = QtWidgets.QLineEdit(parent=self.add_page)
        self.year_lnedit.setGeometry(QtCore.QRect(300, 80, 113, 20))
        self.year_lnedit.setObjectName("year_lnedit")
        self.month_lbl = QtWidgets.QLabel(parent=self.add_page)
        self.month_lbl.setGeometry(QtCore.QRect(80, 50, 41, 16))
        self.month_lbl.setObjectName("month_lbl")
        self.day_lbl = QtWidgets.QLabel(parent=self.add_page)
        self.day_lbl.setGeometry(QtCore.QRect(210, 50, 31, 16))
        self.day_lbl.setObjectName("day_lbl")
        self.year_lbl = QtWidgets.QLabel(parent=self.add_page)
        self.year_lbl.setGeometry(QtCore.QRect(340, 50, 31, 16))
        self.year_lbl.setObjectName("year_lbl")
        self.expense_cost_lbl = QtWidgets.QLabel(parent=self.add_page)
        self.expense_cost_lbl.setGeometry(QtCore.QRect(40, 120, 71, 16))
        self.expense_cost_lbl.setObjectName("expense_cost_lbl")
        self.expense_lnedit = QtWidgets.QLineEdit(parent=self.add_page)
        self.expense_lnedit.setGeometry(QtCore.QRect(40, 140, 113, 20))
        self.expense_lnedit.setObjectName("expense_lnedit")
        self.radioButton = QtWidgets.QRadioButton(parent=self.add_page)
        self.radioButton.setGeometry(QtCore.QRect(40, 200, 83, 18))
        self.radioButton.setObjectName("radioButton")
        self.category_btn_grp = QtWidgets.QButtonGroup(MainWindow)
        self.category_btn_grp.setObjectName("category_btn_grp")
        self.category_btn_grp.addButton(self.radioButton)
        self.category_lbl = QtWidgets.QLabel(parent=self.add_page)
        self.category_lbl.setGeometry(QtCore.QRect(40, 180, 51, 16))
        self.category_lbl.setObjectName("category_lbl")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.add_page)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 200, 83, 18))
        self.radioButton_2.setObjectName("radioButton_2")
        self.category_btn_grp.addButton(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.add_page)
        self.radioButton_3.setGeometry(QtCore.QRect(230, 200, 83, 18))
        self.radioButton_3.setObjectName("radioButton_3")
        self.category_btn_grp.addButton(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(parent=self.add_page)
        self.radioButton_4.setGeometry(QtCore.QRect(310, 200, 91, 18))
        self.radioButton_4.setObjectName("radioButton_4")
        self.category_btn_grp.addButton(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(parent=self.add_page)
        self.radioButton_5.setGeometry(QtCore.QRect(420, 200, 83, 18))
        self.radioButton_5.setObjectName("radioButton_5")
        self.category_btn_grp.addButton(self.radioButton_5)
        self.add_expense_btn = QtWidgets.QPushButton(parent=self.add_page)
        self.add_expense_btn.setGeometry(QtCore.QRect(40, 230, 161, 23))
        self.add_expense_btn.setObjectName("add_expense_btn")
        self.income_lbl = QtWidgets.QLabel(parent=self.add_page)
        self.income_lbl.setGeometry(QtCore.QRect(190, 120, 47, 14))
        self.income_lbl.setObjectName("income_lbl")
        self.income_lnedit = QtWidgets.QLineEdit(parent=self.add_page)
        self.income_lnedit.setGeometry(QtCore.QRect(180, 140, 113, 20))
        self.income_lnedit.setObjectName("income_lnedit")
        self.add_warning_lbl = QtWidgets.QLabel(parent=self.add_page)
        self.add_warning_lbl.setGeometry(QtCore.QRect(40, 260, 451, 21))
        self.add_warning_lbl.setObjectName("add_warning_lbl")
        self.radioButton_6 = QtWidgets.QRadioButton(parent=self.add_page)
        self.radioButton_6.setGeometry(QtCore.QRect(500, 200, 83, 18))
        self.radioButton_6.setObjectName("radioButton_6")
        self.category_btn_grp.addButton(self.radioButton_6)
        self.stackedWidget.addWidget(self.add_page)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_9 = QtWidgets.QLabel(parent=self.page)
        self.label_9.setGeometry(QtCore.QRect(206, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.month_lbl_4 = QtWidgets.QLabel(parent=self.page)
        self.month_lbl_4.setGeometry(QtCore.QRect(170, 80, 41, 16))
        self.month_lbl_4.setObjectName("month_lbl_4")
        self.check_month_lnedit_2 = QtWidgets.QLineEdit(parent=self.page)
        self.check_month_lnedit_2.setGeometry(QtCore.QRect(140, 110, 113, 20))
        self.check_month_lnedit_2.setObjectName("check_month_lnedit_2")
        self.year_lbl_4 = QtWidgets.QLabel(parent=self.page)
        self.year_lbl_4.setGeometry(QtCore.QRect(350, 80, 31, 16))
        self.year_lbl_4.setObjectName("year_lbl_4")
        self.view_month_btn = QtWidgets.QPushButton(parent=self.page)
        self.view_month_btn.setGeometry(QtCore.QRect(240, 140, 75, 23))
        self.view_month_btn.setObjectName("view_month_btn")
        self.check_year_lnedit_2 = QtWidgets.QLineEdit(parent=self.page)
        self.check_year_lnedit_2.setGeometry(QtCore.QRect(300, 110, 113, 20))
        self.check_year_lnedit_2.setObjectName("check_year_lnedit_2")
        self.check_month_warning_lbl = QtWidgets.QLabel(parent=self.page)
        self.check_month_warning_lbl.setGeometry(QtCore.QRect(130, 50, 271, 20))
        self.check_month_warning_lbl.setObjectName("check_month_warning_lbl")
        self.label_11 = QtWidgets.QLabel(parent=self.page)
        self.label_11.setGeometry(QtCore.QRect(400, 180, 47, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.page)
        self.label_12.setGeometry(QtCore.QRect(290, 180, 81, 21))
        self.label_12.setObjectName("label_12")
        self.gas_amount_lbl_2 = QtWidgets.QLabel(parent=self.page)
        self.gas_amount_lbl_2.setGeometry(QtCore.QRect(110, 200, 47, 14))
        self.gas_amount_lbl_2.setObjectName("gas_amount_lbl_2")
        self.label_13 = QtWidgets.QLabel(parent=self.page)
        self.label_13.setGeometry(QtCore.QRect(510, 180, 47, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.page)
        self.label_14.setGeometry(QtCore.QRect(20, 180, 61, 21))
        self.label_14.setObjectName("label_14")
        self.fun_amount_lbl_2 = QtWidgets.QLabel(parent=self.page)
        self.fun_amount_lbl_2.setGeometry(QtCore.QRect(200, 200, 47, 14))
        self.fun_amount_lbl_2.setObjectName("fun_amount_lbl_2")
        self.label_15 = QtWidgets.QLabel(parent=self.page)
        self.label_15.setGeometry(QtCore.QRect(210, 180, 47, 14))
        self.label_15.setObjectName("label_15")
        self.groceries_amount_lbl_2 = QtWidgets.QLabel(parent=self.page)
        self.groceries_amount_lbl_2.setGeometry(QtCore.QRect(20, 200, 47, 14))
        self.groceries_amount_lbl_2.setObjectName("groceries_amount_lbl_2")
        self.subscriptions_amount_lbl_2 = QtWidgets.QLabel(parent=self.page)
        self.subscriptions_amount_lbl_2.setGeometry(QtCore.QRect(300, 200, 47, 14))
        self.subscriptions_amount_lbl_2.setObjectName("subscriptions_amount_lbl_2")
        self.income_amount_lbl_2 = QtWidgets.QLabel(parent=self.page)
        self.income_amount_lbl_2.setGeometry(QtCore.QRect(510, 200, 47, 14))
        self.income_amount_lbl_2.setObjectName("income_amount_lbl_2")
        self.label_16 = QtWidgets.QLabel(parent=self.page)
        self.label_16.setGeometry(QtCore.QRect(120, 180, 47, 21))
        self.label_16.setObjectName("label_16")
        self.savings_amount_lbl_3 = QtWidgets.QLabel(parent=self.page)
        self.savings_amount_lbl_3.setGeometry(QtCore.QRect(400, 200, 47, 14))
        self.savings_amount_lbl_3.setObjectName("savings_amount_lbl_3")
        self.label_17 = QtWidgets.QLabel(parent=self.page)
        self.label_17.setGeometry(QtCore.QRect(20, 240, 101, 16))
        self.label_17.setObjectName("label_17")
        self.total_expenses_lbl = QtWidgets.QLabel(parent=self.page)
        self.total_expenses_lbl.setGeometry(QtCore.QRect(20, 260, 81, 16))
        self.total_expenses_lbl.setObjectName("total_expenses_lbl")
        self.label_19 = QtWidgets.QLabel(parent=self.page)
        self.label_19.setGeometry(QtCore.QRect(130, 240, 71, 16))
        self.label_19.setObjectName("label_19")
        self.total_revenue_lbl = QtWidgets.QLabel(parent=self.page)
        self.total_revenue_lbl.setGeometry(QtCore.QRect(130, 260, 71, 16))
        self.total_revenue_lbl.setObjectName("total_revenue_lbl")
        self.stackedWidget.addWidget(self.page)
        self.add_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.add_btn.setObjectName("add_btn")
        self.check_day_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.check_day_btn.setGeometry(QtCore.QRect(190, 10, 75, 23))
        self.check_day_btn.setObjectName("check_day_btn")
        self.check_month_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.check_month_btn.setGeometry(QtCore.QRect(280, 10, 81, 23))
        self.check_month_btn.setObjectName("check_month_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Financial Manager"))
        self.view_btn.setText(_translate("MainWindow", "View"))
        self.view_lbl.setText(_translate("MainWindow", "View"))
        self.current_checkings_lbl.setText(_translate("MainWindow", "Current Checkings"))
        self.checkings_amount_lbl.setText(_translate("MainWindow", "Amount"))
        self.current_savings_lbl.setText(_translate("MainWindow", "Current Savings"))
        self.savings_amount_lbl.setText(_translate("MainWindow", "Amount"))
        self.current_other_lbl.setText(_translate("MainWindow", "Current Other"))
        self.other_amount_lbl.setText(_translate("MainWindow", "Amount"))
        self.set_amount_checking_btn.setText(_translate("MainWindow", "Set Amount"))
        self.set_amount_saving_btn.setText(_translate("MainWindow", "Set Amount"))
        self.set_amount_other_btn.setText(_translate("MainWindow", "Set Amount"))
        self.view_warning_lbl.setText(_translate("MainWindow", "Warning"))
        self.check_day_lbl.setText(_translate("MainWindow", "Check Day"))
        self.year_lbl_3.setText(_translate("MainWindow", "Year"))
        self.month_lbl_3.setText(_translate("MainWindow", "Month"))
        self.day_lbl_3.setText(_translate("MainWindow", "Day"))
        self.view_day_btn.setText(_translate("MainWindow", "View Day"))
        self.label.setText(_translate("MainWindow", "Groceries"))
        self.label_4.setText(_translate("MainWindow", "Gas"))
        self.label_5.setText(_translate("MainWindow", "Fun"))
        self.label_6.setText(_translate("MainWindow", "Subscriptions"))
        self.label_7.setText(_translate("MainWindow", "Savings"))
        self.label_8.setText(_translate("MainWindow", "Income"))
        self.groceries_amount_lbl.setText(_translate("MainWindow", "Amount"))
        self.gas_amount_lbl.setText(_translate("MainWindow", "Amount"))
        self.fun_amount_lbl.setText(_translate("MainWindow", "Amount"))
        self.subscriptions_amount_lbl.setText(_translate("MainWindow", "Amount"))
        self.savings_amount_lbl_2.setText(_translate("MainWindow", "Amount"))
        self.income_amount_lbl.setText(_translate("MainWindow", "Amount"))
        self.check_day_warning_lbl.setText(_translate("MainWindow", "Warning"))
        self.label_3.setText(_translate("MainWindow", "Total expenses"))
        self.tot_exp_lbl.setText(_translate("MainWindow", "Amount"))
        self.label_10.setText(_translate("MainWindow", "Net Income"))
        self.revenue_for_day_lbl.setText(_translate("MainWindow", "Amount"))
        self.label_2.setText(_translate("MainWindow", "Add / Edit"))
        self.month_lbl.setText(_translate("MainWindow", "Month"))
        self.day_lbl.setText(_translate("MainWindow", "Day"))
        self.year_lbl.setText(_translate("MainWindow", "Year"))
        self.expense_cost_lbl.setText(_translate("MainWindow", "Expense Cost"))
        self.radioButton.setText(_translate("MainWindow", "Groceries"))
        self.category_lbl.setText(_translate("MainWindow", "Category"))
        self.radioButton_2.setText(_translate("MainWindow", "Gas"))
        self.radioButton_3.setText(_translate("MainWindow", "Fun"))
        self.radioButton_4.setText(_translate("MainWindow", "Subscription"))
        self.radioButton_5.setText(_translate("MainWindow", "Savings"))
        self.add_expense_btn.setText(_translate("MainWindow", "Add Expense And Income"))
        self.income_lbl.setText(_translate("MainWindow", "Income"))
        self.add_warning_lbl.setText(_translate("MainWindow", "Warning"))
        self.radioButton_6.setText(_translate("MainWindow", "None"))
        self.label_9.setText(_translate("MainWindow", "Check Month"))
        self.month_lbl_4.setText(_translate("MainWindow", "Month"))
        self.year_lbl_4.setText(_translate("MainWindow", "Year"))
        self.view_month_btn.setText(_translate("MainWindow", "View Month"))
        self.check_month_warning_lbl.setText(_translate("MainWindow", "Warning"))
        self.label_11.setText(_translate("MainWindow", "Savings"))
        self.label_12.setText(_translate("MainWindow", "Subscriptions"))
        self.gas_amount_lbl_2.setText(_translate("MainWindow", "Amount"))
        self.label_13.setText(_translate("MainWindow", "Income"))
        self.label_14.setText(_translate("MainWindow", "Groceries"))
        self.fun_amount_lbl_2.setText(_translate("MainWindow", "Amount"))
        self.label_15.setText(_translate("MainWindow", "Fun"))
        self.groceries_amount_lbl_2.setText(_translate("MainWindow", "Amount"))
        self.subscriptions_amount_lbl_2.setText(_translate("MainWindow", "Amount"))
        self.income_amount_lbl_2.setText(_translate("MainWindow", "Amount"))
        self.label_16.setText(_translate("MainWindow", "Gas"))
        self.savings_amount_lbl_3.setText(_translate("MainWindow", "Amount"))
        self.label_17.setText(_translate("MainWindow", "Total Expenses"))
        self.total_expenses_lbl.setText(_translate("MainWindow", "Amount"))
        self.label_19.setText(_translate("MainWindow", "Net Income"))
        self.total_revenue_lbl.setText(_translate("MainWindow", "Amount"))
        self.add_btn.setText(_translate("MainWindow", "Add / Edit"))
        self.check_day_btn.setText(_translate("MainWindow", "Check Day"))
        self.check_month_btn.setText(_translate("MainWindow", "Check Month"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
