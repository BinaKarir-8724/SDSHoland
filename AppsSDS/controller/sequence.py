#!usr/bin/python


class CalculationRIASEC():
    
    def __init__(self, **kwds):
        self.data = kwds
        pass
    
    def SortRIASEC(self):
            
        sorted_dict = sorted(self.data.items(), key=lambda x: x[1], reverse=True)
#         sorted_dict =dict(sorted_dict)
#         print (sorted_dict[0:3])
        sorted_dict = dict(sorted_dict[0:3])
#         print (sorted_dict)
        return sorted_dict
    
        
if __name__ == "__main__":
   
    data = {"R":3, "I":3, "A":2, "S":3, "E":2, "C":8}
    
    ClassInit = CalculationRIASEC(**data)
    print (ClassInit.SortRIASEC())
    print ("".join(ClassInit.SortRIASEC().keys()))

# #!usr/bin/python
# import wx
#  
#  
# class Frame(wx.Frame):
#      
#     def __init__(self, *args, **kwds):
#         super(Frame, self).__init__(*args, **kwds)
#          
#          
#          
# #         self.start_image = wx.Image("binakarir2.png") 
# #         self.start_image.Rescale(200, 100) 
# #         self.image = wx.BitmapFromImage(self.start_image) 
# #         self.mypic = wx.StaticBitmap(self, -1, self.image, wx.DefaultPosition, style=wx.BITMAP_TYPE_PNG)  
# 
# if __name__ == "__main__":
#     root = wx.App()
#     frame = Frame(None).Show()
#     root.MainLoop()
