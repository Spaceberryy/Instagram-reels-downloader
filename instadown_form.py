# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instadown_form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_instadown(object):
    def setupUi(self, instadown):
        if not instadown.objectName():
            instadown.setObjectName(u"instadown")
        instadown.resize(400, 300)
        instadown.setStyleSheet(u"background-color: #141414;\n"
"")
        self.url_label = QLabel(instadown)
        self.url_label.setObjectName(u"url_label")
        self.url_label.setGeometry(QRect(10, 10, 380, 40))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.url_label.setFont(font)
        self.url_label.setMouseTracking(False)
        self.url_label.setStyleSheet(u"background-color: #190040;\n"
"color: #D3D3D3 ;")
        self.url_label.setFrameShape(QFrame.Shape.NoFrame)
        self.url_label.setFrameShadow(QFrame.Shadow.Sunken)
        self.url_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.insert_url = QLineEdit(instadown)
        self.insert_url.setObjectName(u"insert_url")
        self.insert_url.setGeometry(QRect(10, 60, 380, 50))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        self.insert_url.setFont(font1)
        self.insert_url.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.insert_url.setAutoFillBackground(False)
        self.insert_url.setStyleSheet(u"background-color: #190040 ;\n"
"color: #D3D3D3;")
        self.insert_url.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pb_download = QPushButton(instadown)
        self.pb_download.setObjectName(u"pb_download")
        self.pb_download.setGeometry(QRect(105, 130, 190, 30))
        self.pb_download.setStyleSheet(u"background-color: #190040;\n"
"color: #D3D3D3 ;")
        self.pb_reset = QPushButton(instadown)
        self.pb_reset.setObjectName(u"pb_reset")
        self.pb_reset.setGeometry(QRect(340, 130, 51, 31))
        self.pb_reset.setStyleSheet(u"background-color: #190040 ;\n"
"color: #D3D3D3;")

        self.retranslateUi(instadown)

        QMetaObject.connectSlotsByName(instadown)
    # setupUi

    def retranslateUi(self, instadown):
        instadown.setWindowTitle(QCoreApplication.translate("instadown", u"instadown", None))
        self.url_label.setText(QCoreApplication.translate("instadown", u"Insert url below", None))
        self.insert_url.setText("")
        self.pb_download.setText(QCoreApplication.translate("instadown", u"Download", None))
        self.pb_reset.setText(QCoreApplication.translate("instadown", u"reset", None))
    # retranslateUi

