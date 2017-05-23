from TimeConvert import*

class Calculator:
    def __init__(self, parent):
        self.parent = parent
        self.driving_timer = 0
        self.wtd_timer = 0
        self.break_timer = 0
        self.break_status = 0
        self.wtd_break_status = 0
        self.hgv_infr = False
        self.wtd_infr = False
        self.TC = TimeConvert()

    def timers(self, list):
        self.driving_timer = 0
        self.wtd_timer = 0
        self.break_timer = 0
        self.break_status = 0
        self.wtd_break_status = 0
        self.hgv_infr = False
        self.wtd_infr = False
        for activity in list:
            if activity.mode == "Break":
                if 15 <= activity.duration <= 30 and self.break_status == 0:
                    # Break is valid as at least 15 mins
                    self.break_status = 15
                    self.break_timer += activity.duration
                elif 30 <= activity.duration < 45 and self.break_status == 15:
                    self.break_status = 45
                elif activity.duration >= 45:
                    self.break_status = 45

                if 15 <= activity.duration <= 30:
                    self.wtd_break_status = 15
                elif activity.duration >= 15 and self.wtd_break_status >= 15:
                    # Only need two 15 min breaks for WTD
                    self.wtd_break_status = 30
                elif activity.duration >= 30:
                    self.wtd_break_status = 30

            elif activity.mode == "Driving":
                if self.break_status != 45:
                    self.driving_timer += activity.duration
                    if self.driving_timer > 270:
                        infr_excess = self.driving_timer - 270
                        infr_time = activity.end - infr_excess
                        if self.hgv_infr == False:
                            self.parent.timeLine.infr_flag(infr_time, "hgv")
                            if self.parent.infringements == "wtd":
                                self.parent.infringements = "both"
                            else:
                                self.parent.infringements = "hgv"
                            self.hgv_infr = True
                else:
                    self.break_status = 0
                    self.driving_timer = 0
                    self.driving_timer += activity.duration
                    self.hgv_infr = False
                    self.wtd_infr = False

            if activity.mode == "Working" or activity.mode == "Driving":
                if self.wtd_break_status != 30:
                    self.wtd_timer += activity.duration
                    if self.wtd_timer > 360:
                        infr_excess = self.wtd_timer - 360
                        infr_time = activity.end - infr_excess
                        if self.wtd_infr == False:
                            self.parent.timeLine.infr_flag(infr_time, "wtd")
                            if self.parent.infringements == "hgv":
                                self.parent.infringements = "both"
                            else:
                                self.parent.infringements = "wtd"
                            self.wtd_infr = True
                else:
                    self.wtd_break_status = 0
                    self.wtd_timer = 0
                    self.wtd_timer += activity.duration
                    self.hgv_infr = False
                    self.wtd_infr = False

    def clear(self):
        self.driving_timer = 0
        self.wtd_timer = 0
        self.break_timer = 0
        self.break_status = 0

