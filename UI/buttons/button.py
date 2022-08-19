# ANCHOR Class containing everything needed for simple click detection
class Button:
    def __init__(self, name, tlc, size):
        self.name = name
        self.tlc = tlc
        self.trc = (self.tlc[0] + size, self.tlc[1])
        self.blc = (self.tlc[0], self.tlc[1] + size)
        self.brc = (self.tlc[0] + size, self.tlc[1] + size)

    def is_colliding(self, pos):
        return True if self.trc[0] > pos[0] > self.tlc[0] and self.brc[1] > pos[1] > self.trc[1] else False
