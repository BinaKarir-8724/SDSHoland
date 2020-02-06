'''
Created on Jan 9, 2019

@author: binakarir
'''
import wx
# import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas


class MatplotPanelA(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
       
        self.sizer = wx.BoxSizer(wx.VERTICAL)
         
        self.figure = Figure()
# 
#         self.axes1 = self.figure.add_subplot(111)
# #         self.axes2 = self.figure.add_subplot(111)
# 
#         self.x = ("R","I","A","S","E","C")
#         self.y = (1,2,3,4,5,6)
#         self.y1 = (2,3,4,5,6,7)
#         self.y2 = (2,3,4,5,6,7)
#         self.y3 = (2,3,4,5,6,7)
#         self.y4 = (2,3,4,5,6,7)
#         self.ysum=self.y4
#         
# 
# #         self.axes1.hist(self.x,50,normed=1, facecolor='blue', alpha=0.75,label="contoh a")
# #         self.axes1.hist(self.x, facecolor='blue', label="contoh a")
#         
#         self.axes1.plot(self.x,self.y,'-bo',label ="contoh a")
#         self.axes1.plot(self.x,self.y1,marker='o',color='#8D1C70',label ="contoh b")
#          
# #         self.axes2.plot(self.x,self.ysum,'-o',label = "Summary Scores")
#         self.axes1.legend(loc = 'upper left')
#         self.axes2.legend(loc = "upper left")
        
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()
        self.figure.tight_layout()
        self.canvas.mpl_connect('motion_notify_event', self.onMotion)

    def onMotion(self, event):
#         if event.inaxes:
#             xpos = event.xdata
#             print(' %0.1f' % (xpos))
        pass    
    

class MatplotPanelB(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
       
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.figure = Figure()

#         self.axes1 = self.figure.add_subplot(111)
#         self.axes2 = self.figure.add_subplot(212)

#         self.x = ("R","I","A","S","E","C")
#         self.y = (1,2,3,4,5,6)
#         self.y1 = (2,3,4,5,6,7)
#         self.y2 = (2,3,4,5,6,7)
#         self.y3 = (2,3,4,5,6,7)
#         self.y4 = (2,3,4,5,6,7)
#         self.ysum=self.y4

#         self.axes1.hist(self.x,50,normed=1, facecolor='blue', alpha=0.75,label="contoh a")
#         self.axes1.hist(self.x, facecolor='blue', label="contoh a")
        
#         self.axes1.plot(self.x,self.y,'-go',label ="contoh a")
#         self.axes1.plot(self.x,self.y3,marker='o',color='#8D1C70',label ="contoh b")
#         
# #         self.axes2.plot(self.x,self.ysum,'-o',label = "Summary Scores")
#         self.axes1.legend(loc = 'upper left')
#         self.axes2.legend(loc = "upper left")
        
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()
        self.figure.tight_layout()
        self.canvas.mpl_connect('motion_notify_event', self.onMotion)

    def onMotion(self, event):
#         if event.inaxes:
#             xpos = event.xdata
#             print(' %0.1f' % (xpos))
        pass
