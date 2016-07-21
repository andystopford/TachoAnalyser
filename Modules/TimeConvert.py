class TimeConvert:
    def __init__(self):
        pass

    def hrs_to_mins(self, time):
        time = time.zfill(5)
        hours = time[0:2]
        mins = time[3:5]
        hours = int(hours)
        mins = int(mins)
        mins = (hours*60) + mins
        return mins

    def mins_to_hrs(self, time):
        hours = int(time / 60)
        mins = int(time % 60)
        hours = str(hours)
        mins = str(mins)
        hours = hours.zfill(2)  # Add leading zero to single digits
        mins = mins.zfill(2)
        return hours, mins

