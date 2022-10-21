class TickHandler:
    instance = None

    def __init__(self):
        self.ticks = 0
        TickHandler.instance = self

    def increase(self):
        self.ticks += 1
