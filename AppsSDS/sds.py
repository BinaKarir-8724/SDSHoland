# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug 22 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

from AppsSDS.style import main
import wx
import wx.xrc
import wx.adv
import wx.grid

###########################################################################
## Class WindowUtama
###########################################################################

class WindowUtama ( main ):

	def __init__( self, parent ):
		main.__init__ ( self, parent, id = wx.ID_ANY, title = u"BINAKARIR", pos = wx.DefaultPosition, size = wx.Size( 1000,1000 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 210, 211, 213 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_panel1.SetBackgroundColour( wx.Colour( 210, 211, 213 ) )

		bSizer101 = wx.BoxSizer( wx.VERTICAL )

		self.panel_radiobtn_halaman1 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_radiobtn_halaman1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.panel_radiobtn_halaman1.SetBackgroundColour( wx.Colour( 210, 211, 213 ) )

		fgSizer13 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_radioBtn1 = wx.RadioButton( self.panel_radiobtn_halaman1, wx.ID_ANY, u"Form Pekerjaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer13.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

		self.m_radioBtn2 = wx.RadioButton( self.panel_radiobtn_halaman1, wx.ID_ANY, u"Form Pendidikan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer13.Add( self.m_radioBtn2, 0, wx.ALL, 5 )


		self.panel_radiobtn_halaman1.SetSizer( fgSizer13 )
		self.panel_radiobtn_halaman1.Layout()
		fgSizer13.Fit( self.panel_radiobtn_halaman1 )
		bSizer101.Add( self.panel_radiobtn_halaman1, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.halaman1 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.halaman1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.halaman1.SetBackgroundColour( wx.Colour( 210, 211, 213 ) )

		fgSizer14 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer14.AddGrowableCol( 0 )
		fgSizer14.AddGrowableCol( 1 )
		fgSizer14.AddGrowableCol( 2 )
		fgSizer14.AddGrowableRow( 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_scrolledWindow71 = wx.ScrolledWindow( self.halaman1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow71.SetScrollRate( 5, 5 )
		self.m_scrolledWindow71.SetBackgroundColour( wx.Colour( 210, 211, 213 ) )

		bSizer57 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self.m_scrolledWindow71, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel7.SetBackgroundColour( wx.Colour( 210, 211, 213 ) )

		fgSizer4 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.no_tes = wx.StaticText( self.m_panel7, wx.ID_ANY, u"No Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.no_tes.Wrap( -1 )

		self.no_tes.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.no_tes, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.no_tes_input = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.no_tes_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.no_tes_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.tanggal_tes = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_tes.Wrap( -1 )

		self.tanggal_tes.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.tanggal_tes, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_tes_input = wx.adv.DatePickerCtrl( self.m_panel7, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		self.tanggal_tes_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.tanggal_tes_input, 0, wx.ALL, 5 )

		self.nama_kandidat = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Nama Kandidat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama_kandidat.Wrap( -1 )

		self.nama_kandidat.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.nama_kandidat, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nama_kandidat_input = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.nama_kandidat_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.nama_kandidat_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.jenis_kelamin = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jenis_kelamin.Wrap( -1 )

		self.jenis_kelamin.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.jenis_kelamin, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		jenis_kelamin_inputChoices = [ u"Laki-Laki", u"Perempuan" ]
		self.jenis_kelamin_input = wx.Choice( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, jenis_kelamin_inputChoices, 0 )
		self.jenis_kelamin_input.SetSelection( 1 )
		self.jenis_kelamin_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.jenis_kelamin_input, 0, wx.ALL, 5 )

		self.tanggal_lahir = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_lahir.Wrap( -1 )

		self.tanggal_lahir.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.tanggal_lahir, 0, wx.ALL, 5 )

		self.tanggal_lahir_input = wx.adv.DatePickerCtrl( self.m_panel7, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		self.tanggal_lahir_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.tanggal_lahir_input, 0, wx.ALL, 5 )

		self.pendidikan_terakhir = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Pendidikan Terakhir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pendidikan_terakhir.Wrap( -1 )

		self.pendidikan_terakhir.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.pendidikan_terakhir, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		pendidikan_terakhir_inputChoices = [ u"SD", u"SMP", u"SMA/Sederajat", u"Diploma", u"S1", u"S2", u"S3" ]
		self.pendidikan_terakhir_input = wx.Choice( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pendidikan_terakhir_inputChoices, 0 )
		self.pendidikan_terakhir_input.SetSelection( 0 )
		self.pendidikan_terakhir_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.pendidikan_terakhir_input, 0, wx.ALL, 5 )

		self.jurusan = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Jurusan Pendidikan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan.Wrap( -1 )

		self.jurusan.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.jurusan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan_input = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.jurusan_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.kota = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kota.Wrap( -1 )

		self.kota.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.kota, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kota_input = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kota_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.kota_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.perusahaan_instansi = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Perusahaan/Instansi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.perusahaan_instansi.Wrap( -1 )

		self.perusahaan_instansi.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.perusahaan_instansi, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.perusahaan_instansi_input = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.perusahaan_instansi_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.perusahaan_instansi_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.posisi_jabatan = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Posisi/Jabatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.posisi_jabatan.Wrap( -1 )

		self.posisi_jabatan.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.posisi_jabatan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.posisi_jabatan_input = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.posisi_jabatan_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.posisi_jabatan_input, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel7.SetSizer( fgSizer4 )
		self.m_panel7.Layout()
		fgSizer4.Fit( self.m_panel7 )
		bSizer57.Add( self.m_panel7, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel8 = wx.Panel( self.m_scrolledWindow71, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel8.SetBackgroundColour( wx.Colour( 210, 211, 213 ) )
		self.m_panel8.Hide()

		fgSizer15 = wx.FlexGridSizer( 13, 2, 0, 1 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.nama2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama2.Wrap( -1 )

		self.nama2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.nama2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nama_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.nama_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.nama_input2, 0, wx.ALL, 5 )

		self.tanggal_tes2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_tes2.Wrap( -1 )

		self.tanggal_tes2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.tanggal_tes2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_tes_input2 = wx.adv.DatePickerCtrl( self.m_panel8, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		self.tanggal_tes_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.tanggal_tes_input2, 0, wx.ALL, 5 )

		self.jenis_kelamin2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jenis_kelamin2.Wrap( -1 )

		self.jenis_kelamin2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.jenis_kelamin2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		jenis_kelamin_input2Choices = [ u"Laki-Laki", u"Perempuan" ]
		self.jenis_kelamin_input2 = wx.Choice( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, jenis_kelamin_input2Choices, 0 )
		self.jenis_kelamin_input2.SetSelection( 1 )
		self.jenis_kelamin_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.jenis_kelamin_input2, 0, wx.ALL, 5 )

		self.tanggal_lahir2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_lahir2.Wrap( -1 )

		self.tanggal_lahir2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.tanggal_lahir2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_lahir_input2 = wx.adv.DatePickerCtrl( self.m_panel8, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		self.tanggal_lahir_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.tanggal_lahir_input2, 0, wx.ALL, 5 )

		self.asal_sekolah2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Asal Sekolah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asal_sekolah2.Wrap( -1 )

		self.asal_sekolah2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.asal_sekolah2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.asal_sekolah_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asal_sekolah_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.asal_sekolah_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.jurusan21 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan21.Wrap( -1 )

		self.jurusan21.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.jurusan21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan_input21l = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan_input21l.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.jurusan_input21l, 0, wx.ALL|wx.EXPAND, 5 )

		self.asal_universitas2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Asal Universitas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asal_universitas2.Wrap( -1 )

		self.asal_universitas2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.asal_universitas2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.asal_universitas_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asal_universitas_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.asal_universitas_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.jurusan2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan2.Wrap( -1 )

		self.jurusan2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.jurusan2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.jurusan_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.kota2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kota2.Wrap( -1 )

		self.kota2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.kota2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kota_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kota_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.kota_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.hobi2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Hobi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hobi2.Wrap( -1 )

		self.hobi2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.hobi2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.hobi_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.hobi_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.hobi_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.prestasi_akademik2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Prestasi Akademik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prestasi_akademik2.Wrap( -1 )

		self.prestasi_akademik2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.prestasi_akademik2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.prestasi_akademik_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.prestasi_akademik_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.prestasi_akademik_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.prestasi_non_akademik2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Prestasi Non Akademik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prestasi_non_akademik2.Wrap( -1 )

		self.prestasi_non_akademik2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.prestasi_non_akademik2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.prestasi_non_akademik_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.prestasi_non_akademik_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.prestasi_non_akademik_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.ekskul_yang_diikuti2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Ekskul yang Diikuti", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ekskul_yang_diikuti2.Wrap( -1 )

		self.ekskul_yang_diikuti2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.ekskul_yang_diikuti2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ekskul_yang_diikuti_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.ekskul_yang_diikuti_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.ekskul_yang_diikuti_input2, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel8.SetSizer( fgSizer15 )
		self.m_panel8.Layout()
		fgSizer15.Fit( self.m_panel8 )
		bSizer57.Add( self.m_panel8, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel21 = wx.Panel( self.m_scrolledWindow71, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel21.SetBackgroundColour( wx.Colour( 210, 211, 213 ) )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap31 = wx.StaticBitmap( self.m_panel21, wx.ID_ANY, wx.Bitmap( u"images/logosds.jpeg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_bitmap31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bitmap3 = wx.StaticBitmap( self.m_panel21, wx.ID_ANY, wx.Bitmap( u"images/binakarir.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_bitmap3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel21.SetSizer( bSizer25 )
		self.m_panel21.Layout()
		bSizer25.Fit( self.m_panel21 )
		bSizer57.Add( self.m_panel21, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		self.m_scrolledWindow71.SetSizer( bSizer57 )
		self.m_scrolledWindow71.Layout()
		bSizer57.Fit( self.m_scrolledWindow71 )
		fgSizer14.Add( self.m_scrolledWindow71, 1, wx.EXPAND |wx.ALL, 5 )


		self.halaman1.SetSizer( fgSizer14 )
		self.halaman1.Layout()
		fgSizer14.Fit( self.halaman1 )
		bSizer101.Add( self.halaman1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.halaman2 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.halaman2.SetBackgroundColour( wx.Colour( 249, 250, 249 ) )
		self.halaman2.Hide()

		bSizer301 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow6 = wx.ScrolledWindow( self.halaman2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow6.SetScrollRate( 5, 5 )
		self.m_scrolledWindow6.SetBackgroundColour( wx.Colour( 91, 85, 112 ) )

		bSizer311 = wx.BoxSizer( wx.VERTICAL )

		from AppsSDS.dPage2 import dPage2
		self.m_panelPage2 = dPage2( self.m_scrolledWindow6)
		self.m_panelPage2.textctrl1.Bind( wx.EVT_TEXT, self.textctrl1OnText )
		self.m_panelPage2.textctrl1.Bind( wx.EVT_ENTER_WINDOW, self.textctrl1OnEnterWindow )
		self.m_panelPage2.openlistbox1.Bind( wx.EVT_BUTTON, self.openlistbox1OnButtonClick )
		self.m_panelPage2.textctrl2.Bind( wx.EVT_TEXT, self.textctrl2OnText )
		self.m_panelPage2.openlistbox2.Bind( wx.EVT_BUTTON, self.openlistbox2OnButtonClick )
		self.m_panelPage2.textctrl3.Bind( wx.EVT_TEXT, self.textctrl3OnText )
		self.m_panelPage2.openlistbox3.Bind( wx.EVT_BUTTON, self.openlistbox3OnButtonClick )
		self.m_panelPage2.textctrl4.Bind( wx.EVT_TEXT, self.textctrl4OnText )
		self.m_panelPage2.openlistbox4.Bind( wx.EVT_BUTTON, self.openlistbox4OnButtonClick )
		self.m_panelPage2.textctrl5.Bind( wx.EVT_TEXT, self.textctrl5OnText )
		self.m_panelPage2.openlistbox5.Bind( wx.EVT_BUTTON, self.openlistbox5OnButtonClick )
		self.m_panelPage2.textctrl6.Bind( wx.EVT_TEXT, self.textctrl6OnText )
		self.m_panelPage2.openlistbox6.Bind( wx.EVT_BUTTON, self.openlistbox6OnButtonClick )
		self.m_panelPage2.openlistbox1.Bind( wx.EVT_ENTER_WINDOW, self.openlistbox1OnEnterWindow )
		self.m_panelPage2.label1.Bind( wx.EVT_ENTER_WINDOW, self.label1OnEnterWindow )

		self.m_panelPage2.textctrl1.Bind( wx.EVT_ENTER_WINDOW, self.textctrl1OnEnterWindow )
		self.m_panelPage2.openlistbox1.Bind( wx.EVT_ENTER_WINDOW, self.openlistbox1OnEnterWindow )
		self.m_panelPage2.label1.Bind( wx.EVT_ENTER_WINDOW, self.label1OnEnterWindow )
		self.m_panelPage2.textctrl2.Bind( wx.EVT_ENTER_WINDOW, self.textctrl2OnEnterWindow )
		self.m_panelPage2.openlistbox2.Bind( wx.EVT_ENTER_WINDOW, self.openlistbox2OnEnterWindow )
		self.m_panelPage2.textctrl3.Bind( wx.EVT_ENTER_WINDOW, self.textctrl3OnEnterWindow )
		self.m_panelPage2.openlistbox3.Bind( wx.EVT_ENTER_WINDOW, self.openlistbox3OnEnterWindow )
		self.m_panelPage2.textctrl4.Bind( wx.EVT_ENTER_WINDOW, self.textctrl4OnEnterWindow )
		self.m_panelPage2.openlistbox4.Bind( wx.EVT_ENTER_WINDOW, self.openlistbox4OnEnterWindow )
		self.m_panelPage2.textctrl5.Bind( wx.EVT_ENTER_WINDOW, self.textctrl5OnEnterWindow )
		self.m_panelPage2.openlistbox5.Bind( wx.EVT_ENTER_WINDOW, self.openlistbox5OnEnterWindow )
		self.m_panelPage2.textctrl6.Bind( wx.EVT_ENTER_WINDOW, self.textctrl6OnEnterWindow )
		self.m_panelPage2.openlistbox6.Bind( wx.EVT_ENTER_WINDOW, self.openlistbox6OnEnterWindow )

		bSizer311.Add( self.m_panelPage2, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow6.SetSizer( bSizer311 )
		self.m_scrolledWindow6.Layout()
		bSizer311.Fit( self.m_scrolledWindow6 )
		bSizer301.Add( self.m_scrolledWindow6, 1, wx.EXPAND |wx.ALL, 5 )


		self.halaman2.SetSizer( bSizer301 )
		self.halaman2.Layout()
		bSizer301.Fit( self.halaman2 )
		bSizer101.Add( self.halaman2, 5, wx.ALL|wx.EXPAND, 5 )

		self.halaman3 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.halaman3.SetBackgroundColour( wx.Colour( 249, 250, 249 ) )
		self.halaman3.Hide()

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self.halaman3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		self.m_scrolledWindow1.SetBackgroundColour( wx.Colour( 91, 85, 112 ) )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		from AppsSDS.dPage3 import dPage3
		self.m_panelPage3 = dPage3(self.m_scrolledWindow1)


		self.m_panelPage3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer16.Add( self.m_panelPage3, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer16 )
		self.m_scrolledWindow1.Layout()
		bSizer16.Fit( self.m_scrolledWindow1 )
		bSizer15.Add( self.m_scrolledWindow1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.halaman3.SetSizer( bSizer15 )
		self.halaman3.Layout()
		bSizer15.Fit( self.halaman3 )
		bSizer101.Add( self.halaman3, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.halaman4 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.halaman4.SetBackgroundColour( wx.Colour( 249, 250, 249 ) )
		self.halaman4.Hide()

		bSizer151 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow11 = wx.ScrolledWindow( self.halaman4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow11.SetScrollRate( 5, 5 )
		self.m_scrolledWindow11.SetBackgroundColour( wx.Colour( 91, 85, 112 ) )

		bSizer161 = wx.BoxSizer( wx.VERTICAL )

		from AppsSDS.dPage4 import dPage4
		self.m_panelPage4 = dPage4( self.m_scrolledWindow11)
		self.m_panelPage4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer161.Add( self.m_panelPage4, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow11.SetSizer( bSizer161 )
		self.m_scrolledWindow11.Layout()
		bSizer161.Fit( self.m_scrolledWindow11 )
		bSizer151.Add( self.m_scrolledWindow11, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.halaman4.SetSizer( bSizer151 )
		self.halaman4.Layout()
		bSizer151.Fit( self.halaman4 )
		bSizer101.Add( self.halaman4, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.halaman5 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.halaman5.SetBackgroundColour( wx.Colour( 249, 250, 249 ) )
		self.halaman5.Hide()

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow71 = wx.ScrolledWindow( self.halaman5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow71.SetScrollRate( 5, 5 )
		self.m_scrolledWindow71.SetBackgroundColour( wx.Colour( 91, 85, 112 ) )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		from AppsSDS.dPage5 import dPage5
		self.m_panelPage5 = dPage5( self.m_scrolledWindow71)
		self.m_panelPage5.m_tombolHitung.Bind( wx.EVT_BUTTON, self.m_tombolHitungOnButtonClick )

		self.m_panelPage5.m_tampilgrafik.Bind( wx.EVT_BUTTON, self.m_tampilgrafikOnButtonClick )
		self.m_panelPage5.m_grafikproperties.Bind( wx.EVT_BUTTON, self.m_grafikpropertiesOnButtonClick )

		self.m_panelPage5.m_tampilgrafik.Bind( wx.EVT_BUTTON,self.m_tampilgrafikOnButtonClick)
		self.m_panelPage5.m_buttonDetailA.Bind( wx.EVT_BUTTON, self.m_buttonDetailAOnButtonClick )
		self.m_panelPage5.m_buttonDetailK.Bind( wx.EVT_BUTTON, self.m_buttonDetailKOnButtonClick )
		self.m_panelPage5.m_buttonDetailP.Bind( wx.EVT_BUTTON, self.m_buttonDetailPOnButtonClick )
		self.m_panelPage5.m_buttonDetailPD1.Bind( wx.EVT_BUTTON, self.m_buttonDetailPD1OnButtonClick )
		self.m_panelPage5.m_buttonDetailPD2.Bind( wx.EVT_BUTTON, self.m_buttonDetailPD2OnButtonClick )

		bSizer29.Add( self.m_panelPage5, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow71.SetSizer( bSizer29 )
		self.m_scrolledWindow71.Layout()
		bSizer29.Fit( self.m_scrolledWindow71 )
		bSizer27.Add( self.m_scrolledWindow71, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel25 = wx.Panel( self.halaman5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel25.SetBackgroundColour( wx.Colour( 91, 85, 112 ) )
		self.m_panel25.Hide()

		bSizer27.Add( self.m_panel25, 1, wx.EXPAND |wx.ALL, 5 )


		self.halaman5.SetSizer( bSizer27 )
		self.halaman5.Layout()
		bSizer27.Fit( self.halaman5 )
		bSizer101.Add( self.halaman5, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.halaman6 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.halaman6.SetBackgroundColour( wx.Colour( 249, 250, 249 ) )
		self.halaman6.Hide()

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow8 = wx.ScrolledWindow( self.halaman6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow8.SetScrollRate( 5, 5 )
		self.m_scrolledWindow8.SetBackgroundColour( wx.Colour( 91, 85, 112 ) )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		from AppsSDS.dPage6 import dPage6
		self.m_panelPage6 = dPage6( self.m_scrolledWindow8)

		self.m_panelPage6.SetBackgroundColour( wx.Colour( 249, 250, 249 ) )

		bSizer31.Add( self.m_panelPage6, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow8.SetSizer( bSizer31 )
		self.m_scrolledWindow8.Layout()
		bSizer31.Fit( self.m_scrolledWindow8 )
		bSizer30.Add( self.m_scrolledWindow8, 1, wx.EXPAND |wx.ALL, 5 )


		self.halaman6.SetSizer( bSizer30 )
		self.halaman6.Layout()
		bSizer30.Fit( self.halaman6 )
		bSizer101.Add( self.halaman6, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.halaman7 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.halaman7.SetBackgroundColour( wx.Colour( 249, 250, 249 ) )
		self.halaman7.Hide()

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow9 = wx.ScrolledWindow( self.halaman7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow9.SetScrollRate( 5, 5 )
		self.m_scrolledWindow9.SetBackgroundColour( wx.Colour( 91, 85, 112 ) )
		self.m_scrolledWindow9.Hide()

		bSizer31.Add( self.m_scrolledWindow9, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel26 = wx.Panel( self.halaman7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel26.SetBackgroundColour( wx.Colour( 91, 85, 112 ) )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		from AppsSDS.dPage7 import dPage7
		self.m_panelPage7 = dPage7( self.m_panel26)


		self.m_panelPage7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer32.Add( self.m_panelPage7, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel26.SetSizer( bSizer32 )
		self.m_panel26.Layout()
		bSizer32.Fit( self.m_panel26 )
		bSizer31.Add( self.m_panel26, 1, wx.EXPAND |wx.ALL, 5 )


		self.halaman7.SetSizer( bSizer31 )
		self.halaman7.Layout()
		bSizer31.Fit( self.halaman7 )
		bSizer101.Add( self.halaman7, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel9 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel9.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_panel9.SetBackgroundColour( wx.Colour( 210, 211, 213 ) )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button3 = wx.Button( self.m_panel9, wx.ID_ANY, u"Ke Awal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_button3.Enable( False )

		bSizer5.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self.m_panel9, wx.ID_ANY, u"< Sebelumnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_button1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_button1.Enable( False )

		bSizer5.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button2 = wx.Button( self.m_panel9, wx.ID_ANY, u"> Selanjutnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_button2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_button2.SetBackgroundColour( wx.Colour( 73, 209, 182 ) )

		bSizer5.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		self.m_panel9.SetSizer( bSizer5 )
		self.m_panel9.Layout()
		bSizer5.Fit( self.m_panel9 )
		bSizer101.Add( self.m_panel9, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer101 )
		self.m_panel1.Layout()
		bSizer101.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menubar1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_menubar1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_menubar1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		self.m_menu2 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Database", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem3 )
		self.m_menuItem3.Enable( False )

		self.m_menuItem2 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Tutup Aplikasi", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem2 )

		self.m_menubar1.Append( self.m_menu2, u"Berkas" )

		self.m_menu3 = wx.Menu()
		self.m_DataPesertaSeleksi = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Lihat Data Peserta Tes Pekerjaan", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_DataPesertaSeleksi )

		self.m_DataPesertaTes = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Lihat Data Peserta Tes Pendidikan", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_DataPesertaTes )

		self.m_menubar1.Append( self.m_menu3, u"View" )

		self.m_menu21 = wx.Menu()
		self.m_menuItem31 = wx.MenuItem( self.m_menu21, wx.ID_ANY, u"Tentang Aplikasi", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu21.Append( self.m_menuItem31 )

		self.m_menubar1.Append( self.m_menu21, u"Tentang" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.WindowUtamaOnClose )
		self.m_radioBtn1.Bind( wx.EVT_RADIOBUTTON, self.btnradio_formtes )
		self.m_radioBtn2.Bind( wx.EVT_RADIOBUTTON, self.btnradio_formseleksi )
		self.no_tes_input.Bind( wx.EVT_TEXT, self.no_tes_inputOnText )
		self.tanggal_tes_input.Bind( wx.adv.EVT_DATE_CHANGED, self.tanggal_tes_inputOnDateChanged )
		self.nama_kandidat_input.Bind( wx.EVT_TEXT, self.nama_kandidat_inputOnText )
		self.jenis_kelamin_input.Bind( wx.EVT_CHOICE, self.jenis_kelamin_inputOnChoice )
		self.m_button3.Bind( wx.EVT_BUTTON, self.btn_kembaliawal )
		self.m_button1.Bind( wx.EVT_BUTTON, self.btn_balik )
		self.m_button2.Bind( wx.EVT_BUTTON, self.btn_selanjutnya )
		self.Bind( wx.EVT_MENU, self.m_btn_bukadatabase, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.m_btn_tutupaplikasi, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.m_DataPesertaSeleksiOnMenuSelection, id = self.m_DataPesertaSeleksi.GetId() )
		self.Bind( wx.EVT_MENU, self.m_DataPesertaTesOnMenuSelection, id = self.m_DataPesertaTes.GetId() )
		self.Bind( wx.EVT_MENU, self.m_btn_ttgaplikasi, id = self.m_menuItem31.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def WindowUtamaOnClose( self, event ):
		event.Skip()

	def btnradio_formtes( self, event ):
		event.Skip()

	def btnradio_formseleksi( self, event ):
		event.Skip()

	def no_tes_inputOnText( self, event ):
		event.Skip()

	def tanggal_tes_inputOnDateChanged( self, event ):
		event.Skip()

	def nama_kandidat_inputOnText( self, event ):
		event.Skip()

	def jenis_kelamin_inputOnChoice( self, event ):
		event.Skip()

	def btn_kembaliawal( self, event ):
		event.Skip()

	def btn_balik( self, event ):
		event.Skip()

	def btn_selanjutnya( self, event ):
		event.Skip()

	def m_btn_bukadatabase( self, event ):
		event.Skip()

	def m_btn_tutupaplikasi( self, event ):
		event.Skip()

	def m_DataPesertaSeleksiOnMenuSelection( self, event ):
		event.Skip()

	def m_DataPesertaTesOnMenuSelection( self, event ):
		event.Skip()

	def m_btn_ttgaplikasi( self, event ):
		event.Skip()


###########################################################################
## Class TentangAplikasi
###########################################################################

class TentangAplikasi ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Binakarir", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel21 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap2 = wx.StaticBitmap( self.m_panel21, wx.ID_ANY, wx.Bitmap( u"images/binakarir.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.m_bitmap2, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl45 = wx.TextCtrl( self.m_panel21, wx.ID_ANY, u"\nBandung - INDONESIA.\nEmail: careindonesiasolusi@gmail.com\nTelp. 022 8724 1354", wx.DefaultPosition, wx.Size( 500,200 ), wx.TE_CENTER|wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		self.m_textCtrl45.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_textCtrl45.Enable( False )

		bSizer42.Add( self.m_textCtrl45, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )


		self.m_panel21.SetSizer( bSizer42 )
		self.m_panel21.Layout()
		bSizer42.Fit( self.m_panel21 )
		bSizer41.Add( self.m_panel21, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class Page2
###########################################################################

class Page2 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,409 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )


		bSizer10.Add( ( 0, 75), 0, 0, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"OCCUPATIONAL DAYDREAM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )

		bSizer10.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer10.Add( ( 0, 25), 0, 0, 5 )

		bSizer63 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer71 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer71.AddGrowableCol( 1 )
		fgSizer71.SetFlexibleDirection( wx.BOTH )
		fgSizer71.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer71.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.textctrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.textctrl1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.textctrl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.openlistbox1 = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.openlistbox1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.openlistbox1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.openlistbox1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer71.Add( self.openlistbox1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.label1 = wx.StaticText( self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label1.Wrap( -1 )

		self.label1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.label1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer71.Add( self.label1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer71.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.textctrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.textctrl2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.textctrl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.openlistbox2 = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.openlistbox2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.openlistbox2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.openlistbox2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer71.Add( self.openlistbox2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.label2 = wx.StaticText( self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label2.Wrap( -1 )

		self.label2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.label2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText132 = wx.StaticText( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText132.Wrap( -1 )

		fgSizer71.Add( self.m_staticText132, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.textctrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.textctrl3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.textctrl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.openlistbox3 = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.openlistbox3.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.openlistbox3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.openlistbox3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer71.Add( self.openlistbox3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.label3 = wx.StaticText( self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label3.Wrap( -1 )

		self.label3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.label3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText134 = wx.StaticText( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText134.Wrap( -1 )

		fgSizer71.Add( self.m_staticText134, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textctrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.textctrl4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.textctrl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.openlistbox4 = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.openlistbox4.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.openlistbox4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.openlistbox4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer71.Add( self.openlistbox4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.label4 = wx.StaticText( self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label4.Wrap( -1 )

		self.label4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.label4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText138 = wx.StaticText( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText138.Wrap( -1 )

		fgSizer71.Add( self.m_staticText138, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textctrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.textctrl5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.textctrl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.openlistbox5 = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.openlistbox5.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.openlistbox5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.openlistbox5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer71.Add( self.openlistbox5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.label5 = wx.StaticText( self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label5.Wrap( -1 )

		self.label5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.label5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText139 = wx.StaticText( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText139.Wrap( -1 )

		self.m_staticText139.Hide()

		fgSizer71.Add( self.m_staticText139, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.textctrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.textctrl6.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.textctrl6.Hide()

		fgSizer71.Add( self.textctrl6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.openlistbox6 = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.openlistbox6.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.openlistbox6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.openlistbox6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.openlistbox6.Hide()

		fgSizer71.Add( self.openlistbox6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.label6 = wx.StaticText( self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label6.Wrap( -1 )

		self.label6.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.label6.Hide()

		fgSizer71.Add( self.label6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer63.Add( fgSizer71, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer64 = wx.BoxSizer( wx.VERTICAL )


		bSizer64.Add( ( 25, 0), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer63.Add( bSizer64, 0, 0, 5 )


		bSizer10.Add( bSizer63, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		# Connect Events
		self.textctrl1.Bind( wx.EVT_ENTER_WINDOW, self.textctrl1OnEnterWindow )
		self.textctrl1.Bind( wx.EVT_TEXT, self.textctrl1OnText )
		self.openlistbox1.Bind( wx.EVT_BUTTON, self.openlistbox1OnButtonClick )
		self.openlistbox1.Bind( wx.EVT_ENTER_WINDOW, self.openlistbox1OnEnterWindow )
		self.label1.Bind( wx.EVT_ENTER_WINDOW, self.label1OnEnterWindow )
		self.textctrl2.Bind( wx.EVT_ENTER_WINDOW, self.textctrl2OnEnterWindow )
		self.textctrl2.Bind( wx.EVT_TEXT, self.textctrl2OnText )
		self.openlistbox2.Bind( wx.EVT_BUTTON, self.openlistbox2OnButtonClick )
		self.openlistbox2.Bind( wx.EVT_ENTER_WINDOW, self.openlistbox2OnEnterWindow )
		self.textctrl3.Bind( wx.EVT_ENTER_WINDOW, self.textctrl3OnEnterWindow )
		self.textctrl3.Bind( wx.EVT_TEXT, self.textctrl3OnText )
		self.openlistbox3.Bind( wx.EVT_BUTTON, self.openlistbox3OnButtonClick )
		self.openlistbox3.Bind( wx.EVT_ENTER_WINDOW, self.openlistbox3OnEnterWindow )
		self.textctrl4.Bind( wx.EVT_ENTER_WINDOW, self.textctrl4OnEnterWindow )
		self.textctrl4.Bind( wx.EVT_TEXT, self.textctrl4OnText )
		self.openlistbox4.Bind( wx.EVT_BUTTON, self.openlistbox4OnButtonClick )
		self.openlistbox4.Bind( wx.EVT_ENTER_WINDOW, self.openlistbox4OnEnterWindow )
		self.textctrl5.Bind( wx.EVT_ENTER_WINDOW, self.textctrl5OnEnterWindow )
		self.textctrl5.Bind( wx.EVT_TEXT, self.textctrl5OnText )
		self.openlistbox5.Bind( wx.EVT_BUTTON, self.openlistbox5OnButtonClick )
		self.openlistbox5.Bind( wx.EVT_ENTER_WINDOW, self.openlistbox5OnEnterWindow )
		self.textctrl6.Bind( wx.EVT_ENTER_WINDOW, self.textctrl6OnEnterWindow )
		self.textctrl6.Bind( wx.EVT_TEXT, self.textctrl6OnText )
		self.openlistbox6.Bind( wx.EVT_BUTTON, self.openlistbox6OnButtonClick )
		self.openlistbox6.Bind( wx.EVT_ENTER_WINDOW, self.openlistbox6OnEnterWindow )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def textctrl1OnEnterWindow( self, event ):
		event.Skip()

	def textctrl1OnText( self, event ):
		event.Skip()

	def openlistbox1OnButtonClick( self, event ):
		event.Skip()

	def openlistbox1OnEnterWindow( self, event ):
		event.Skip()

	def label1OnEnterWindow( self, event ):
		event.Skip()

	def textctrl2OnEnterWindow( self, event ):
		event.Skip()

	def textctrl2OnText( self, event ):
		event.Skip()

	def openlistbox2OnButtonClick( self, event ):
		event.Skip()

	def openlistbox2OnEnterWindow( self, event ):
		event.Skip()

	def textctrl3OnEnterWindow( self, event ):
		event.Skip()

	def textctrl3OnText( self, event ):
		event.Skip()

	def openlistbox3OnButtonClick( self, event ):
		event.Skip()

	def openlistbox3OnEnterWindow( self, event ):
		event.Skip()

	def textctrl4OnEnterWindow( self, event ):
		event.Skip()

	def textctrl4OnText( self, event ):
		event.Skip()

	def openlistbox4OnButtonClick( self, event ):
		event.Skip()

	def openlistbox4OnEnterWindow( self, event ):
		event.Skip()

	def textctrl5OnEnterWindow( self, event ):
		event.Skip()

	def textctrl5OnText( self, event ):
		event.Skip()

	def openlistbox5OnButtonClick( self, event ):
		event.Skip()

	def openlistbox5OnEnterWindow( self, event ):
		event.Skip()

	def textctrl6OnEnterWindow( self, event ):
		event.Skip()

	def textctrl6OnText( self, event ):
		event.Skip()

	def openlistbox6OnButtonClick( self, event ):
		event.Skip()

	def openlistbox6OnEnterWindow( self, event ):
		event.Skip()


###########################################################################
## Class Page3
###########################################################################

class Page3 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 717,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( ( 0, 75), 0, 0, 5 )

		self.m_staticText144 = wx.StaticText( self, wx.ID_ANY, u"AKTIVITAS, KOMPETENSI, DAN PEKERJAAN", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText144.Wrap( -1 )

		self.m_staticText144.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )

		bSizer27.Add( self.m_staticText144, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer27.Add( ( 0, 25), 0, 0, 5 )

		fgSizer25 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer25.AddGrowableCol( 0 )
		fgSizer25.AddGrowableCol( 1 )
		fgSizer25.AddGrowableCol( 2 )
		fgSizer25.AddGrowableRow( 0 )
		fgSizer25.SetFlexibleDirection( wx.BOTH )
		fgSizer25.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		bSizer27.Add( fgSizer25, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel28 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel28.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel28.SetBackgroundColour( wx.Colour( 88, 85, 112 ) )

		bSizer56 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText167 = wx.StaticText( self.m_panel28, wx.ID_ANY, u"AKTIVITAS", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText167.Wrap( -1 )

		self.m_staticText167.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )

		bSizer56.Add( self.m_staticText167, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel28.SetSizer( bSizer56 )
		self.m_panel28.Layout()
		bSizer56.Fit( self.m_panel28 )
		bSizer52.Add( self.m_panel28, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer52.Add( ( 0, 10), 0, 0, 5 )

		self.m_panel27 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel27.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel27.SetBackgroundColour( wx.Colour( 88, 85, 112 ) )

		fgSizer16 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel29 = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel29.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel29.SetBackgroundColour( wx.Colour( 208, 87, 66 ) )

		bSizer57 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText141 = wx.StaticText( self.m_panel29, wx.ID_ANY, u"Realistic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )

		self.m_staticText141.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText141.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_staticText141.SetBackgroundColour( wx.Colour( 208, 87, 66 ) )

		bSizer57.Add( self.m_staticText141, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel29.SetSizer( bSizer57 )
		self.m_panel29.Layout()
		bSizer57.Fit( self.m_panel29 )
		fgSizer16.Add( self.m_panel29, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_RealisticA = wx.SpinCtrl( self.m_panel27, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_RealisticA.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_RealisticA.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer16.Add( self.m_RealisticA, 0, wx.ALL, 5 )

		self.m_panel36 = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel36.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_panel36.SetBackgroundColour( wx.Colour( 245, 135, 79 ) )

		bSizer62 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText143 = wx.StaticText( self.m_panel36, wx.ID_ANY, u"Investigative", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText143.Wrap( -1 )

		self.m_staticText143.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText143.SetBackgroundColour( wx.Colour( 245, 135, 79 ) )

		bSizer62.Add( self.m_staticText143, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel36.SetSizer( bSizer62 )
		self.m_panel36.Layout()
		bSizer62.Fit( self.m_panel36 )
		fgSizer16.Add( self.m_panel36, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_InvestigativeA = wx.SpinCtrl( self.m_panel27, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_InvestigativeA.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_InvestigativeA.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer16.Add( self.m_InvestigativeA, 0, wx.ALL, 5 )

		self.m_panel37 = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel37.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_panel37.SetBackgroundColour( wx.Colour( 255, 204, 41 ) )

		bSizer63 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText145 = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Artistic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText145.Wrap( -1 )

		self.m_staticText145.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer63.Add( self.m_staticText145, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel37.SetSizer( bSizer63 )
		self.m_panel37.Layout()
		bSizer63.Fit( self.m_panel37 )
		fgSizer16.Add( self.m_panel37, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_ArtisticA = wx.SpinCtrl( self.m_panel27, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_ArtisticA.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_ArtisticA.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer16.Add( self.m_ArtisticA, 0, wx.ALL, 5 )

		self.m_panel38 = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel38.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_panel38.SetBackgroundColour( wx.Colour( 88, 122, 54 ) )

		bSizer64 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText146 = wx.StaticText( self.m_panel38, wx.ID_ANY, u"Social", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText146.Wrap( -1 )

		self.m_staticText146.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText146.SetForegroundColour( wx.Colour( 249, 250, 249 ) )

		bSizer64.Add( self.m_staticText146, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel38.SetSizer( bSizer64 )
		self.m_panel38.Layout()
		bSizer64.Fit( self.m_panel38 )
		fgSizer16.Add( self.m_panel38, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_SocialA = wx.SpinCtrl( self.m_panel27, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_SocialA.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_SocialA.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer16.Add( self.m_SocialA, 0, wx.ALL, 5 )

		self.m_panel39 = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel39.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_panel39.SetBackgroundColour( wx.Colour( 0, 152, 218 ) )

		bSizer65 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText147 = wx.StaticText( self.m_panel39, wx.ID_ANY, u"Enterprising", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText147.Wrap( -1 )

		self.m_staticText147.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer65.Add( self.m_staticText147, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel39.SetSizer( bSizer65 )
		self.m_panel39.Layout()
		bSizer65.Fit( self.m_panel39 )
		fgSizer16.Add( self.m_panel39, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_EnterprisingA = wx.SpinCtrl( self.m_panel27, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_EnterprisingA.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_EnterprisingA.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer16.Add( self.m_EnterprisingA, 0, wx.ALL, 5 )

		self.m_panel40 = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel40.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_panel40.SetBackgroundColour( wx.Colour( 169, 138, 172 ) )

		bSizer66 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText148 = wx.StaticText( self.m_panel40, wx.ID_ANY, u"Conventional", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText148.Wrap( -1 )

		self.m_staticText148.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer66.Add( self.m_staticText148, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel40.SetSizer( bSizer66 )
		self.m_panel40.Layout()
		bSizer66.Fit( self.m_panel40 )
		fgSizer16.Add( self.m_panel40, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_ConventionalA = wx.SpinCtrl( self.m_panel27, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_ConventionalA.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_ConventionalA.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer16.Add( self.m_ConventionalA, 0, wx.ALL, 5 )


		self.m_panel27.SetSizer( fgSizer16 )
		self.m_panel27.Layout()
		fgSizer16.Fit( self.m_panel27 )
		bSizer52.Add( self.m_panel27, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer28.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer28.Add( ( 25, 0), 0, 0, 5 )

		bSizer53 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel30 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel30.SetBackgroundColour( wx.Colour( 125, 100, 139 ) )

		bSizer58 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText168 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"KOMPETENSI", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.m_staticText168.Wrap( -1 )

		self.m_staticText168.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText168.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer58.Add( self.m_staticText168, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel30.SetSizer( bSizer58 )
		self.m_panel30.Layout()
		bSizer58.Fit( self.m_panel30 )
		bSizer53.Add( self.m_panel30, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		bSizer53.Add( ( 0, 10), 0, 0, 5 )

		self.m_panel31 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel31.SetBackgroundColour( wx.Colour( 125, 100, 139 ) )

		fgSizer161 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer161.SetFlexibleDirection( wx.BOTH )
		fgSizer161.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel34 = wx.Panel( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel34.SetBackgroundColour( wx.Colour( 208, 87, 66 ) )

		bSizer60 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1411 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Realistic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1411.Wrap( -1 )

		self.m_staticText1411.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText1411.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_staticText1411.SetBackgroundColour( wx.Colour( 208, 87, 66 ) )

		bSizer60.Add( self.m_staticText1411, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel34.SetSizer( bSizer60 )
		self.m_panel34.Layout()
		bSizer60.Fit( self.m_panel34 )
		fgSizer161.Add( self.m_panel34, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_RealisticK = wx.SpinCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_RealisticK.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer161.Add( self.m_RealisticK, 0, wx.ALL, 5 )

		self.m_panel41 = wx.Panel( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel41.SetBackgroundColour( wx.Colour( 245, 135, 79 ) )

		bSizer67 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1431 = wx.StaticText( self.m_panel41, wx.ID_ANY, u"Investigative", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1431.Wrap( -1 )

		self.m_staticText1431.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText1431.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer67.Add( self.m_staticText1431, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel41.SetSizer( bSizer67 )
		self.m_panel41.Layout()
		bSizer67.Fit( self.m_panel41 )
		fgSizer161.Add( self.m_panel41, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_InvestigativeK = wx.SpinCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_InvestigativeK.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer161.Add( self.m_InvestigativeK, 0, wx.ALL, 5 )

		self.m_panel42 = wx.Panel( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel42.SetBackgroundColour( wx.Colour( 255, 204, 41 ) )

		bSizer68 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1451 = wx.StaticText( self.m_panel42, wx.ID_ANY, u"Artistic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1451.Wrap( -1 )

		self.m_staticText1451.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText1451.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer68.Add( self.m_staticText1451, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel42.SetSizer( bSizer68 )
		self.m_panel42.Layout()
		bSizer68.Fit( self.m_panel42 )
		fgSizer161.Add( self.m_panel42, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_ArtisticK = wx.SpinCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_ArtisticK.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer161.Add( self.m_ArtisticK, 0, wx.ALL, 5 )

		self.m_panel43 = wx.Panel( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel43.SetBackgroundColour( wx.Colour( 88, 122, 54 ) )

		bSizer69 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1461 = wx.StaticText( self.m_panel43, wx.ID_ANY, u"Social", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1461.Wrap( -1 )

		self.m_staticText1461.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText1461.SetForegroundColour( wx.Colour( 249, 250, 249 ) )

		bSizer69.Add( self.m_staticText1461, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel43.SetSizer( bSizer69 )
		self.m_panel43.Layout()
		bSizer69.Fit( self.m_panel43 )
		fgSizer161.Add( self.m_panel43, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_SocialK = wx.SpinCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_SocialK.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer161.Add( self.m_SocialK, 0, wx.ALL, 5 )

		self.m_panel50 = wx.Panel( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel50.SetBackgroundColour( wx.Colour( 0, 152, 218 ) )

		bSizer76 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1471 = wx.StaticText( self.m_panel50, wx.ID_ANY, u"Enterprising", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1471.Wrap( -1 )

		self.m_staticText1471.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText1471.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer76.Add( self.m_staticText1471, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel50.SetSizer( bSizer76 )
		self.m_panel50.Layout()
		bSizer76.Fit( self.m_panel50 )
		fgSizer161.Add( self.m_panel50, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_EnterprisingK = wx.SpinCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_EnterprisingK.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer161.Add( self.m_EnterprisingK, 0, wx.ALL, 5 )

		self.m_panel44 = wx.Panel( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel44.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_panel44.SetBackgroundColour( wx.Colour( 169, 138, 172 ) )

		bSizer70 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1481 = wx.StaticText( self.m_panel44, wx.ID_ANY, u"Conventional", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1481.Wrap( -1 )

		self.m_staticText1481.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText1481.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer70.Add( self.m_staticText1481, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel44.SetSizer( bSizer70 )
		self.m_panel44.Layout()
		bSizer70.Fit( self.m_panel44 )
		fgSizer161.Add( self.m_panel44, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_ConventionalK = wx.SpinCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_ConventionalK.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer161.Add( self.m_ConventionalK, 0, wx.ALL, 5 )


		self.m_panel31.SetSizer( fgSizer161 )
		self.m_panel31.Layout()
		fgSizer161.Fit( self.m_panel31 )
		bSizer53.Add( self.m_panel31, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer28.Add( bSizer53, 1, wx.EXPAND, 5 )


		bSizer28.Add( ( 25, 0), 0, 0, 5 )

		bSizer54 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel32 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel32.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel32.SetBackgroundColour( wx.Colour( 150, 152, 154 ) )

		bSizer59 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText169 = wx.StaticText( self.m_panel32, wx.ID_ANY, u"PEKERJAAN", wx.Point( -1,-1 ), wx.Size( 100,-1 ), 0 )
		self.m_staticText169.Wrap( -1 )

		self.m_staticText169.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )

		bSizer59.Add( self.m_staticText169, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel32.SetSizer( bSizer59 )
		self.m_panel32.Layout()
		bSizer59.Fit( self.m_panel32 )
		bSizer54.Add( self.m_panel32, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer54.Add( ( 0, 10), 0, 0, 5 )

		self.m_panel33 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel33.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel33.SetBackgroundColour( wx.Colour( 150, 152, 154 ) )

		fgSizer162 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer162.SetFlexibleDirection( wx.BOTH )
		fgSizer162.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel35 = wx.Panel( self.m_panel33, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel35.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel35.SetBackgroundColour( wx.Colour( 208, 87, 66 ) )

		bSizer61 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1412 = wx.StaticText( self.m_panel35, wx.ID_ANY, u"Realistic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1412.Wrap( -1 )

		self.m_staticText1412.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText1412.SetBackgroundColour( wx.Colour( 208, 87, 66 ) )

		bSizer61.Add( self.m_staticText1412, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel35.SetSizer( bSizer61 )
		self.m_panel35.Layout()
		bSizer61.Fit( self.m_panel35 )
		fgSizer162.Add( self.m_panel35, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_RealisticP = wx.SpinCtrl( self.m_panel33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_RealisticP.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_RealisticP.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer162.Add( self.m_RealisticP, 0, wx.ALL, 5 )

		self.m_panel45 = wx.Panel( self.m_panel33, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel45.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel45.SetBackgroundColour( wx.Colour( 245, 135, 79 ) )

		bSizer71 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1432 = wx.StaticText( self.m_panel45, wx.ID_ANY, u"Investigative", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1432.Wrap( -1 )

		self.m_staticText1432.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText1432.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_staticText1432.SetBackgroundColour( wx.Colour( 245, 135, 79 ) )

		bSizer71.Add( self.m_staticText1432, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel45.SetSizer( bSizer71 )
		self.m_panel45.Layout()
		bSizer71.Fit( self.m_panel45 )
		fgSizer162.Add( self.m_panel45, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_InvestigativeP = wx.SpinCtrl( self.m_panel33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_InvestigativeP.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_InvestigativeP.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer162.Add( self.m_InvestigativeP, 0, wx.ALL, 5 )

		self.m_panel49 = wx.Panel( self.m_panel33, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel49.SetBackgroundColour( wx.Colour( 255, 204, 41 ) )

		bSizer75 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1452 = wx.StaticText( self.m_panel49, wx.ID_ANY, u"Artistic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1452.Wrap( -1 )

		self.m_staticText1452.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer75.Add( self.m_staticText1452, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel49.SetSizer( bSizer75 )
		self.m_panel49.Layout()
		bSizer75.Fit( self.m_panel49 )
		fgSizer162.Add( self.m_panel49, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_ArtisticP = wx.SpinCtrl( self.m_panel33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_ArtisticP.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_ArtisticP.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer162.Add( self.m_ArtisticP, 0, wx.ALL, 5 )

		self.m_panel46 = wx.Panel( self.m_panel33, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel46.SetBackgroundColour( wx.Colour( 88, 122, 54 ) )

		bSizer72 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1462 = wx.StaticText( self.m_panel46, wx.ID_ANY, u"Social", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1462.Wrap( -1 )

		self.m_staticText1462.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText1462.SetForegroundColour( wx.Colour( 249, 250, 249 ) )

		bSizer72.Add( self.m_staticText1462, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel46.SetSizer( bSizer72 )
		self.m_panel46.Layout()
		bSizer72.Fit( self.m_panel46 )
		fgSizer162.Add( self.m_panel46, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_SocialP = wx.SpinCtrl( self.m_panel33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_SocialP.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_SocialP.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer162.Add( self.m_SocialP, 0, wx.ALL, 5 )

		self.m_panel47 = wx.Panel( self.m_panel33, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel47.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel47.SetBackgroundColour( wx.Colour( 0, 152, 218 ) )

		bSizer73 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1472 = wx.StaticText( self.m_panel47, wx.ID_ANY, u"Enterprising", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1472.Wrap( -1 )

		self.m_staticText1472.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText1472.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer73.Add( self.m_staticText1472, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel47.SetSizer( bSizer73 )
		self.m_panel47.Layout()
		bSizer73.Fit( self.m_panel47 )
		fgSizer162.Add( self.m_panel47, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_EnterprisingP = wx.SpinCtrl( self.m_panel33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_EnterprisingP.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_EnterprisingP.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer162.Add( self.m_EnterprisingP, 0, wx.ALL, 5 )

		self.m_panel48 = wx.Panel( self.m_panel33, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel48.SetBackgroundColour( wx.Colour( 169, 138, 172 ) )

		bSizer74 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1482 = wx.StaticText( self.m_panel48, wx.ID_ANY, u"Conventional", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1482.Wrap( -1 )

		self.m_staticText1482.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer74.Add( self.m_staticText1482, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel48.SetSizer( bSizer74 )
		self.m_panel48.Layout()
		bSizer74.Fit( self.m_panel48 )
		fgSizer162.Add( self.m_panel48, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_ConventionalP = wx.SpinCtrl( self.m_panel33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 14, 0 )
		self.m_ConventionalP.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_ConventionalP.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer162.Add( self.m_ConventionalP, 0, wx.ALL, 5 )


		self.m_panel33.SetSizer( fgSizer162 )
		self.m_panel33.Layout()
		fgSizer162.Fit( self.m_panel33 )
		bSizer54.Add( self.m_panel33, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer28.Add( bSizer54, 1, wx.EXPAND, 5 )


		bSizer27.Add( bSizer28, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer27 )
		self.Layout()

		# Connect Events
		self.m_InvestigativeA.Bind( wx.EVT_SPINCTRL, self.m_InvestigativeAOnSpinCtrl )
		self.m_ArtisticA.Bind( wx.EVT_SPINCTRL, self.m_spinCtrl3OnSpinCtrl )
		self.m_SocialA.Bind( wx.EVT_SPINCTRL, self.m_SocialAOnSpinCtrl )
		self.m_EnterprisingA.Bind( wx.EVT_SPINCTRL, self.m_EnterprisingAOnSpinCtrl )
		self.m_ConventionalA.Bind( wx.EVT_SPINCTRL, self.m_ConventionalAOnSpinCtrl )
		self.m_RealisticK.Bind( wx.EVT_SPINCTRL, self.m_RealisticKOnSpinCtrl )
		self.m_InvestigativeK.Bind( wx.EVT_SPINCTRL, self.m_InvestigativeKOnSpinCtrl )
		self.m_ArtisticK.Bind( wx.EVT_SPINCTRL, self.m_ArtisticKOnSpinCtrl )
		self.m_SocialK.Bind( wx.EVT_SPINCTRL, self.m_SocialKOnSpinCtrl )
		self.m_EnterprisingK.Bind( wx.EVT_SPINCTRL, self.m_EnterprisingKOnSpinCtrl )
		self.m_ConventionalK.Bind( wx.EVT_SPINCTRL, self.m_ConventionalKOnSpinCtrl )
		self.m_RealisticP.Bind( wx.EVT_SPINCTRL, self.m_RealisticPOnSpinCtrl )
		self.m_InvestigativeP.Bind( wx.EVT_SPINCTRL, self.m_InvestigativePOnSpinCtrl )
		self.m_ArtisticP.Bind( wx.EVT_SPINCTRL, self.m_ArtisticPOnSpinCtrl )
		self.m_SocialP.Bind( wx.EVT_SPINCTRL, self.m_SocialPOnSpinCtrl )
		self.m_EnterprisingP.Bind( wx.EVT_SPINCTRL, self.m_EnterprisingPOnSpinCtrl )
		self.m_ConventionalP.Bind( wx.EVT_SPINCTRL, self.m_ConventionalPOnSpinCtrl )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_InvestigativeAOnSpinCtrl( self, event ):
		event.Skip()

	def m_spinCtrl3OnSpinCtrl( self, event ):
		event.Skip()

	def m_SocialAOnSpinCtrl( self, event ):
		event.Skip()

	def m_EnterprisingAOnSpinCtrl( self, event ):
		event.Skip()

	def m_ConventionalAOnSpinCtrl( self, event ):
		event.Skip()

	def m_RealisticKOnSpinCtrl( self, event ):
		event.Skip()

	def m_InvestigativeKOnSpinCtrl( self, event ):
		event.Skip()

	def m_ArtisticKOnSpinCtrl( self, event ):
		event.Skip()

	def m_SocialKOnSpinCtrl( self, event ):
		event.Skip()

	def m_EnterprisingKOnSpinCtrl( self, event ):
		event.Skip()

	def m_ConventionalKOnSpinCtrl( self, event ):
		event.Skip()

	def m_RealisticPOnSpinCtrl( self, event ):
		event.Skip()

	def m_InvestigativePOnSpinCtrl( self, event ):
		event.Skip()

	def m_ArtisticPOnSpinCtrl( self, event ):
		event.Skip()

	def m_SocialPOnSpinCtrl( self, event ):
		event.Skip()

	def m_EnterprisingPOnSpinCtrl( self, event ):
		event.Skip()

	def m_ConventionalPOnSpinCtrl( self, event ):
		event.Skip()


###########################################################################
## Class Page4
###########################################################################

class Page4 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1200,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )


		bSizer33.Add( ( 0, 75), 0, 0, 5 )

		self.m_staticText203 = wx.StaticText( self, wx.ID_ANY, u"PENILAIAN DIRI ANDA", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText203.Wrap( -1 )

		self.m_staticText203.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )

		bSizer33.Add( self.m_staticText203, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer33.Add( ( 0, 25), 0, 0, 5 )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel831 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel831.SetBackgroundColour( wx.Colour( 212, 113, 73 ) )

		bSizer1061 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText204 = wx.StaticText( self.m_panel831, wx.ID_ANY, u"BAGIAN 1", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText204.Wrap( -1 )

		self.m_staticText204.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText204.SetForegroundColour( wx.Colour( 249, 250, 249 ) )

		bSizer1061.Add( self.m_staticText204, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel831.SetSizer( bSizer1061 )
		self.m_panel831.Layout()
		bSizer1061.Fit( self.m_panel831 )
		bSizer34.Add( self.m_panel831, 1, wx.EXPAND |wx.ALL, 5 )

		fgSizer27 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer27.SetFlexibleDirection( wx.BOTH )
		fgSizer27.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer29 = wx.FlexGridSizer( 0, 7, 0, 0 )
		fgSizer29.SetFlexibleDirection( wx.BOTH )
		fgSizer29.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText213 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText213.Wrap( -1 )

		self.m_staticText213.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		fgSizer29.Add( self.m_staticText213, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel57 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel57.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel57.SetBackgroundColour( wx.Colour( 208, 87, 66 ) )

		bSizer81 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText214 = wx.StaticText( self.m_panel57, wx.ID_ANY, u"Kemampuan\n    Mekanis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText214.Wrap( -1 )

		self.m_staticText214.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer81.Add( self.m_staticText214, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel57.SetSizer( bSizer81 )
		self.m_panel57.Layout()
		bSizer81.Fit( self.m_panel57 )
		fgSizer29.Add( self.m_panel57, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel59 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel59.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel59.SetBackgroundColour( wx.Colour( 245, 135, 79 ) )

		bSizer83 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText215 = wx.StaticText( self.m_panel59, wx.ID_ANY, u"Kemampuan\n     Ilmiah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText215.Wrap( -1 )

		self.m_staticText215.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer83.Add( self.m_staticText215, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel59.SetSizer( bSizer83 )
		self.m_panel59.Layout()
		bSizer83.Fit( self.m_panel59 )
		fgSizer29.Add( self.m_panel59, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel60 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel60.SetBackgroundColour( wx.Colour( 255, 204, 41 ) )

		bSizer84 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText216 = wx.StaticText( self.m_panel60, wx.ID_ANY, u"Kemampuan\n     Artistik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText216.Wrap( -1 )

		self.m_staticText216.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer84.Add( self.m_staticText216, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel60.SetSizer( bSizer84 )
		self.m_panel60.Layout()
		bSizer84.Fit( self.m_panel60 )
		fgSizer29.Add( self.m_panel60, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel61 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel61.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel61.SetBackgroundColour( wx.Colour( 88, 122, 54 ) )

		bSizer85 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText217 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"Kemampuan\n   Mengajar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText217.Wrap( -1 )

		self.m_staticText217.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer85.Add( self.m_staticText217, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel61.SetSizer( bSizer85 )
		self.m_panel61.Layout()
		bSizer85.Fit( self.m_panel61 )
		fgSizer29.Add( self.m_panel61, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel62 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel62.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel62.SetBackgroundColour( wx.Colour( 0, 88, 218 ) )

		bSizer86 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText218 = wx.StaticText( self.m_panel62, wx.ID_ANY, u"Kemampuan\n   Penjualan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText218.Wrap( -1 )

		self.m_staticText218.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText218.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_staticText218.SetBackgroundColour( wx.Colour( 0, 88, 218 ) )

		bSizer86.Add( self.m_staticText218, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel62.SetSizer( bSizer86 )
		self.m_panel62.Layout()
		bSizer86.Fit( self.m_panel62 )
		fgSizer29.Add( self.m_panel62, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel63 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel63.SetBackgroundColour( wx.Colour( 169, 138, 172 ) )

		bSizer87 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText219 = wx.StaticText( self.m_panel63, wx.ID_ANY, u"Kemampuan\nAdministrasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText219.Wrap( -1 )

		self.m_staticText219.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer87.Add( self.m_staticText219, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel63.SetSizer( bSizer87 )
		self.m_panel63.Layout()
		bSizer87.Fit( self.m_panel63 )
		fgSizer29.Add( self.m_panel63, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel64 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel64.SetBackgroundColour( wx.Colour( 210, 211, 5 ) )

		bSizer88 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText221 = wx.StaticText( self.m_panel64, wx.ID_ANY, u"Tingkat (1-7)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )

		self.m_staticText221.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer88.Add( self.m_staticText221, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel64.SetSizer( bSizer88 )
		self.m_panel64.Layout()
		bSizer88.Fit( self.m_panel64 )
		fgSizer29.Add( self.m_panel64, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_panel65 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel65.SetBackgroundColour( wx.Colour( 208, 87, 66 ) )

		bSizer89 = wx.BoxSizer( wx.VERTICAL )

		self.m_kmekanisb1 = wx.SpinCtrl( self.m_panel65, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 7, 0 )
		self.m_kmekanisb1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer89.Add( self.m_kmekanisb1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel65.SetSizer( bSizer89 )
		self.m_panel65.Layout()
		bSizer89.Fit( self.m_panel65 )
		fgSizer29.Add( self.m_panel65, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel66 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel66.SetBackgroundColour( wx.Colour( 245, 135, 79 ) )

		bSizer90 = wx.BoxSizer( wx.VERTICAL )

		self.m_kilmiahb1 = wx.SpinCtrl( self.m_panel66, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 7, 0 )
		self.m_kilmiahb1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer90.Add( self.m_kilmiahb1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel66.SetSizer( bSizer90 )
		self.m_panel66.Layout()
		bSizer90.Fit( self.m_panel66 )
		fgSizer29.Add( self.m_panel66, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel67 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel67.SetBackgroundColour( wx.Colour( 255, 204, 41 ) )

		bSizer91 = wx.BoxSizer( wx.VERTICAL )

		self.m_kartistikb1 = wx.SpinCtrl( self.m_panel67, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 7, 0 )
		self.m_kartistikb1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer91.Add( self.m_kartistikb1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel67.SetSizer( bSizer91 )
		self.m_panel67.Layout()
		bSizer91.Fit( self.m_panel67 )
		fgSizer29.Add( self.m_panel67, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel68 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel68.SetBackgroundColour( wx.Colour( 88, 122, 54 ) )

		bSizer92 = wx.BoxSizer( wx.VERTICAL )

		self.m_kmengajarb1 = wx.SpinCtrl( self.m_panel68, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 7, 0 )
		self.m_kmengajarb1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer92.Add( self.m_kmengajarb1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel68.SetSizer( bSizer92 )
		self.m_panel68.Layout()
		bSizer92.Fit( self.m_panel68 )
		fgSizer29.Add( self.m_panel68, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel69 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel69.SetBackgroundColour( wx.Colour( 0, 88, 218 ) )

		bSizer93 = wx.BoxSizer( wx.VERTICAL )

		self.m_kpenjualanb1 = wx.SpinCtrl( self.m_panel69, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 7, 0 )
		self.m_kpenjualanb1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer93.Add( self.m_kpenjualanb1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel69.SetSizer( bSizer93 )
		self.m_panel69.Layout()
		bSizer93.Fit( self.m_panel69 )
		fgSizer29.Add( self.m_panel69, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel70 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel70.SetBackgroundColour( wx.Colour( 169, 138, 172 ) )

		bSizer94 = wx.BoxSizer( wx.VERTICAL )

		self.m_kadministrasib1 = wx.SpinCtrl( self.m_panel70, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 7, 0 )
		self.m_kadministrasib1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer94.Add( self.m_kadministrasib1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel70.SetSizer( bSizer94 )
		self.m_panel70.Layout()
		bSizer94.Fit( self.m_panel70 )
		fgSizer29.Add( self.m_panel70, 1, wx.EXPAND |wx.ALL, 5 )


		fgSizer27.Add( fgSizer29, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer34.Add( fgSizer27, 0, 0, 5 )


		bSizer33.Add( bSizer34, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer33.Add( ( 0, 5), 0, 0, 5 )

		bSizer154 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap_hal4 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer154.Add( self.m_bitmap_hal4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer33.Add( bSizer154, 0, wx.EXPAND, 5 )


		bSizer33.Add( ( 0, 5), 0, 0, 5 )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel84 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel84.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel84.SetBackgroundColour( wx.Colour( 214, 145, 56 ) )

		bSizer107 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText205 = wx.StaticText( self.m_panel84, wx.ID_ANY, u"BAGIAN 2", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText205.Wrap( -1 )

		self.m_staticText205.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText205.SetBackgroundColour( wx.Colour( 214, 145, 56 ) )

		bSizer107.Add( self.m_staticText205, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel84.SetSizer( bSizer107 )
		self.m_panel84.Layout()
		bSizer107.Fit( self.m_panel84 )
		bSizer35.Add( self.m_panel84, 1, wx.EXPAND |wx.ALL, 5 )

		fgSizer291 = wx.FlexGridSizer( 0, 7, 0, 0 )
		fgSizer291.SetFlexibleDirection( wx.BOTH )
		fgSizer291.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2131 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2131.Wrap( -1 )

		fgSizer291.Add( self.m_staticText2131, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_panel71 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel71.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel71.SetBackgroundColour( wx.Colour( 208, 87, 66 ) )

		bSizer95 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2141 = wx.StaticText( self.m_panel71, wx.ID_ANY, u"Keterampilan \n     Tangan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2141.Wrap( -1 )

		self.m_staticText2141.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer95.Add( self.m_staticText2141, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel71.SetSizer( bSizer95 )
		self.m_panel71.Layout()
		bSizer95.Fit( self.m_panel71 )
		fgSizer291.Add( self.m_panel71, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel72 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel72.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel72.SetBackgroundColour( wx.Colour( 245, 135, 79 ) )

		bSizer96 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2151 = wx.StaticText( self.m_panel72, wx.ID_ANY, u"Kemampuan \n Matematika", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2151.Wrap( -1 )

		self.m_staticText2151.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText2151.SetBackgroundColour( wx.Colour( 245, 135, 79 ) )

		bSizer96.Add( self.m_staticText2151, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel72.SetSizer( bSizer96 )
		self.m_panel72.Layout()
		bSizer96.Fit( self.m_panel72 )
		fgSizer291.Add( self.m_panel72, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel73 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel73.SetBackgroundColour( wx.Colour( 255, 204, 41 ) )

		bSizer97 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2161 = wx.StaticText( self.m_panel73, wx.ID_ANY, u"Kemampuan \n      Musik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2161.Wrap( -1 )

		self.m_staticText2161.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText2161.SetBackgroundColour( wx.Colour( 255, 204, 41 ) )

		bSizer97.Add( self.m_staticText2161, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel73.SetSizer( bSizer97 )
		self.m_panel73.Layout()
		bSizer97.Fit( self.m_panel73 )
		fgSizer291.Add( self.m_panel73, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel74 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel74.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel74.SetBackgroundColour( wx.Colour( 88, 122, 54 ) )

		bSizer98 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2171 = wx.StaticText( self.m_panel74, wx.ID_ANY, u"Memahami\nOrang Lain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2171.Wrap( -1 )

		self.m_staticText2171.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText2171.SetBackgroundColour( wx.Colour( 88, 122, 54 ) )

		bSizer98.Add( self.m_staticText2171, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel74.SetSizer( bSizer98 )
		self.m_panel74.Layout()
		bSizer98.Fit( self.m_panel74 )
		fgSizer291.Add( self.m_panel74, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel75 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel75.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel75.SetBackgroundColour( wx.Colour( 0, 88, 218 ) )

		bSizer99 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2181 = wx.StaticText( self.m_panel75, wx.ID_ANY, u"Keterampilan \n   Manajerial", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2181.Wrap( -1 )

		self.m_staticText2181.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText2181.SetBackgroundColour( wx.Colour( 0, 88, 218 ) )

		bSizer99.Add( self.m_staticText2181, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel75.SetSizer( bSizer99 )
		self.m_panel75.Layout()
		bSizer99.Fit( self.m_panel75 )
		fgSizer291.Add( self.m_panel75, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel76 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel76.SetBackgroundColour( wx.Colour( 169, 138, 172 ) )

		bSizer100 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2191 = wx.StaticText( self.m_panel76, wx.ID_ANY, u"Kemampuan \nPerkantoran", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2191.Wrap( -1 )

		self.m_staticText2191.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_staticText2191.SetBackgroundColour( wx.Colour( 169, 138, 172 ) )

		bSizer100.Add( self.m_staticText2191, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel76.SetSizer( bSizer100 )
		self.m_panel76.Layout()
		bSizer100.Fit( self.m_panel76 )
		fgSizer291.Add( self.m_panel76, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel77 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel77.SetBackgroundColour( wx.Colour( 210, 211, 5 ) )

		bSizer101 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2211 = wx.StaticText( self.m_panel77, wx.ID_ANY, u"Tingkat (1-7)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2211.Wrap( -1 )

		self.m_staticText2211.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer101.Add( self.m_staticText2211, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel77.SetSizer( bSizer101 )
		self.m_panel77.Layout()
		bSizer101.Fit( self.m_panel77 )
		fgSizer291.Add( self.m_panel77, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_panel78 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel78.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel78.SetBackgroundColour( wx.Colour( 208, 87, 66 ) )

		bSizer103 = wx.BoxSizer( wx.VERTICAL )

		self.m_ktanganb2 = wx.SpinCtrl( self.m_panel78, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 7, 0 )
		self.m_ktanganb2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_ktanganb2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer103.Add( self.m_ktanganb2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel78.SetSizer( bSizer103 )
		self.m_panel78.Layout()
		bSizer103.Fit( self.m_panel78 )
		fgSizer291.Add( self.m_panel78, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel79 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel79.SetBackgroundColour( wx.Colour( 245, 135, 79 ) )

		bSizer104 = wx.BoxSizer( wx.VERTICAL )

		self.m_kmatematikab2 = wx.SpinCtrl( self.m_panel79, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 7, 0 )
		self.m_kmatematikab2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer104.Add( self.m_kmatematikab2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel79.SetSizer( bSizer104 )
		self.m_panel79.Layout()
		bSizer104.Fit( self.m_panel79 )
		fgSizer291.Add( self.m_panel79, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel80 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel80.SetBackgroundColour( wx.Colour( 255, 204, 41 ) )

		bSizer105 = wx.BoxSizer( wx.VERTICAL )

		self.m_kmusikb2 = wx.SpinCtrl( self.m_panel80, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 7, 0 )
		self.m_kmusikb2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer105.Add( self.m_kmusikb2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel80.SetSizer( bSizer105 )
		self.m_panel80.Layout()
		bSizer105.Fit( self.m_panel80 )
		fgSizer291.Add( self.m_panel80, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel81 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel81.SetBackgroundColour( wx.Colour( 88, 122, 54 ) )

		bSizer109 = wx.BoxSizer( wx.VERTICAL )

		self.m_moranglainb2 = wx.SpinCtrl( self.m_panel81, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 7, 0 )
		self.m_moranglainb2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer109.Add( self.m_moranglainb2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel81.SetSizer( bSizer109 )
		self.m_panel81.Layout()
		bSizer109.Fit( self.m_panel81 )
		fgSizer291.Add( self.m_panel81, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel82 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel82.SetBackgroundColour( wx.Colour( 0, 88, 218 ) )

		bSizer108 = wx.BoxSizer( wx.VERTICAL )

		self.m_kmanajerialb2 = wx.SpinCtrl( self.m_panel82, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 7, 0 )
		self.m_kmanajerialb2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer108.Add( self.m_kmanajerialb2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel82.SetSizer( bSizer108 )
		self.m_panel82.Layout()
		bSizer108.Fit( self.m_panel82 )
		fgSizer291.Add( self.m_panel82, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel83 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel83.SetBackgroundColour( wx.Colour( 169, 138, 172 ) )

		bSizer106 = wx.BoxSizer( wx.VERTICAL )

		self.m_kperkantoranb2 = wx.SpinCtrl( self.m_panel83, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.SP_ARROW_KEYS, 0, 7, 0 )
		self.m_kperkantoranb2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		bSizer106.Add( self.m_kperkantoranb2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel83.SetSizer( bSizer106 )
		self.m_panel83.Layout()
		bSizer106.Fit( self.m_panel83 )
		fgSizer291.Add( self.m_panel83, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer35.Add( fgSizer291, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer33.Add( bSizer35, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer33 )
		self.Layout()

		# Connect Events
		self.m_kmekanisb1.Bind( wx.EVT_SPINCTRL, self.m_kmekanisb1OnSpinCtrl )
		self.m_kilmiahb1.Bind( wx.EVT_SPINCTRL, self.m_kilmiahb1OnSpinCtrl )
		self.m_kartistikb1.Bind( wx.EVT_SPINCTRL, self.m_kartistikb1OnSpinCtrl )
		self.m_kmengajarb1.Bind( wx.EVT_SPINCTRL, self.m_kmengajarb1OnSpinCtrl )
		self.m_kpenjualanb1.Bind( wx.EVT_SPINCTRL, self.m_kpenjualanb1OnSpinCtrl )
		self.m_kadministrasib1.Bind( wx.EVT_SPINCTRL, self.m_kadministrasib1OnSpinCtrl )
		self.m_ktanganb2.Bind( wx.EVT_SPINCTRL, self.m_ktanganb2OnSpinCtrl )
		self.m_kmatematikab2.Bind( wx.EVT_SPINCTRL, self.m_kmatematikab2OnSpinCtrl )
		self.m_kmusikb2.Bind( wx.EVT_SPINCTRL, self.m_kmusikb2OnSpinCtrl )
		self.m_moranglainb2.Bind( wx.EVT_SPINCTRL, self.m_moranglainb2OnSpinCtrl )
		self.m_kmanajerialb2.Bind( wx.EVT_SPINCTRL, self.m_kmanajerialb2OnSpinCtrl )
		self.m_kperkantoranb2.Bind( wx.EVT_SPINCTRL, self.m_kperkantoranb2OnSpinCtrl )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_kmekanisb1OnSpinCtrl( self, event ):
		event.Skip()

	def m_kilmiahb1OnSpinCtrl( self, event ):
		event.Skip()

	def m_kartistikb1OnSpinCtrl( self, event ):
		event.Skip()

	def m_kmengajarb1OnSpinCtrl( self, event ):
		event.Skip()

	def m_kpenjualanb1OnSpinCtrl( self, event ):
		event.Skip()

	def m_kadministrasib1OnSpinCtrl( self, event ):
		event.Skip()

	def m_ktanganb2OnSpinCtrl( self, event ):
		event.Skip()

	def m_kmatematikab2OnSpinCtrl( self, event ):
		event.Skip()

	def m_kmusikb2OnSpinCtrl( self, event ):
		event.Skip()

	def m_moranglainb2OnSpinCtrl( self, event ):
		event.Skip()

	def m_kmanajerialb2OnSpinCtrl( self, event ):
		event.Skip()

	def m_kperkantoranb2OnSpinCtrl( self, event ):
		event.Skip()


###########################################################################
## Class Page5
###########################################################################

class Page5 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )


		bSizer32.Add( ( 0, 10), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText193 = wx.StaticText( self, wx.ID_ANY, u"MENGORGANISIR JAWABAN", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText193.Wrap( -1 )

		self.m_staticText193.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )

		bSizer32.Add( self.m_staticText193, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer45 = wx.BoxSizer( wx.VERTICAL )

		fgSizer26 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer26.AddGrowableRow( 0 )
		fgSizer26.SetFlexibleDirection( wx.BOTH )
		fgSizer26.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_tombolHitung = wx.Button( self, wx.ID_ANY, u"Hitung", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_tombolHitung.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_tombolHitung.SetBackgroundColour( wx.Colour( 249, 250, 249 ) )

		fgSizer26.Add( self.m_tombolHitung, 0, wx.ALL, 5 )


		fgSizer26.Add( ( 800, 0), 1, wx.EXPAND, 5 )

		self.m_bitmap_hal5 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer26.Add( self.m_bitmap_hal5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_tampilgrafik = wx.Button( self, wx.ID_ANY, u"Detail Grafik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_tampilgrafik.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer26.Add( self.m_tampilgrafik, 0, wx.ALL, 5 )

		self.m_grafikproperties = wx.Button( self, wx.ID_ANY, u"Print Grafik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_grafikproperties.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer26.Add( self.m_grafikproperties, 0, wx.ALL, 5 )


		bSizer45.Add( fgSizer26, 0, wx.EXPAND, 5 )

		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		fgSizer31 = wx.FlexGridSizer( 2, 6, 0, 0 )
		fgSizer31.AddGrowableCol( 0 )
		fgSizer31.AddGrowableCol( 1 )
		fgSizer31.AddGrowableCol( 2 )
		fgSizer31.AddGrowableCol( 3 )
		fgSizer31.AddGrowableCol( 4 )
		fgSizer31.AddGrowableCol( 5 )
		fgSizer31.AddGrowableRow( 1 )
		fgSizer31.SetFlexibleDirection( wx.BOTH )
		fgSizer31.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer31.SetMinSize( wx.Size( -1,200 ) )
		self.m_panel51 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 175,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel51.SetBackgroundColour( wx.Colour( 88, 85, 112 ) )

		fgSizer30 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer30.AddGrowableCol( 1 )
		fgSizer30.AddGrowableRow( 0 )
		fgSizer30.SetFlexibleDirection( wx.BOTH )
		fgSizer30.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_aktivitas = wx.StaticText( self.m_panel51, wx.ID_ANY, u"Aktivitas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_aktivitas.Wrap( -1 )

		self.m_aktivitas.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_aktivitas.SetForegroundColour( wx.Colour( 249, 250, 249 ) )

		fgSizer30.Add( self.m_aktivitas, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_buttonDetailA = wx.Button( self.m_panel51, wx.ID_ANY, u"Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonDetailA.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer30.Add( self.m_buttonDetailA, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )


		self.m_panel51.SetSizer( fgSizer30 )
		self.m_panel51.Layout()
		fgSizer31.Add( self.m_panel51, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel54 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 175,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel54.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel54.SetBackgroundColour( wx.Colour( 125, 100, 139 ) )

		fgSizer311 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer311.AddGrowableCol( 1 )
		fgSizer311.AddGrowableRow( 0 )
		fgSizer311.SetFlexibleDirection( wx.BOTH )
		fgSizer311.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_kompetensi = wx.StaticText( self.m_panel54, wx.ID_ANY, u"Kompetensi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_kompetensi.Wrap( -1 )

		self.m_kompetensi.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer311.Add( self.m_kompetensi, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_buttonDetailK = wx.Button( self.m_panel54, wx.ID_ANY, u"Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonDetailK.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer311.Add( self.m_buttonDetailK, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		self.m_panel54.SetSizer( fgSizer311 )
		self.m_panel54.Layout()
		fgSizer31.Add( self.m_panel54, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel55 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 175,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel55.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel55.SetBackgroundColour( wx.Colour( 150, 152, 154 ) )

		fgSizer32 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer32.AddGrowableCol( 1 )
		fgSizer32.AddGrowableRow( 0 )
		fgSizer32.SetFlexibleDirection( wx.BOTH )
		fgSizer32.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_Pekerjaan = wx.StaticText( self.m_panel55, wx.ID_ANY, u"Pekerjaan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Pekerjaan.Wrap( -1 )

		self.m_Pekerjaan.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer32.Add( self.m_Pekerjaan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_buttonDetailP = wx.Button( self.m_panel55, wx.ID_ANY, u"Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonDetailP.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer32.Add( self.m_buttonDetailP, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_panel55.SetSizer( fgSizer32 )
		self.m_panel55.Layout()
		fgSizer31.Add( self.m_panel55, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel86 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel86.SetBackgroundColour( wx.Colour( 212, 113, 73 ) )

		fgSizer33 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer33.AddGrowableCol( 1 )
		fgSizer33.AddGrowableRow( 0 )
		fgSizer33.SetFlexibleDirection( wx.BOTH )
		fgSizer33.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_pdiribag1 = wx.StaticText( self.m_panel86, wx.ID_ANY, u"Penilaian Diri\n    Bagian 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_pdiribag1.Wrap( -1 )

		self.m_pdiribag1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer33.Add( self.m_pdiribag1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_buttonDetailPD1 = wx.Button( self.m_panel86, wx.ID_ANY, u"Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonDetailPD1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer33.Add( self.m_buttonDetailPD1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_panel86.SetSizer( fgSizer33 )
		self.m_panel86.Layout()
		fgSizer33.Fit( self.m_panel86 )
		fgSizer31.Add( self.m_panel86, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel88 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel88.SetBackgroundColour( wx.Colour( 214, 145, 56 ) )

		bSizer110 = wx.BoxSizer( wx.VERTICAL )

		fgSizer34 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer34.AddGrowableCol( 1 )
		fgSizer34.AddGrowableRow( 0 )
		fgSizer34.SetFlexibleDirection( wx.BOTH )
		fgSizer34.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_pdiribag2 = wx.StaticText( self.m_panel88, wx.ID_ANY, u"Penilaian Diri \n    Bagian 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_pdiribag2.Wrap( -1 )

		self.m_pdiribag2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer34.Add( self.m_pdiribag2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_buttonDetailPD2 = wx.Button( self.m_panel88, wx.ID_ANY, u"Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonDetailPD2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer34.Add( self.m_buttonDetailPD2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer110.Add( fgSizer34, 0, 0, 5 )


		self.m_panel88.SetSizer( bSizer110 )
		self.m_panel88.Layout()
		fgSizer31.Add( self.m_panel88, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel90 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel90.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel90.SetBackgroundColour( wx.Colour( 88, 85, 112 ) )

		bSizer112 = wx.BoxSizer( wx.VERTICAL )

		fgSizer36 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer36.AddGrowableCol( 0 )
		fgSizer36.AddGrowableRow( 0 )
		fgSizer36.SetFlexibleDirection( wx.BOTH )
		fgSizer36.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_summaryscores = wx.StaticText( self.m_panel90, wx.ID_ANY, u"Summary Scores", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_summaryscores.Wrap( -1 )

		self.m_summaryscores.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer36.Add( self.m_summaryscores, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer112.Add( fgSizer36, 1, wx.EXPAND, 5 )


		self.m_panel90.SetSizer( bSizer112 )
		self.m_panel90.Layout()
		bSizer112.Fit( self.m_panel90 )
		fgSizer31.Add( self.m_panel90, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_panel52 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel52.SetBackgroundColour( wx.Colour( 88, 85, 112 ) )

		bSizer78 = wx.BoxSizer( wx.VERTICAL )

		m_lbaktivitasChoices = []
		self.m_lbaktivitas = wx.ListBox( self.m_panel52, wx.ID_ANY, wx.DefaultPosition, wx.Size( 175,100 ), m_lbaktivitasChoices, wx.LB_ALWAYS_SB )
		self.m_lbaktivitas.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_lbaktivitas.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_lbaktivitas.SetBackgroundColour( wx.Colour( 88, 85, 112 ) )

		bSizer78.Add( self.m_lbaktivitas, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel52.SetSizer( bSizer78 )
		self.m_panel52.Layout()
		bSizer78.Fit( self.m_panel52 )
		fgSizer31.Add( self.m_panel52, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel53 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel53.SetBackgroundColour( wx.Colour( 125, 100, 139 ) )

		bSizer79 = wx.BoxSizer( wx.VERTICAL )

		m_lbkompetensiChoices = []
		self.m_lbkompetensi = wx.ListBox( self.m_panel53, wx.ID_ANY, wx.DefaultPosition, wx.Size( 175,100 ), m_lbkompetensiChoices, wx.LB_ALWAYS_SB )
		self.m_lbkompetensi.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_lbkompetensi.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_lbkompetensi.SetBackgroundColour( wx.Colour( 125, 100, 139 ) )

		bSizer79.Add( self.m_lbkompetensi, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel53.SetSizer( bSizer79 )
		self.m_panel53.Layout()
		bSizer79.Fit( self.m_panel53 )
		fgSizer31.Add( self.m_panel53, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel56 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel56.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel56.SetBackgroundColour( wx.Colour( 150, 152, 154 ) )

		bSizer80 = wx.BoxSizer( wx.VERTICAL )

		m_lbpekerjaanChoices = []
		self.m_lbpekerjaan = wx.ListBox( self.m_panel56, wx.ID_ANY, wx.DefaultPosition, wx.Size( 175,100 ), m_lbpekerjaanChoices, wx.LB_ALWAYS_SB )
		self.m_lbpekerjaan.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_lbpekerjaan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_lbpekerjaan.SetBackgroundColour( wx.Colour( 150, 152, 154 ) )

		bSizer80.Add( self.m_lbpekerjaan, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel56.SetSizer( bSizer80 )
		self.m_panel56.Layout()
		bSizer80.Fit( self.m_panel56 )
		fgSizer31.Add( self.m_panel56, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel85 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel85.SetBackgroundColour( wx.Colour( 212, 113, 73 ) )

		bSizer108 = wx.BoxSizer( wx.VERTICAL )

		m_lbpenilaianbag1Choices = []
		self.m_lbpenilaianbag1 = wx.ListBox( self.m_panel85, wx.ID_ANY, wx.DefaultPosition, wx.Size( 175,100 ), m_lbpenilaianbag1Choices, wx.LB_ALWAYS_SB )
		self.m_lbpenilaianbag1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_lbpenilaianbag1.SetBackgroundColour( wx.Colour( 212, 113, 73 ) )

		bSizer108.Add( self.m_lbpenilaianbag1, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel85.SetSizer( bSizer108 )
		self.m_panel85.Layout()
		bSizer108.Fit( self.m_panel85 )
		fgSizer31.Add( self.m_panel85, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel87 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel87.SetBackgroundColour( wx.Colour( 214, 145, 56 ) )

		bSizer109 = wx.BoxSizer( wx.VERTICAL )

		m_lbpenilaianbag2Choices = []
		self.m_lbpenilaianbag2 = wx.ListBox( self.m_panel87, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,100 ), m_lbpenilaianbag2Choices, wx.LB_ALWAYS_SB )
		self.m_lbpenilaianbag2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_lbpenilaianbag2.SetBackgroundColour( wx.Colour( 214, 145, 56 ) )

		bSizer109.Add( self.m_lbpenilaianbag2, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel87.SetSizer( bSizer109 )
		self.m_panel87.Layout()
		fgSizer31.Add( self.m_panel87, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel89 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel89.SetBackgroundColour( wx.Colour( 88, 85, 112 ) )

		bSizer111 = wx.BoxSizer( wx.VERTICAL )

		m_lbsummaryscoresChoices = []
		self.m_lbsummaryscores = wx.ListBox( self.m_panel89, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,100 ), m_lbsummaryscoresChoices, wx.LB_ALWAYS_SB )
		self.m_lbsummaryscores.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_lbsummaryscores.SetBackgroundColour( wx.Colour( 88, 85, 112 ) )

		bSizer111.Add( self.m_lbsummaryscores, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel89.SetSizer( bSizer111 )
		self.m_panel89.Layout()
		bSizer111.Fit( self.m_panel89 )
		fgSizer31.Add( self.m_panel89, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer44.Add( fgSizer31, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		from AppsSDS.MplotLib import MatplotPanelA

		self.m_plota=MatplotPanelA(self)
		self.m_plota.canvas.mpl_connect('motion_notify_event', self.onMotion)

		bSizer44.Add( self.m_plota, 1, wx.ALL|wx.EXPAND, 5 )

		from AppsSDS.MplotLib import MatplotPanelB

		self.m_plotb=MatplotPanelB(self)
		self.m_plotb.canvas.mpl_connect('motion_notify_event', self.onMotion)

		self.m_plotb.Hide()

		bSizer44.Add( self.m_plotb, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer45.Add( bSizer44, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer32.Add( bSizer45, 1, wx.EXPAND, 5 )

		self.m_scrolledWindow9 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow9.SetScrollRate( 5, 5 )
		self.m_scrolledWindow9.Hide()

		bSizer32.Add( self.m_scrolledWindow9, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer32 )
		self.Layout()
		bSizer32.Fit( self )

		# Connect Events
		self.m_tombolHitung.Bind( wx.EVT_BUTTON, self.m_tombolHitungOnButtonClick )
		self.m_tampilgrafik.Bind( wx.EVT_BUTTON, self.m_tampilgrafikOnButtonClick )
		self.m_grafikproperties.Bind( wx.EVT_BUTTON, self.m_grafikpropertiesOnButtonClick )
		self.m_buttonDetailA.Bind( wx.EVT_BUTTON, self.m_buttonDetailAOnButtonClick )
		self.m_buttonDetailK.Bind( wx.EVT_BUTTON, self.m_buttonDetailKOnButtonClick )
		self.m_buttonDetailP.Bind( wx.EVT_BUTTON, self.m_buttonDetailPOnButtonClick )
		self.m_buttonDetailPD1.Bind( wx.EVT_BUTTON, self.m_buttonDetailPD1OnButtonClick )
		self.m_buttonDetailPD2.Bind( wx.EVT_BUTTON, self.m_buttonDetailPD2OnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_tombolHitungOnButtonClick( self, event ):
		event.Skip()

	def m_tampilgrafikOnButtonClick( self, event ):
		event.Skip()

	def m_grafikpropertiesOnButtonClick( self, event ):
		event.Skip()

	def m_buttonDetailAOnButtonClick( self, event ):
		event.Skip()

	def m_buttonDetailKOnButtonClick( self, event ):
		event.Skip()

	def m_buttonDetailPOnButtonClick( self, event ):
		event.Skip()

	def m_buttonDetailPD1OnButtonClick( self, event ):
		event.Skip()

	def m_buttonDetailPD2OnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Page6
###########################################################################

class Page6 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 567,467 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap_hal6 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_bitmap_hal6, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer32.Add( ( 0, 75), 0, 0, 5 )

		fgSizer28 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer28.AddGrowableRow( 0 )
		fgSizer28.SetFlexibleDirection( wx.BOTH )
		fgSizer28.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText195 = wx.StaticText( self, wx.ID_ANY, u"KESIMPULAN TIPE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText195.Wrap( -1 )

		self.m_staticText195.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )

		fgSizer28.Add( self.m_staticText195, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panelWarnaHasil = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelWarnaHasil.SetBackgroundColour( wx.Colour( 219, 227, 37 ) )

		bSizer48 = wx.BoxSizer( wx.VERTICAL )

		self.m_stHasil1 = wx.StaticText( self.m_panelWarnaHasil, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_stHasil1.Wrap( -1 )

		self.m_stHasil1.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_stHasil1.SetBackgroundColour( wx.Colour( 93, 218, 193 ) )

		bSizer48.Add( self.m_stHasil1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panelWarnaHasil.SetSizer( bSizer48 )
		self.m_panelWarnaHasil.Layout()
		bSizer48.Fit( self.m_panelWarnaHasil )
		fgSizer28.Add( self.m_panelWarnaHasil, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer32.Add( fgSizer28, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer32.Add( ( 0, 25), 0, 0, 5 )

		bSizer124 = wx.BoxSizer( wx.VERTICAL )

		fgSizer36 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer36.AddGrowableRow( 1 )
		fgSizer36.SetFlexibleDirection( wx.BOTH )
		fgSizer36.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticCR1 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticCR1.Wrap( -1 )

		self.m_staticCR1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer36.Add( self.m_staticCR1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticCR2 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticCR2.Wrap( -1 )

		self.m_staticCR2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer36.Add( self.m_staticCR2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_listCtrlCR1 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrlCR1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrlCR1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrlCR1.SetBackgroundColour( wx.Colour( 82, 101, 140 ) )

		fgSizer36.Add( self.m_listCtrlCR1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_listCtrlCR2 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrlCR2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrlCR2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrlCR2.SetBackgroundColour( wx.Colour( 150, 152, 154 ) )

		fgSizer36.Add( self.m_listCtrlCR2, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText181 = wx.StaticText( self, wx.ID_ANY, u"*Kode dalam kurung adalah pekerjaan untuk dipertimbangkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )

		self.m_staticText181.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer36.Add( self.m_staticText181, 0, wx.ALL, 5 )


		bSizer124.Add( fgSizer36, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer32.Add( bSizer124, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.SetSizer( bSizer32 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class Page7
###########################################################################

class Page7 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1289,3000 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer60 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow8 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow8.SetScrollRate( 5, 5 )
		self.m_scrolledWindow8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer58 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap_hal7 = wx.StaticBitmap( self.m_scrolledWindow8, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer58.Add( self.m_bitmap_hal7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer29 = wx.FlexGridSizer( 1, 0, 0, 0 )
		fgSizer29.AddGrowableCol( 0 )
		fgSizer29.AddGrowableRow( 0 )
		fgSizer29.SetFlexibleDirection( wx.BOTH )
		fgSizer29.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_buttonBersihkan = wx.Button( self.m_scrolledWindow8, wx.ID_ANY, u"Hapuskan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonBersihkan.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer29.Add( self.m_buttonBersihkan, 0, wx.ALL, 5 )

		self.m_SimpanPage6 = wx.Button( self.m_scrolledWindow8, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_SimpanPage6.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_SimpanPage6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_SimpanPage6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer29.Add( self.m_SimpanPage6, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		bSizer58.Add( fgSizer29, 0, wx.ALIGN_RIGHT, 5 )

		fgSizer37 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer37.SetFlexibleDirection( wx.BOTH )
		fgSizer37.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel92 = wx.Panel( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel92.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel92.SetBackgroundColour( wx.Colour( 88, 85, 112 ) )

		bSizer119 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel97 = wx.Panel( self.m_panel92, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer125 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText212 = wx.StaticText( self.m_panel97, wx.ID_ANY, u"BIODATA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )

		self.m_staticText212.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )

		bSizer125.Add( self.m_staticText212, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel97.SetSizer( bSizer125 )
		self.m_panel97.Layout()
		bSizer125.Fit( self.m_panel97 )
		bSizer119.Add( self.m_panel97, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer4 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.no_tes = wx.StaticText( self.m_panel92, wx.ID_ANY, u"No Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.no_tes.Wrap( -1 )

		self.no_tes.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.no_tes, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.no_tes_input = wx.TextCtrl( self.m_panel92, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_READONLY )
		self.no_tes_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.no_tes_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.tanggal_tes = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_tes.Wrap( -1 )

		self.tanggal_tes.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.tanggal_tes, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_tes_input = wx.adv.DatePickerCtrl( self.m_panel92, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( -1,-1 ), wx.adv.DP_DEFAULT )
		self.tanggal_tes_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.tanggal_tes_input, 0, wx.ALL, 5 )

		self.nama_kandidat = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Nama Kandidat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama_kandidat.Wrap( -1 )

		self.nama_kandidat.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.nama_kandidat, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nama_kandidat_input = wx.TextCtrl( self.m_panel92, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_READONLY )
		self.nama_kandidat_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.nama_kandidat_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.jenis_kelamin = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jenis_kelamin.Wrap( -1 )

		self.jenis_kelamin.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.jenis_kelamin, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		jenis_kelamin_inputChoices = [ u"Laki-Laki", u"Perempuan" ]
		self.jenis_kelamin_input = wx.Choice( self.m_panel92, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, jenis_kelamin_inputChoices, 0 )
		self.jenis_kelamin_input.SetSelection( 1 )
		self.jenis_kelamin_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.jenis_kelamin_input, 0, wx.ALL, 5 )

		self.tanggal_lahir = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_lahir.Wrap( -1 )

		self.tanggal_lahir.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.tanggal_lahir, 0, wx.ALL, 5 )

		self.tanggal_lahir_input = wx.adv.DatePickerCtrl( self.m_panel92, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( -1,-1 ), wx.adv.DP_DEFAULT )
		self.tanggal_lahir_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.tanggal_lahir_input, 0, wx.ALL, 5 )

		self.pendidikan_terakhir = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Pendidikan Terakhir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pendidikan_terakhir.Wrap( -1 )

		self.pendidikan_terakhir.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.pendidikan_terakhir, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		pendidikan_terakhir_inputChoices = [ u"SD", u"SMP", u"SMA/Sederajat", u"S1", u"S2", u"S3" ]
		self.pendidikan_terakhir_input = wx.Choice( self.m_panel92, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pendidikan_terakhir_inputChoices, 0 )
		self.pendidikan_terakhir_input.SetSelection( 5 )
		self.pendidikan_terakhir_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.pendidikan_terakhir_input, 0, wx.ALL, 5 )

		self.jurusan = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Jurusan Pendidikan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan.Wrap( -1 )

		self.jurusan.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.jurusan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan_input = wx.TextCtrl( self.m_panel92, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.jurusan_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.jurusan_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.kota = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kota.Wrap( -1 )

		self.kota.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.kota, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kota_input = wx.TextCtrl( self.m_panel92, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.kota_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.kota_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.perusahaan_instansi = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Perusahaan/Instansi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.perusahaan_instansi.Wrap( -1 )

		self.perusahaan_instansi.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.perusahaan_instansi, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.perusahaan_instansi_input = wx.TextCtrl( self.m_panel92, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.perusahaan_instansi_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.perusahaan_instansi_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.posisi_jabatan = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Posisi/Jabatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.posisi_jabatan.Wrap( -1 )

		self.posisi_jabatan.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.posisi_jabatan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.posisi_jabatan_input = wx.TextCtrl( self.m_panel92, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.posisi_jabatan_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.posisi_jabatan_input, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer119.Add( fgSizer4, 1, wx.EXPAND, 5 )


		self.m_panel92.SetSizer( bSizer119 )
		self.m_panel92.Layout()
		bSizer119.Fit( self.m_panel92 )
		fgSizer37.Add( self.m_panel92, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel93 = wx.Panel( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel93.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel93.SetBackgroundColour( wx.Colour( 88, 85, 112 ) )
		self.m_panel93.Hide()

		bSizer121 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel98 = wx.Panel( self.m_panel93, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer126 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText213 = wx.StaticText( self.m_panel98, wx.ID_ANY, u"BIODATA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText213.Wrap( -1 )

		self.m_staticText213.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )

		bSizer126.Add( self.m_staticText213, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel98.SetSizer( bSizer126 )
		self.m_panel98.Layout()
		bSizer126.Fit( self.m_panel98 )
		bSizer121.Add( self.m_panel98, 0, wx.EXPAND |wx.ALL, 5 )

		fgSizer15 = wx.FlexGridSizer( 13, 2, 0, 1 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.nama2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama2.Wrap( -1 )

		self.nama2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.nama2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nama_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.nama_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.nama_input2, 0, wx.ALL, 5 )

		self.tanggal_tes2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_tes2.Wrap( -1 )

		self.tanggal_tes2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.tanggal_tes2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_tes_input2 = wx.adv.DatePickerCtrl( self.m_panel93, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		self.tanggal_tes_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.tanggal_tes_input2, 0, wx.ALL, 5 )

		self.jenis_kelamin2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jenis_kelamin2.Wrap( -1 )

		self.jenis_kelamin2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.jenis_kelamin2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		jenis_kelamin_input2Choices = [ u"Laki-Laki", u"Perempuan" ]
		self.jenis_kelamin_input2 = wx.Choice( self.m_panel93, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, jenis_kelamin_input2Choices, 0 )
		self.jenis_kelamin_input2.SetSelection( 1 )
		self.jenis_kelamin_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.jenis_kelamin_input2, 0, wx.ALL, 5 )

		self.tanggal_lahir2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_lahir2.Wrap( -1 )

		self.tanggal_lahir2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.tanggal_lahir2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_lahir_input2 = wx.adv.DatePickerCtrl( self.m_panel93, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		self.tanggal_lahir_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.tanggal_lahir_input2, 0, wx.ALL, 5 )

		self.asal_sekolah2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Asal Sekolah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asal_sekolah2.Wrap( -1 )

		self.asal_sekolah2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.asal_sekolah2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.asal_sekolah_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.asal_sekolah_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.asal_sekolah_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.jurusan21 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan21.Wrap( -1 )

		self.jurusan21.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.jurusan21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan_input21 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.jurusan_input21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.jurusan_input21, 0, wx.ALL|wx.EXPAND, 5 )

		self.asal_universitas2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Asal Universitas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asal_universitas2.Wrap( -1 )

		self.asal_universitas2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.asal_universitas2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.asal_universitas_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.asal_universitas_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.asal_universitas_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.jurusan2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan2.Wrap( -1 )

		self.jurusan2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.jurusan2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.jurusan_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.jurusan_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.kota2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kota2.Wrap( -1 )

		self.kota2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.kota2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kota_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.kota_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.kota_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.hobi2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Hobi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hobi2.Wrap( -1 )

		self.hobi2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.hobi2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.hobi_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.hobi_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.hobi_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.prestasi_akademik2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Prestasi Akademik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prestasi_akademik2.Wrap( -1 )

		self.prestasi_akademik2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.prestasi_akademik2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.prestasi_akademik_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.prestasi_akademik_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.prestasi_akademik_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.prestasi_non_akademik2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Prestasi Non Akademik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prestasi_non_akademik2.Wrap( -1 )

		self.prestasi_non_akademik2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.prestasi_non_akademik2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.prestasi_non_akademik_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.prestasi_non_akademik_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.prestasi_non_akademik_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.ekskul_yang_diikuti2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Ekskul yang Diikuti", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ekskul_yang_diikuti2.Wrap( -1 )

		self.ekskul_yang_diikuti2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.ekskul_yang_diikuti2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ekskul_yang_diikuti_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.ekskul_yang_diikuti_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.ekskul_yang_diikuti_input2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer121.Add( fgSizer15, 1, wx.EXPAND, 5 )


		self.m_panel93.SetSizer( bSizer121 )
		self.m_panel93.Layout()
		bSizer121.Fit( self.m_panel93 )
		fgSizer37.Add( self.m_panel93, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel91 = wx.Panel( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel91.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel91.SetBackgroundColour( wx.Colour( 125, 100, 139 ) )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel96 = wx.Panel( self.m_panel91, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer123 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self.m_panel96, wx.ID_ANY, u"OCCUPATIONAL DAYDREAM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )

		bSizer123.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel96.SetSizer( bSizer123 )
		self.m_panel96.Layout()
		bSizer123.Fit( self.m_panel96 )
		bSizer10.Add( self.m_panel96, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel981 = wx.Panel( self.m_panel91, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel981.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel981.SetBackgroundColour( wx.Colour( 125, 100, 139 ) )

		bSizer631 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer71 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer71.AddGrowableCol( 1 )
		fgSizer71.SetFlexibleDirection( wx.BOTH )
		fgSizer71.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText8 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer71.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.textctrl1 = wx.TextCtrl( self.m_panel981, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.textctrl1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.textctrl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label1 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label1.Wrap( -1 )

		self.label1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.label1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText10 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer71.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.textctrl2 = wx.TextCtrl( self.m_panel981, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.textctrl2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.textctrl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label2 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label2.Wrap( -1 )

		self.label2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.label2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText132 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText132.Wrap( -1 )

		fgSizer71.Add( self.m_staticText132, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.textctrl3 = wx.TextCtrl( self.m_panel981, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.textctrl3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.textctrl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label3 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label3.Wrap( -1 )

		self.label3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.label3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText134 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText134.Wrap( -1 )

		fgSizer71.Add( self.m_staticText134, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textctrl4 = wx.TextCtrl( self.m_panel981, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.textctrl4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.textctrl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label4 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label4.Wrap( -1 )

		self.label4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.label4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText138 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText138.Wrap( -1 )

		fgSizer71.Add( self.m_staticText138, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textctrl5 = wx.TextCtrl( self.m_panel981, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.textctrl5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.textctrl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label5 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label5.Wrap( -1 )

		self.label5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.label5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText139 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText139.Wrap( -1 )

		self.m_staticText139.Hide()

		fgSizer71.Add( self.m_staticText139, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.textctrl6 = wx.TextCtrl( self.m_panel981, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.textctrl6.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.textctrl6.Hide()

		fgSizer71.Add( self.textctrl6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label6 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label6.Wrap( -1 )

		self.label6.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.label6.Hide()

		fgSizer71.Add( self.label6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer631.Add( fgSizer71, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer64 = wx.BoxSizer( wx.VERTICAL )


		bSizer64.Add( ( 25, 0), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer631.Add( bSizer64, 0, 0, 5 )


		self.m_panel981.SetSizer( bSizer631 )
		self.m_panel981.Layout()
		bSizer631.Fit( self.m_panel981 )
		bSizer10.Add( self.m_panel981, 0, wx.ALL, 5 )


		self.m_panel91.SetSizer( bSizer10 )
		self.m_panel91.Layout()
		bSizer10.Fit( self.m_panel91 )
		fgSizer37.Add( self.m_panel91, 0, wx.ALL, 5 )


		bSizer58.Add( fgSizer37, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer58.Add( ( 0, 75), 0, 0, 5 )

		self.m_panelA = wx.Panel( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelA.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer61 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel117 = wx.Panel( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel117.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.m_panel117.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel117.SetBackgroundColour( wx.Colour( 82, 101, 140 ) )

		bSizer152 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText290 = wx.StaticText( self.m_panel117, wx.ID_ANY, u"OCCUPATIONAL FINDER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText290.Wrap( -1 )

		self.m_staticText290.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText290.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer152.Add( self.m_staticText290, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel117.SetSizer( bSizer152 )
		self.m_panel117.Layout()
		bSizer152.Fit( self.m_panel117 )
		bSizer61.Add( self.m_panel117, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		bSizer61.Add( ( 0, 25), 0, 0, 5 )

		bSizer171 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_statictextfromcircle1 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_statictextfromcircle1.Wrap( -1 )

		self.m_statictextfromcircle1.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer171.Add( self.m_statictextfromcircle1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText404 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"*Kode dalam kurung adalah pekerjaan untuk dipertimbangkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText404.Wrap( -1 )

		self.m_staticText404.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer171.Add( self.m_staticText404, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		bSizer61.Add( bSizer171, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer35 = wx.FlexGridSizer( 4, 3, 0, 0 )
		fgSizer35.SetFlexibleDirection( wx.BOTH )
		fgSizer35.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticA = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA.Wrap( -1 )

		self.m_staticA.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_staticA, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA2 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA2.Wrap( -1 )

		self.m_staticA2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_staticA2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA3 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA3.Wrap( -1 )

		self.m_staticA3.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_staticA3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.m_listCtrl1 = wx.ListCtrl( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl1.SetBackgroundColour( wx.Colour( 82, 101, 140 ) )

		fgSizer35.Add( self.m_listCtrl1, 0, wx.ALL, 5 )

		self.m_listCtrl2 = wx.ListCtrl( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl2.SetBackgroundColour( wx.Colour( 150, 152, 154 ) )

		fgSizer35.Add( self.m_listCtrl2, 0, wx.ALL, 5 )

		self.m_listCtrl3 = wx.ListCtrl( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl3.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl3.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_listCtrl3.SetBackgroundColour( wx.Colour( 230, 231, 232 ) )

		fgSizer35.Add( self.m_listCtrl3, 0, wx.ALL, 5 )

		self.m_staticA4 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA4.Wrap( -1 )

		self.m_staticA4.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_staticA4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA5 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA5.Wrap( -1 )

		self.m_staticA5.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_staticA5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA6 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA6.Wrap( -1 )

		self.m_staticA6.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_staticA6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_listCtrl4 = wx.ListCtrl( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl4.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl4.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl4.SetBackgroundColour( wx.Colour( 82, 101, 140 ) )

		fgSizer35.Add( self.m_listCtrl4, 0, wx.ALL, 5 )

		self.m_listCtrl5 = wx.ListCtrl( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl5.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl5.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl5.SetBackgroundColour( wx.Colour( 150, 152, 154 ) )

		fgSizer35.Add( self.m_listCtrl5, 0, wx.ALL, 5 )

		self.m_listCtrl6 = wx.ListCtrl( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl6.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl6.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_listCtrl6.SetBackgroundColour( wx.Colour( 230, 231, 232 ) )

		fgSizer35.Add( self.m_listCtrl6, 0, wx.ALL, 5 )


		bSizer61.Add( fgSizer35, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panelA.SetSizer( bSizer61 )
		self.m_panelA.Layout()
		bSizer61.Fit( self.m_panelA )
		bSizer58.Add( self.m_panelA, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline5 = wx.StaticLine( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer58.Add( self.m_staticline5, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_panelA1 = wx.Panel( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer63 = wx.BoxSizer( wx.VERTICAL )

		bSizer172 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticfromcircle2 = wx.StaticText( self.m_panelA1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticfromcircle2.Wrap( -1 )

		self.m_staticfromcircle2.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer172.Add( self.m_staticfromcircle2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText405 = wx.StaticText( self.m_panelA1, wx.ID_ANY, u"*Kode dalam kurung adalah pekerjaan untuk dipertimbangkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText405.Wrap( -1 )

		self.m_staticText405.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer172.Add( self.m_staticText405, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		bSizer63.Add( bSizer172, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer351 = wx.FlexGridSizer( 4, 3, 0, 0 )
		fgSizer351.SetFlexibleDirection( wx.BOTH )
		fgSizer351.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticA7 = wx.StaticText( self.m_panelA1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA7.Wrap( -1 )

		self.m_staticA7.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer351.Add( self.m_staticA7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA8 = wx.StaticText( self.m_panelA1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA8.Wrap( -1 )

		self.m_staticA8.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer351.Add( self.m_staticA8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA9 = wx.StaticText( self.m_panelA1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA9.Wrap( -1 )

		self.m_staticA9.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer351.Add( self.m_staticA9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.m_listCtrl7 = wx.ListCtrl( self.m_panelA1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl7.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl7.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl7.SetBackgroundColour( wx.Colour( 82, 101, 140 ) )

		fgSizer351.Add( self.m_listCtrl7, 0, wx.ALL, 5 )

		self.m_listCtrl8 = wx.ListCtrl( self.m_panelA1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl8.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl8.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl8.SetBackgroundColour( wx.Colour( 150, 152, 154 ) )

		fgSizer351.Add( self.m_listCtrl8, 0, wx.ALL, 5 )

		self.m_listCtrl9 = wx.ListCtrl( self.m_panelA1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl9.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl9.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_listCtrl9.SetBackgroundColour( wx.Colour( 230, 231, 232 ) )

		fgSizer351.Add( self.m_listCtrl9, 0, wx.ALL, 5 )

		self.m_staticA10 = wx.StaticText( self.m_panelA1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA10.Wrap( -1 )

		self.m_staticA10.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer351.Add( self.m_staticA10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA11 = wx.StaticText( self.m_panelA1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA11.Wrap( -1 )

		self.m_staticA11.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer351.Add( self.m_staticA11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA12 = wx.StaticText( self.m_panelA1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA12.Wrap( -1 )

		self.m_staticA12.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer351.Add( self.m_staticA12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_listCtrl10 = wx.ListCtrl( self.m_panelA1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl10.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl10.SetBackgroundColour( wx.Colour( 82, 101, 140 ) )

		fgSizer351.Add( self.m_listCtrl10, 0, wx.ALL, 5 )

		self.m_listCtrl11 = wx.ListCtrl( self.m_panelA1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl11.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl11.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl11.SetBackgroundColour( wx.Colour( 150, 152, 154 ) )

		fgSizer351.Add( self.m_listCtrl11, 0, wx.ALL, 5 )

		self.m_listCtrl12 = wx.ListCtrl( self.m_panelA1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl12.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl12.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_listCtrl12.SetBackgroundColour( wx.Colour( 230, 231, 232 ) )

		fgSizer351.Add( self.m_listCtrl12, 0, wx.ALL, 5 )


		bSizer63.Add( fgSizer351, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panelA1.SetSizer( bSizer63 )
		self.m_panelA1.Layout()
		bSizer63.Fit( self.m_panelA1 )
		bSizer58.Add( self.m_panelA1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline8 = wx.StaticLine( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer58.Add( self.m_staticline8, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer58.Add( ( 0, 50), 0, 0, 5 )

		self.m_bitmap_hal7_1 = wx.StaticBitmap( self.m_scrolledWindow8, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer58.Add( self.m_bitmap_hal7_1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer371 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer371.SetFlexibleDirection( wx.BOTH )
		fgSizer371.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel921 = wx.Panel( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel921.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel921.SetBackgroundColour( wx.Colour( 72, 136, 123 ) )

		bSizer1191 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel971 = wx.Panel( self.m_panel921, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1251 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2121 = wx.StaticText( self.m_panel971, wx.ID_ANY, u"BIODATA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2121.Wrap( -1 )

		self.m_staticText2121.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )

		bSizer1251.Add( self.m_staticText2121, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel971.SetSizer( bSizer1251 )
		self.m_panel971.Layout()
		bSizer1251.Fit( self.m_panel971 )
		bSizer1191.Add( self.m_panel971, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer41 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer41.AddGrowableCol( 1 )
		fgSizer41.SetFlexibleDirection( wx.BOTH )
		fgSizer41.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.no_tes1 = wx.StaticText( self.m_panel921, wx.ID_ANY, u"No Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.no_tes1.Wrap( -1 )

		self.no_tes1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer41.Add( self.no_tes1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.no_tes_input1 = wx.TextCtrl( self.m_panel921, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		self.no_tes_input1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer41.Add( self.no_tes_input1, 0, wx.ALL|wx.EXPAND, 5 )

		self.tanggal_tes1 = wx.StaticText( self.m_panel921, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_tes1.Wrap( -1 )

		self.tanggal_tes1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer41.Add( self.tanggal_tes1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_tes_input1 = wx.adv.DatePickerCtrl( self.m_panel921, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		self.tanggal_tes_input1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer41.Add( self.tanggal_tes_input1, 0, wx.ALL, 5 )

		self.nama_kandidat1 = wx.StaticText( self.m_panel921, wx.ID_ANY, u"Nama Kandidat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama_kandidat1.Wrap( -1 )

		self.nama_kandidat1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer41.Add( self.nama_kandidat1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nama_kandidat_input1 = wx.TextCtrl( self.m_panel921, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		self.nama_kandidat_input1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer41.Add( self.nama_kandidat_input1, 0, wx.ALL|wx.EXPAND, 5 )

		self.jenis_kelamin1 = wx.StaticText( self.m_panel921, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jenis_kelamin1.Wrap( -1 )

		self.jenis_kelamin1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer41.Add( self.jenis_kelamin1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		jenis_kelamin_input1Choices = [ u"Laki-Laki", u"Perempuan" ]
		self.jenis_kelamin_input1 = wx.Choice( self.m_panel921, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, jenis_kelamin_input1Choices, 0 )
		self.jenis_kelamin_input1.SetSelection( 1 )
		self.jenis_kelamin_input1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer41.Add( self.jenis_kelamin_input1, 0, wx.ALL, 5 )

		self.tanggal_lahir1 = wx.StaticText( self.m_panel921, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_lahir1.Wrap( -1 )

		self.tanggal_lahir1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer41.Add( self.tanggal_lahir1, 0, wx.ALL, 5 )

		self.tanggal_lahir_input1 = wx.adv.DatePickerCtrl( self.m_panel921, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		self.tanggal_lahir_input1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer41.Add( self.tanggal_lahir_input1, 0, wx.ALL, 5 )

		self.pendidikan_terakhir1 = wx.StaticText( self.m_panel921, wx.ID_ANY, u"Pendidikan Terakhir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pendidikan_terakhir1.Wrap( -1 )

		self.pendidikan_terakhir1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer41.Add( self.pendidikan_terakhir1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		pendidikan_terakhir_input1Choices = [ u"SD", u"SMP", u"SMA/Sederajat", u"S1", u"S2", u"S3" ]
		self.pendidikan_terakhir_input1 = wx.Choice( self.m_panel921, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pendidikan_terakhir_input1Choices, 0 )
		self.pendidikan_terakhir_input1.SetSelection( 0 )
		self.pendidikan_terakhir_input1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer41.Add( self.pendidikan_terakhir_input1, 0, wx.ALL, 5 )

		self.jurusan1 = wx.StaticText( self.m_panel921, wx.ID_ANY, u"Jurusan Pendidikan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan1.Wrap( -1 )

		self.jurusan1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer41.Add( self.jurusan1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan_input1 = wx.TextCtrl( self.m_panel921, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.jurusan_input1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer41.Add( self.jurusan_input1, 0, wx.ALL|wx.EXPAND, 5 )

		self.kota1 = wx.StaticText( self.m_panel921, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kota1.Wrap( -1 )

		self.kota1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer41.Add( self.kota1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kota_input1 = wx.TextCtrl( self.m_panel921, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.kota_input1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer41.Add( self.kota_input1, 0, wx.ALL|wx.EXPAND, 5 )

		self.perusahaan_instansi1 = wx.StaticText( self.m_panel921, wx.ID_ANY, u"Perusahaan/Instansi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.perusahaan_instansi1.Wrap( -1 )

		self.perusahaan_instansi1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer41.Add( self.perusahaan_instansi1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.perusahaan_instansi_input1 = wx.TextCtrl( self.m_panel921, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.perusahaan_instansi_input1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer41.Add( self.perusahaan_instansi_input1, 0, wx.ALL|wx.EXPAND, 5 )

		self.posisi_jabatan1 = wx.StaticText( self.m_panel921, wx.ID_ANY, u"Posisi/Jabatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.posisi_jabatan1.Wrap( -1 )

		self.posisi_jabatan1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer41.Add( self.posisi_jabatan1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.posisi_jabatan_input1 = wx.TextCtrl( self.m_panel921, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.posisi_jabatan_input1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer41.Add( self.posisi_jabatan_input1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1191.Add( fgSizer41, 1, wx.EXPAND, 5 )


		self.m_panel921.SetSizer( bSizer1191 )
		self.m_panel921.Layout()
		bSizer1191.Fit( self.m_panel921 )
		fgSizer371.Add( self.m_panel921, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel931 = wx.Panel( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel931.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel931.SetBackgroundColour( wx.Colour( 72, 136, 123 ) )
		self.m_panel931.Hide()

		bSizer1211 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel982 = wx.Panel( self.m_panel931, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1261 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2131 = wx.StaticText( self.m_panel982, wx.ID_ANY, u"BIODATA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2131.Wrap( -1 )

		self.m_staticText2131.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )

		bSizer1261.Add( self.m_staticText2131, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel982.SetSizer( bSizer1261 )
		self.m_panel982.Layout()
		bSizer1261.Fit( self.m_panel982 )
		bSizer1211.Add( self.m_panel982, 0, wx.EXPAND |wx.ALL, 5 )

		fgSizer151 = wx.FlexGridSizer( 13, 2, 0, 1 )
		fgSizer151.SetFlexibleDirection( wx.BOTH )
		fgSizer151.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.nama21 = wx.StaticText( self.m_panel931, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama21.Wrap( -1 )

		self.nama21.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer151.Add( self.nama21, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nama_input21 = wx.TextCtrl( self.m_panel931, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.nama_input21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer151.Add( self.nama_input21, 0, wx.ALL, 5 )

		self.tanggal_tes21 = wx.StaticText( self.m_panel931, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_tes21.Wrap( -1 )

		self.tanggal_tes21.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer151.Add( self.tanggal_tes21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_tes_input21 = wx.adv.DatePickerCtrl( self.m_panel931, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		self.tanggal_tes_input21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer151.Add( self.tanggal_tes_input21, 0, wx.ALL, 5 )

		self.jenis_kelamin21 = wx.StaticText( self.m_panel931, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jenis_kelamin21.Wrap( -1 )

		self.jenis_kelamin21.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer151.Add( self.jenis_kelamin21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		jenis_kelamin_input21Choices = [ u"Laki-Laki", u"Perempuan" ]
		self.jenis_kelamin_input21 = wx.Choice( self.m_panel931, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, jenis_kelamin_input21Choices, 0 )
		self.jenis_kelamin_input21.SetSelection( 1 )
		self.jenis_kelamin_input21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer151.Add( self.jenis_kelamin_input21, 0, wx.ALL, 5 )

		self.tanggal_lahir21 = wx.StaticText( self.m_panel931, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_lahir21.Wrap( -1 )

		self.tanggal_lahir21.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer151.Add( self.tanggal_lahir21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_lahir_input21 = wx.adv.DatePickerCtrl( self.m_panel931, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		self.tanggal_lahir_input21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer151.Add( self.tanggal_lahir_input21, 0, wx.ALL, 5 )

		self.asal_sekolah21 = wx.StaticText( self.m_panel931, wx.ID_ANY, u"Asal Sekolah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asal_sekolah21.Wrap( -1 )

		self.asal_sekolah21.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer151.Add( self.asal_sekolah21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.asal_sekolah_input21 = wx.TextCtrl( self.m_panel931, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.asal_sekolah_input21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer151.Add( self.asal_sekolah_input21, 0, wx.ALL|wx.EXPAND, 5 )

		self.jurusan211 = wx.StaticText( self.m_panel931, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan211.Wrap( -1 )

		self.jurusan211.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer151.Add( self.jurusan211, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan_input211 = wx.TextCtrl( self.m_panel931, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.jurusan_input211.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer151.Add( self.jurusan_input211, 0, wx.ALL|wx.EXPAND, 5 )

		self.asal_universitas21 = wx.StaticText( self.m_panel931, wx.ID_ANY, u"Asal Universitas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asal_universitas21.Wrap( -1 )

		self.asal_universitas21.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer151.Add( self.asal_universitas21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.asal_universitas_input21 = wx.TextCtrl( self.m_panel931, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.asal_universitas_input21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer151.Add( self.asal_universitas_input21, 0, wx.ALL|wx.EXPAND, 5 )

		self.jurusan22 = wx.StaticText( self.m_panel931, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan22.Wrap( -1 )

		self.jurusan22.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer151.Add( self.jurusan22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan_input22 = wx.TextCtrl( self.m_panel931, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.jurusan_input22.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer151.Add( self.jurusan_input22, 0, wx.ALL|wx.EXPAND, 5 )

		self.kota21 = wx.StaticText( self.m_panel931, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kota21.Wrap( -1 )

		self.kota21.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer151.Add( self.kota21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kota_input21 = wx.TextCtrl( self.m_panel931, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.kota_input21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer151.Add( self.kota_input21, 0, wx.ALL|wx.EXPAND, 5 )

		self.hobi21 = wx.StaticText( self.m_panel931, wx.ID_ANY, u"Hobi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hobi21.Wrap( -1 )

		self.hobi21.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer151.Add( self.hobi21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.hobi_input21 = wx.TextCtrl( self.m_panel931, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.hobi_input21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer151.Add( self.hobi_input21, 0, wx.ALL|wx.EXPAND, 5 )

		self.prestasi_akademik21 = wx.StaticText( self.m_panel931, wx.ID_ANY, u"Prestasi Akademik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prestasi_akademik21.Wrap( -1 )

		self.prestasi_akademik21.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer151.Add( self.prestasi_akademik21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.prestasi_akademik_input21 = wx.TextCtrl( self.m_panel931, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.prestasi_akademik_input21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer151.Add( self.prestasi_akademik_input21, 0, wx.ALL|wx.EXPAND, 5 )

		self.prestasi_non_akademik21 = wx.StaticText( self.m_panel931, wx.ID_ANY, u"Prestasi Non Akademik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prestasi_non_akademik21.Wrap( -1 )

		self.prestasi_non_akademik21.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer151.Add( self.prestasi_non_akademik21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.prestasi_non_akademik_input21 = wx.TextCtrl( self.m_panel931, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.prestasi_non_akademik_input21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer151.Add( self.prestasi_non_akademik_input21, 0, wx.ALL|wx.EXPAND, 5 )

		self.ekskul_yang_diikuti21 = wx.StaticText( self.m_panel931, wx.ID_ANY, u"Ekskul yang Diikuti", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ekskul_yang_diikuti21.Wrap( -1 )

		self.ekskul_yang_diikuti21.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer151.Add( self.ekskul_yang_diikuti21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ekskul_yang_diikuti_input21 = wx.TextCtrl( self.m_panel931, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.ekskul_yang_diikuti_input21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer151.Add( self.ekskul_yang_diikuti_input21, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1211.Add( fgSizer151, 1, wx.EXPAND, 5 )


		self.m_panel931.SetSizer( bSizer1211 )
		self.m_panel931.Layout()
		bSizer1211.Fit( self.m_panel931 )
		fgSizer371.Add( self.m_panel931, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel911 = wx.Panel( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel911.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel911.SetBackgroundColour( wx.Colour( 125, 100, 139 ) )
		self.m_panel911.Hide()

		bSizer101 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel961 = wx.Panel( self.m_panel911, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1231 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText71 = wx.StaticText( self.m_panel961, wx.ID_ANY, u"OCCUPATIONAL DAYDREAM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		self.m_staticText71.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )

		bSizer1231.Add( self.m_staticText71, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel961.SetSizer( bSizer1231 )
		self.m_panel961.Layout()
		bSizer1231.Fit( self.m_panel961 )
		bSizer101.Add( self.m_panel961, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel9811 = wx.Panel( self.m_panel911, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel9811.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel9811.SetBackgroundColour( wx.Colour( 125, 100, 139 ) )

		bSizer6311 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer711 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer711.AddGrowableCol( 1 )
		fgSizer711.SetFlexibleDirection( wx.BOTH )
		fgSizer711.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText81 = wx.StaticText( self.m_panel9811, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		fgSizer711.Add( self.m_staticText81, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.textctrl11 = wx.TextCtrl( self.m_panel9811, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.textctrl11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer711.Add( self.textctrl11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label11 = wx.StaticText( self.m_panel9811, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label11.Wrap( -1 )

		self.label11.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer711.Add( self.label11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText101 = wx.StaticText( self.m_panel9811, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		fgSizer711.Add( self.m_staticText101, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.textctrl21 = wx.TextCtrl( self.m_panel9811, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.textctrl21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer711.Add( self.textctrl21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label21 = wx.StaticText( self.m_panel9811, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label21.Wrap( -1 )

		self.label21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer711.Add( self.label21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText1321 = wx.StaticText( self.m_panel9811, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1321.Wrap( -1 )

		fgSizer711.Add( self.m_staticText1321, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.textctrl31 = wx.TextCtrl( self.m_panel9811, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.textctrl31.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer711.Add( self.textctrl31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label31 = wx.StaticText( self.m_panel9811, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label31.Wrap( -1 )

		self.label31.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer711.Add( self.label31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText1341 = wx.StaticText( self.m_panel9811, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1341.Wrap( -1 )

		fgSizer711.Add( self.m_staticText1341, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textctrl41 = wx.TextCtrl( self.m_panel9811, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.textctrl41.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer711.Add( self.textctrl41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label41 = wx.StaticText( self.m_panel9811, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label41.Wrap( -1 )

		self.label41.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer711.Add( self.label41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText1381 = wx.StaticText( self.m_panel9811, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1381.Wrap( -1 )

		fgSizer711.Add( self.m_staticText1381, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textctrl51 = wx.TextCtrl( self.m_panel9811, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.textctrl51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer711.Add( self.textctrl51, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label51 = wx.StaticText( self.m_panel9811, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label51.Wrap( -1 )

		self.label51.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer711.Add( self.label51, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText1391 = wx.StaticText( self.m_panel9811, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1391.Wrap( -1 )

		self.m_staticText1391.Hide()

		fgSizer711.Add( self.m_staticText1391, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.textctrl61 = wx.TextCtrl( self.m_panel9811, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.textctrl61.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.textctrl61.Hide()

		fgSizer711.Add( self.textctrl61, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label61 = wx.StaticText( self.m_panel9811, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label61.Wrap( -1 )

		self.label61.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.label61.Hide()

		fgSizer711.Add( self.label61, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer6311.Add( fgSizer711, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer641 = wx.BoxSizer( wx.VERTICAL )


		bSizer641.Add( ( 25, 0), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer6311.Add( bSizer641, 0, 0, 5 )


		self.m_panel9811.SetSizer( bSizer6311 )
		self.m_panel9811.Layout()
		bSizer6311.Fit( self.m_panel9811 )
		bSizer101.Add( self.m_panel9811, 0, wx.ALL, 5 )


		self.m_panel911.SetSizer( bSizer101 )
		self.m_panel911.Layout()
		bSizer101.Fit( self.m_panel911 )
		fgSizer371.Add( self.m_panel911, 0, wx.ALL, 5 )


		bSizer58.Add( fgSizer371, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer58.Add( ( 0, 75), 0, 0, 5 )

		self.m_panelA2 = wx.Panel( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelA2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer611 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel118 = wx.Panel( self.m_panelA2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel118.SetBackgroundColour( wx.Colour( 91, 122, 54 ) )

		bSizer153 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText291 = wx.StaticText( self.m_panel118, wx.ID_ANY, u"EDUCATIONAL FINDER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText291.Wrap( -1 )

		self.m_staticText291.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )
		self.m_staticText291.SetForegroundColour( wx.Colour( 249, 250, 249 ) )

		bSizer153.Add( self.m_staticText291, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel118.SetSizer( bSizer153 )
		self.m_panel118.Layout()
		bSizer153.Fit( self.m_panel118 )
		bSizer611.Add( self.m_panel118, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer611.Add( ( 0, 50), 0, 0, 5 )

		bSizer173 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_statictextfromcircle11 = wx.StaticText( self.m_panelA2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_statictextfromcircle11.Wrap( -1 )

		self.m_statictextfromcircle11.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer173.Add( self.m_statictextfromcircle11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText406 = wx.StaticText( self.m_panelA2, wx.ID_ANY, u"\"kode dalam kurung adalah program studi untuk dipertimbangkan\"", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText406.Wrap( -1 )

		self.m_staticText406.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer173.Add( self.m_staticText406, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		bSizer611.Add( bSizer173, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer352 = wx.FlexGridSizer( 4, 3, 0, 0 )
		fgSizer352.SetFlexibleDirection( wx.BOTH )
		fgSizer352.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticA1 = wx.StaticText( self.m_panelA2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA1.Wrap( -1 )

		self.m_staticA1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer352.Add( self.m_staticA1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA21 = wx.StaticText( self.m_panelA2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA21.Wrap( -1 )

		self.m_staticA21.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer352.Add( self.m_staticA21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA31 = wx.StaticText( self.m_panelA2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA31.Wrap( -1 )

		self.m_staticA31.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer352.Add( self.m_staticA31, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.m_listCtrl13 = wx.ListCtrl( self.m_panelA2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl13.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl13.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl13.SetBackgroundColour( wx.Colour( 91, 122, 54 ) )

		fgSizer352.Add( self.m_listCtrl13, 0, wx.ALL, 5 )

		self.m_listCtrl21 = wx.ListCtrl( self.m_panelA2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl21.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl21.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_listCtrl21.SetBackgroundColour( wx.Colour( 168, 207, 69 ) )

		fgSizer352.Add( self.m_listCtrl21, 0, wx.ALL, 5 )

		self.m_listCtrl31 = wx.ListCtrl( self.m_panelA2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl31.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl31.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_listCtrl31.SetBackgroundColour( wx.Colour( 185, 199, 130 ) )

		fgSizer352.Add( self.m_listCtrl31, 0, wx.ALL, 5 )

		self.m_staticA41 = wx.StaticText( self.m_panelA2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA41.Wrap( -1 )

		self.m_staticA41.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer352.Add( self.m_staticA41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA51 = wx.StaticText( self.m_panelA2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA51.Wrap( -1 )

		self.m_staticA51.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer352.Add( self.m_staticA51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA61 = wx.StaticText( self.m_panelA2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA61.Wrap( -1 )

		self.m_staticA61.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer352.Add( self.m_staticA61, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_listCtrl41 = wx.ListCtrl( self.m_panelA2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl41.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl41.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl41.SetBackgroundColour( wx.Colour( 91, 122, 54 ) )

		fgSizer352.Add( self.m_listCtrl41, 0, wx.ALL, 5 )

		self.m_listCtrl51 = wx.ListCtrl( self.m_panelA2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl51.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl51.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_listCtrl51.SetBackgroundColour( wx.Colour( 168, 207, 69 ) )

		fgSizer352.Add( self.m_listCtrl51, 0, wx.ALL, 5 )

		self.m_listCtrl61 = wx.ListCtrl( self.m_panelA2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl61.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl61.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_listCtrl61.SetBackgroundColour( wx.Colour( 185, 199, 130 ) )

		fgSizer352.Add( self.m_listCtrl61, 0, wx.ALL, 5 )


		bSizer611.Add( fgSizer352, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panelA2.SetSizer( bSizer611 )
		self.m_panelA2.Layout()
		bSizer611.Fit( self.m_panelA2 )
		bSizer58.Add( self.m_panelA2, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline51 = wx.StaticLine( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer58.Add( self.m_staticline51, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panelA11 = wx.Panel( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer632 = wx.BoxSizer( wx.VERTICAL )

		bSizer175 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticfromcircle21 = wx.StaticText( self.m_panelA11, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticfromcircle21.Wrap( -1 )

		self.m_staticfromcircle21.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer175.Add( self.m_staticfromcircle21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText407 = wx.StaticText( self.m_panelA11, wx.ID_ANY, u"\"kode dalam kurung adalah program studi untuk dipertimbangkan\"", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText407.Wrap( -1 )

		self.m_staticText407.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer175.Add( self.m_staticText407, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		bSizer632.Add( bSizer175, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer3511 = wx.FlexGridSizer( 4, 3, 0, 0 )
		fgSizer3511.SetFlexibleDirection( wx.BOTH )
		fgSizer3511.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticA71 = wx.StaticText( self.m_panelA11, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA71.Wrap( -1 )

		self.m_staticA71.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer3511.Add( self.m_staticA71, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA81 = wx.StaticText( self.m_panelA11, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA81.Wrap( -1 )

		self.m_staticA81.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer3511.Add( self.m_staticA81, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA91 = wx.StaticText( self.m_panelA11, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA91.Wrap( -1 )

		self.m_staticA91.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer3511.Add( self.m_staticA91, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.m_listCtrl71 = wx.ListCtrl( self.m_panelA11, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl71.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl71.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl71.SetBackgroundColour( wx.Colour( 91, 122, 54 ) )

		fgSizer3511.Add( self.m_listCtrl71, 0, wx.ALL, 5 )

		self.m_listCtrl81 = wx.ListCtrl( self.m_panelA11, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl81.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl81.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_listCtrl81.SetBackgroundColour( wx.Colour( 168, 207, 69 ) )

		fgSizer3511.Add( self.m_listCtrl81, 0, wx.ALL, 5 )

		self.m_listCtrl91 = wx.ListCtrl( self.m_panelA11, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl91.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl91.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_listCtrl91.SetBackgroundColour( wx.Colour( 185, 199, 130 ) )

		fgSizer3511.Add( self.m_listCtrl91, 0, wx.ALL, 5 )

		self.m_staticA101 = wx.StaticText( self.m_panelA11, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA101.Wrap( -1 )

		self.m_staticA101.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer3511.Add( self.m_staticA101, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA111 = wx.StaticText( self.m_panelA11, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA111.Wrap( -1 )

		self.m_staticA111.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer3511.Add( self.m_staticA111, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA121 = wx.StaticText( self.m_panelA11, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA121.Wrap( -1 )

		self.m_staticA121.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer3511.Add( self.m_staticA121, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_listCtrl101 = wx.ListCtrl( self.m_panelA11, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl101.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl101.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl101.SetBackgroundColour( wx.Colour( 91, 122, 54 ) )

		fgSizer3511.Add( self.m_listCtrl101, 0, wx.ALL, 5 )

		self.m_listCtrl111 = wx.ListCtrl( self.m_panelA11, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl111.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl111.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_listCtrl111.SetBackgroundColour( wx.Colour( 168, 207, 69 ) )

		fgSizer3511.Add( self.m_listCtrl111, 0, wx.ALL, 5 )

		self.m_listCtrl121 = wx.ListCtrl( self.m_panelA11, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl121.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl121.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_listCtrl121.SetBackgroundColour( wx.Colour( 185, 199, 130 ) )

		fgSizer3511.Add( self.m_listCtrl121, 0, wx.ALL, 5 )


		bSizer632.Add( fgSizer3511, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panelA11.SetSizer( bSizer632 )
		self.m_panelA11.Layout()
		bSizer632.Fit( self.m_panelA11 )
		bSizer58.Add( self.m_panelA11, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer174 = wx.BoxSizer( wx.VERTICAL )


		bSizer58.Add( bSizer174, 1, wx.EXPAND, 5 )


		self.m_scrolledWindow8.SetSizer( bSizer58 )
		self.m_scrolledWindow8.Layout()
		bSizer58.Fit( self.m_scrolledWindow8 )
		bSizer60.Add( self.m_scrolledWindow8, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer60 )
		self.Layout()

		# Connect Events
		self.m_buttonBersihkan.Bind( wx.EVT_BUTTON, self.m_buttonBersihkanOnButtonClick )
		self.m_SimpanPage6.Bind( wx.EVT_BUTTON, self.m_SimpanPage6OnButtonClick )
		self.tanggal_tes_input.Bind( wx.adv.EVT_DATE_CHANGED, self.tanggal_tes_inputOnDateChanged )
		self.nama_kandidat_input.Bind( wx.EVT_TEXT, self.nama_kandidat_inputOnText )
		self.jenis_kelamin_input.Bind( wx.EVT_CHOICE, self.jenis_kelamin_inputOnChoice )
		self.textctrl1.Bind( wx.EVT_ENTER_WINDOW, self.textctrl1OnEnterWindow )
		self.textctrl1.Bind( wx.EVT_TEXT, self.textctrl1OnText )
		self.label1.Bind( wx.EVT_ENTER_WINDOW, self.label1OnEnterWindow )
		self.textctrl2.Bind( wx.EVT_ENTER_WINDOW, self.textctrl2OnEnterWindow )
		self.textctrl2.Bind( wx.EVT_TEXT, self.textctrl2OnText )
		self.textctrl3.Bind( wx.EVT_ENTER_WINDOW, self.textctrl3OnEnterWindow )
		self.textctrl3.Bind( wx.EVT_TEXT, self.textctrl3OnText )
		self.textctrl4.Bind( wx.EVT_ENTER_WINDOW, self.textctrl4OnEnterWindow )
		self.textctrl4.Bind( wx.EVT_TEXT, self.textctrl4OnText )
		self.textctrl5.Bind( wx.EVT_ENTER_WINDOW, self.textctrl5OnEnterWindow )
		self.textctrl5.Bind( wx.EVT_TEXT, self.textctrl5OnText )
		self.textctrl6.Bind( wx.EVT_ENTER_WINDOW, self.textctrl6OnEnterWindow )
		self.textctrl6.Bind( wx.EVT_TEXT, self.textctrl6OnText )
		self.tanggal_tes_input1.Bind( wx.adv.EVT_DATE_CHANGED, self.tanggal_tes_inputOnDateChanged )
		self.nama_kandidat_input1.Bind( wx.EVT_TEXT, self.nama_kandidat_inputOnText )
		self.jenis_kelamin_input1.Bind( wx.EVT_CHOICE, self.jenis_kelamin_inputOnChoice )
		self.textctrl11.Bind( wx.EVT_ENTER_WINDOW, self.textctrl1OnEnterWindow )
		self.textctrl11.Bind( wx.EVT_TEXT, self.textctrl1OnText )
		self.label11.Bind( wx.EVT_ENTER_WINDOW, self.label1OnEnterWindow )
		self.textctrl21.Bind( wx.EVT_ENTER_WINDOW, self.textctrl2OnEnterWindow )
		self.textctrl21.Bind( wx.EVT_TEXT, self.textctrl2OnText )
		self.textctrl31.Bind( wx.EVT_ENTER_WINDOW, self.textctrl3OnEnterWindow )
		self.textctrl31.Bind( wx.EVT_TEXT, self.textctrl3OnText )
		self.textctrl41.Bind( wx.EVT_ENTER_WINDOW, self.textctrl4OnEnterWindow )
		self.textctrl41.Bind( wx.EVT_TEXT, self.textctrl4OnText )
		self.textctrl51.Bind( wx.EVT_ENTER_WINDOW, self.textctrl5OnEnterWindow )
		self.textctrl51.Bind( wx.EVT_TEXT, self.textctrl5OnText )
		self.textctrl61.Bind( wx.EVT_ENTER_WINDOW, self.textctrl6OnEnterWindow )
		self.textctrl61.Bind( wx.EVT_TEXT, self.textctrl6OnText )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_buttonBersihkanOnButtonClick( self, event ):
		event.Skip()

	def m_SimpanPage6OnButtonClick( self, event ):
		event.Skip()

	def tanggal_tes_inputOnDateChanged( self, event ):
		event.Skip()

	def nama_kandidat_inputOnText( self, event ):
		event.Skip()

	def jenis_kelamin_inputOnChoice( self, event ):
		event.Skip()

	def textctrl1OnEnterWindow( self, event ):
		event.Skip()

	def textctrl1OnText( self, event ):
		event.Skip()

	def label1OnEnterWindow( self, event ):
		event.Skip()

	def textctrl2OnEnterWindow( self, event ):
		event.Skip()

	def textctrl2OnText( self, event ):
		event.Skip()

	def textctrl3OnEnterWindow( self, event ):
		event.Skip()

	def textctrl3OnText( self, event ):
		event.Skip()

	def textctrl4OnEnterWindow( self, event ):
		event.Skip()

	def textctrl4OnText( self, event ):
		event.Skip()

	def textctrl5OnEnterWindow( self, event ):
		event.Skip()

	def textctrl5OnText( self, event ):
		event.Skip()

	def textctrl6OnEnterWindow( self, event ):
		event.Skip()

	def textctrl6OnText( self, event ):
		event.Skip()


















###########################################################################
## Class Page71
###########################################################################

class Page71 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1289,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer60 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow8 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow8.SetScrollRate( 5, 5 )
		self.m_scrolledWindow8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer58 = wx.BoxSizer( wx.VERTICAL )

		fgSizer29 = wx.FlexGridSizer( 1, 0, 0, 0 )
		fgSizer29.AddGrowableCol( 0 )
		fgSizer29.AddGrowableRow( 0 )
		fgSizer29.SetFlexibleDirection( wx.BOTH )
		fgSizer29.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_buttonBersihkan = wx.Button( self.m_scrolledWindow8, wx.ID_ANY, u"Hapuskan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonBersihkan.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer29.Add( self.m_buttonBersihkan, 0, wx.ALL, 5 )

		self.m_SimpanPage6 = wx.Button( self.m_scrolledWindow8, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_SimpanPage6.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_SimpanPage6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_SimpanPage6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer29.Add( self.m_SimpanPage6, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		bSizer58.Add( fgSizer29, 0, wx.ALIGN_RIGHT, 5 )

		fgSizer37 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer37.SetFlexibleDirection( wx.BOTH )
		fgSizer37.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel92 = wx.Panel( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel92.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel92.SetBackgroundColour( wx.Colour( 88, 85, 112 ) )

		bSizer119 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel97 = wx.Panel( self.m_panel92, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer125 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText212 = wx.StaticText( self.m_panel97, wx.ID_ANY, u"BIODATA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )

		self.m_staticText212.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )

		bSizer125.Add( self.m_staticText212, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel97.SetSizer( bSizer125 )
		self.m_panel97.Layout()
		bSizer125.Fit( self.m_panel97 )
		bSizer119.Add( self.m_panel97, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer4 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.no_tes = wx.StaticText( self.m_panel92, wx.ID_ANY, u"No Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.no_tes.Wrap( -1 )

		self.no_tes.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.no_tes, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.no_tes_input = wx.TextCtrl( self.m_panel92, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		self.no_tes_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.no_tes_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.tanggal_tes = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_tes.Wrap( -1 )

		self.tanggal_tes.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.tanggal_tes, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_tes_input = wx.adv.DatePickerCtrl( self.m_panel92, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		self.tanggal_tes_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.tanggal_tes_input, 0, wx.ALL, 5 )

		self.nama_kandidat = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Nama Kandidat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama_kandidat.Wrap( -1 )

		self.nama_kandidat.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.nama_kandidat, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nama_kandidat_input = wx.TextCtrl( self.m_panel92, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		self.nama_kandidat_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.nama_kandidat_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.jenis_kelamin = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jenis_kelamin.Wrap( -1 )

		self.jenis_kelamin.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.jenis_kelamin, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		jenis_kelamin_inputChoices = [ u"Laki-Laki", u"Perempuan" ]
		self.jenis_kelamin_input = wx.Choice( self.m_panel92, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, jenis_kelamin_inputChoices, 0 )
		self.jenis_kelamin_input.SetSelection( 1 )
		self.jenis_kelamin_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.jenis_kelamin_input, 0, wx.ALL, 5 )

		self.tanggal_lahir = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_lahir.Wrap( -1 )

		self.tanggal_lahir.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.tanggal_lahir, 0, wx.ALL, 5 )

		self.tanggal_lahir_input = wx.adv.DatePickerCtrl( self.m_panel92, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		self.tanggal_lahir_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.tanggal_lahir_input, 0, wx.ALL, 5 )

		self.pendidikan_terakhir = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Pendidikan Terakhir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pendidikan_terakhir.Wrap( -1 )

		self.pendidikan_terakhir.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.pendidikan_terakhir, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		pendidikan_terakhir_inputChoices = [ u"SD", u"SMP", u"SMA/Sederajat", u"S1", u"S2", u"S3" ]
		self.pendidikan_terakhir_input = wx.Choice( self.m_panel92, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pendidikan_terakhir_inputChoices, 0 )
		self.pendidikan_terakhir_input.SetSelection( 0 )
		self.pendidikan_terakhir_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.pendidikan_terakhir_input, 0, wx.ALL, 5 )

		self.jurusan = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Jurusan Pendidikan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan.Wrap( -1 )

		self.jurusan.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.jurusan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan_input = wx.TextCtrl( self.m_panel92, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.jurusan_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.jurusan_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.kota = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kota.Wrap( -1 )

		self.kota.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.kota, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kota_input = wx.TextCtrl( self.m_panel92, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.kota_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.kota_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.perusahaan_instansi = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Perusahaan/Instansi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.perusahaan_instansi.Wrap( -1 )

		self.perusahaan_instansi.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.perusahaan_instansi, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.perusahaan_instansi_input = wx.TextCtrl( self.m_panel92, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.perusahaan_instansi_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.perusahaan_instansi_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.posisi_jabatan = wx.StaticText( self.m_panel92, wx.ID_ANY, u"Posisi/Jabatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.posisi_jabatan.Wrap( -1 )

		self.posisi_jabatan.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer4.Add( self.posisi_jabatan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.posisi_jabatan_input = wx.TextCtrl( self.m_panel92, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.posisi_jabatan_input.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer4.Add( self.posisi_jabatan_input, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer119.Add( fgSizer4, 1, wx.EXPAND, 5 )


		self.m_panel92.SetSizer( bSizer119 )
		self.m_panel92.Layout()
		bSizer119.Fit( self.m_panel92 )
		fgSizer37.Add( self.m_panel92, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel93 = wx.Panel( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel93.Hide()

		bSizer121 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel98 = wx.Panel( self.m_panel93, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer126 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText213 = wx.StaticText( self.m_panel98, wx.ID_ANY, u"BIODATA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText213.Wrap( -1 )

		self.m_staticText213.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )

		bSizer126.Add( self.m_staticText213, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel98.SetSizer( bSizer126 )
		self.m_panel98.Layout()
		bSizer126.Fit( self.m_panel98 )
		bSizer121.Add( self.m_panel98, 0, wx.EXPAND |wx.ALL, 5 )

		fgSizer15 = wx.FlexGridSizer( 13, 2, 0, 1 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.nama2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama2.Wrap( -1 )

		self.nama2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.nama2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nama_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.nama_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.nama_input2, 0, wx.ALL, 5 )

		self.tanggal_tes2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_tes2.Wrap( -1 )

		self.tanggal_tes2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.tanggal_tes2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_tes_input2 = wx.adv.DatePickerCtrl( self.m_panel93, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		self.tanggal_tes_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.tanggal_tes_input2, 0, wx.ALL, 5 )

		self.jenis_kelamin2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jenis_kelamin2.Wrap( -1 )

		self.jenis_kelamin2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.jenis_kelamin2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		jenis_kelamin_input2Choices = [ u"Laki-Laki", u"Perempuan" ]
		self.jenis_kelamin_input2 = wx.Choice( self.m_panel93, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, jenis_kelamin_input2Choices, 0 )
		self.jenis_kelamin_input2.SetSelection( 1 )
		self.jenis_kelamin_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.jenis_kelamin_input2, 0, wx.ALL, 5 )

		self.tanggal_lahir2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_lahir2.Wrap( -1 )

		self.tanggal_lahir2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.tanggal_lahir2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_lahir_input2 = wx.adv.DatePickerCtrl( self.m_panel93, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		self.tanggal_lahir_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.tanggal_lahir_input2, 0, wx.ALL, 5 )

		self.asal_sekolah2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Asal Sekolah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asal_sekolah2.Wrap( -1 )

		self.asal_sekolah2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.asal_sekolah2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.asal_sekolah_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.asal_sekolah_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.asal_sekolah_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.jurusan21 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan21.Wrap( -1 )

		self.jurusan21.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.jurusan21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan_input21 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.jurusan_input21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.jurusan_input21, 0, wx.ALL|wx.EXPAND, 5 )

		self.asal_universitas2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Asal Universitas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asal_universitas2.Wrap( -1 )

		self.asal_universitas2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.asal_universitas2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.asal_universitas_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.asal_universitas_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.asal_universitas_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.jurusan2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan2.Wrap( -1 )

		self.jurusan2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.jurusan2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.jurusan_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.jurusan_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.kota2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kota2.Wrap( -1 )

		self.kota2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.kota2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kota_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.kota_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.kota_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.hobi2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Hobi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hobi2.Wrap( -1 )

		self.hobi2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.hobi2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.hobi_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.hobi_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.hobi_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.prestasi_akademik2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Prestasi Akademik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prestasi_akademik2.Wrap( -1 )

		self.prestasi_akademik2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.prestasi_akademik2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.prestasi_akademik_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.prestasi_akademik_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.prestasi_akademik_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.prestasi_non_akademik2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Prestasi Non Akademik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prestasi_non_akademik2.Wrap( -1 )

		self.prestasi_non_akademik2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.prestasi_non_akademik2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.prestasi_non_akademik_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.prestasi_non_akademik_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.prestasi_non_akademik_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.ekskul_yang_diikuti2 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Ekskul yang Diikuti", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ekskul_yang_diikuti2.Wrap( -1 )

		self.ekskul_yang_diikuti2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer15.Add( self.ekskul_yang_diikuti2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ekskul_yang_diikuti_input2 = wx.TextCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.ekskul_yang_diikuti_input2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer15.Add( self.ekskul_yang_diikuti_input2, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer121.Add( fgSizer15, 1, wx.EXPAND, 5 )


		self.m_panel93.SetSizer( bSizer121 )
		self.m_panel93.Layout()
		bSizer121.Fit( self.m_panel93 )
		fgSizer37.Add( self.m_panel93, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel91 = wx.Panel( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel91.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel91.SetBackgroundColour( wx.Colour( 125, 100, 139 ) )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel96 = wx.Panel( self.m_panel91, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer123 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self.m_panel96, wx.ID_ANY, u"OCCUPATIONAL DAYDREAM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Tw Cen MT" ) )

		bSizer123.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel96.SetSizer( bSizer123 )
		self.m_panel96.Layout()
		bSizer123.Fit( self.m_panel96 )
		bSizer10.Add( self.m_panel96, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel981 = wx.Panel( self.m_panel91, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel981.SetForegroundColour( wx.Colour( 249, 250, 249 ) )
		self.m_panel981.SetBackgroundColour( wx.Colour( 125, 100, 139 ) )

		bSizer631 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer71 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer71.AddGrowableCol( 1 )
		fgSizer71.SetFlexibleDirection( wx.BOTH )
		fgSizer71.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText8 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer71.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.textctrl1 = wx.TextCtrl( self.m_panel981, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.textctrl1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.textctrl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label1 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label1.Wrap( -1 )

		self.label1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.label1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText10 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer71.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.textctrl2 = wx.TextCtrl( self.m_panel981, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.textctrl2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.textctrl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label2 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label2.Wrap( -1 )

		self.label2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.label2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText132 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText132.Wrap( -1 )

		fgSizer71.Add( self.m_staticText132, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.textctrl3 = wx.TextCtrl( self.m_panel981, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.textctrl3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.textctrl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label3 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label3.Wrap( -1 )

		self.label3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.label3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText134 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText134.Wrap( -1 )

		fgSizer71.Add( self.m_staticText134, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textctrl4 = wx.TextCtrl( self.m_panel981, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.textctrl4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.textctrl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label4 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label4.Wrap( -1 )

		self.label4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.label4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText138 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText138.Wrap( -1 )

		fgSizer71.Add( self.m_staticText138, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.textctrl5 = wx.TextCtrl( self.m_panel981, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		self.textctrl5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.textctrl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label5 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label5.Wrap( -1 )

		self.label5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )

		fgSizer71.Add( self.label5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText139 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText139.Wrap( -1 )

		self.m_staticText139.Hide()

		fgSizer71.Add( self.m_staticText139, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.textctrl6 = wx.TextCtrl( self.m_panel981, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.textctrl6.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.textctrl6.Hide()

		fgSizer71.Add( self.textctrl6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.label6 = wx.StaticText( self.m_panel981, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label6.Wrap( -1 )

		self.label6.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Sans" ) )
		self.label6.Hide()

		fgSizer71.Add( self.label6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer631.Add( fgSizer71, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer64 = wx.BoxSizer( wx.VERTICAL )


		bSizer64.Add( ( 25, 0), 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer631.Add( bSizer64, 0, 0, 5 )


		self.m_panel981.SetSizer( bSizer631 )
		self.m_panel981.Layout()
		bSizer631.Fit( self.m_panel981 )
		bSizer10.Add( self.m_panel981, 0, wx.ALL, 5 )


		self.m_panel91.SetSizer( bSizer10 )
		self.m_panel91.Layout()
		bSizer10.Fit( self.m_panel91 )
		fgSizer37.Add( self.m_panel91, 0, wx.ALL, 5 )


		bSizer58.Add( fgSizer37, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panelA = wx.Panel( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelA.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer61 = wx.BoxSizer( wx.VERTICAL )

		self.m_statictextfromcircle1 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_statictextfromcircle1.Wrap( -1 )

		self.m_statictextfromcircle1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer61.Add( self.m_statictextfromcircle1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer35 = wx.FlexGridSizer( 4, 3, 0, 0 )
		fgSizer35.SetFlexibleDirection( wx.BOTH )
		fgSizer35.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticA = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA.Wrap( -1 )

		self.m_staticA.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_staticA, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA2 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA2.Wrap( -1 )

		self.m_staticA2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_staticA2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA3 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA3.Wrap( -1 )

		self.m_staticA3.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_staticA3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.m_listCtrl1 = wx.ListCtrl( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl1.SetBackgroundColour( wx.Colour( 82, 101, 140 ) )

		fgSizer35.Add( self.m_listCtrl1, 0, wx.ALL, 5 )

		self.m_listCtrl2 = wx.ListCtrl( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl2.SetBackgroundColour( wx.Colour( 150, 152, 154 ) )

		fgSizer35.Add( self.m_listCtrl2, 0, wx.ALL, 5 )

		self.m_listCtrl3 = wx.ListCtrl( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl3.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl3.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_listCtrl3.SetBackgroundColour( wx.Colour( 230, 231, 232 ) )

		fgSizer35.Add( self.m_listCtrl3, 0, wx.ALL, 5 )

		self.m_staticA4 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA4.Wrap( -1 )

		self.m_staticA4.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_staticA4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA5 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA5.Wrap( -1 )

		self.m_staticA5.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_staticA5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA6 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA6.Wrap( -1 )

		self.m_staticA6.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_staticA6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_listCtrl4 = wx.ListCtrl( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl4.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl4.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl4.SetBackgroundColour( wx.Colour( 82, 101, 140 ) )

		fgSizer35.Add( self.m_listCtrl4, 0, wx.ALL, 5 )

		self.m_listCtrl5 = wx.ListCtrl( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl5.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl5.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl5.SetBackgroundColour( wx.Colour( 150, 152, 154 ) )

		fgSizer35.Add( self.m_listCtrl5, 0, wx.ALL, 5 )


		bSizer61.Add( fgSizer35, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panelA.SetSizer( bSizer61 )
		self.m_panelA.Layout()
		bSizer61.Fit( self.m_panelA )
		bSizer58.Add( self.m_panelA, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline5 = wx.StaticLine( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer58.Add( self.m_staticline5, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_panelA1 = wx.Panel( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer63 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticfromcircle2 = wx.StaticText( self.m_panelA1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticfromcircle2.Wrap( -1 )

		self.m_staticfromcircle2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer63.Add( self.m_staticfromcircle2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer351 = wx.FlexGridSizer( 4, 3, 0, 0 )
		fgSizer351.SetFlexibleDirection( wx.BOTH )
		fgSizer351.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticA7 = wx.StaticText( self.m_panelA1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA7.Wrap( -1 )

		self.m_staticA7.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer351.Add( self.m_staticA7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA8 = wx.StaticText( self.m_panelA1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA8.Wrap( -1 )

		self.m_staticA8.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer351.Add( self.m_staticA8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA9 = wx.StaticText( self.m_panelA1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA9.Wrap( -1 )

		self.m_staticA9.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer351.Add( self.m_staticA9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.m_listCtrl7 = wx.ListCtrl( self.m_panelA1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl7.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl7.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl7.SetBackgroundColour( wx.Colour( 82, 101, 140 ) )

		fgSizer351.Add( self.m_listCtrl7, 0, wx.ALL, 5 )

		self.m_listCtrl8 = wx.ListCtrl( self.m_panelA1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl8.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl8.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl8.SetBackgroundColour( wx.Colour( 150, 152, 154 ) )

		fgSizer351.Add( self.m_listCtrl8, 0, wx.ALL, 5 )

		self.m_listCtrl9 = wx.ListCtrl( self.m_panelA1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl9.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl9.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_listCtrl9.SetBackgroundColour( wx.Colour( 230, 231, 232 ) )

		fgSizer351.Add( self.m_listCtrl9, 0, wx.ALL, 5 )

		self.m_staticA10 = wx.StaticText( self.m_panelA1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA10.Wrap( -1 )

		self.m_staticA10.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer351.Add( self.m_staticA10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA11 = wx.StaticText( self.m_panelA1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA11.Wrap( -1 )

		self.m_staticA11.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer351.Add( self.m_staticA11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA12 = wx.StaticText( self.m_panelA1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA12.Wrap( -1 )

		self.m_staticA12.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer351.Add( self.m_staticA12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_listCtrl10 = wx.ListCtrl( self.m_panelA1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl10.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl10.SetBackgroundColour( wx.Colour( 82, 101, 140 ) )

		fgSizer351.Add( self.m_listCtrl10, 0, wx.ALL, 5 )

		self.m_listCtrl11 = wx.ListCtrl( self.m_panelA1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl11.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl11.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_listCtrl11.SetBackgroundColour( wx.Colour( 150, 152, 154 ) )

		fgSizer351.Add( self.m_listCtrl11, 0, wx.ALL, 5 )

		self.m_listCtrl12 = wx.ListCtrl( self.m_panelA1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_AUTOARRANGE|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_listCtrl12.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )
		self.m_listCtrl12.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_listCtrl12.SetBackgroundColour( wx.Colour( 230, 231, 232 ) )

		fgSizer351.Add( self.m_listCtrl12, 0, wx.ALL, 5 )


		bSizer63.Add( fgSizer351, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panelA1.SetSizer( bSizer63 )
		self.m_panelA1.Layout()
		bSizer63.Fit( self.m_panelA1 )
		bSizer58.Add( self.m_panelA1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_scrolledWindow8.SetSizer( bSizer58 )
		self.m_scrolledWindow8.Layout()
		bSizer58.Fit( self.m_scrolledWindow8 )
		bSizer60.Add( self.m_scrolledWindow8, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer60 )
		self.Layout()

		# Connect Events
		self.m_buttonBersihkan.Bind( wx.EVT_BUTTON, self.m_buttonBersihkanOnButtonClick )
		self.m_SimpanPage6.Bind( wx.EVT_BUTTON, self.m_SimpanPage6OnButtonClick )
		self.tanggal_tes_input.Bind( wx.adv.EVT_DATE_CHANGED, self.tanggal_tes_inputOnDateChanged )
		self.nama_kandidat_input.Bind( wx.EVT_TEXT, self.nama_kandidat_inputOnText )
		self.jenis_kelamin_input.Bind( wx.EVT_CHOICE, self.jenis_kelamin_inputOnChoice )
		self.textctrl1.Bind( wx.EVT_ENTER_WINDOW, self.textctrl1OnEnterWindow )
		self.textctrl1.Bind( wx.EVT_TEXT, self.textctrl1OnText )
		self.label1.Bind( wx.EVT_ENTER_WINDOW, self.label1OnEnterWindow )
		self.textctrl2.Bind( wx.EVT_ENTER_WINDOW, self.textctrl2OnEnterWindow )
		self.textctrl2.Bind( wx.EVT_TEXT, self.textctrl2OnText )
		self.textctrl3.Bind( wx.EVT_ENTER_WINDOW, self.textctrl3OnEnterWindow )
		self.textctrl3.Bind( wx.EVT_TEXT, self.textctrl3OnText )
		self.textctrl4.Bind( wx.EVT_ENTER_WINDOW, self.textctrl4OnEnterWindow )
		self.textctrl4.Bind( wx.EVT_TEXT, self.textctrl4OnText )
		self.textctrl5.Bind( wx.EVT_ENTER_WINDOW, self.textctrl5OnEnterWindow )
		self.textctrl5.Bind( wx.EVT_TEXT, self.textctrl5OnText )
		self.textctrl6.Bind( wx.EVT_ENTER_WINDOW, self.textctrl6OnEnterWindow )
		self.textctrl6.Bind( wx.EVT_TEXT, self.textctrl6OnText )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_buttonBersihkanOnButtonClick( self, event ):
		event.Skip()

	def m_SimpanPage6OnButtonClick( self, event ):
		event.Skip()

	def tanggal_tes_inputOnDateChanged( self, event ):
		event.Skip()

	def nama_kandidat_inputOnText( self, event ):
		event.Skip()

	def jenis_kelamin_inputOnChoice( self, event ):
		event.Skip()

	def textctrl1OnEnterWindow( self, event ):
		event.Skip()

	def textctrl1OnText( self, event ):
		event.Skip()

	def label1OnEnterWindow( self, event ):
		event.Skip()

	def textctrl2OnEnterWindow( self, event ):
		event.Skip()

	def textctrl2OnText( self, event ):
		event.Skip()

	def textctrl3OnEnterWindow( self, event ):
		event.Skip()

	def textctrl3OnText( self, event ):
		event.Skip()

	def textctrl4OnEnterWindow( self, event ):
		event.Skip()

	def textctrl4OnText( self, event ):
		event.Skip()

	def textctrl5OnEnterWindow( self, event ):
		event.Skip()

	def textctrl5OnText( self, event ):
		event.Skip()

	def textctrl6OnEnterWindow( self, event ):
		event.Skip()

	def textctrl6OnText( self, event ):
		event.Skip()


###########################################################################
## Class OccupationFinder
###########################################################################

class OccupationFinder ( main ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		main.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer17 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer17.AddGrowableCol( 0 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_searchCtrl2 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.m_searchCtrl2.ShowSearchButton( True )
		self.m_searchCtrl2.ShowCancelButton( False )
		fgSizer17.Add( self.m_searchCtrl2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.nomor_jawaban = wx.StaticText( self, wx.ID_ANY, u"Nomor Jawaban", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nomor_jawaban.Wrap( -1 )

		fgSizer17.Add( self.nomor_jawaban, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_choice4Choices = [ u"1", u"2", u"3", u"4", u"5", u"6", u"7", wx.EmptyString ]
		self.m_choice4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 4 )
		fgSizer17.Add( self.m_choice4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.OccupationF_tombol_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.OccupationF_tombol_ok, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer27.Add( fgSizer17, 1, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer11.Add( bSizer27, 0, wx.EXPAND, 5 )

		m_listBox3Choices = [ u"1", u"2", u"3", u"4", u"5", u"6", wx.EmptyString ]
		self.m_listBox3 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox3Choices, wx.LB_ALWAYS_SB )
		bSizer11.Add( self.m_listBox3, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		# Connect Events
		self.OccupationF_tombol_ok.Bind( wx.EVT_BUTTON, self.OccupationF_tombol_okOnButtonClick )
		self.m_listBox3.Bind( wx.EVT_LISTBOX_DCLICK, self.btn_occupationfinder )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OccupationF_tombol_okOnButtonClick( self, event ):
		event.Skip()

	def btn_occupationfinder( self, event ):
		event.Skip()


###########################################################################
## Class Page4altern
###########################################################################

class Page4altern ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer5 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer5.AddGrowableCol( 0 )
		fgSizer5.AddGrowableRow( 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_grid6 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid6.CreateGrid( 20, 20 )
		self.m_grid6.EnableEditing( True )
		self.m_grid6.EnableGridLines( True )
		self.m_grid6.EnableDragGridSize( False )
		self.m_grid6.SetMargins( 0, 0 )

		# Columns
		self.m_grid6.EnableDragColMove( False )
		self.m_grid6.EnableDragColSize( True )
		self.m_grid6.SetColLabelSize( 30 )
		self.m_grid6.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid6.EnableDragRowSize( True )
		self.m_grid6.SetRowLabelSize( 80 )
		self.m_grid6.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid6.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer5.Add( self.m_grid6, 5, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( fgSizer5 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class WindowsOpenFilter
###########################################################################

class WindowsOpenFilter ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer50 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel20 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText206 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Filter pilihan anda berdasarkan kriteria berikut ini", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText206.Wrap( -1 )

		self.m_staticText206.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Sans" ) )

		bSizer51.Add( self.m_staticText206, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline2 = wx.StaticLine( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer51.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer51.Add( ( 0, 20), 0, 0, 5 )

		self.m_staticText207 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Tanggal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText207.Wrap( -1 )

		bSizer51.Add( self.m_staticText207, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer39 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer39.SetFlexibleDirection( wx.BOTH )
		fgSizer39.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText209 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Dari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText209.Wrap( -1 )

		fgSizer39.Add( self.m_staticText209, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_datePickerdaritgl = wx.adv.DatePickerCtrl( self.m_panel20, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 125,-1 ), wx.adv.DP_DEFAULT|wx.TAB_TRAVERSAL )
		fgSizer39.Add( self.m_datePickerdaritgl, 0, wx.ALL, 5 )

		self.m_staticText210 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Sampai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText210.Wrap( -1 )

		fgSizer39.Add( self.m_staticText210, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_datePickersampaitgl = wx.adv.DatePickerCtrl( self.m_panel20, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 125,-1 ), wx.adv.DP_DEFAULT|wx.TAB_TRAVERSAL )
		fgSizer39.Add( self.m_datePickersampaitgl, 0, wx.ALL, 5 )


		bSizer51.Add( fgSizer39, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_buttonKlikFilterTanggal = wx.Button( self.m_panel20, wx.ID_ANY, u"Klik Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.m_buttonKlikFilterTanggal, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer51.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText208 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Nama Orang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText208.Wrap( -1 )

		bSizer51.Add( self.m_staticText208, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_textCtrlnamaorang = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0|wx.TAB_TRAVERSAL )
		bSizer51.Add( self.m_textCtrlnamaorang, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_buttonKlikFilterOrang = wx.Button( self.m_panel20, wx.ID_ANY, u"Klik Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.m_buttonKlikFilterOrang, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline3 = wx.StaticLine( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer51.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText211 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Nomor Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )

		bSizer51.Add( self.m_staticText211, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrlnomortes = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0|wx.TAB_TRAVERSAL )
		bSizer51.Add( self.m_textCtrlnomortes, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_buttonKlikFilterNoTes = wx.Button( self.m_panel20, wx.ID_ANY, u"Klik Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.m_buttonKlikFilterNoTes, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer40 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer40.AddGrowableCol( 0 )
		fgSizer40.AddGrowableRow( 0 )
		fgSizer40.SetFlexibleDirection( wx.BOTH )
		fgSizer40.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticline4 = wx.StaticLine( self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer40.Add( self.m_staticline4, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_buttonFilterBatal = wx.Button( self.m_panel20, wx.ID_ANY, u"Batal", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer40.Add( self.m_buttonFilterBatal, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )


		bSizer51.Add( fgSizer40, 1, wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		self.m_panel20.SetSizer( bSizer51 )
		self.m_panel20.Layout()
		bSizer51.Fit( self.m_panel20 )
		bSizer50.Add( self.m_panel20, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer50 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonKlikFilterTanggal.Bind( wx.EVT_BUTTON, self.m_buttonKlikFilterTanggalOnButtonClick )
		self.m_buttonKlikFilterOrang.Bind( wx.EVT_BUTTON, self.m_buttonKlikFilterOrangOnButtonClick )
		self.m_buttonKlikFilterNoTes.Bind( wx.EVT_BUTTON, self.m_buttonKlikFilterNoTesOnButtonClick )
		self.m_buttonFilterBatal.Bind( wx.EVT_BUTTON, self.m_buttonFilterBatalOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_buttonKlikFilterTanggalOnButtonClick( self, event ):
		event.Skip()

	def m_buttonKlikFilterOrangOnButtonClick( self, event ):
		event.Skip()

	def m_buttonKlikFilterNoTesOnButtonClick( self, event ):
		event.Skip()

	def m_buttonFilterBatalOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class RincianData
###########################################################################

class RincianData ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		self.m_panelRincianData = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelRincianData.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer53 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText212 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Rincian Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )

		bSizer53.Add( self.m_staticText212, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer42 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer42.AddGrowableCol( 1 )
		fgSizer42.SetFlexibleDirection( wx.BOTH )
		fgSizer42.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText213 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"No Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText213.Wrap( -1 )

		fgSizer42.Add( self.m_staticText213, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.notes = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.notes, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText214 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText214.Wrap( -1 )

		fgSizer42.Add( self.m_staticText214, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_tes = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.tanggal_tes, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText215 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Nama Kandidat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText215.Wrap( -1 )

		fgSizer42.Add( self.m_staticText215, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nama_kandidat = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.nama_kandidat, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText216 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText216.Wrap( -1 )

		fgSizer42.Add( self.m_staticText216, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jenis_kelamin = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.jenis_kelamin, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText217 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText217.Wrap( -1 )

		fgSizer42.Add( self.m_staticText217, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_lahir = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.tanggal_lahir, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText218 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Pendidikan Terakhir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText218.Wrap( -1 )

		fgSizer42.Add( self.m_staticText218, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.pendidikan_terakhir = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.pendidikan_terakhir, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText219 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText219.Wrap( -1 )

		fgSizer42.Add( self.m_staticText219, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.jurusan, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText220 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText220.Wrap( -1 )

		fgSizer42.Add( self.m_staticText220, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kota = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.kota, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText221 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Perusahaan / Instansi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )

		fgSizer42.Add( self.m_staticText221, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.perusahaan_instansi = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.perusahaan_instansi, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText222 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Posisi / Jabatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText222.Wrap( -1 )

		fgSizer42.Add( self.m_staticText222, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.posisi_jabatan = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.posisi_jabatan, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer53.Add( fgSizer42, 1, wx.EXPAND, 5 )

		fgSizer421 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer421.AddGrowableCol( 0 )
		fgSizer421.SetFlexibleDirection( wx.BOTH )
		fgSizer421.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_buttonHapus = wx.Button( self.m_panelRincianData, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer421.Add( self.m_buttonHapus, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_buttonTutupDetail = wx.Button( self.m_panelRincianData, wx.ID_ANY, u"Tutup", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer421.Add( self.m_buttonTutupDetail, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer53.Add( fgSizer421, 1, wx.EXPAND, 5 )


		self.m_panelRincianData.SetSizer( bSizer53 )
		self.m_panelRincianData.Layout()
		bSizer53.Fit( self.m_panelRincianData )
		bSizer52.Add( self.m_panelRincianData, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer52 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonHapus.Bind( wx.EVT_BUTTON, self.m_buttonHapusOnButtonClick )
		self.m_buttonTutupDetail.Bind( wx.EVT_BUTTON, self.m_buttonTutupDetailOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_buttonHapusOnButtonClick( self, event ):
		event.Skip()

	def m_buttonTutupDetailOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class RincianDataTes
###########################################################################

class RincianDataTes ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,625 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		self.m_panelRincianData = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelRincianData.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer53 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText212 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Rincian Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )

		bSizer53.Add( self.m_staticText212, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer42 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer42.AddGrowableCol( 1 )
		fgSizer42.SetFlexibleDirection( wx.BOTH )
		fgSizer42.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText213 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText213.Wrap( -1 )

		fgSizer42.Add( self.m_staticText213, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nama = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.nama, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText214 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText214.Wrap( -1 )

		fgSizer42.Add( self.m_staticText214, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_tes = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.tanggal_tes, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText216 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText216.Wrap( -1 )

		fgSizer42.Add( self.m_staticText216, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jenis_kelamin = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.jenis_kelamin, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText217 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText217.Wrap( -1 )

		fgSizer42.Add( self.m_staticText217, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_lahir = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.tanggal_lahir, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText218 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Asal Sekolah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText218.Wrap( -1 )

		fgSizer42.Add( self.m_staticText218, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.asal_sekolah = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.asal_sekolah, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText219 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText219.Wrap( -1 )

		fgSizer42.Add( self.m_staticText219, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.jurusan, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText245 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Asal Universitas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText245.Wrap( -1 )

		fgSizer42.Add( self.m_staticText245, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.asal_universitas = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer42.Add( self.asal_universitas, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText246 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText246.Wrap( -1 )

		fgSizer42.Add( self.m_staticText246, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan2 = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer42.Add( self.jurusan2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText220 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText220.Wrap( -1 )

		fgSizer42.Add( self.m_staticText220, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kota = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.kota, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText221 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Hobi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )

		fgSizer42.Add( self.m_staticText221, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.hobi = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.hobi, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText222 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Prestasi Akademik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText222.Wrap( -1 )

		fgSizer42.Add( self.m_staticText222, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.prestasi_akademik = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer42.Add( self.prestasi_akademik, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText247 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Prestasi Non Akademik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText247.Wrap( -1 )

		fgSizer42.Add( self.m_staticText247, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.prestasi_non_akademik = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer42.Add( self.prestasi_non_akademik, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText249 = wx.StaticText( self.m_panelRincianData, wx.ID_ANY, u"Ekskul Yang Diikuti", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText249.Wrap( -1 )

		fgSizer42.Add( self.m_staticText249, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.ekskul_yang_diikuti = wx.TextCtrl( self.m_panelRincianData, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer42.Add( self.ekskul_yang_diikuti, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer53.Add( fgSizer42, 1, wx.EXPAND, 5 )

		fgSizer421 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer421.AddGrowableCol( 0 )
		fgSizer421.AddGrowableCol( 1 )
		fgSizer421.AddGrowableRow( 0 )
		fgSizer421.SetFlexibleDirection( wx.BOTH )
		fgSizer421.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_buttonHapus = wx.Button( self.m_panelRincianData, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer421.Add( self.m_buttonHapus, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_buttonTutupDetail = wx.Button( self.m_panelRincianData, wx.ID_ANY, u"Tutup", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer421.Add( self.m_buttonTutupDetail, 1, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM, 5 )


		bSizer53.Add( fgSizer421, 1, wx.EXPAND, 5 )


		self.m_panelRincianData.SetSizer( bSizer53 )
		self.m_panelRincianData.Layout()
		bSizer53.Fit( self.m_panelRincianData )
		bSizer52.Add( self.m_panelRincianData, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer52 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonHapus.Bind( wx.EVT_BUTTON, self.m_buttonHapusOnButtonClick )
		self.m_buttonTutupDetail.Bind( wx.EVT_BUTTON, self.m_buttonTutupDetailOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_buttonHapusOnButtonClick( self, event ):
		event.Skip()

	def m_buttonTutupDetailOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class DataPeserta
###########################################################################

class DataPeserta ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel22 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel22.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		fgSizer37 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer37.SetFlexibleDirection( wx.BOTH )
		fgSizer37.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_buttonLihatDataBulanIni = wx.Button( self.m_panel22, wx.ID_ANY, u"Data Bulan ini", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonLihatDataBulanIni.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer37.Add( self.m_buttonLihatDataBulanIni, 0, wx.ALL, 5 )

		self.m_buttonLihatNilai = wx.Button( self.m_panel22, wx.ID_ANY, u"Lihat Nilai", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer37.Add( self.m_buttonLihatNilai, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )

		self.m_buttonDetail = wx.Button( self.m_panel22, wx.ID_ANY, u"Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer37.Add( self.m_buttonDetail, 1, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_filter = wx.Button( self.m_panel22, wx.ID_ANY, u"Pilihan Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer37.Add( self.m_filter, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer42.Add( fgSizer37, 0, 0, 5 )

		self.m_ListDataPeserta = wx.ListCtrl( self.m_panel22, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		self.m_ListDataPeserta.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer42.Add( self.m_ListDataPeserta, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel22.SetSizer( bSizer42 )
		self.m_panel22.Layout()
		bSizer42.Fit( self.m_panel22 )
		bSizer41.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonLihatDataBulanIni.Bind( wx.EVT_BUTTON, self.m_buttonLihatDataBulanIniOnButtonClick )
		self.m_buttonLihatNilai.Bind( wx.EVT_BUTTON, self.m_buttonLihatNilaiOnButtonClick )
		self.m_buttonDetail.Bind( wx.EVT_BUTTON, self.m_buttonDetailOnButtonClick )
		self.m_filter.Bind( wx.EVT_BUTTON, self.m_filterOnButtonClick )
		self.m_ListDataPeserta.Bind( wx.EVT_LIST_ITEM_SELECTED, self.m_ListDataPesertaOnListItemSelected )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_buttonLihatDataBulanIniOnButtonClick( self, event ):
		event.Skip()

	def m_buttonLihatNilaiOnButtonClick( self, event ):
		event.Skip()

	def m_buttonDetailOnButtonClick( self, event ):
		event.Skip()

	def m_filterOnButtonClick( self, event ):
		event.Skip()

	def m_ListDataPesertaOnListItemSelected( self, event ):
		event.Skip()


###########################################################################
## Class DataPesertaTes
###########################################################################

class DataPesertaTes ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel22 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel22.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		fgSizer37 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer37.SetFlexibleDirection( wx.BOTH )
		fgSizer37.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_buttonLihatDataBulanIni = wx.Button( self.m_panel22, wx.ID_ANY, u"Data Bulan Ini", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer37.Add( self.m_buttonLihatDataBulanIni, 0, wx.ALL, 5 )

		self.m_buttonLihatNilai = wx.Button( self.m_panel22, wx.ID_ANY, u"Lihat Nilai", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer37.Add( self.m_buttonLihatNilai, 0, wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )

		self.m_buttonDetail = wx.Button( self.m_panel22, wx.ID_ANY, u"Detail", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer37.Add( self.m_buttonDetail, 1, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_filter = wx.Button( self.m_panel22, wx.ID_ANY, u"Pilihan Filter", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer37.Add( self.m_filter, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer42.Add( fgSizer37, 0, 0, 5 )

		self.m_ListDataPeserta = wx.ListCtrl( self.m_panel22, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		self.m_ListDataPeserta.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer42.Add( self.m_ListDataPeserta, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel22.SetSizer( bSizer42 )
		self.m_panel22.Layout()
		bSizer42.Fit( self.m_panel22 )
		bSizer41.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer41 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonLihatDataBulanIni.Bind( wx.EVT_BUTTON, self.m_buttonLihatDataBulanIniOnButtonClick )
		self.m_buttonLihatNilai.Bind( wx.EVT_BUTTON, self.m_buttonLihatNilaiOnButtonClick )
		self.m_buttonDetail.Bind( wx.EVT_BUTTON, self.m_buttonDetailOnButtonClick )
		self.m_filter.Bind( wx.EVT_BUTTON, self.m_filterOnButtonClick )
		self.m_ListDataPeserta.Bind( wx.EVT_LIST_ITEM_SELECTED, self.m_ListDataPesertaOnListItemSelected )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_buttonLihatDataBulanIniOnButtonClick( self, event ):
		event.Skip()

	def m_buttonLihatNilaiOnButtonClick( self, event ):
		event.Skip()

	def m_buttonDetailOnButtonClick( self, event ):
		event.Skip()

	def m_filterOnButtonClick( self, event ):
		event.Skip()

	def m_ListDataPesertaOnListItemSelected( self, event ):
		event.Skip()


###########################################################################
## Class DialogError
###########################################################################

class DialogError ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer43 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel26 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel26.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer55 = wx.BoxSizer( wx.VERTICAL )

		self.m_StaticTextError = wx.StaticText( self.m_panel26, wx.ID_ANY, u"Anda salah input", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_StaticTextError.Wrap( -1 )

		self.m_StaticTextError.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer55.Add( self.m_StaticTextError, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_okuntukerror = wx.Button( self.m_panel26, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_okuntukerror.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer55.Add( self.m_okuntukerror, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel26.SetSizer( bSizer55 )
		self.m_panel26.Layout()
		bSizer55.Fit( self.m_panel26 )
		bSizer43.Add( self.m_panel26, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer43 )
		self.Layout()
		bSizer43.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_okuntukerror.Bind( wx.EVT_BUTTON, self.m_okuntukerrorOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_okuntukerrorOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class MatPlotLibFrame
###########################################################################

class MatPlotLibFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer46 = wx.BoxSizer( wx.VERTICAL )

		from AppsSDS.MplotLib import MatplotPanel
		self.m_MatplotPanel=MatplotPanel(self)
		bSizer46.Add( self.m_MatplotPanel, 0, wx.ALL, 5 )


		self.SetSizer( bSizer46 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class PageAResult
###########################################################################

class PageAResult ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer55 = wx.BoxSizer( wx.VERTICAL )

		self.m_panelA = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelA.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35 = wx.FlexGridSizer( 4, 3, 0, 0 )
		fgSizer35.AddGrowableCol( 0 )
		fgSizer35.AddGrowableCol( 1 )
		fgSizer35.AddGrowableCol( 2 )
		fgSizer35.AddGrowableRow( 1 )
		fgSizer35.AddGrowableRow( 3 )
		fgSizer35.SetFlexibleDirection( wx.BOTH )
		fgSizer35.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticA = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA.Wrap( -1 )

		fgSizer35.Add( self.m_staticA, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA2 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA2.Wrap( -1 )

		fgSizer35.Add( self.m_staticA2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA3 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA3.Wrap( -1 )

		fgSizer35.Add( self.m_staticA3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		m_listBoxA1Choices = []
		self.m_listBoxA1 = wx.ListBox( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxA1Choices, 0 )
		self.m_listBoxA1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_listBoxA1, 1, wx.ALL|wx.EXPAND, 5 )

		m_listBoxA2Choices = []
		self.m_listBoxA2 = wx.ListBox( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxA2Choices, 0 )
		self.m_listBoxA2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_listBoxA2, 1, wx.ALL|wx.EXPAND, 5 )

		m_listBoxA3Choices = []
		self.m_listBoxA3 = wx.ListBox( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxA3Choices, 0 )
		self.m_listBoxA3.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_listBoxA3, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticA4 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA4.Wrap( -1 )

		fgSizer35.Add( self.m_staticA4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA5 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA5.Wrap( -1 )

		fgSizer35.Add( self.m_staticA5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticA6 = wx.StaticText( self.m_panelA, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticA6.Wrap( -1 )

		self.m_staticA6.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_staticA6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_listBoxA4Choices = []
		self.m_listBoxA4 = wx.ListBox( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxA4Choices, 0 )
		self.m_listBoxA4.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_listBoxA4, 1, wx.ALL|wx.EXPAND, 5 )

		m_listBoxA5Choices = []
		self.m_listBoxA5 = wx.ListBox( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxA5Choices, 0 )
		self.m_listBoxA5.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_listBoxA5, 1, wx.ALL|wx.EXPAND, 5 )

		m_listBoxA6Choices = []
		self.m_listBoxA6 = wx.ListBox( self.m_panelA, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxA6Choices, 0 )
		self.m_listBoxA6.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		fgSizer35.Add( self.m_listBoxA6, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panelA.SetSizer( fgSizer35 )
		self.m_panelA.Layout()
		fgSizer35.Fit( self.m_panelA )
		bSizer55.Add( self.m_panelA, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer55 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class Listbox1
###########################################################################

class Listbox1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cari Pekerjaan", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer117 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer118 = wx.BoxSizer( wx.VERTICAL )

		bSizer119 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer119.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer119.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl1.SetMaxLength( 0 )
		self.m_textCtrl1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Tw Cen MT" ) )

		bSizer119.Add( self.m_textCtrl1, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button3 = wx.Button( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer119.Add( self.m_button3, 0, wx.ALL, 5 )


		bSizer118.Add( bSizer119, 0, wx.EXPAND, 5 )

		m_listBox1Choices = [ u"list&of&occupation" ]
		self.m_listBox1 = wx.ListBox( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, wx.LB_NEEDED_SB|wx.LB_SORT )
		bSizer118.Add( self.m_listBox1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_listCtrl17 = wx.ListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		bSizer118.Add( self.m_listCtrl17, 0, wx.ALL, 5 )

		fgSizer40 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer40.AddGrowableCol( 0 )
		fgSizer40.AddGrowableCol( 1 )
		fgSizer40.AddGrowableRow( 0 )
		fgSizer40.SetFlexibleDirection( wx.BOTH )
		fgSizer40.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.cancel = wx.Button( self.m_panel1, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer40.Add( self.cancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.ok = wx.Button( self.m_panel1, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer40.Add( self.ok, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer118.Add( fgSizer40, 0, wx.EXPAND|wx.ALIGN_RIGHT, 5 )


		self.m_panel1.SetSizer( bSizer118 )
		self.m_panel1.Layout()
		bSizer118.Fit( self.m_panel1 )
		bSizer117.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer117 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


