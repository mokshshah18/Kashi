from tkinter import *
from tkinter import ttk
import threading

class uiElements:
    
    def __init__(self):
        t = threading.Thread(target=self.render)
        t.start()
    
    def render(root):
        root.mainloop()
