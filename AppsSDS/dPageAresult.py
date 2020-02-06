"""Subclass of PageAresult, which is generated by wxFormBuilder."""

import wx
import AppsSDS.sds as sds


# Implementing PageAresult
class dPageAresult(sds.PageAResult):
	
	def __init__(self, parent):
	
		sds.PageAResult.__init__(self, parent)
		self.parent = parent
		self.SetSize((1000, 800))
		self.Centre()
		self.Maximize(True)
		
		try :
			self.sumriasec = self.parent.sumscoresR + self.parent.sumscoresI + self.parent.sumscoresA\
							+self.parent.sumscoresE + self.parent.sumscoresC

		except :
			self.sumriasec = 0

		if self.sumriasec == 0 or self.parent.sum == 0:
			self.m_staticA.SetLabel("___")		
			self.m_staticA2.SetLabel("___")		
			self.m_staticA3.SetLabel("___")		
			self.m_staticA4.SetLabel("___")		
			self.m_staticA5.SetLabel("___")		
			self.m_staticA6.SetLabel("___")		

		else :
			self.m_staticA.SetLabel(self.parent.listpermut[0])		
			self.m_staticA2.SetLabel(self.parent.listpermut[1])		
			self.m_staticA3.SetLabel(self.parent.listpermut[2])		
			self.m_staticA4.SetLabel(self.parent.listpermut[3])		
			self.m_staticA5.SetLabel(self.parent.listpermut[4])		
			self.m_staticA6.SetLabel(self.parent.listpermut[5])		
					
			from AppsSDS.db import db
	
			self.buka = db.QueryList()
	
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[0])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA1.InsertItems(list(self.buka2.keys()), 0)
		
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[1])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA2.InsertItems(list(self.buka2.keys()), 0)
	
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[2])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA3.InsertItems(list(self.buka2.keys()), 0)
			
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[3])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA4.InsertItems(list(self.buka2.keys()), 0)
	
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[4])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA5.InsertItems(list(self.buka2.keys()), 0)
			
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[5])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA6.InsertItems(list(self.buka2.keys()), 0)
		
		self.Refresh()
		self.Layout()

	
class dPageBresult(sds.PageAResult):

	def __init__(self, parent):
		sds.PageAResult.__init__(self, parent)
		self.parent = parent
		self.SetSize((1000, 800))
		self.Centre()
		self.Maximize(True)

		try :
			self.sumriasec = self.parent.sumscoresR + self.parent.sumscoresI + self.parent.sumscoresA\
							+self.parent.sumscoresE + self.parent.sumscoresC

		except :
			self.sumriasec = 0

		if self.sumriasec == 0 or self.parent.sum == 0:
			self.m_staticA.SetLabel("___")		
			self.m_staticA2.SetLabel("___")		
			self.m_staticA3.SetLabel("___")		
			self.m_staticA4.SetLabel("___")		
			self.m_staticA5.SetLabel("___")		
			self.m_staticA6.SetLabel("___")		

		else :
		
			self.m_staticA.SetLabel(self.parent.listpermut[0])		
			self.m_staticA2.SetLabel(self.parent.listpermut[1])		
			self.m_staticA3.SetLabel(self.parent.listpermut[2])		
			self.m_staticA4.SetLabel(self.parent.listpermut[3])		
			self.m_staticA5.SetLabel(self.parent.listpermut[4])		
			self.m_staticA6.SetLabel(self.parent.listpermut[5])		
					
			from AppsSDS.db import db
	
			self.buka = db.QueryList()
	
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[0])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA1.InsertItems(list(self.buka2.keys()), 0)
		
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[1])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA2.InsertItems(list(self.buka2.keys()), 0)
	
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[2])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA3.InsertItems(list(self.buka2.keys()), 0)
			
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[3])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA4.InsertItems(list(self.buka2.keys()), 0)
	
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[4])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA5.InsertItems(list(self.buka2.keys()), 0)
			
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[5])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA6.InsertItems(list(self.buka2.keys()), 0)
		
		self.Refresh()
		self.Layout()

		
class dPageCresult(sds.PageAResult):

	def __init__(self, parent):
		sds.PageAResult.__init__(self, parent)
		self.parent = parent
		self.SetSize((1000, 800))
		self.Centre()
		self.Maximize(True)

		try :
			self.sumriasec = self.parent.sumscoresR + self.parent.sumscoresI + self.parent.sumscoresA\
							+self.parent.sumscoresE + self.parent.sumscoresC

		except :
			self.sumriasec = 0

		if self.sumriasec == 0 or self.parent.sum == 0:
			self.m_staticA.SetLabel("___")		
			self.m_staticA2.SetLabel("___")		
			self.m_staticA3.SetLabel("___")		
			self.m_staticA4.SetLabel("___")		
			self.m_staticA5.SetLabel("___")		
			self.m_staticA6.SetLabel("___")		

		else :		
			self.m_staticA.SetLabel(self.parent.listpermut[0])		
			self.m_staticA2.SetLabel(self.parent.listpermut[1])		
			self.m_staticA3.SetLabel(self.parent.listpermut[2])		
			self.m_staticA4.SetLabel(self.parent.listpermut[3])		
			self.m_staticA5.SetLabel(self.parent.listpermut[4])		
			self.m_staticA6.SetLabel(self.parent.listpermut[5])		
					
			from AppsSDS.db import db
	
			self.buka = db.QueryList()
	
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[0])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA1.InsertItems(list(self.buka2.keys()), 0)
		
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[1])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA2.InsertItems(list(self.buka2.keys()), 0)
	
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[2])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA3.InsertItems(list(self.buka2.keys()), 0)
			
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[3])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA4.InsertItems(list(self.buka2.keys()), 0)
	
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[4])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA5.InsertItems(list(self.buka2.keys()), 0)
			
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[5])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA6.InsertItems(list(self.buka2.keys()), 0)
	
		self.Refresh()
		self.Layout()

	
class dPageDresult(sds.PageAResult):

	def __init__(self, parent):
		sds.PageAResult.__init__(self, parent)
		self.parent = parent
		self.SetSize((1000, 800))
		self.Centre()
		self.Maximize(True)

		try :
			self.sumriasec = self.parent.sumscoresR + self.parent.sumscoresI + self.parent.sumscoresA\
							+self.parent.sumscoresE + self.parent.sumscoresC

		except :
			self.sumriasec = 0

		if self.sumriasec == 0 or self.parent.sum == 0:
			self.m_staticA.SetLabel("___")		
			self.m_staticA2.SetLabel("___")		
			self.m_staticA3.SetLabel("___")		
			self.m_staticA4.SetLabel("___")		
			self.m_staticA5.SetLabel("___")		
			self.m_staticA6.SetLabel("___")		

		else :		
			self.m_staticA.SetLabel(self.parent.listpermut[0])		
			self.m_staticA2.SetLabel(self.parent.listpermut[1])		
			self.m_staticA3.SetLabel(self.parent.listpermut[2])		
			self.m_staticA4.SetLabel(self.parent.listpermut[3])		
			self.m_staticA5.SetLabel(self.parent.listpermut[4])		
			self.m_staticA6.SetLabel(self.parent.listpermut[5])		
					
			from AppsSDS.db import db
	
			self.buka = db.QueryList()
	
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[0])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA1.InsertItems(list(self.buka2.keys()), 0)
		
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[1])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA2.InsertItems(list(self.buka2.keys()), 0)
	
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[2])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA3.InsertItems(list(self.buka2.keys()), 0)
			
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[3])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA4.InsertItems(list(self.buka2.keys()), 0)
	
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[4])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA5.InsertItems(list(self.buka2.keys()), 0)
			
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[5])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA6.InsertItems(list(self.buka2.keys()), 0)
	
		self.Refresh()
		self.Layout()

		
class dPageEresult(sds.PageAResult):

	def __init__(self, parent):
		sds.PageAResult.__init__(self, parent)
		self.parent = parent
		self.SetSize((1000, 800))
		self.Centre()
		self.Maximize(True)

		try :
			self.sumriasec = self.parent.sumscoresR + self.parent.sumscoresI + self.parent.sumscoresA\
							+self.parent.sumscoresE + self.parent.sumscoresC

		except :
			self.sumriasec = 0

		if self.sumriasec == 0 or self.parent.sum == 0:
			self.m_staticA.SetLabel("___")		
			self.m_staticA2.SetLabel("___")		
			self.m_staticA3.SetLabel("___")		
			self.m_staticA4.SetLabel("___")		
			self.m_staticA5.SetLabel("___")		
			self.m_staticA6.SetLabel("___")		

		else :		
			self.m_staticA.SetLabel(self.parent.listpermut[0])		
			self.m_staticA2.SetLabel(self.parent.listpermut[1])		
			self.m_staticA3.SetLabel(self.parent.listpermut[2])		
			self.m_staticA4.SetLabel(self.parent.listpermut[3])		
			self.m_staticA5.SetLabel(self.parent.listpermut[4])		
			self.m_staticA6.SetLabel(self.parent.listpermut[5])		
					
			from AppsSDS.db import db
	
			self.buka = db.QueryList()
	
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[0])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA1.InsertItems(list(self.buka2.keys()), 0)
		
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[1])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA2.InsertItems(list(self.buka2.keys()), 0)
	
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[2])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA3.InsertItems(list(self.buka2.keys()), 0)
			
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[3])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA4.InsertItems(list(self.buka2.keys()), 0)
	
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[4])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA5.InsertItems(list(self.buka2.keys()), 0)
			
			self.buka1, self.buka2 = self.buka.CheckQuery(None, self.parent.listpermut[5])
			if list(self.buka2.keys()) == []:
				self.buka2["Kosong"] = "Kosong"
				print ("hello")
			self.m_listBoxA6.InsertItems(list(self.buka2.keys()), 0)
	
		self.Refresh()
		self.Layout()			

		
if __name__ == '__main__':
	tes = wx.App()
	windows = dPageAresult(None)
	windows.Show()
	tes.MainLoop()
