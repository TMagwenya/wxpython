import wx

class MyFrame(wx.Frame):
	def__int__(self):
       super().__init__(parent=None,title="Hello World")
       self.Show()
       
       
 if __name__=="__main__":
 	app=wx.App
     frame==MyFrame()
     app.MainLoop()