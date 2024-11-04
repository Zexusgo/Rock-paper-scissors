from program_numb import random_numb
from PyQt5 import  QtWidgets
from UI_ import Ui_Mainwindow

class Mainwin(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mainwin,self).__init__()
        self.ui = Ui_Mainwindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.on_button_click)
        self.ui.pushButton_2.clicked.connect(self.on_button_click_1)
        self.ui.pushButton_3.clicked.connect(self.on_button_click_2)
        

    def on_button_click(self):
        click =("Scissors")
        Computer_choose= f'{random_numb()}'
        result = self.determine_winner("Scissors",Computer_choose)
        self.ui.label.setText(f"You choose: {click}<br>Computer choose: {Computer_choose}")
        self.ui.label_2.setText(result)

    def on_button_click_1(self):
        click =("Paper")
        Computer_choose= f'{random_numb()}'
        result = self.determine_winner("Paper",Computer_choose)
        self.ui.label.setText(f"You choose: {click}<br>Computer choose: {Computer_choose}")
        self.ui.label_2.setText(result)
    
    def on_button_click_2(self):
        click =("Rock")
        Computer_choose= f'{random_numb()}'
        result = self.determine_winner("Rock",Computer_choose)
        self.ui.label.setText(f"You choose: {click}<br>Computer choose: {Computer_choose}")
        self.ui.label_2.setText(result)

    def determine_winner(self,click, computer_choose):
        if click == computer_choose:
            return "It's A Tie"
        elif (click == "Scissors" and computer_choose == "Paper") or \
         (click == "Paper" and computer_choose == "Rock") or \
         (click == "Rock" and computer_choose== "Scissors"):
            return "You Win!"
        else:
            return "You Lose!"


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    obj=Mainwin()
    obj.show()
    sys.exit(app.exec_())
