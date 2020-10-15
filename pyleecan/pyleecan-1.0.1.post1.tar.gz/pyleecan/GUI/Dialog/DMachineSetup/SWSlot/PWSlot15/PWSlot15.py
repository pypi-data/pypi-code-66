# -*- coding: utf-8 -*-

import PySide2.QtCore
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget

from ......Classes.SlotW15 import SlotW15
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SWSlot.PWSlot15.Gen_PWSlot15 import Gen_PWSlot15
from ......Methods.Slot.Slot.check import SlotCheckError

translate = PySide2.QtCore.QCoreApplication.translate


class PWSlot15(Gen_PWSlot15, QWidget):
    """Page to set the Slot Type 15"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for Slot combobox
    slot_name = "Slot Type 15"
    slot_type = SlotW15

    def __init__(self, lamination=None):
        """Initialize the GUI according to current lamination

        Parameters
        ----------
        self : PWSlot15
            A PWSlot15 widget
        lamination : Lamination
            current lamination to edit
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.lamination = lamination
        self.slot = lamination.slot

        # Set FloatEdit unit
        self.lf_W0.unit = "m"
        self.lf_W3.unit = "m"
        self.lf_H0.unit = "m"
        self.lf_H1.unit = "m"
        self.lf_H2.unit = "m"
        self.lf_R1.unit = "m"
        self.lf_R2.unit = "m"

        # Set unit name (m ou mm)
        wid_list = [
            self.unit_W0,
            self.unit_W3,
            self.unit_H0,
            self.unit_H1,
            self.unit_H2,
            self.unit_R1,
            self.unit_R2,
        ]
        for wid in wid_list:
            wid.setText(gui_option.unit.get_m_name())

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.slot.W0)
        self.lf_W3.setValue(self.slot.W3)
        self.lf_H0.setValue(self.slot.H0)
        self.lf_H1.setValue(self.slot.H1)
        self.lf_H2.setValue(self.slot.H2)
        self.lf_R1.setValue(self.slot.R1)
        self.lf_R2.setValue(self.slot.R2)

        # Display the main output of the slot (surface, height...)
        self.w_out.comp_output()

        # Connect the signal
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_W3.editingFinished.connect(self.set_W3)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_H1.editingFinished.connect(self.set_H1)
        self.lf_H2.editingFinished.connect(self.set_H2)
        self.lf_R1.editingFinished.connect(self.set_R1)
        self.lf_R2.editingFinished.connect(self.set_R2)

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PWSlot15
            A PWSlot15 object
        """
        self.slot.W0 = self.lf_W0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W3(self):
        """Signal to update the value of W3 according to the line edit

        Parameters
        ----------
        self : PWSlot15
            A PWSlot15 object
        """
        self.slot.W3 = self.lf_W3.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PWSlot15
            A PWSlot15 object
        """
        self.slot.H0 = self.lf_H0.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H1(self):
        """Signal to update the value of H1 according to the line edit

        Parameters
        ----------
        self : PWSlot15
            A PWSlot15 object
        """
        self.slot.H1 = self.lf_H1.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H2(self):
        """Signal to update the value of H2 according to the line edit

        Parameters
        ----------
        self : PWSlot15
            A PWSlot15 object
        """
        self.slot.H2 = self.lf_H2.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_R1(self):
        """Signal to update the value of R1 according to the line edit

        Parameters
        ----------
        self : PWSlot15
            A PWSlot15 object
        """
        self.slot.R1 = self.lf_R1.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_R2(self):
        """Signal to update the value of R2 according to the line edit

        Parameters
        ----------
        self : PWSlot15
            A PWSlot15 object
        """
        self.slot.R2 = self.lf_R2.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    @staticmethod
    def check(lam):
        """Check that the current lamination have all the needed field set

        Parameters
        ----------
        lam: LamSlotWind
            Lamination to check

        Returns
        -------
        error: str
            Error message (return None if no error)
        """

        # Check that everything is set
        if lam.slot.W0 is None:
            return translate("You must set W0 !", "PWSlot15")
        elif lam.slot.W3 is None:
            return translate("You must set W3 !", "PWSlot15")
        elif lam.slot.H0 is None:
            return translate("You must set H0 !", "PWSlot15")
        elif lam.slot.H1 is None:
            return translate("You must set H1 !", "PWSlot15")
        elif lam.slot.H2 is None:
            return translate("You must set H2 !", "PWSlot15")
        elif lam.slot.R1 is None:
            return translate("You must set R1 !", "PWSlot15")
        elif lam.slot.R2 is None:
            return translate("You must set R2 !", "PWSlot15")

        # Check that everything is set right
        # Constraints
        try:
            lam.slot.check()
        except SlotCheckError as error:
            return str(error)

        # Output
        try:
            yoke_height = lam.comp_height_yoke()
        except Exception as error:
            return translate("Unable to compute yoke height:", "PWSlot15") + str(error)
        if yoke_height <= 0:
            return translate(
                "The slot height is greater than the lamination !", "PWSlot15"
            )
