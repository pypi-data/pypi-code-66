# -*- coding: utf-8 -*-

from numpy import pi
from PySide2.QtCore import Signal
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget

from ......Classes.HoleM58 import HoleM58
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SMHoleMag.PHoleM58.Gen_PHoleM58 import Gen_PHoleM58
from ......GUI.Dialog.DMatLib.MatLib import MatLib
from ......Methods.Slot.Slot.check import SlotCheckError


class PHoleM58(Gen_PHoleM58, QWidget):
    """Page to set the Hole Type 58"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for WHoleMag
    hole_name = "Slot Type 58"
    hole_type = HoleM58

    def __init__(self, hole=None, matlib=MatLib()):
        """Initialize the widget according to hole

        Parameters
        ----------
        self : PHoleM58
            A PHoleM58 widget
        hole : HoleM58
            current hole to edit
        matlib : MatLib
            Material Library
        """
        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        self.matlib = matlib
        self.hole = hole

        # Set FloatEdit unit
        self.lf_W0.unit = "m"
        self.lf_W1.unit = "m"
        self.lf_W2.unit = "m"
        self.lf_W3.unit = "rad"
        self.lf_R0.unit = "m"
        self.lf_H0.unit = "m"
        self.lf_H1.unit = "m"
        self.lf_H2.unit = "m"

        # Set default materials
        self.w_mat_0.setText("mat_void:")
        self.w_mat_0.def_mat = "Air"
        self.w_mat_1.setText("magnet_0:")
        self.w_mat_1.def_mat = "Magnet1"

        # Adapt GUI with/without magnet
        if hole.magnet_0 is None:  # SyRM
            self.img_slot.setPixmap(
                QPixmap(":/images/images/MachineSetup/WSlot/Slot_58_no_mag.PNG")
            )
            self.W1 = 0
            self.W2 = 0
            self.w_mat_0.update(self.hole, "mat_void", self.matlib)
            self.w_mat_1.hide()
        else:
            # Set current material
            self.w_mat_0.update(self.hole, "mat_void", self.matlib)
            self.w_mat_1.update(self.hole.magnet_0, "mat_type", self.matlib)

        # Set unit name (m ou mm)
        self.u = gui_option.unit
        wid_list = [
            self.unit_W0,
            self.unit_W1,
            self.unit_W2,
            self.unit_R0,
            self.unit_H0,
            self.unit_H1,
            self.unit_H2,
        ]
        for wid in wid_list:
            wid.setText(self.u.get_m_name())

        # Fill the fields with the machine values (if they're filled)
        self.lf_W0.setValue(self.hole.W0)
        self.lf_W1.setValue(self.hole.W1)
        self.lf_W2.setValue(self.hole.W2)
        self.lf_W3.setValue(self.hole.W3)
        self.lf_R0.setValue(self.hole.R0)
        self.lf_H0.setValue(self.hole.H0)
        self.lf_H1.setValue(self.hole.H1)
        self.lf_H2.setValue(self.hole.H2)

        # Display the main output of the hole (surface, height...)
        self.comp_output()

        # Connect the signal
        self.lf_W0.editingFinished.connect(self.set_W0)
        self.lf_W1.editingFinished.connect(self.set_W1)
        self.lf_W2.editingFinished.connect(self.set_W2)
        self.lf_W3.editingFinished.connect(self.set_W3)
        self.lf_R0.editingFinished.connect(self.set_R0)
        self.lf_H0.editingFinished.connect(self.set_H0)
        self.lf_H1.editingFinished.connect(self.set_H1)
        self.lf_H2.editingFinished.connect(self.set_H2)
        self.w_mat_0.saveNeeded.connect(self.emit_save)
        self.w_mat_1.saveNeeded.connect(self.emit_save)

    def set_W0(self):
        """Signal to update the value of W0 according to the line edit

        Parameters
        ----------
        self : PHoleM58
            A PHoleM58 widget
        """
        self.hole.W0 = self.lf_W0.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W1(self):
        """Signal to update the value of W1 according to the line edit

        Parameters
        ----------
        self : PHoleM58
            A PHoleM58 widget
        """
        self.hole.W1 = self.lf_W1.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W2(self):
        """Signal to update the value of W2 according to the line edit

        Parameters
        ----------
        self : PHoleM58
            A PHoleM58 widget
        """
        self.hole.W2 = self.lf_W2.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_W3(self):
        """Signal to update the value of W3 according to the line edit

        Parameters
        ----------
        self : PHoleM58
            A PHoleM58 widget
        """
        self.hole.W3 = self.lf_W3.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_R0(self):
        """Signal to update the value of R0 according to the line edit

        Parameters
        ----------
        self : PHoleM58
            A PHoleM58 widget
        """
        self.hole.R0 = self.lf_R0.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PHoleM58
            A PHoleM58 widget
        """
        self.hole.H0 = self.lf_H0.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H1(self):
        """Signal to update the value of H1 according to the line edit

        Parameters
        ----------
        self : PHoleM58
            A PHoleM58 widget
        """
        self.hole.H1 = self.lf_H1.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_H2(self):
        """Signal to update the value of H2 according to the line edit

        Parameters
        ----------
        self : PHoleM58
            A PHoleM58 widget
        """
        self.hole.H2 = self.lf_H2.value()
        self.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def comp_output(self):
        """Compute and display the hole output

        Parameters
        ----------
        self : PHoleM58
            A PHoleM58 widget
        """
        is_set = False
        if self.check() is None:
            try:
                # We compute the output only if the hole is correctly set
                # Compute all the needed output as string
                s_surf = format(self.u.get_m2(self.hole.comp_surface()), ".4g")
                m_surf = format(self.u.get_m2(self.hole.comp_surface_magnets()), ".4g")

                # Update the GUI to display the Output
                self.out_slot_surface.setText(
                    "Hole suface: " + s_surf + " " + self.u.get_m2_name()
                )
                self.out_magnet_surface.setText(
                    "Magnet surface: " + m_surf + " " + self.u.get_m2_name()
                )
                is_set = True
            except:
                pass

        if not is_set:
            # We can't compute the output => We erase the previous version
            # (that way the user know that something is wrong)
            self.out_slot_surface.setText("Hole suface: ?")
            self.out_magnet_surface.setText("Magnet surface: ?")

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : PHoleM58
            A PHoleM58 widget

        Returns
        -------
        error : str
            Error message (return None if no error)
        """

        # Constraints and None
        try:
            self.hole.check()
        except SlotCheckError as error:
            return str(error)

    def emit_save(self):
        """Send a saveNeeded signal to the DMachineSetup"""
        self.saveNeeded.emit()
