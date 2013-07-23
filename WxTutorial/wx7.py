#7- Static Text
import wx
 
class jeff(wx.Frame):
 
	def __init__(self,parent,id):
		wx.Frame.__init__(self, parent, id, 'Window', size=(300,200))
		panel=wx.Panel(self)
		
		wx.StaticText(panel, -1, "This is static text",(10,10))
		
		custom = wx.StaticText(panel, -1, "This is custom", (10,30),(260,-1),wx.ALIGN_CENTER)
		custom.SetForegroundColour('white')
		custom.SetBackgroundColour('blue')
	
if __name__=='__main__':
	app=wx.PySimpleApp()
	frame = jeff(parent = None, id = -1)
	frame.Show()
	app.MainLoop()