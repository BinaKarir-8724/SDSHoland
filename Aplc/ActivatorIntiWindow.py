"""Subclass of IntiWindow, which is generated by wxFormBuilder."""

import Aplc.Activator as Activator


# Implementing IntiWindow
class ActivatorIntiWindow(Activator.IntiWindow):

	def __init__(self, parent):
		Activator.IntiWindow.__init__(self, parent)

	# Handlers for IntiWindow events.
	def btn_lanjut(self, event):
		# TODO: Implement btn_lanjut
		print ("Tutup Aplikasi")
		self.Close(True)
		pass

	def btn_admin(self, event):
		# TODO: Implement btn_admin
		print ("Hello")
		from Aplc.ActivatorDialogPasswd import ActivatorDialogPasswd as D
		self.D = D(self)
		self.D.Show(True)
		pass

