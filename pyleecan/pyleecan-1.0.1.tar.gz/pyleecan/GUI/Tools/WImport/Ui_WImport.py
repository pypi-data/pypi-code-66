# -*- coding: utf-8 -*-

# File generated according to WImport.ui
# WARNING! All changes made in this file will be lost!
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyleecan.GUI.Resources import pyleecan_rc


class Ui_WImport(object):
    def setupUi(self, WImport):
        if not WImport.objectName():
            WImport.setObjectName(u"WImport")
        WImport.resize(678, 491)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WImport.sizePolicy().hasHeightForWidth())
        WImport.setSizePolicy(sizePolicy)
        WImport.setMinimumSize(QSize(0, 0))
        self.main_layout = QVBoxLayout(WImport)
        self.main_layout.setObjectName(u"main_layout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.in_param = QLabel(WImport)
        self.in_param.setObjectName(u"in_param")

        self.horizontalLayout.addWidget(self.in_param)

        self.c_type_import = QComboBox(WImport)
        self.c_type_import.setObjectName(u"c_type_import")

        self.horizontalLayout.addWidget(self.c_type_import)

        self.main_layout.addLayout(self.horizontalLayout)

        self.w_import = QWidget(WImport)
        self.w_import.setObjectName(u"w_import")

        self.main_layout.addWidget(self.w_import)

        self.retranslateUi(WImport)

        QMetaObject.connectSlotsByName(WImport)

    # setupUi

    def retranslateUi(self, WImport):
        WImport.setWindowTitle(QCoreApplication.translate("WImport", u"Form", None))
        self.in_param.setText(
            QCoreApplication.translate("WImport", u"Param_name: ", None)
        )

    # retranslateUi
