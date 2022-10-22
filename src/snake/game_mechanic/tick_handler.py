from typing import Callable


class TickHandler:
    instance: 'TickHandler' = None

    def __init__(self):
        self.ticks = 0
        self.timers: list = list()
        TickHandler.instance = self

    def increase(self):
        self.ticks += 1

    def check_timers(self):
        to_remove = list()
        for timer in self.timers:
            if self.ticks >= timer.end_tick:
                timer.call()
                to_remove.append(timer)
        self.timers = [timer for timer in self.timers if timer not in to_remove]

    def update(self):
        self.increase()
        self.check_timers()

    def timer(self, nb_ticks_to_wait: int, func: Callable, *args, **kwargs):
        t = TickHandler.Timer(self.ticks, nb_ticks_to_wait, func, *args, **kwargs)
        self.timers.append(t)

    class Timer:
        def __init__(self, current_tick, tick_before_call, func, *args, **kwargs):
            self.start_tick = current_tick
            self.end_tick = current_tick + tick_before_call
            print(self.start_tick, self.end_tick)
            self.callback = func
            self.args = args
            self.kwargs = kwargs

        def call(self):
            self.callback(*self.args, **self.kwargs)
