'''
Created on Feb 16, 2019

@author: binakarir
'''

import wx


class Warningid(wx.Frame):
    
    def __init__(self, parent):
        super(Warningid, self).__init__(parent)
        self.SetTitle("Binakarir")
        self.SetSize(200, 110)
        # self.SetWindowStyleFlag(wx.STAY_ON_TOP|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
        
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Data tidak akurat", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        bSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer1 = wx.FlexGridSizer(0, 1, 0, 0)
        fgSizer1.AddGrowableCol(0)
        fgSizer1.AddGrowableRow(0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.m_button1 = wx.Button(self.m_panel1, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.m_button1, 0, wx.ALL | wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer2.Add(fgSizer1, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.m_button1OnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def m_button1OnButtonClick(self, event):
        self.Close()
        event.Skip()

