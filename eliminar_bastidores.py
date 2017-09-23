#!/usr/bin/env python
#coding=utf-8
import wx
import accesoOracle
class MyFrame(wx.Frame):
    """ Una clase personalizada de frame """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,200))
        # Control de texto multilínea
        self.txt = wx.TextCtrl(self, pos=(0,0), size=(100,20))
        self.control = wx.TextCtrl(self, pos=(0,55), style=wx.TE_MULTILINE)
        self.buttonTextArea = wx.Button(self, label="hola", pos=(0, 100), size=(50,50))
        self.buttonTextArea.Bind(wx.EVT_BUTTON, self.OnbuttonTextArea)
        connectionString='WORK_SKO/WORK_SKO@bvn002b.bbdo.local/PRDBATCH'
        self.Show(True)

    def OnbuttonTextArea(self, e):
        textAreaBastidores = self.control.GetValue()
        #listaBastidores = [texto.split()]
        #self.txt.SetValue(textAreaBastidores.split())
        #print(textAreaBastidores.split())
        ao=accesoOracle.connectToOracle(self.connectionString, textAreaBastidores)

app = wx.App(False)
frame = MyFrame(None, 'Editor simple')
app.MainLoop()