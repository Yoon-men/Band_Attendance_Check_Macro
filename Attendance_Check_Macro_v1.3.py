# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ACmain.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# =====================================================
# Attendance_Check_Macro_v1.3
# 따로 설치를 해야하는 라이브러리 : Pyqt5, pyautogui

from PyQt5 import QtCore, QtGui, QtWidgets
import pyautogui as m
import time
m.PAUSE = 0.2

print("="*35)
print("\n  출석체크 자동 매크로 커맨더 창\n")
print("="*35)


class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(291, 203)
        mainwindow.setMouseTracking(False)
        self.label = QtWidgets.QLabel(mainwindow)
        self.label.setGeometry(QtCore.QRect(20, 10, 261, 141))
        font = QtGui.QFont()
        font.setFamily("휴먼옛체")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(mainwindow)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 271, 71))
        font = QtGui.QFont()
        font.setFamily("휴먼옛체")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(mainwindow)
        self.label_3.setGeometry(QtCore.QRect(200, 180, 91, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
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
        self.CheckButton.setGeometry(QtCore.QRect(60, 100, 171, 71))
        self.CheckButton.setObjectName("CheckButton")

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)
        # =====================================================
        # Button 클릭 시
        self.CheckButton.clicked.connect(self.Checkbutton)
        
    # =====================================================

    def retranslateUi(self, mainwindow):                                 # 매크로 프로그램 화면
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "출석체크 매크로"))
        self.label.setText(_translate("mainwindow", "Auto Mouse Macro"))
        self.label_2.setText(_translate("mainwindow", "Attendance Check"))
        self.label_3.setText(_translate("mainwindow", "by. Yoonmen"))
        self.label_4.setText(_translate("mainwindow", "v1.3"))
        self.CheckButton.setText(_translate("mainwindow", "출석체크"))

    # =====================================================

    def Checkbutton(self):
        # -----------------------------------------------------
        # [새글 피드 버튼을 찾는 함수 : Feed_Check]
        #    ㄴ> 잡글 인식 및 무시 기능 포함
        def Feed_check() : 
            global moving_man
            moving_man = 0
            while True : 
                if moving_man == 1 : 
                    break
                else : 
                    while True :
                        m.moveTo(954, 185)                                           # 새글 피드 버튼 위치로 이동
                        for i in range(1, 3) : 
                            m.hotkey('Alt', 'Tab')                                   # 'Alt+Tab'을 사용해 새글 피드 버튼 생성 확인
                        x, y = m.position()
                        RGB = m.screenshot().getpixel((x, y))                        # 색깔 잡기
                        if RGB == (46, 204, 113):                                    # 새글 피드 버튼이 생기면
                            m.click(x, y)                                            # 버튼 누르기
                            print('\n[system] : 새 글 확인 버튼을 눌렀습니다.')
                            time.sleep(2)
                            break
                        else:
                            time.sleep(10)                                           # 없으면 10초 기다리기

                    m.moveTo(704, 400)                                               # 출석체크 아이콘 버튼의 x좌표로 이동

                    time_limit = time.time() + (60) # 60초(1분) 안에 글에서 출석체크 아이콘을 못찾으면 잡글로 규정하고 패스 처리
                    while True :
                        if time.time() > time_limit : 
                            print('\n[system] : 잡글을 인식했습니다. 피드 탐지를 재시작합니다.')
                            break
                        x, y = m.position()
                        RGB = m.screenshot().getpixel((x, y))                        # 색깔 잡기
                        if RGB == (52, 204, 108) or RGB == (255, 91, 114) or RGB == (255, 112, 61) or RGB == (147, 112, 240) or RGB == (50, 176, 229) or RGB == (248, 117, 192) or RGB == (33, 199, 0) or RGB == (253, 176, 13) or RGB == (0, 185, 148) or RGB == (84, 113, 216) :   # 출석체크 아이콘 버튼의 색깔을 찾으면
                            # (순서대로) 회색&남색 / 주홍색 / 주황색 / 보라색 / 하늘색 / 분홍색 / 녹색 / 노란색 / 청록색 / 파란색
                            x, y = m.position()
                            m.click(x, y)                                            # 클릭해서 출석체크 창으로 이동
                            print('\n[system] : 출석체크 창으로 이동했습니다.')
                            moving_man = 1
                            break
                        else:                                                        # 그 색깔이 아니면
                            m.move(0, +1)                                            # y축 방향으로 -1 만큼 이동
        # -----------------------------------------------------
        print('\nCheck button is clicked')
        print('\n[system] : 출석체크 자동 매크로를 시작합니다.')
        global moving_type
        moving_type = 0
        
        while True :        # 출석체크의 무한 츠쿠요미
            time.sleep(2)
            m.click(1569, 122)                                              # 새글 피드 화면만 보이도록 하기
            # -----------------------------------------------------
            if moving_type == 0 :       # 새글 피드 버튼 체크를 위한 준비 (처음 실행했을 때 매크로창을 세 번째 창으로 만든다.)
                for i in range(1, 3):       # (매크로창이 맨 앞에 올라와 있으면 Alt+Tab 정상적으로 동작 X)
                    m.keyDown('Alt')
                    for j in range(1, 3):
                        m.press('Tab')
                    m.keyUp('Alt')

            else :                      # 출석체크를 한 번 끝낸 후
                for i in range(1, 3) :  
                    m.hotkey('Alt', 'Tab')
            # -----------------------------------------------------
            Feed_check()
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
                    moving_type = 1
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