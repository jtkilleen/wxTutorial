#5 - TEXT BOXES
import wx
 
class jeff(wx.Frame):
 
	def __init__(self,parent,id):
		wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300,200))
		panel=wx.Panel(self)
		
		box=wx.TextEntryDialog(None, "How many comics do you want?","RANDOM COMICS GENERATOR","Enter a number")
		if box.ShowModal()==wx.ID_OK:
			answer = box.GetValue()
	
if __name__=='__main__':
	app=wx.PySimpleApp()
	frame = jeff(parent = None, id = -1)
	frame.Show()
	app.MainLoop()