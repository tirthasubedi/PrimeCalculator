import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Prime Number Calculator'
        self.left = 20
        self.top = 20
        self.width = 500
        self.height = 300
        self.window()

    def window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #to add text on screen

        self.statusBar().showMessage("Welcome to Prime Number Calculator! Enjoy !")


        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)

        # Create a button in the window
        self.button = QPushButton('Check', self)
        self.button.move(20,80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()


    def on_click(self):

        #
        textboxValue = self.textbox.text()
        if (textboxValue.isdigit())== False:

            QMessageBox.question(self, 'Prime Number Calculated', "Please Type Valid Number! You Typed :" + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
            return textboxValue

        while True:


        # prime number is always greater than 1
            if int(textboxValue) > 1:
                for i in range(2, int(textboxValue)):
                    if (int(textboxValue) % i) == 0:
                        # print(textboxValue, "is not a prime number")
                        QMessageBox.question(self, 'Prime Number Checker', "Your typed Number is NOT Prime: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
                        # self.textbox.setText("")
                        break
                else:
                    QMessageBox.question(self, 'Prime Number Checker', "Your typed Number is Prime: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
                    # self.textbox.setText("")
                    # print(textboxValue, "is a prime number")
                    break

            # if the entered number is less than or equal to 1
            # then it is not prime number
            else:
                QMessageBox.question(self, 'Prime Number Checker', "Your typed Number is NOT prime: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)

                break
            break




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
