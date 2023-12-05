from PyQt6.QtWidgets import *
from gui import *
import csv


class Manager(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__active_radio_button = None

        try:
            with open('accounts.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                header = next(csv_reader, None)

                if header:
                    self.__checkings_amount = float(header[0])
                    self.__savings_amount = float(header[1])
                    self.__other_amount = float(header[2])
                else:
                    self.__checkings_amount = 0
                    self.__savings_amount = 0
                    self.__other_amount = 0
        except:
            with open('accounts.csv', 'w') as csv_file:
                csv_writer = csv.writer(csv_file)
                data = [0,0,0]
                csv_writer.writerow(data)

                self.__checkings_amount = 0
                self.__savings_amount = 0
                self.__other_amount = 0

        try:
            with open('logs.csv', 'r') as csv_file:
                pass
        except:
            with open('logs.csv', 'w') as csv_file:
                csv_writer = csv.writer(csv_file)
                data = ['Date', 'Income', 'Groceries', 'Gas', 'Fun', 'Subscription', 'Savings']
                csv_writer.writerow(data)

        self.update_display_view()

        self.view_btn.clicked.connect(lambda: self.switch_page(0))
        self.check_day_btn.clicked.connect(lambda: self.switch_page(1))
        self.add_btn.clicked.connect(lambda: self.switch_page(2))

        self.set_amount_checking_btn.clicked.connect(lambda: self.set_checking())
        self.set_amount_saving_btn.clicked.connect(lambda: self.set_saving())
        self.set_amount_other_btn.clicked.connect(lambda: self.set_other())
        self.save_btn.clicked.connect(lambda: self.save_view())

        self.add_expense_btn.clicked.connect(lambda: self.save_add_edit())
        self.auto_fill_btn.clicked.connect(lambda: self.auto_fill())

        self.category_btn_grp.buttonClicked.connect(self.radio_button_selected)
        self.stackedWidget.setCurrentIndex(0)

    def auto_fill(self):
        self.month_lnedit.setText('1')
        self.day_lnedit.setText('1')
        self.year_lnedit.setText('1')
        self.expense_lnedit.setText('10')
        self.income_lnedit.setText('0')

    def update_display_view(self):
        self.view_warning_lbl.clear()

        self.checkings_amount_lbl.setText(f'${self.__checkings_amount:.2f}')
        self.savings_amount_lbl.setText(f'${self.__savings_amount:.2f}')
        self.other_amount_lbl.setText(f'${self.__other_amount:.2f}')

    def switch_page(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def set_checking(self):
        try:
            new_value = float(self.set_amount_checking_lnedit.text())
        except:
            self.view_warning_lbl.setText('value must be numeric')
            return
        self.__checkings_amount = new_value
        self.set_amount_checking_lnedit.clear()
        self.update_display_view()

    def set_saving(self):
        try:
            new_value = float(self.set_amount_saving_lnedit.text())
        except:
            self.view_warning_lbl.setText('value must be numeric')
            return
        self.__savings_amount = new_value
        self.set_amount_saving_lnedit.clear()
        self.update_display_view()

    def set_other(self):
        try:
            new_value = float(self.set_amount_other_lnedit.text())
        except:
            self.view_warning_lbl.setText('value must be numeric')
            return

        self.__other_amount = new_value
        self.set_amount_other_lnedit.clear()
        self.update_display_view()

    def save_view(self):
        data = [self.__checkings_amount, self.__savings_amount, self.__other_amount]
        with open('accounts.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader, None)

            with open('accounts.csv', 'w') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(data)

    def radio_button_selected(self, button):
        self.__active_radio_button = button.text()
        if self.__active_radio_button == 'None':
            self.__active_radio_button = 0
        elif self.__active_radio_button == 'Groceries':
            self.__active_radio_button = 1
        elif self.__active_radio_button == 'Gas':
            self.__active_radio_button = 2
        elif self.__active_radio_button == 'Fun':
            self.__active_radio_button = 3
        elif self.__active_radio_button == 'Subscription':
            self.__active_radio_button = 4
        elif self.__active_radio_button == 'Savings':
            self.__active_radio_button = 5

    def save_add_edit(self):
        try:
            month = int(self.month_lnedit.text())
            day = int(self.day_lnedit.text())
            year = int(self.year_lnedit.text())
            cost = float(self.expense_lnedit.text())
            income = float(self.income_lnedit.text())
            category = int(self.__active_radio_button)
        except:
            self.add_warning_lbl.setText('Must include values for all fields in numbers')
            return

        exists = False

        with open('logs.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            lines = list(csv.reader(csv_file))

        # if log already exists for day
            for i, line in enumerate(lines):
                if line and line[0] == str(f'{month}{day}{year}'):
                    # Modify the line with new values
                    exists = True

                    line[1] = str(float(line[1]) + income)

                    if category == 1:
                        line[2] = str(float(line[2]) + cost)

            # Write the modified content back to the file
        with open('logs.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(lines)

        # if log is not made for day
        if exists == False:
            with open('logs.csv', 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                if category == 0:
                    data = [str(f'{month}{day}{year}'), str(income), '0', '0', '0', '0', '0']
                elif category == 1:
                    data = [str(f'{month}{day}{year}'), str(income), str(cost), '0', '0', '0', '0']
                elif category == 2:
                    data = [str(f'{month}{day}{year}'), str(income), '0', str(cost), '0', '0', '0']
                elif category == 3:
                    data = [str(f'{month}{day}{year}'), str(income), '0', '0', str(cost), '0', '0']
                elif category == 4:
                    data = [str(f'{month}{day}{year}'), str(income), '0', '0', '0', str(cost), '0']
                elif category == 5:
                    data = [str(f'{month}{day}{year}'), str(income), '0', '0', '0', '0', str(cost)]

                csv_writer.writerow(data)
