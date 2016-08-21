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
                break_start = item.start
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
                                self.end_block(index)
                                break_total = 0
                        else:
                            # If no 15 min taken count this as 15 break
                            fifteen_break == True
                            break_num = 1
                elif break_total >= 45:
                    #print("45+")
                    fortyfive_break = True
                    index = self.parent.workDay.activity_list.index(item)
                    self.end_block(index)
                    break_total = 0
                else:
                    print("ok")
                    index = self.parent.workDay.activity_list.index(item)
                    self.end_block(index)


    def end_block(self, index):
        # This will end the driving block because sufficient breaks have been taken
        # 'index' is the index of the block-ending break
        # TODO This needs a return to check_breaks so evaluation of whole activity_list continues
        # maybe all activities need to be totalled in one pass through activity_list
        self.block_list.append(index)
        print('block_list =', self.block_list)
        self.check_driving()


    def check_driving(self):
        # Find indices for the breaks in the block_list and calculate hours driven between them
        # and identify infringements
        total = 0
        infringement = False

        for item in self.block_list:
            driving_total = 0
            if item != 0:
                # Divide block_list into start-end pairs
                end_index = self.block_list.index(item)
                start_index = end_index - 1
                start = self.block_list[start_index]
                end = self.block_list[end_index]
                for activity in self.parent.workDay.activity_list:
                    if start < self.parent.workDay.activity_list.index(activity) < end:
                        if activity.mode == "Driving":
                            driving_total += activity.duration
                            self.driving_list.append(activity)
                            if driving_total > 270:  # i.e. 41/2 hrs.
                                infringement = True
                            total = self.timeConvert.mins_to_hrs(driving_total)
        print(infringement, total)
        # Need to zero the total after 4.5 hrs
