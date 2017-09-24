#!/usr/bin/env python
#coding=utf-8
import wx
import accesoOracle
import eliminarBastidores
class MyFrame(wx.Frame):
    """ Una clase personalizada de frame """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500,300))
        # Control de texto multilínea

        self.labelTransactionID = wx.StaticText(self, label="Introduce abajo los TransactionID (Separados por Return o por un espacio entre ellos)", pos=(0,10), size=(500, 20))
        self.textAreaBastidores = wx.TextCtrl(self, pos=(0,30), size=(200,70))
        self.labelBastidores = wx.StaticText(self, label="Introduce abajo los Bastidores (Separados por Return o por un espacio entre ellos)", pos=(0,110), size=(500, 20))
        self.textAreaTransactionID = wx.TextCtrl(self, pos=(0,130), size=(200,70), style=wx.TE_MULTILINE)
        self.buttonTextArea = wx.Button(self, label="Ejecutar borrado", pos=(0,210), size=(100,20))
        self.buttonTextArea.Bind(wx.EVT_BUTTON, self.OnbuttonTextArea)
        
        self.Show(True)

    def OnbuttonTextArea(self, e):
        bastidores = self.textAreaBastidores.GetValue()
        transactionID = self.textAreaTransactionID.GetValue()
        
        if len(bastidores) == 0 and len(transactionID) == 0:
        	self.textAreaBastidores.SetValue("No puede estar vacio")
        	self.textAreaTransactionID.SetValue("No puede estar vacio")
        	print("no puedes dejar en blanco ningun texto")
        elif len(bastidores) == 0:
        	self.textAreaBastidores.SetValue("No puede estar vacio")
        	print("no puedes dejar en blanco ningun texto")
        elif len(transactionID) == 0:
        	self.textAreaTransactionID.SetValue("No puede estar vacio")
        	print("no puedes dejar en blanco ningun texto")
        else:
        	eb=eliminarBastidores.deleteBastidores(bastidores, transactionID)
        	eb.delete()

app = wx.App(False)
frame = MyFrame(None, 'Eliminar Bastidores')
app.MainLoop()