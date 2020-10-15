# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TagsCompatibilityOptionsPage(object):
    def setupUi(self, TagsCompatibilityOptionsPage):
        TagsCompatibilityOptionsPage.setObjectName("TagsCompatibilityOptionsPage")
        TagsCompatibilityOptionsPage.resize(539, 705)
        self.vboxlayout = QtWidgets.QVBoxLayout(TagsCompatibilityOptionsPage)
        self.vboxlayout.setObjectName("vboxlayout")
        self.tag_compatibility = QtWidgets.QGroupBox(TagsCompatibilityOptionsPage)
        self.tag_compatibility.setObjectName("tag_compatibility")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.tag_compatibility)
        self.vboxlayout1.setContentsMargins(-1, 6, -1, 7)
        self.vboxlayout1.setSpacing(2)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.id3v2_version = QtWidgets.QGroupBox(self.tag_compatibility)
        self.id3v2_version.setFlat(False)
        self.id3v2_version.setCheckable(False)
        self.id3v2_version.setObjectName("id3v2_version")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.id3v2_version)
        self.horizontalLayout.setContentsMargins(-1, 6, -1, 7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.write_id3v24 = QtWidgets.QRadioButton(self.id3v2_version)
        self.write_id3v24.setChecked(True)
        self.write_id3v24.setObjectName("write_id3v24")
        self.horizontalLayout.addWidget(self.write_id3v24)
        self.write_id3v23 = QtWidgets.QRadioButton(self.id3v2_version)
        self.write_id3v23.setChecked(False)
        self.write_id3v23.setObjectName("write_id3v23")
        self.horizontalLayout.addWidget(self.write_id3v23)
        self.label = QtWidgets.QLabel(self.id3v2_version)
        self.label.setText("")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.vboxlayout1.addWidget(self.id3v2_version)
        self.id3v2_text_encoding = QtWidgets.QGroupBox(self.tag_compatibility)
        self.id3v2_text_encoding.setObjectName("id3v2_text_encoding")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.id3v2_text_encoding)
        self.horizontalLayout_2.setContentsMargins(-1, 6, -1, 7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.enc_utf8 = QtWidgets.QRadioButton(self.id3v2_text_encoding)
        self.enc_utf8.setObjectName("enc_utf8")
        self.horizontalLayout_2.addWidget(self.enc_utf8)
        self.enc_utf16 = QtWidgets.QRadioButton(self.id3v2_text_encoding)
        self.enc_utf16.setObjectName("enc_utf16")
        self.horizontalLayout_2.addWidget(self.enc_utf16)
        self.enc_iso88591 = QtWidgets.QRadioButton(self.id3v2_text_encoding)
        self.enc_iso88591.setObjectName("enc_iso88591")
        self.horizontalLayout_2.addWidget(self.enc_iso88591)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.id3v2_text_encoding)
        self.label_2.setText("")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.vboxlayout1.addWidget(self.id3v2_text_encoding)
        self.hbox_id3v23_join_with = QtWidgets.QHBoxLayout()
        self.hbox_id3v23_join_with.setObjectName("hbox_id3v23_join_with")
        self.label_id3v23_join_with = QtWidgets.QLabel(self.tag_compatibility)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_id3v23_join_with.sizePolicy().hasHeightForWidth())
        self.label_id3v23_join_with.setSizePolicy(sizePolicy)
        self.label_id3v23_join_with.setObjectName("label_id3v23_join_with")
        self.hbox_id3v23_join_with.addWidget(self.label_id3v23_join_with)
        self.id3v23_join_with = QtWidgets.QComboBox(self.tag_compatibility)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.id3v23_join_with.sizePolicy().hasHeightForWidth())
        self.id3v23_join_with.setSizePolicy(sizePolicy)
        self.id3v23_join_with.setEditable(True)
        self.id3v23_join_with.setObjectName("id3v23_join_with")
        self.id3v23_join_with.addItem("")
        self.id3v23_join_with.setItemText(0, "/")
        self.id3v23_join_with.addItem("")
        self.id3v23_join_with.setItemText(1, "; ")
        self.id3v23_join_with.addItem("")
        self.id3v23_join_with.setItemText(2, " / ")
        self.hbox_id3v23_join_with.addWidget(self.id3v23_join_with)
        self.vboxlayout1.addLayout(self.hbox_id3v23_join_with)
        self.itunes_compatible_grouping = QtWidgets.QCheckBox(self.tag_compatibility)
        self.itunes_compatible_grouping.setObjectName("itunes_compatible_grouping")
        self.vboxlayout1.addWidget(self.itunes_compatible_grouping)
        self.write_id3v1 = QtWidgets.QCheckBox(self.tag_compatibility)
        self.write_id3v1.setObjectName("write_id3v1")
        self.vboxlayout1.addWidget(self.write_id3v1)
        self.vboxlayout.addWidget(self.tag_compatibility)
        spacerItem2 = QtWidgets.QSpacerItem(274, 41, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem2)

        self.retranslateUi(TagsCompatibilityOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(TagsCompatibilityOptionsPage)
        TagsCompatibilityOptionsPage.setTabOrder(self.write_id3v24, self.write_id3v23)
        TagsCompatibilityOptionsPage.setTabOrder(self.write_id3v23, self.enc_utf8)
        TagsCompatibilityOptionsPage.setTabOrder(self.enc_utf8, self.enc_utf16)
        TagsCompatibilityOptionsPage.setTabOrder(self.enc_utf16, self.enc_iso88591)
        TagsCompatibilityOptionsPage.setTabOrder(self.enc_iso88591, self.id3v23_join_with)
        TagsCompatibilityOptionsPage.setTabOrder(self.id3v23_join_with, self.write_id3v1)

    def retranslateUi(self, TagsCompatibilityOptionsPage):
        _translate = QtCore.QCoreApplication.translate
        self.tag_compatibility.setTitle(_("ID3"))
        self.id3v2_version.setTitle(_("ID3v2 Version"))
        self.write_id3v24.setText(_("2.4"))
        self.write_id3v23.setText(_("2.3"))
        self.id3v2_text_encoding.setTitle(_("ID3v2 Text Encoding"))
        self.enc_utf8.setText(_("UTF-8"))
        self.enc_utf16.setText(_("UTF-16"))
        self.enc_iso88591.setText(_("ISO-8859-1"))
        self.label_id3v23_join_with.setText(_("Join multiple ID3v2.3 tags with:"))
        self.id3v23_join_with.setToolTip(_("<html><head/><body><p>Default is \'/\' to maintain compatibility with previous Picard releases.</p><p>New alternatives are \';_\' or \'_/_\' or type your own. </p></body></html>"))
        self.itunes_compatible_grouping.setText(_("Save iTunes compatible grouping and work"))
        self.write_id3v1.setText(_("Also include ID3v1 tags in the files"))
