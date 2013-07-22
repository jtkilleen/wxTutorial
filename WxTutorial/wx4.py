import wx
 
class jeff(wx.Frame):
 
	def __init__(self,parent,id):
		wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300,200))
		panel=wx.Panel(self)
		
		box=wx.MessageDialog(None, 'Do you like waffles?','Title',wx.YES_NO)
		answer = box.ShowModal()
		box.Destroy()
	
if __name__=='__main__':
	app=wx.PySimpleApp()
	frame = jeff(parent = None, id = -1)
	frame.Show()
	app.MainLoop()