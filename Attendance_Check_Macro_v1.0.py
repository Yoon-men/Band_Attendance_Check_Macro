# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ACmain.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# =====================================================
# Attendance_Check_Macro_v1.0
# 따로 설치를 해야하는 라이브러리 : Pyqt5, pyautogui

from PyQt5 import QtCore, QtGui, QtWidgets
import pyautogui as m
import time

print("="*35)
print("\n  출석체크 자동 매크로 커맨더 창\n")
print("="*35)


class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(274, 204)
        mainwindow.setMouseTracking(False)
        self.label = QtWidgets.QLabel(mainwindow)
        self.label.setGeometry(QtCore.QRect(20, 10, 261, 141))
        font = QtGui.QFont()
        font.setFamily("전주 완판본 각B")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(mainwindow)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 271, 71))
        font = QtGui.QFont()
        font.setFamily("전주 완판본 각B")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(mainwindow)
        self.label_3.setGeometry(QtCore.QRect(180, 180, 91, 20))
        font = QtGui.QFont()
        font.setFamily("경기천년바탕 Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(mainwindow)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 64, 15))
        font = QtGui.QFont()
        font.setFamily("경기천년바탕 Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.CheckButton = QtWidgets.QPushButton(mainwindow)
        self.CheckButton.setGeometry(QtCore.QRect(50, 100, 171, 71))
        self.CheckButton.setObjectName("CheckButton")

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

        # =====================================================
        # Button 클릭 시
        self.CheckButton.clicked.connect(self.Checkbutton)
        # =====================================================

    def retranslateUi(self, mainwindow):                # 매크로 프로그램 화면
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "출석체크 매크로"))
        self.label.setText(_translate("mainwindow", "Auto Mouse Macro"))
        self.label_2.setText(_translate("mainwindow", "Attendance Check"))
        self.label_3.setText(_translate("mainwindow", "by. Yoonmen"))
        self.label_4.setText(_translate("mainwindow", "v1.0"))
        self.CheckButton.setText(_translate("mainwindow", "출석체크"))

        # =====================================================
    def Checkbutton(self):
        print('\nCheck button is clicked')
        print('\n[system] : 출석체크 자동 매크로를 시작합니다.')

        # -----------------------------------------------------
        time.sleep(2)
        while True :
            m.moveTo(954, 185)                                           # 새 글 피드 버튼 위치로 이동
            x, y = m.position()
            RGB = m.screenshot().getpixel((x, y))                        # 색깔 잡기
            if RGB == (46, 204, 113):                                    # 새 글 피드 버튼이 생기면
                m.click(x, y)                                            # 버튼 누르기
                print('\n[system] : 새 글 확인 버튼을 눌렀습니다.')
                break
            else:
                time.sleep(10)                                           # 없으면 10초 기다리기
        # -----------------------------------------------------
        time.sleep(2)
        m.moveTo(704, 400)                                               # 출석체크 아이콘 버튼의 x좌표로 이동
        while True :
            x, y = m.position()
            RGB = m.screenshot().getpixel((x, y))                        # 색깔 잡기
            if RGB == (52, 204, 108) :                                   # 출석체크 아이콘 버튼의 색깔을 찾으면
                x, y = m.position()
                m.click(x, y)                                            # 클릭해서 출석체크 창으로 이동
                print('\n[system] : 출석체크 창으로 이동했습니다.')
                break
            else:                                                        # 그 색깔이 아니면
                m.move(0, +1)                                            # y축 방향으로 -1 만큼 이동
        # -----------------------------------------------------
        time.sleep(2)
        m.moveTo(1149, 350)                                              # 출석체크 체크 버튼의 x좌표로 이동
        while True :
            x, y = m.position()
            RGB = m.screenshot().getpixel((x, y))                        # 색깔 잡기
            if RGB == (205, 205, 205) :
                x, y = m.position()
                m.click(x, y)                                            # 클릭해서 출석체크
                print('\n[system] : 출석체크를 완료했습니다.')
                break
            else:                                                        # 그 색깔이 아니면
                m.move(0, +1)                                            # y축 방향으로 -1 만큼 이동
        # -----------------------------------------------------


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QDialog()
    ui = Ui_mainwindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
