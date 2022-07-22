import sys
from PyQt5 import QtWidgets
from test import Ui_Form
from PyQt5.QtCore import QThread
import socket

class sendThread(QThread):

    def __init__(self,sendTxt):
        super(sendThread, self).__init__()
        self.txt=sendTxt
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect()

    def run(self):
        self.sendMsg()

    # 消息编码，发送
    def sendMsg(self):
        self.sendData = bytes(self.txt.toPlainText(),encoding='utf-8')
        self.socket.send(self.sendData)

class mainForm(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mainForm, self).__init__()
        self.setupUi(self)

    def sendMsg(self):
        self.sendTrd=sendThread(self.textEditSend)
        self.sendTrd.start()

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    mw=mainForm()
    mw.show()
    sys.exit(app.exec_())
