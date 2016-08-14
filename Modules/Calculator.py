from TimeConvert import*

class Calculator:
    def __init__(self, parent):
        self.parent = parent
        self.driving_timer = 0
        self.break_timer = 0
        self.break_status = 0
        self.TC = TimeConvert()

    def timers(self):
        for activity in self.parent.activity_list:
            if self.driving_timer == 0:
                if activity.mode == "Break":
                    print("Initial break")

            if activity.mode == "Break":
                if 15 <= activity.duration <= 30 and self.break_status == 0:
                    self.break_status = 15
                    self.break_timer += activity.duration
                elif 30 <= activity.duration < 45 and self.break_status == 15:
                    self.break_status = 45
                elif activity.duration >= 45:
                    self.break_status = 45

            elif activity.mode == "Driving":
                start = self.TC.mins_to_hrs(activity.start)
                if self.break_status != 45:
                    self.driving_timer += activity.duration
                    if self.driving_timer > 270:
                        print()
                        print("Infringement", start, self.driving_timer)
                else:
                    print("driving start", start)
                    self.break_status = 0
                    self.driving_timer = 0
                    self.driving_timer += activity.duration
            print()
            print(activity.mode, self.break_status, self.driving_timer)