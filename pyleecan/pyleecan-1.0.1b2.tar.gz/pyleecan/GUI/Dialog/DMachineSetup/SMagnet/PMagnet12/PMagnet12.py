# -*- coding: utf-8 -*-

from PySide2.QtCore import Signal
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QDialog, QMessageBox

from ......Classes.MagnetType12 import MagnetType12
from ......Classes.SlotMFlat import SlotMFlat
from ......GUI import gui_option
from ......GUI.Dialog.DMachineSetup.SMagnet.PMagnet12.Gen_PMagnet12 import Gen_PMagnet12


class PMagnet12(Gen_PMagnet12, QDialog):
    """Page to set the Magnet Type 12"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for Magnet combobox
    mag_name = "Flat bottom, polar top"
    mag_type = MagnetType12
    slot_type = SlotMFlat

    def __init__(self, machine=None):
        """Initialize the widget according to machine

        Parameters
        ----------
        self : PMagnet12
            A PMagnet12 widget
        machine : Machine
            current machine to edit
        """
        # Build the interface according to the .ui file
        QDialog.__init__(self)
        self.setupUi(self)

        # Saving arguments
        self.machine = machine

        # Set FloatEdit unit
        self.lf_H0.unit = "m"
        self.lf_Hmag.unit = "m"
        self.lf_Wmag.unit = "m"
        self.u = gui_option.unit
        # Set unit name (m ou mm)
        wid_list = [self.unit_H0, self.unit_Hmag, self.unit_Wmag]
        for wid in wid_list:
            wid.setText(self.u.get_m_name())

        # Fill the fields with the lamination values (if they're filled)
        self.lf_Hmag.setValue(self.machine.rotor.slot.magnet[0].Hmag)
        self.lf_Wmag.setValue(self.machine.rotor.slot.magnet[0].Wmag)
        if self.machine.type_machine == 6 and self.machine.rotor.slot.H0 is None:
            self.machine.rotor.slot.H0 = 0  # Default value for SPMSM
        self.lf_H0.setValue(self.machine.rotor.slot.H0)

        # Display the main output of the slot (surface, height...)
        self.w_out.comp_output()

        # Connect the signal/slot
        self.lf_Hmag.editingFinished.connect(self.set_Hmag)
        self.lf_Wmag.editingFinished.connect(self.set_Wmag)
        self.lf_H0.editingFinished.connect(self.set_H0)

    def set_H0(self):
        """Signal to update the value of H0 according to the line edit

        Parameters
        ----------
        self : PMagnet12
            A PMagnet12 object
        """
        self.machine.rotor.slot.H0 = self.lf_H0.value()
        if self.machine.rotor.slot.H0 > 0:
            self.machine.type_machine = 7  # Inset
        else:
            self.machine.type_machine = 6  # Surface
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Wmag(self):
        """Signal to update the value of Wmag according to the line edit

        Parameters
        ----------
        self : PMagnet12
            A PMagnet12 object
        """
        self.machine.rotor.slot.magnet[0].Wmag = self.lf_Wmag.value()
        self.machine.rotor.slot.W0 = self.lf_Wmag.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def set_Hmag(self):
        """Signal to update the value of Hmag according to the line edit

        Parameters
        ----------
        self : PMagnet12
            A PMagnet12 object
        """
        self.machine.rotor.slot.magnet[0].Hmag = self.lf_Hmag.value()
        self.w_out.comp_output()
        # Notify the machine GUI that the machine has changed
        self.saveNeeded.emit()

    def check(self):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        self : PMagnet12
            A PMagnet12 object

        Returns
        -------
        error: str
            Error message (return None if no error)
        """
        # Check that everything is set
        if self.machine.rotor.slot.magnet[0].Wmag is None:
            return self.tr("You must set Wmag !")
        if self.machine.rotor.slot.magnet[0].Hmag is None:
            return self.tr("You must set Hmag !")
        if self.machine.rotor.slot.H0 is None:
            return self.tr("You must set H0 !")

        # Check that everything is set right
        try:
            mec_gap = self.machine.comp_width_airgap_mec()
        except:
            return self.tr("Unable to draw the magnet, " "please check your geometry !")

        if mec_gap <= 0:
            return self.tr("You must have gap_min > 0 (reduce Hmag) !")

    def comp_output(self):
        """Compute and display the magnet output

        Parameters
        ----------
        self : PMagnet12
            A PMagnet12 object
        """
        # Gap is set in SMachineDimension
        gap = format(self.u.get_m(self.machine.comp_width_airgap_mag()), ".4g")
        self.out_gap.setText(self.tr("gap: ") + gap + " " + self.u.get_m_name())

        mag_txt = self.tr("Magnet surface: ")
        gm_txt = self.tr("gap_min: ")
        taum_txt = self.tr("taum: ")

        if self.check() is None:
            # We compute the output only if the slot is correctly set
            Zs = self.machine.rotor.slot.Zs
            # Compute all the needed output as string (scientific notation with
            # 2 digits)
            Smag = format(
                self.u.get_m2(self.machine.rotor.slot.magnet[0].comp_surface()), ".4g"
            )
            gap_min = format(self.u.get_m(self.machine.comp_width_airgap_mec()), ".4g")

            taum = 100 * self.machine.rotor.slot.magnet[0].comp_ratio_opening(Zs / 2.0)
            taum = "%.4g" % (taum)

            # Update the GUI to display the Output
            self.out_Smag.setText(mag_txt + Smag + " " + self.u.get_m2_name())
            self.out_gap_min.setText(gm_txt + gap_min + " " + self.u.get_m_name())
            self.out_taum.setText(taum_txt + taum + " %")
        else:
            # We can't compute the output => We erase the previous version
            # (that way the user know that something is wrong without
            # clicking next)
            self.out_Smag.setText(mag_txt + "?")
            self.out_gap_min.setText(gm_txt + "?")
            self.out_taum.setText(taum_txt + " ?")
