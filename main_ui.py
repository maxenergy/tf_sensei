# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tf_Sensei.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmmain(object):
    def setupUi(self, frmmain):
        frmmain.setObjectName("frmmain")
        frmmain.resize(801, 603)
        self.centralwidget = QtWidgets.QWidget(frmmain)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 781, 81))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 160, 781, 201))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 621, 91))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.bttnlaunchannotator = QtWidgets.QPushButton(self.groupBox)
        self.bttnlaunchannotator.setGeometry(QtCore.QRect(470, 155, 131, 31))
        self.bttnlaunchannotator.setObjectName("bttnlaunchannotator")
        self.bttnbrowse = QtWidgets.QPushButton(self.groupBox)
        self.bttnbrowse.setGeometry(QtCore.QRect(10, 130, 99, 41))
        self.bttnbrowse.setObjectName("bttnbrowse")
        self.lbldatafolder = QtWidgets.QLabel(self.groupBox)
        self.lbldatafolder.setGeometry(QtCore.QRect(110, 130, 341, 16))
        self.lbldatafolder.setText("")
        self.lbldatafolder.setObjectName("lbldatafolder")
        self.bttngenerate = QtWidgets.QPushButton(self.groupBox)
        self.bttngenerate.setGeometry(QtCore.QRect(110, 155, 341, 31))
        self.bttngenerate.setObjectName("bttngenerate")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(640, 30, 101, 16))
        self.label_3.setObjectName("label_3")
        self.lstlabels = QtWidgets.QListWidget(self.groupBox)
        self.lstlabels.setGeometry(QtCore.QRect(640, 50, 131, 141))
        self.lstlabels.setObjectName("lstlabels")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 501, 16))
        self.label_4.setObjectName("label_4")
        self.lblprojectpath = QtWidgets.QLabel(self.centralwidget)
        self.lblprojectpath.setGeometry(QtCore.QRect(100, 125, 521, 16))
        self.lblprojectpath.setText("")
        self.lblprojectpath.setObjectName("lblprojectpath")
        self.bttnbrowseprj = QtWidgets.QPushButton(self.centralwidget)
        self.bttnbrowseprj.setGeometry(QtCore.QRect(10, 120, 71, 27))
        self.bttnbrowseprj.setObjectName("bttnbrowseprj")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 360, 781, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 751, 101))
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 101, 16))
        self.label_7.setObjectName("label_7")
        self.cbomodels = QtWidgets.QComboBox(self.groupBox_2)
        self.cbomodels.setGeometry(QtCore.QRect(110, 125, 201, 26))
        self.cbomodels.setObjectName("cbomodels")
        self.bttnloadmodel = QtWidgets.QPushButton(self.groupBox_2)
        self.bttnloadmodel.setGeometry(QtCore.QRect(320, 125, 99, 27))
        self.bttnloadmodel.setObjectName("bttnloadmodel")
        self.bttneditconfig = QtWidgets.QPushButton(self.groupBox_2)
        self.bttneditconfig.setGeometry(QtCore.QRect(560, 125, 191, 27))
        self.bttneditconfig.setObjectName("bttneditconfig")
        self.dwp = QtWidgets.QProgressBar(self.groupBox_2)
        self.dwp.setGeometry(QtCore.QRect(430, 128, 118, 23))
        self.dwp.setProperty("value", 0)
        self.dwp.setObjectName("dwp")
        self.txtstatus = QtWidgets.QTextEdit(self.centralwidget)
        self.txtstatus.setGeometry(QtCore.QRect(20, 520, 481, 71))
        self.txtstatus.setUndoRedoEnabled(False)
        self.txtstatus.setReadOnly(True)
        self.txtstatus.setObjectName("txtstatus")
        self.bttntrain = QtWidgets.QPushButton(self.centralwidget)
        self.bttntrain.setGeometry(QtCore.QRect(510, 520, 121, 71))
        self.bttntrain.setObjectName("bttntrain")
        self.bttngettrainedmodel = QtWidgets.QPushButton(self.centralwidget)
        self.bttngettrainedmodel.setGeometry(QtCore.QRect(640, 520, 121, 71))
        self.bttngettrainedmodel.setObjectName("bttngettrainedmodel")
        frmmain.setCentralWidget(self.centralwidget)

        self.retranslateUi(frmmain)
        QtCore.QMetaObject.connectSlotsByName(frmmain)

    def retranslateUi(self, frmmain):
        _translate = QtCore.QCoreApplication.translate
        frmmain.setWindowTitle(_translate("frmmain", "TF Sensei"))
        self.label.setText(_translate("frmmain", "<html><head/><body><p align=\"justify\">Welcome to TF sensei, a GUI based utility for training on your own datasets/models(TODO) using the Google Tensorflow Object Detection API. This program uses code snippets from <a href=\"https://github.com/datitran/raccoon_dataset\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/datitran/raccoon_dataset</span></a> Also thanks to sentdex from <a href=\"https://pythonprogramming.net/\"><span style=\" text-decoration: underline; color:#0000ff;\">https://pythonprogramming.net/</span></a> for his awesome tutorials on machine learning and Tensorflow.</p></body></html>"))
        self.groupBox.setTitle(_translate("frmmain", "Dataset Options:"))
        self.label_2.setText(_translate("frmmain", "<html><head/><body><p align=\"justify\">Path to a directory containing all data images(train and test folders inside that directory). Images must be annotated. you can download the annotator from <a href=\"https://github.com/tzutalin/labelImg\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/tzutalin/labelImg</span></a> . Download and extract the LabelImg directory here. If your have it already, paste the directory into tf_sensei directory. Then you would be able to run it from here,</p></body></html>"))
        self.bttnlaunchannotator.setText(_translate("frmmain", "Launch Tool"))
        self.bttnbrowse.setText(_translate("frmmain", "Browse..."))
        self.bttngenerate.setText(_translate("frmmain", "Generate TFRecords and Label map"))
        self.label_3.setText(_translate("frmmain", "List of labels"))
        self.label_4.setText(_translate("frmmain", "Path to a project directory where all the necessary files will be created"))
        self.bttnbrowseprj.setText(_translate("frmmain", "Browse..."))
        self.groupBox_2.setTitle(_translate("frmmain", "Model Options:"))
        self.label_6.setText(_translate("frmmain", "<html><head/><body><p align=\"justify\">You can select from existing models or you may decide to use your own. Right now, the GUI does not support creating own models. So just select one from the existing list of models and it will be downloaded and extracted and its config file would be automatically added for tuning. Just make sure you are using the latest version of the API(config files would be fetched from the samples folder so you can paste the config file there if you want)</p></body></html>"))
        self.label_7.setText(_translate("frmmain", "Select Model:"))
        self.bttnloadmodel.setText(_translate("frmmain", "Load Model"))
        self.bttneditconfig.setText(_translate("frmmain", "Set config file..."))
        self.bttntrain.setText(_translate("frmmain", "Generate\n"
"Trainer Script"))
        self.bttngettrainedmodel.setText(_translate("frmmain", "Export \n"
"Inference\n"
"Graph"))

