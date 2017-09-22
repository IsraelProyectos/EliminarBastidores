import wx
import accesoOracle

class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        self.panel = wx.Panel(self)
        self.label = wx.StaticText(self.panel, label="Introduce la query....", pos=(0,0))
        self.txtQuery = wx.TextCtrl(self.panel, value=" ", size=(140,-1), pos=(0,30))

        #self.button = wx.Button(self.panel, label='Ejecutar borrado', size=(100, 100))

        self.button = wx.Button(self.panel, label="click Me", pos=(0,30))
        self.connectionString='WORK_SKO/WORK_SKO@bvn002b.bbdo.local/PRDBATCH'
        
        self.sizer = wx.BoxSizer()
        self.sizer.Add(self.label, 1)
        self.sizer.Add(self.button)

        self.button.Bind(wx.EVT_BUTTON, self.OnButton)

        self.panel.SetSizerAndFit(self.sizer)  
        self.Show()

    def OnButton(self, e):

    	ao=accesoOracle.connectToOracle(self.txtQuery.GetValue(), self.connectionString)
    	
    	if ao is not None:
    		self.txtQuery.SetValue("correcto")

    	else:
    		self.txtQuery.SetValue("incorrecto")

        #self.label.SetLabel("Oh, this is very looooong!")
        #self.sizer.Layout()
        # self.panel.Layout()  #Either works

app = wx.App(False)
win = MainWindow(None)
app.MainLoop()