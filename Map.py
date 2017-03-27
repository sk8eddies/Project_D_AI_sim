from Tkinter import *


class Map(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self._map = [[0 for x in range(50)] for y in range(50)]
        self._nodes = {}
        self._parent = parent

        self.init_ui()

    def init_ui(self):
        self._parent.title("AI test")
        self.pack(fill=BOTH)

    def draw_grid(self, canvas):
        for i in range(50):
                canvas.create_line(i*10, 0, i*10, 500, fill="grey")
                canvas.create_line(0, i * 10, 500, i * 10, fill="grey")

    def draw_objects_in_map(self):
        pass