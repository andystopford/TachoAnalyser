from TimeConvert import*

class Calculator:
    def __init__(self, parent):
        self.parent = parent
        self.driving_timer = 0
        self.wtd_timer = 0
        self.break_timer = 0
        self.break_status = 0
        self.TC = TimeConvert() # Prob remove this later

    def timers(self):
        for activity in self.parent.activity_list:
            if activity.mode == "Break":
                if 15 <= activity.duration <= 30 and self.break_status == 0:
                    self.break_status = 15
                    self.break_timer += activity.duration
                    self.wtd_timer = 0
                elif 30 <= activity.duration < 45 and self.break_status == 15:
                    self.break_status = 45
                    self.wtd_timer = 0
                elif activity.duration >= 45:
                    self.break_status = 45
                    self.wtd_timer = 0

            elif activity.mode == "Driving":
                if self.break_status != 45:
                    self.driving_timer += activity.duration
                    if self.driving_timer > 270:
                        infr_excess = self.driving_timer - 270
                        infr_time = activity.end - infr_excess
                        self.parent.timeLine.infr_flag(infr_time, "hgv")
                        infr_time = self.TC.mins_to_hrs(infr_time)
                        activity.infr = activity.infr + " " + "HGV" + "@" + infr_time
                else:
                    self.break_status = 0
                    self.driving_timer = 0
                    self.driving_timer += activity.duration

            if activity.mode == "Working" or activity.mode == "Driving":
                self.wtd_timer += activity.duration
                if self.wtd_timer > 360:
                    infr_excess = self.wtd_timer - 360
                    infr_time = activity.end - infr_excess
                    self.parent.timeLine.infr_flag(infr_time, "wtd")
                    infr_time = self.TC.mins_to_hrs(infr_time)
                    activity.infr = activity.infr + " " + "WTD" + "@" + infr_time


    def clear(self):
        self.driving_timer = 0
        self.wtd_timer = 0
        self.break_timer = 0
        self.break_status = 0

    # TODO infringement list for populating dayView (change this name)
