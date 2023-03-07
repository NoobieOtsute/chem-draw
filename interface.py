# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChemDrawer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import requests
import base64
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 698)
        MainWindow.setStyleSheet("#centralwidget{\n"
"    background-color: #01435B;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("color: #FFFFFF;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("border-radius: 15px;\n"
"background-color: #208A71;\n"
"border: 2px solid #BFDB39;")
        self.lineEdit.setText("")
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.Ilabel = QtWidgets.QLabel(self.frame)
        self.Ilabel.setGeometry(QtCore.QRect(10, 0, 431, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ilabel.sizePolicy().hasHeightForWidth())
        self.Ilabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Ilabel.setFont(font)
        self.Ilabel.setStyleSheet("")
        self.Ilabel.setObjectName("Ilabel")
        self.SkeletalImage = QtWidgets.QLabel(self.frame)
        self.SkeletalImage.setGeometry(QtCore.QRect(80, 150, 300, 300))
        self.SkeletalImage.setStyleSheet("border-radius: 15px;\n"
"background-color: #208A71;\n"
"border: 2px solid #BFDB39;")
        self.SkeletalImage.setText("")
        self.SkeletalImage.setObjectName("SkeletalImage")
        self.Slabel = QtWidgets.QLabel(self.frame)
        self.Slabel.setGeometry(QtCore.QRect(140, 100, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slabel.sizePolicy().hasHeightForWidth())
        self.Slabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Slabel.setFont(font)
        self.Slabel.setStyleSheet("")
        self.Slabel.setObjectName("Slabel")
        self.SearchButton = QtWidgets.QPushButton(self.frame)
        self.SearchButton.setGeometry(QtCore.QRect(290, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.SearchButton.setFont(font)
        self.SearchButton.setStyleSheet("background-color: #FC7300;\n"
"border-radius: 5px;\n"
"border: 2px solid #BFDB38;")
        self.SearchButton.setObjectName("SearchButton")
        self.Flabel = QtWidgets.QLabel(self.frame)
        self.Flabel.setGeometry(QtCore.QRect(170, 470, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Flabel.sizePolicy().hasHeightForWidth())
        self.Flabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Flabel.setFont(font)
        self.Flabel.setStyleSheet("")
        self.Flabel.setObjectName("Flabel")
        self.Formula = QtWidgets.QLabel(self.frame)
        self.Formula.setGeometry(QtCore.QRect(10, 520, 441, 41))
        self.Formula.setStyleSheet("border-radius: 15px;\n"
"background-color: #208A71;\n"
"border: 2px solid #BFDB39;")
        self.Formula.setText("")
        self.Formula.setObjectName("Formula")
        self.Alabel = QtWidgets.QLabel(self.frame)
        self.Alabel.setGeometry(QtCore.QRect(150, 570, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Alabel.sizePolicy().hasHeightForWidth())
        self.Alabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Alabel.setFont(font)
        self.Alabel.setStyleSheet("")
        self.Alabel.setObjectName("Alabel")
        self.AverageMass = QtWidgets.QLabel(self.frame)
        self.AverageMass.setGeometry(QtCore.QRect(10, 620, 441, 41))
        self.AverageMass.setStyleSheet("border-radius: 15px;\n"
"background-color: #208A71;\n"
"border: 2px solid #BFDB39;")
        self.AverageMass.setText("")
        self.AverageMass.setObjectName("AverageMass")
        self.verticalLayout.addWidget(self.frame)
        self.url = "https://api.rsc.org/compounds/v1/filter/name"
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.SearchButton.clicked.connect(lambda : self.search(self.lineEdit.text()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChemDrawer"))
        self.Ilabel.setText(_translate("MainWindow", "IUPAC name of chemical"))
        self.Slabel.setText(_translate("MainWindow", "Skeletal Formula"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))
        self.Flabel.setText(_translate("MainWindow", "Formula"))
        self.Alabel.setText(_translate("MainWindow", "Average Mass"))

    def search(self, name):
        if name == "":
            return None
        id = requests.post(self.url, headers={"apikey" : "EwoHCk4Mwe5f0nbOwigG31cSI6XL3IUj"},
                                 json={"name" : name})
        Id = id.json()["queryId"]
        results = requests.get(f"https://api.rsc.org/compounds/v1/filter/{Id}/results", 
                               headers={"apikey" : "EwoHCk4Mwe5f0nbOwigG31cSI6XL3IUj"})
        recordId = results.json()["results"][0]
        image = requests.get(f"https://api.rsc.org/compounds/v1/records/{recordId}/image",
                             headers={"apikey" : "EwoHCk4Mwe5f0nbOwigG31cSI6XL3IUj"})
        formula = requests.get(f"https://api.rsc.org/compounds/v1/records/{recordId}/details?fields=Formula",
                             headers={"apikey" : "EwoHCk4Mwe5f0nbOwigG31cSI6XL3IUj"})
        self.Formula.setText(formula.json()["formula"])
        weight = requests.get(f"https://api.rsc.org/compounds/v1/records/{recordId}/details?fields=MolecularWeight",
                             headers={"apikey" : "EwoHCk4Mwe5f0nbOwigG31cSI6XL3IUj"})
        self.AverageMass.setText(str(weight.json()["molecularWeight"]))
        imageb64 = image.json()["image"]
        decoded_data=base64.b64decode((imageb64))
        img_file = open('image.png', 'wb')
        img_file.write(decoded_data)
        img_file.close()
        self.SkeletalImage.setPixmap(QtGui.QPixmap("image.png").scaled(290,290, QtCore.Qt.KeepAspectRatio))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())