# -*- coding: utf-8 -*-

###########################################################################
# # Python code generated with wxFormBuilder (version Oct 29 2018)
# # http://www.wxformbuilder.org/
# #
# # PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# # Class Listbox1
###########################################################################


class Listbox1 (wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=u"Cari Pekerjaan", pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		bSizer1 = wx.BoxSizer(wx.VERTICAL)

		self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.m_panel1.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT"))

		bSizer5 = wx.BoxSizer(wx.VERTICAL)

		bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

		bSizer2.Add((0, 0), 1, wx.EXPAND, 5)

		self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Nama Pekerjaan", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText1.Wrap(-1)

		bSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.m_textCtrl1 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_textCtrl1.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT"))

		bSizer2.Add(self.m_textCtrl1, 1, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.m_button3 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_button3.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT"))

		self.m_staticTextKode = wx.StaticText(self.m_panel1, wx.ID_ANY, label="Cari Dalam Bahasa Inggris")
		self.m_staticTextKode.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT"))
		self.m_staticTextKode.Wrap(-1)

		# self.m_button3 = wx.Button( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		# self.m_button3.SetBitmap( wx.NullBitmap )

		bSizer2.Add(self.m_staticTextKode, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

		bSizer2.Add(self.m_button3, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

		bSizer5.Add(bSizer2, 0, wx.EXPAND, 5)

		from AppsSDS.db import db
		self.listprofesiona = db.QueryList()
		print (self.listprofesiona.query2())
		# print (list(self.listprofesiona.query().keys()))
		# m_listBox1Choices = list(self.listprofesiona.query().keys())
		m_listBox1Choices = list(self.listprofesiona.query2())

		print(type(m_listBox1Choices))
		# self.m_listBox1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, wx.LB_NEEDED_SB|wx.LB_SORT )
		# bSizer5.Add( self.m_listBox1, 1, wx.ALL|wx.EXPAND, 5 )
		# self.m_listBox1.Hide()

		self.m_listCtrl1 = wx.ListCtrl(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_EDIT_LABELS | wx.LC_REPORT)
		bSizer5.Add(self.m_listCtrl1, 1, wx.ALL | wx.EXPAND, 5)

		self.m_listCtrl1.InsertColumn(0, "Nama Pekerjaan", width=450, format=wx.LIST_FORMAT_LEFT)
		self.m_listCtrl1.InsertColumn(1, "Kode", width=75, format=wx.LIST_FORMAT_LEFT)
		self.m_listCtrl1.InsertColumn(2, "Pekerjaan Bahasa Indonesia", width=450, format=wx.LIST_FORMAT_LEFT)
		
		# print (m_listBox1Choices)
		for listdatabaseimport in range(len(m_listBox1Choices)) :
			print (listdatabaseimport)
			self.m_listCtrl1.InsertItem(listdatabaseimport, m_listBox1Choices[listdatabaseimport][0])
			self.m_listCtrl1.SetItem(listdatabaseimport, 1, m_listBox1Choices[listdatabaseimport][1])
			self.m_listCtrl1.SetItem(listdatabaseimport, 2, m_listBox1Choices[listdatabaseimport][2])

		fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
		fgSizer1.AddGrowableCol(0)
		fgSizer1.AddGrowableCol(1)
		fgSizer1.AddGrowableRow(0)
		fgSizer1.SetFlexibleDirection(wx.BOTH)
		fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		self.cancel = wx.Button(self.m_panel1, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer1.Add(self.cancel, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, 5)

		self.ok = wx.Button(self.m_panel1, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0)
		fgSizer1.Add(self.ok, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		bSizer5.Add(fgSizer1, 0, wx.EXPAND | wx.ALIGN_RIGHT, 5)

		self.m_panel1.SetSizer(bSizer5)
		self.m_panel1.Layout()
		bSizer5.Fit(self.m_panel1)
		bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

		self.SetSizer(bSizer1)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.m_textCtrl1.Bind(wx.EVT_TEXT, self.m_textCtrl_listOnText)
		# self.m_button3.Bind( wx.EVT_BUTTON, self.m_button3_cariOnButtonClick )
		self.m_staticTextKode.Bind(wx.EVT_TEXT, self.m_textCtrlKode_listOnText)

		import os
		import pathlib
		pathf = pathlib.Path.cwd() / "images/symbol/search.jpg"
		self.image = wx.Image(str(pathf))
		self.re_image = self.image.Rescale(40, 20)
		# self.m_button3.SetBitmap( wx.Bitmap( self.re_image ) )

		self.m_button3.Refresh()
		self.m_button3.Layout()
		self.SetSizer(bSizer1)
		self.Refresh()
		self.Layout()
		self.SetSize(800, 600)
		self.Centre(wx.BOTH)

		# Connect Events
		self.m_textCtrl1.Bind(wx.EVT_TEXT, self.m_textCtrl_listOnText)
		self.m_button3.Bind(wx.EVT_TEXT, self.m_button3_cariOnButtonClick)

		# Connect Events
		self.cancel.Bind(wx.EVT_BUTTON, self.m_tombolcancel_lb)
		self.ok.Bind(wx.EVT_BUTTON, self.tombolok_lb)
		# self.m_listBox1.Bind( wx.EVT_LISTBOX_DCLICK, self.m_listboxselect )
		self.m_textCtrl1.Bind(wx.EVT_TEXT, self.m_textCtrl_listOnText)
		# self.m_button3.Bind( wx.EVT_BUTTON, self.m_button3_cariOnButtonClick )
		self.m_listCtrl1.Bind(wx.EVT_LEFT_DCLICK, self.m_listCtrl1OnLeftDClick)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def m_tombolcancel_lb(self, event):
		event.Skip()

	def m_textCtrlKode_listOnText(self, event):
		print ("hh")
		event.Skip()

	def tombolok_lb(self, event):
		event.Skip()

	def m_listboxselect(self, event):
		event.Skip()

	def m_textCtrl_listOnText(self, event):
		event.Skip()

	def m_button3_cariOnButtonClick(self, event):
		# deleted_item = self.m_listBox1.GetStringSelection()
		# numOfItems=self.m_listBox1.GetCount()
		# itemsArr = []
		# for i in range(numOfItems):
		# 	x = self.m_listBox1.GetString(i)
		# 	if x != deleted_item:
		# 		itemsArr.append(x)
		# m_listBox1Choices = itemsArr
		# self.m_listBox1.Clear()
		# self.m_listBox1.Set(m_listBox1Choices)
		# self.m_listBox1.Update()
		event.Skip()

