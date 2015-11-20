#!/usr/bin/env python2

# minimaleditor.py
#
# wxWidgets Python Text Editor Minimal code

import os
import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open file")
        menuSave = filemenu.Append(wx.ID_SAVE, "&Save", "Save file")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Vimsy Editor")
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate Vimsy Editor")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)

        self.Show(True)

    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "Vimsy Editor 0.0.1 - written by tirrit", "Vimsy Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destory()

    def OnExit(self, e):
        self.Close(True)

    def OnOpen(self, e):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')

            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def OnSave(self, e):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a filename", self.dirname, "", "*.*", wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() ==  wx.ID_OK:
            itcontains = self.control.GetValue()
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            filehandle = open(os.path.join(self.dirname, self.filename), 'w')
            filehandle.write(itcontains)
            filehandle.close()
        dlg.Destroy()

app = wx.App(False)
frame = MainWindow(None, 'Vimsy Text Editor')
app.MainLoop()