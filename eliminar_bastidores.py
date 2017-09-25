#!/usr/bin/env python
#coding=utf-8
import wx
import accesoOracle
import eliminarBastidores
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500,300))
        
        #Elementos gráficos del formulario
        self.labelTransactionID = wx.StaticText(self, label="Introduce abajo los TransactionID (Separados por salto de linea o por un espacio entre ellos)", pos=(0,10), size=(500, 20))
        self.textAreaTransactionID = wx.TextCtrl(self, pos=(0,30), size=(200,70), style=wx.TE_MULTILINE)
        self.labelBastidores = wx.StaticText(self, label="Introduce abajo los Bastidores (Separados por por salto de linea o por un espacio entre ellos)", pos=(0,110), size=(500, 20))
        self.textAreaBastidores = wx.TextCtrl(self, pos=(0,130), size=(200,70), style=wx.TE_MULTILINE)
        self.buttonTextArea = wx.Button(self, label="Ejecutar borrado", pos=(0,210), size=(100,20))
        self.statusbar = self.CreateStatusBar(2)
        self.statusbar.SetStatusText('go')
        
        #Asignación del evento al botón
        self.buttonTextArea.Bind(wx.EVT_BUTTON, self.OnbuttonTextArea)
        
        #Mostrar formulario
        self.Show(True)

    #Acción del boton al presionar   
    def OnbuttonTextArea(self, e):
        
        #Captura del texto de los TextBox
        bastidores = self.textAreaBastidores.GetValue()
        transactionID = self.textAreaTransactionID.GetValue()

        #Comprobación que los TextBox no vienen null
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

#Inicio de la aplicación
app = wx.App(False)
frame = MyFrame(None, 'Eliminar Bastidores')
app.MainLoop()