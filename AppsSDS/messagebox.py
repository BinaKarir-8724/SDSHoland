#!/usr/bin/python
import wx


class MessBx(wx.MessageDialog):
    
    def __init__(self, *args, **kwds):
        wx.MessageDialog.__init__(self, *args, **kwds)
        self.judul = "BINAKARIR"
        self.pesan = "Apakah anda ingin menutup aplikasi"

        self.SetTitle(self.judul)
        self.SetMessage(self.pesan)
        
        self.SetOKCancelLabels("Iya", "Tidak")

    def getiddestroy(self):
        
        return self.ShowModal()   
    
    
if __name__ == "__main__":
    root = wx.App()
    frame = MessBx(None, "", style=wx.OK | wx.CANCEL)
    root.MainLoop()
    
