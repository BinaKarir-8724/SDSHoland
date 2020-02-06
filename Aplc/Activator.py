# -*- coding: utf-8 -*-

###########################################################################
# # Python code generated with wxFormBuilder (version Oct 29 2018)
# # http://www.wxformbuilder.org/
# #
# # PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
myimage = u"img/binakarir2.png"
import wx.adv

###########################################################################
# # Class IntiWindow
###########################################################################


class IntiWindow (wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=u"BinaKarir", pos=wx.DefaultPosition, size=wx.Size(300, 300), style=wx.CAPTION | wx.CLOSE_BOX | wx.TAB_TRAVERSAL, name=u"IntiWindow")

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		bSizer1 = wx.BoxSizer(wx.VERTICAL)

		self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 300), wx.TAB_TRAVERSAL)
		bSizer3 = wx.BoxSizer(wx.VERTICAL)

		self.start_image = wx.Image(myimage)
		self.start_image.Rescale(250, 100)
		self.image = wx.BitmapFromImage(self.start_image)

		self.mypic = wx.StaticBitmap(self, -1, self.image, 	wx.DefaultPosition, style=wx.BITMAP_TYPE_PNG)
		bSizer3.Add(self.mypic, 1, wx.ALL | wx.EXPAND, 5)

		self.m_button1 = wx.Button(self.m_panel1, wx.ID_ANY, u"Lanjut", wx.Point(-1, -1), wx.Size(-1, -1), 0)
		bSizer3.Add(self.m_button1, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

		bSizer4.Add((0, 0), 1, wx.EXPAND, 5)

		self.m_button2 = wx.Button(self.m_panel1, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer4.Add(self.m_button2, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

		bSizer3.Add(bSizer4, 1, wx.EXPAND, 5)

		self.m_panel1.SetSizer(bSizer3)
		self.m_panel1.Layout()
		bSizer1.Add(self.m_panel1, 1, wx.ALL | wx.EXPAND, 5)

		self.SetSizer(bSizer1)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.m_button1.Bind(wx.EVT_BUTTON, self.btn_lanjut)
		self.m_button2.Bind(wx.EVT_BUTTON, self.btn_admin)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def btn_lanjut(self, event):
		event.Skip()

	def btn_admin(self, event):
		event.Skip()

###########################################################################
# # Class Konfigurasi
###########################################################################


class Konfigurasi (wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=u"BinaKarir", pos=wx.DefaultPosition, size=wx.Size(450, 300), style=wx.FRAME_NO_TASKBAR | wx.STAY_ON_TOP | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		bSizer7 = wx.BoxSizer(wx.VERTICAL)

		fgSizer4 = wx.FlexGridSizer(3, 1, 0, 0)
		fgSizer4.AddGrowableCol(0)
		fgSizer4.AddGrowableRow(2)
		fgSizer4.SetFlexibleDirection(wx.BOTH)
		fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Konfigurasi", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText1.Wrap(-1)

		self.m_staticText1.SetFont(wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans"))

		fgSizer4.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		fgSizer31 = wx.FlexGridSizer(0, 3, 0, 0)
		fgSizer31.AddGrowableCol(2)
		fgSizer31.SetFlexibleDirection(wx.BOTH)
		fgSizer31.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_panel5 = wx.Panel(self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		fgSizer3 = wx.FlexGridSizer(0, 3, 0, 0)
		fgSizer3.AddGrowableCol(1)
		fgSizer3.AddGrowableCol(2)
		fgSizer3.SetFlexibleDirection(wx.BOTH)
		fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_staticText5 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"Batas Tanggal Aktif", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText5.Wrap(-1)

		fgSizer3.Add(self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

		self.m_datePicker1 = wx.adv.DatePickerCtrl(self.m_panel5, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size(-1, -1), wx.adv.DP_DEFAULT)
		fgSizer3.Add(self.m_datePicker1, 0, wx.ALL | wx.EXPAND, 5)

		fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
		fgSizer2.AddGrowableCol(1)
		fgSizer2.AddGrowableRow(0)
		fgSizer2.SetFlexibleDirection(wx.BOTH)
		fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_staticText51 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"Tanggal Aktif :", wx.DefaultPosition, wx.Size(-1, -1), 0)
		self.m_staticText51.Wrap(-1)

		fgSizer2.Add(self.m_staticText51, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.tanggal_aktif = wx.StaticText(self.m_panel5, wx.ID_ANY, u"tanggal_aktif", wx.DefaultPosition, wx.DefaultSize, 0)
		self.tanggal_aktif.Wrap(-1)

		fgSizer2.Add(self.tanggal_aktif, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		fgSizer3.Add(fgSizer2, 1, wx.EXPAND, 5)

		self.m_staticText3 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"Password", wx.Point(-1, -1), wx.Size(-1, -1), 0)
		self.m_staticText3.Wrap(-1)

		fgSizer3.Add(self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

		self.password = wx.StaticText(self.m_panel5, wx.ID_ANY, u"Belum ada", wx.DefaultPosition, wx.DefaultSize, 0)
		self.password.Wrap(-1)

		self.password.SetBackgroundColour(wx.Colour(148, 245, 51))

		fgSizer3.Add(self.password, 1, wx.ALL | wx.EXPAND, 5)

		fgSizer3.Add((0, 0), 1, wx.EXPAND, 5)

		self.m_staticText4 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"Ubah Password", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText4.Wrap(-1)

		fgSizer3.Add(self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

		self.ubah_password = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer3.Add(self.ubah_password, 0, wx.ALL | wx.EXPAND, 5)

		self.Ubah = wx.Button(self.m_panel5, wx.ID_ANY, u"Ubah", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer3.Add(self.Ubah, 0, wx.ALL, 5)

		self.m_panel5.SetSizer(fgSizer3)
		self.m_panel5.Layout()
		fgSizer3.Fit(self.m_panel5)
		fgSizer31.Add(self.m_panel5, 0, wx.ALL | wx.EXPAND, 5)

		self.m_panel4.SetSizer(fgSizer31)
		self.m_panel4.Layout()
		fgSizer31.Fit(self.m_panel4)
		fgSizer4.Add(self.m_panel4, 1, wx.ALL | wx.EXPAND, 5)

		fgSizer7 = wx.FlexGridSizer(1, 3, 0, 0)
		fgSizer7.AddGrowableCol(2)
		fgSizer7.AddGrowableRow(0)
		fgSizer7.SetFlexibleDirection(wx.BOTH)
		fgSizer7.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.m_button6 = wx.Button(self, wx.ID_ANY, u"Non Aktifkan", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer7.Add(self.m_button6, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.m_button7 = wx.Button(self, wx.ID_ANY, u"Aktifkan", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer7.Add(self.m_button7, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

		self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"DisAktif", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText8.Wrap(-1)

		self.m_staticText8.SetFont(wx.Font(26, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans"))
		self.m_staticText8.SetBackgroundColour(wx.Colour(21, 182, 21))

		fgSizer7.Add(self.m_staticText8, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		fgSizer4.Add(fgSizer7, 1, wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

		bSizer7.Add(fgSizer4, 1, wx.EXPAND, 5)

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button(self, wx.ID_OK)
		m_sdbSizer1.AddButton(self.m_sdbSizer1OK)
		self.m_sdbSizer1Cancel = wx.Button(self, wx.ID_CANCEL)
		m_sdbSizer1.AddButton(self.m_sdbSizer1Cancel)
		m_sdbSizer1.Realize();

		bSizer7.Add(m_sdbSizer1, 0, wx.EXPAND, 5)

		self.SetSizer(bSizer7)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.m_datePicker1.Bind(wx.adv.EVT_DATE_CHANGED, self.m_datechange)
		self.Ubah.Bind(wx.EVT_BUTTON, self.btn_ubah)
		self.m_button6.Bind(wx.EVT_BUTTON, self.btn_non_aktifkan)
		self.m_button7.Bind(wx.EVT_BUTTON, self.btn_aktifkan)
		self.m_sdbSizer1Cancel.Bind(wx.EVT_BUTTON, self.btn_cancel)
		self.m_sdbSizer1OK.Bind(wx.EVT_BUTTON, self.btn_lanjut)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def m_datechange(self, event):
		event.Skip()

	def btn_ubah(self, event):
		event.Skip()

	def btn_non_aktifkan(self, event):
		event.Skip()

	def btn_aktifkan(self, event):
		event.Skip()

	def btn_cancel(self, event):
		event.Skip()

	def btn_lanjut(self, event):
		event.Skip()

###########################################################################
# # Class DialogPasswd
###########################################################################


class DialogPasswd (wx.Dialog):

	def __init__(self, parent):
		wx.Dialog.__init__ (self, parent, id=wx.ID_ANY, title=u"BinaKarir", pos=wx.DefaultPosition, size=wx.Size(300, 100), style=wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		bSizer6 = wx.BoxSizer(wx.VERTICAL)

		self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		bSizer6.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

		self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), wx.TE_PASSWORD)
		bSizer6.Add(self.m_textCtrl1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.Okay = wx.Button(self, wx.ID_ANY, u"Okay", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer6.Add(self.Okay, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

		self.SetSizer(bSizer6)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.Okay.Bind(wx.EVT_BUTTON, self.btn_passwd)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def btn_passwd(self, event):
		event.Skip()

