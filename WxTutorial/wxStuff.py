import wx,urllib,re,os
from random import randrange
 
class jeff(wx.Frame):
 
	def __init__(self,parent,id):
		wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300,200))
		panel=wx.Panel(self)
		
		box=wx.TextEntryDialog(None, "How many comics do you want?","RANDOM COMICS GENERATOR","Enter a number")
		if box.ShowModal()==wx.ID_OK:
			answer = box.GetValue()
			count = 0
			while count < int(answer):
				if not os.path.exists('xkcdIMAGES'):
					os.mkdir('xkcdIMAGES')

				source = urllib.urlopen('http://xkcd.com/'+str(randrange(0,1000))).read()

				imgs = re.findall(r'http.*png|http.*jpg',source)
				for img in imgs:
					filename = 'xkcdIMAGES/' + img.split('/')[-1]
					if not os.path.exists(filename):
						urllib.urlretrieve(img,filename)
				count +=1
		button=wx.Button(panel, label="exit", pos=(130,10),size=(60,60))
		self.Bind(wx.EVT_BUTTON, self.closebutton, button)
		self.Bind(wx.EVT_CLOSE, self.closewindow)
		
	def closebutton(self, event):
		self.Close()
		
	def closewindow(self, event):
		self.Destroy()
				
			
	
if __name__=='__main__':
	app=wx.PySimpleApp()
	frame = jeff(parent = None, id = -1)
	frame.Show()
	app.MainLoop()