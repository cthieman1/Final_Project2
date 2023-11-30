from PyQt6.QtWidgets import *
from gui import *
import csv

class Manager(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
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

                self.__checkings_amount = 0
                self.__savings_amount = 0
                self.__other_amount = 0

        self.update_display()

        self.view_btn.clicked.connect(lambda : self.switch_page(0))
        self.check_day_btn.clicked.connect(lambda: self.switch_page(1))
        self.add_btn.clicked.connect(lambda : self.switch_page(2))

        self.set_amount_checking_btn.clicked.connect(lambda : self.set_checking())
        self.set_amount_saving_btn.clicked.connect(lambda : self.set_saving())
        self.set_amount_other_btn.clicked.connect(lambda : self.set_other())
        self.save_btn.clicked.connect(lambda : self.save())

        self.stackedWidget.setCurrentIndex(0)

    def update_display(self):
        self.checkings_amount_lbl.setText(f'${self.__checkings_amount:.2f}')
        self.savings_amount_lbl.setText(f'${self.__savings_amount:.2f}')
        self.other_amount_lbl.setText(f'${self.__other_amount:.2f}')

    def switch_page(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def set_checking(self):
        #TODO check for invalid values
        new_value = float(self.set_amount_checking_lnedit.text())
        self.__checkings_amount = new_value
        self.update_display()

    def set_saving(self):
        # TODO check for invalid values
        new_value = float(self.set_amount_saving_lnedit.text())
        self.__savings_amount = new_value
        self.update_display()

    def set_other(self):
        # TODO check for invalid values
        new_value = float(self.set_amount_other_lnedit.text())
        self.__other_amount = new_value
        self.update_display()

    def save(self):
        #TODO reset entry fields
         data = [self.__checkings_amount, self.__savings_amount, self.__other_amount]
         with open('accounts.csv', 'r') as csv_file:
             csv_reader = csv.reader(csv_file)
             header = next(csv_reader, None)

             with open('accounts.csv', 'w') as csv_file:
                 csv_writer = csv.writer(csv_file)
                 csv_writer.writerow(data)



