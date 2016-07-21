from datetime import datetime, timedelta
from TimeConvert import*

class WorkDay:
    def __init__(self, parent, date):
        self.parent = parent
        self.date = date
        self.activity_list = []
        self.driving_list =[]
        self.block_list = [0]    # To keep track of driving/work/break blocks
        self.infringement = False
        self.timeConvert = TimeConvert()

    def sort(self):
        self.activity_list.sort(key=lambda x: x.start, reverse=False)

    def check_breaks(self):
        break_total = 0     # Total duration of breaks
        break_num = 0   # Count number of breaks
        fifteen_break = False
        thirty_break = False
        fortyfive_break = False
        for item in self.parent.workDay.activity_list:
            if item.mode == "Break":
                if break_total < 45:
                    # Test for 15 min break
                    if 15 <= item.duration < 30:
                        #print("15 to 30")
                        fifteen_break = True
                        break_num = 1
                        break_total += item.duration
                    if 30 <= item.duration < 45:
                        #print("30 to 45")
                        # Test for 30 min break if 15 min already taken
                        if fifteen_break == True:
                            thirty_break = True
                            break_num = 2
                            break_total += item.duration
                            if break_total >= 45:
                                index = self.parent.workDay.activity_list.index(item)
                                self.end_block(item.end, index)
                        else:
                            # If no 15 min taken count this as 15 break
                            fifteen_break == True
                            break_num = 1
                elif break_total >= 45:
                    #print("45+")
                    fortyfive_break = True
                    index = self.parent.workDay.activity_list.index(item)
                    self.end_block(item.end, index)
                else:
                    print("ok")
                    index = self.parent.workDay.activity_list.index(item)
                    self.end_block(item.end, index)
        #self.check_driving()


    def check_driving_new(self):
        driving_total = 0
        time_to_break = 270
        for item in self.parent.workDay.activity_list:
            if item.mode == "Driving":
                driving_total += item.duration
                time_to_break -= item.duration
        #print("driving_total", driving_total, time_to_break)


    def end_block(self, time, index):
        # This will end the driving block because sufficient breaks have been taken
        # 'index' is the index of the block-ending break
        #end = self.timeConvert.mins_to_hrs(time)
        self.block_list.append(index)
        #print(end, index)
        print('block_list =', self.block_list)
        self.check_driving()


    def check_driving(self):
        # Find indices for the breaks in the block_list and calculate hours driven between them
        # and identify infringements
        driving_total = 0
        total = 0
        infringement = False

        for item in self.block_list:
            if item != 0:
                end_index = self.block_list.index(item)
                start_index = end_index - 1
                #print('start index, end index', self.block_list[start_index], self.block_list[end_index])
                start = self.block_list[start_index]
                end = self.block_list[end_index]
                for item in self.parent.workDay.activity_list:
                    if start < self.parent.workDay.activity_list.index(item) < end:
                        if item.mode == "Driving":
                            driving_total += item.duration
                            self.driving_list.append(item)
                            if driving_total > 270:  # i.e. 41/2 hrs.
                                infringement = True
                            total = self.timeConvert.mins_to_hrs(driving_total)
                        print(infringement, total)
                        # Getting some odd results here
