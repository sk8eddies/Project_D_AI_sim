from Map import *
from NPC import *


def main():
    root = Tk()
    root.geometry("600x600")
    canvas = Canvas(root, width=500, height=500)
    canvas.pack()
    app = Map(root)
    # Create grid
    app.draw_grid(canvas=canvas)

    npc1 = NPC(canvas=canvas)
    npc1.draw()

    root.mainloop()






main()