import os
import sys
import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

os.system('cls' if os.name == 'nt' else 'clear') #Очистка экрана

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://duckduckgo.com/?t=h_"))  # первая страница
        self.setCentralWidget(self.browser)


         #задаем масштаб
        self.set_zoom(1.5)

    def set_zoom(self, factor):
        #диапазон
        if factor < 0.25:
            factor = 0.25
        elif factor > 3.0:
            factor = 3.0
        self.browser.setZoomFactor(factor)


        # навигация
        navtb = QToolBar()
        self.addToolBar(navtb)

        back_btn = QAction("❮", self)
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction("❯", self)
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction("⭮", self)
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        # строка редактирования для URL
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)

        self.show()

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("https")
        self.browser.setUrl(q)

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle(f"{title} - Sx browser")

    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = MainWindow()
    window.show()
    app.exec_()