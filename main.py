from manager import *

def main():
    application = QApplication([])
    window = Manager()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()