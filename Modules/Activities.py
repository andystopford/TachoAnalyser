
class Activity:
    def __init__(self, act_mode, start, end):
        self.start = start
        self.end = end
        self.mode = act_mode
        self.duration = 0

    def calc_duration(self):
        self.duration = self.end - self.start



