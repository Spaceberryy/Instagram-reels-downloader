# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the instadown_form.py file
#     pyside6-uic instadown_form.ui -o instadown_form.py, or
#     pyside2-uic instadown_form.ui -o instadown_form.py
from instadown_form import Ui_instadown
import instaloader

class instadown(QWidget, Ui_instadown):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_instadown()
        self.ui.setupUi(self)

        self.reel_url = ""
        self.ui.pb_download.clicked.connect(self.download)
        self.ui.pb_reset.clicked.connect(self.reset)


    def reset(self):
        self.reel_url = ""
        self.ui.insert_url.setText("")
        self.ui.url_label.setText("Insert url below")
    def input_url(self):
        self.reel_url = self.ui.insert_url.text()
        print(self.reel_url)

    def download(self):
        self.input_url()
        try:
                loaded = instaloader.Instaloader()
                short_code = self.reel_url.split("/")[-2]
                reel_post = instaloader.Post.from_shortcode(loaded.context, short_code)
                loaded.download_post(reel_post, target="reels")

                self.ui.url_label.setText("Downloaded")
        except:
                self.ui.url_label.setText("Invalid input")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = instadown()
    app.setStyle("fusion")
    widget.show()
    sys.exit(app.exec())
