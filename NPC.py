import random


class NPC:

    def __init__(self, canvas):
        self._position = (0, 0)
        self._delta_distance = (0, 0)
        self._rect = None
        self._canvas = canvas

    def set_position(self, x, y):
        # self.get_distance_from_last(x, y)
        self._position = (x, y)

    def get_distance_from_last(self, x, y):
        self._delta_distance = (x-self._delta_distance[0], y-self._delta_distance[1])

    def draw(self):
        self.set_new_position()
        self._canvas.delete(self._rect)

        relative_x = self._position[0] * 10
        relative_y = self._position[1] * 10

        self._rect = self._canvas.create_rectangle(relative_x, relative_y, relative_x+10, relative_y+10, fill="blue")

        self._canvas.after(500, self.draw)

    def set_new_position(self):
        self.set_position(random.randint(0, 49), random.randint(0, 49))