
### Reference link ##
###https://wikidocs.net/33817

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp , QCheckBox, QLabel, QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ### Addition icon - 추후 자체 icon 만들기 ###
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('./img/icon.png'))
        
        ### Exit manu addition ### 
        exitAction = QAction(QIcon('./img/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+x')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
       
        self.statusBar()
        ### 상위 메뉴 설정 
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        filemenu = menubar.addMenu('&Edit')
        filemenu = menubar.addMenu('&View')
        filemenu = menubar.addMenu('&Tool')
        filemenu = menubar.addMenu('&Help')
        ### ToolBar define
        self.statusBar()
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        
        ### Label 
        label1 = QLabel('Memory type', self)
        label1.setAlignment(Qt.AlignCenter)
        font1 = label1.font()
        font1.setPointSize(10)

        label2 = QLabel('Memory feature', self)
        label2.setAlignment(Qt.AlignCenter)


        ### Combo box 만들기
        comb = QComboBox(self)
        comb.addItem('SP-1P')
        comb.addItem('RF-2P')
        comb.addItem('DP')
        comb.addItem('ROM')
        comb.addItem('TCAM')
        comb.move(100, 100)
        ### Check box 만들기 
        cb = QCheckBox('Power gating', self)
        cb.move(350,100)

        cb = QCheckBox('Redundancy', self)
        cb.move(350,120)

        cb = QCheckBox('BIST MUX', self)
        cb.move(350,140)
        ### 함수 지정해서 수행 ### 
        #cb.stateChanged.connect(self.changeTitle)
        ### Default toggle on 
        #cb.toggle()
        #######

       
        
        ### window 열기 ##
        # Title 이름 정의 
        self.setWindowTitle('MC sniper')
        ## Window size 정의 (X,Y,Width , Height)
        self.setGeometry(300, 300, 600, 600)
        self.resize(600, 600)
        #self.center()
        self.show()
   
    # def center(self):
    #     qr = self.frameGeometry()
    #     cp = QDesktopWidget().availableGeometry().center()
    #     qr.moveCenter(cp)
    #     self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())