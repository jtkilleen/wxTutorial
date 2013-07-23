#6- List for Input
import wx
 
class jeff(wx.Frame):
 
	def __init__(self,parent,id):
		wx.Frame.__init__(self, parent, id, 'Window', size=(300,200))
		panel=wx.Panel(self)
		
		box=wx.SingleChoiceDialog(None,'What is your favorite food?','Title',['Beef','Burger','BBQ'])
		if box.ShowModal()==wx.ID_OK:
			answer=box.GetStringSelection()
	
if __name__=='__main__':
	app=wx.PySimpleApp()
	frame = jeff(parent = None, id = -1)
	frame.Show()
	app.MainLoop()