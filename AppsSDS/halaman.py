'''
Created on Jan 4, 2019

@author: binakarir
'''
import wx


class Halaman2():
    
    def __init__(self, parent):
        self.hal2 = parent
        
        self.hal2.panel_radiobtn_halaman1.Hide()
        self.hal2.m_panel1.SetBackgroundColour(wx.Colour(91, 85, 112))
        self.hal2.SetBackgroundColour(wx.Colour(91, 85, 112))
        self.hal2.m_panel9.SetBackgroundColour(wx.Colour(91, 85, 112))
#         self.hal2.m_button2.SetForegroundColour( wx.Colour( 62, 60, 60 ) )
#         self.hal2.m_button2.SetBackgroundColour( wx.Colour( 101, 236, 101 ) )

        self.hal2.halaman1.Hide()
        self.hal2.halaman2.Show()
        self.hal2.m_button1.Enable()
        self.hal2.m_button3.Enable()

        print ("halaman 2")


class Halaman3():
    
    def __init__(self, parent):
        self.hal3 = parent
        self.hal3.halaman2.Hide()
        self.hal3.halaman3.Show()

        # self.hal3.m_panel1.SetBackgroundColour( wx.Colour( 91, 85, 112 ) )
        # self.hal3.SetBackgroundColour( wx.Colour( 91, 85, 112 ) )
        # self.hal3.m_panel9.SetBackgroundColour( wx.Colour( 91, 85, 112 ) )
#       print ("halaman 3")
        
        
class Halaman4():
    
    def __init__(self, parent):
    
        self.hal4 = parent
        self.hal4.halaman3.Hide()
        self.hal4.halaman4.Show()
#         self.hal4.m_panel1.SetBackgroundColour( wx.Colour( 4, 109, 64 ) )
#         self.hal4.SetBackgroundColour( wx.Colour( 4, 109, 64 ) )
#         self.hal4.m_panel9.SetBackgroundColour( wx.Colour( 4, 109, 64 ) )
        print ("halaman 4")


class Halaman5():
        
    def __init__(self, parent):
        self.hal5 = parent
        self.hal5.halaman4.Hide()
        self.hal5.halaman5.Show()
#         self.hal5.m_panel1.SetBackgroundColour( wx.Colour( 4, 109, 64 ) )
#         self.hal5.SetBackgroundColour( wx.Colour( 4, 109, 64 ) )
#         self.hal5.m_panel9.SetBackgroundColour( wx.Colour( 4, 109, 64 ) )
#         self.hal5.m_button2.Disable()
        print ("halaman 5")

        
class Halaman6():
        
    def __init__(self, parent):
        self.hal6 = parent
        self.hal6.halaman5.Hide()
        self.hal6.halaman6.Show()
#         self.hal6.m_panel1.SetBackgroundColour( wx.Colour( 4, 109, 64 ) )
#         self.hal6.SetBackgroundColour( wx.Colour( 4, 109, 64 ) )
#         self.hal6.m_panel9.SetBackgroundColour( wx.Colour( 4, 109, 64 ) )
#         self.hal6.m_button2.Disable()
        print ("halaman 6")

        
class Halaman7():
         
    def __init__(self, parent):
        self.hal7 = parent
        self.hal7.halaman6.Hide()
        self.hal7.halaman7.Show()
        self.hal7.m_button2.Disable()


class Halaman1m():
        
    def __init__(self, parent):
        self.hal1 = parent
        self.hal1.panel_radiobtn_halaman1.Show()
        self.hal1.halaman1.Show()
        self.hal1.halaman2.Hide()
        self.hal1.halaman3.Hide()
        self.hal1.halaman4.Hide()
        self.hal1.halaman5.Hide()
        self.hal1.halaman6.Hide()
        self.hal1.halaman7.Hide()

        self.hal1.m_button1.Disable()
        self.hal1.m_button3.Disable()
        self.hal1.m_button2.Enable()
        self.hal1.m_panel1.SetBackgroundColour(wx.Colour(210, 211, 213))
        self.hal1.SetBackgroundColour(wx.Colour(210, 211, 213))
        self.hal1.m_panel9.SetBackgroundColour(wx.Colour(210, 211, 213))
        self.hal1.Refresh()

        self.hal1.Layout()
        print ("halaman 1")
        pass

    
class Halaman2m():

    def __init__(self, parent):
        
        self.hal2 = parent
        self.hal2.halaman2.Show()
        self.hal2.halaman3.Hide()
        
    
class Halaman3m():
        
    def __init__(self, parent):
        self.hal3 = parent
        self.hal3.halaman4.Hide()
        self.hal3.halaman3.Show()
        
        print ("halaman 2")
        pass

    
class Halaman4m():
        
    def __init__(self, parent):
        self.hal4 = parent
        self.hal4.halaman4.Show()
        self.hal4.halaman5.Hide()
#         self.hal4.m_button2.Enable()
        print ("halaman4")
        pass


class Halaman5m():
        
    def __init__(self, parent):
        self.hal5 = parent
        self.hal5.halaman5.Show()
        self.hal5.halaman6.Hide()
        print ("halaman5")
        pass

 
class Halaman6m():

    def __init__(self, parent):
        self.hal6 = parent
        self.hal6.halaman6.Show()
        self.hal6.halaman7.Hide()
        self.hal6.m_button2.Enable()
 
        print('halaman6')
 
        pass

        
