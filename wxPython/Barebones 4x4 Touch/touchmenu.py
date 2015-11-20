#!/usr/bin/env python2

# touchmenu.py - barebones touchscreen menu using wx python - written by tirrit

import os
import subprocess
import wx

from wx.lib import buttons

class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent

        bmp = buttons.GenBitmapButton(self, 1, wx.Image("satelitt.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap(), (20, 80), (150, 150), style=wx.BORDER_NONE)
        bmp = buttons.GenBitmapButton(self, 2, wx.Image("video.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap(), (185, 80), (150, 150), style=wx.BORDER_NONE)
        bmp = buttons.GenBitmapButton(self, 3, wx.Image("kamera.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap(), (455, 80), (150, 150), style=wx.BORDER_NONE)
        bmp = buttons.GenBitmapButton(self, 4, wx.Image("music.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap(), (615, 80), (150, 150), style=wx.BORDER_NONE)
        bmp = buttons.GenBitmapButton(self, 5, wx.Image("terninger.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap(), (20, 270), (275, 185), style=wx.BORDER_NONE)
        bmp = buttons.GenBitmapButton(self, 6, wx.Image("server.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap(), (455, 300), (150, 150), style=wx.BORDER_NONE)
        bmp = buttons.GenBitmapButton(self, 7, wx.Image("settings.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap(), (615, 300), (150, 150), style=wx.BORDER_NONE)
        bmp = buttons.GenBitmapButton(self, 8, wx.Image("pingu.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap(), (345, 220), (100, 100), style=wx.BORDER_NONE)

        self.Bind(wx.EVT_BUTTON, self.OnNavit, id=1)
        self.Bind(wx.EVT_BUTTON, self.OnVideo, id=2)
        self.Bind(wx.EVT_BUTTON, self.OnCamera, id=3)
        self.Bind(wx.EVT_BUTTON, self.OnMusic, id=4)
        self.Bind(wx.EVT_BUTTON, self.OnGames, id=5)
        self.Bind(wx.EVT_BUTTON, self.OnServer, id=6)
        self.Bind(wx.EVT_BUTTON, self.OnSettings, id=7)
        self.Bind(wx.EVT_BUTTON, self.OnTerminal, id=8)

        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
 
        hSizer.Add((1,1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 0)
        hSizer.Add((1,1), 0, wx.ALL, 0)
        self.SetSizer(hSizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

    def OnNavit(self, evt):
        subprocess.call(["navit"], shell=False)

    def OnVideo(self, evt):
        subprocess.call(["./video.py"])

    def OnCamera(self, evt):
        subprocess.call(["./camera.py"]) 

    def OnMusic(self, evt):
        subprocess.call(["vlc"], shell=False)

    def OnGames(self, evt):
        subprocess.call(["./games.py"])

    def OnServer(self, evt):
        subprocess.call(["./server.py"])

    def OnSettings(self, evt):
        subprocess.call(["./settings.py"])

    def OnTerminal(self, evt):
        subprocess.call(["./terminal.py"])

    def OnEraseBackground(self, evt):
        dc = evt.GetDC()
 
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("meny.jpg")
        dc.DrawBitmap(bmp, 0, 0)

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, size=(600,450))
        panel = MainPanel(self)        
        self.Center()

class Main(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        dlg = MainFrame()
        dlg.Show()

if __name__ == "__main__":
    app = Main()
    app.MainLoop()
