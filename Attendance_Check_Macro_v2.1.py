# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ACmain2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
# =====================================================
"""
<Attendance_Check_Macro_v2.1> - 21.12.6.월 18:02
* Made by Yoonmen *
[update] 캡차 해제 기능 추가
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from xml.etree.ElementTree import Element
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import shutil
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
import sys
import pyautogui
pyautogui.PAUSE = 0.5
import time

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(351, 534)
        self.CheckButton = QtWidgets.QPushButton(Form)
        self.CheckButton.setGeometry(QtCore.QRect(100, 200, 151, 31))
        self.CheckButton.setObjectName("CheckButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 271, 71))
        font = QtGui.QFont()
        font.setFamily("휴먼옛체")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 20, 261, 141))
        font = QtGui.QFont()
        font.setFamily("휴먼옛체")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 64, 15))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 130, 71, 20))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(130, 510, 101, 16))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_ID = QtWidgets.QLineEdit(Form)
        self.lineEdit_ID.setGeometry(QtCore.QRect(130, 130, 181, 20))
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.lineEdit_PW = QtWidgets.QLineEdit(Form)
        self.lineEdit_PW.setGeometry(QtCore.QRect(130, 160, 181, 20))
        self.lineEdit_PW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_PW.setObjectName("lineEdit_PW")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(30, 160, 81, 20))
        self.label_7.setObjectName("label_7")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(40, 250, 271, 251))
        self.listWidget.setDragEnabled(False)
        self.listWidget.setObjectName("listWidget")
        self.CAPCHA_Button = QtWidgets.QToolButton(Form)
        self.CAPCHA_Button.setGeometry(QtCore.QRect(250, 10, 91, 20))
        self.CAPCHA_Button.setObjectName("CAPCHA_Button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # ====================================================================================================
        '''Button 클릭 시'''
        self.CheckButton.clicked.connect(self.Checking_start)
        self.CAPCHA_Button.clicked.connect(self.Clear_CAPCHA)
        # ----------------------------------------------------------------------------------------------------
        '''실행되자마자'''
        self.listWidget.addItem('[system] 이 프로그램은 사용자의 개인정보를\n            가져가지 않습니다.')
        # self.listWidget.addItem('[system] START 버튼을 누르기 전에\n            이 프로그램으로 인해 열렸던 크롬 창이\n            있다면 닫아주세요.')
        self.listWidget.addItem('[system] 매크로 진행 중에 프로그램을 종료할\n            때는 강제종료하시면 됩니다.')
        self.listWidget.addItem('[system] <문의사항 or 오류제보>\n            *인스타 & 카톡 ID : Yoonmen_03 *')
        global CAPCHA_Error
        CAPCHA_Error = 0                # 캡차로 인해 막히지 않은 경우 == 0
        # ====================================================================================================


    # ====================================================================================================
    def retranslateUi(self, Form):      # 매크로 프로그램 화면
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "밴드 출석체크 매크로"))
        self.CheckButton.setText(_translate("Form", "출석체크"))
        self.label_2.setText(_translate("Form", "Attendance Check"))
        self.label.setText(_translate("Form", "Auto Macro"))
        self.label_4.setText(_translate("Form", "v2.1"))
        self.label_6.setText(_translate("Form", "Facebook_ID"))
        self.label_8.setText(_translate("Form", "by. Yoonmen"))
        self.label_7.setText(_translate("Form", "Facebook_PW"))
        self.CAPCHA_Button.setText(_translate("Form", "CAPCHA 해제"))
    # ====================================================================================================


    # ====================================================================================================
    def Checking_start(self) : 
        # ----------------------------------------------------------------------------------------------------
        '''사용자 입력 저장'''
        facebook_ID = self.lineEdit_ID.text()
        facebook_PW = self.lineEdit_PW.text()
        # ----------------------------------------------------------------------------------------------------
        


        # ----------------------------------------------------------------------------------------------------
        '''이스터에그'''
        if facebook_ID == '' or facebook_PW == '' : 
            self.listWidget.addItem('[system] 입력란을 모두 채워주세요.')
        # ----------------------------------------------------------------------------------------------------



        else :      # 디버깅 크롬에 남은 기록 삭제
            try:
                shutil.rmtree(f"c:\chrometemp")  #쿠키 / 캐쉬파일 삭제
            except FileNotFoundError:
                pass
            


            # ----------------------------------------------------------------------------------------------------
            '''크롬 구동부'''
            option = Options()
            option.add_argument('start-maximized')  # 전체 화면
            chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
            try:
                driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
            except:
                chromedriver_autoinstaller.install(True)
                driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)

            driver.implicitly_wait(10)      # 페이지 로딩 10초 기다려준다. 10초 후에는 얄짤없다.
            # ----------------------------------------------------------------------------------------------------



            # ----------------------------------------------------------------------------------------------------
            '''(밴드 입장 ~ 페이스북 로그인)'''
            driver.get('https://band.us/feed')

            driver.find_element_by_xpath('//*[@id="login_list"]/li[4]/a').click()       # '페이스북 로그인' 버튼

            driver.find_element_by_xpath('//*[@id="email"]').send_keys(facebook_ID)
            driver.find_element_by_xpath('//*[@id="pass"]').send_keys(facebook_PW)

            driver.find_element_by_xpath('//*[@id="loginbutton"]').click()              # 로그인 버튼
            # ----------------------------------------------------------------------------------------------------
            

            def First_Check() : 
                # (매크로 GUI가 맨 앞에 올라와 있으면 Alt+Tab 정상적으로 동작 X)
                pyautogui.keyDown('Alt')
                for j in range(1, 3):
                    pyautogui.press('Tab')
                pyautogui.keyUp('Alt')
                pyautogui.hotkey('Alt', 'Tab')

                while True : 
                    new_feed = driver.find_elements_by_css_selector('#content > div > button.btnFeedTop._btnNewFeedUpdate[style=""]')        # '새글 보기' 버튼 나왔는지 확인

                    if len(new_feed) == 1 : 
                        driver.find_element_by_css_selector('#content > div > button.btnFeedTop._btnNewFeedUpdate[style=""]').click()
                        break
                    
                    else : 
                        time.sleep(10)


                        for i in range(1, 3) : 
                            pyautogui.hotkey('Alt', 'Tab')
                        
                time.sleep(0.5)
                driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/section[1]/section/div/div/section/div/div[2]/div[2]/div/div').click()      # 출석체크 위젯
                time.sleep(0.2)
                try : 
                    driver.find_element_by_class_name('etc').click()                            # 출석체크 클릭
                
                except NoSuchElementException : 
                    pass


            def Next_Checks() : 
                time.sleep(0.2)
                driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/button[4]').click()        # 닫기 버튼

                while True : 
                    new_feed = driver.find_elements_by_css_selector('#content > div > button.btnFeedTop._btnNewFeedUpdate[style="display: block;"]')        # '새글 보기' 버튼 나왔는지 확인

                    if len(new_feed) == 1 : 
                        driver.find_element_by_css_selector('#content > div > button.btnFeedTop._btnNewFeedUpdate[style="display: block;"]').click()
                        break
                    
                    else : 
                        time.sleep(10)
                        for i in range(1, 3) : 
                            pyautogui.hotkey('Alt', 'Tab')

                time.sleep(0.5)
                driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/section[1]/section/div/div/section/div/div[2]/div[2]/div/div').click()      # 출석체크 위젯
                time.sleep(0.2)
                try : 
                    driver.find_element_by_class_name('etc').click()                            # 출석체크 클릭
                
                except NoSuchElementException : 
                    pass



            # ----------------------------------------------------------------------------------------------------
            '''(캡차 감지 ~ 출석체크 무한 츠쿠요미)'''
            try : 
                driver.find_element_by_xpath('//*[@id="content"]/div/button[2]')    # 캡차 떴는지 '새글 보기' 버튼 확인으로 떠보기

            except NoSuchElementException : 
                pyautogui.hotkey('Alt', 'Tab')
                driver.close()
                self.listWidget.addItem('[system] CAPCHA 때문에 더 이상 진행할 수\n            없습니다. 5분 후에 다시 시도해주세요.')

                global CAPCHA_Error
                CAPCHA_Error = 1                                                    # 캡차로 인해 막힌 경우 == 1

            else  :
                check_count = 1
                while True : 
                    if check_count == 1 :
                        First_Check()

                    else : 
                        Next_Checks()
                    check_count += 1
            # ----------------------------------------------------------------------------------------------------
    # ====================================================================================================


    # ====================================================================================================
    def Clear_CAPCHA(self) : 
        if CAPCHA_Error == 0 : 
            self.listWidget.addItem('[system] 이 기능은 CAPCHA에 의해 진행이 막힌\n            후에 사용 가능합니다.')
        
        else : 
            # ----------------------------------------------------------------------------------------------------
            '''사용자 입력 저장'''
            facebook_ID = self.lineEdit_ID.text()
            facebook_PW = self.lineEdit_PW.text()
            # ----------------------------------------------------------------------------------------------------
            


            # ----------------------------------------------------------------------------------------------------
            '''이스터에그'''
            if facebook_ID == 'sex' or facebook_PW == 'sex' : 
                self.listWidget.addItem('[system] 꼭 이런 빈칸만 있으면 \'sex\' 쳐보는\n            사람 있을 줄 알았다...')

            elif facebook_ID == '윤태영' or facebook_PW == 'dbsxodud' : 
                self.listWidget.addItem('[system] ㅊㅋ! 이스터에그를 발견하셨습니다!\n            문자 주면 선물을 드립니다.')

            elif facebook_ID == '' or facebook_PW == '' : 
                self.listWidget.addItem('[system] 입력란을 모두 채워주세요.')
            # ----------------------------------------------------------------------------------------------------



            else :      # 디버깅 크롬에 남은 기록 삭제
                try:
                    shutil.rmtree(f"c:\chrometemp")  #쿠키 / 캐쉬파일 삭제
                except FileNotFoundError:
                    pass
                


                # ----------------------------------------------------------------------------------------------------
                '''크롬 구동부'''
                option = Options()
                option.add_argument('start-maximized')  # 전체 화면
                chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
                try:
                    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
                except:
                    chromedriver_autoinstaller.install(True)
                    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)

                driver.implicitly_wait(10)      # 페이지 로딩 10초 기다려준다. 10초 후에는 얄짤없다.
                # ----------------------------------------------------------------------------------------------------



                # ----------------------------------------------------------------------------------------------------
                '''(밴드 입장 ~ 페이스북 로그인)'''
                driver.get('https://band.us/feed')

                driver.find_element_by_xpath('//*[@id="login_list"]/li[4]/a').click()       # '페이스북 로그인' 버튼

                driver.find_element_by_xpath('//*[@id="email"]').send_keys(facebook_ID)
                driver.find_element_by_xpath('//*[@id="pass"]').send_keys(facebook_PW)

                driver.find_element_by_xpath('//*[@id="loginbutton"]').click()              # 로그인 버튼
                # ----------------------------------------------------------------------------------------------------


                self.listWidget.addItem('[system] CAPCHA를 해제하고 크롬을 닫아주세요.')
    # ====================================================================================================


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
