"""
The Break class does the work of figuring out what's going on by getting its break state from its predecessor (if any),
checking for driving or work between it and its child, and then initialising the child to repeat the process.
"""
from TimeConvert import*
class BreakClass:
    def __init__(self, parent, start, end, duration, index):
        self.TC = TimeConvert()
        self.parent = parent
        self.start = start
        self.end = end
        self.duration = duration
        self.index = index
        self.break_curr = 0

    def set_state(self, break_prev):
        # Adds previous break to current
        if break_prev == -1:
            self.break_curr = 0
        else:
            self.break_curr = self.calc_break_curr()
        if break_prev >= 15 and self.break_curr >= 30:
            self.break_curr = 45
        self.get_child()

    def calc_break_curr(self):
        # Test whether current break is legally valid, and what it counts as
        if 15 <= self.duration < 30:
            self.break_curr = 15
        elif 30 <= self.duration < 45:
            self.break_curr = 30
        elif self.duration >= 45:
            self.break_curr = 45
        else:
            self.break_curr = 0
        return self.break_curr

    def get_child(self):
        # i.e. the break after this one
        length = len(self.parent.break_list)
        if self.index != length - 1:
            child = self.parent.break_list[self.index + 1]
            self.driving_times(child)

    def driving_times(self, child):
        # Works out driving times between breaks and totals them
        # Somewhere set up activity list for populating dayView table
        for dt in self.parent.driving_list:
            if dt.start >= self.end and dt.end <= child.start:
                driving_time = dt.duration
                self.parent.driving_block += driving_time
                ########################################################################
                # Print info ###########################################################
                d_time = self.TC.mins_to_hrs(dt.duration)
                d_start = self.TC.mins_to_hrs(dt.start)
                d_end = self.TC.mins_to_hrs(dt.end)
                print("")
                #print("driving", d_time)
                d_block = self.TC.mins_to_hrs(self.parent.driving_block)
                curr_start = self.TC.mins_to_hrs(self.start)
                #print("driving block", d_block)
                #print("break_curr", self.break_curr, "starts at", curr_start)
                # End Print Info #######################################################
                ########################################################################
                if self.parent.driving_block > 270:
                    block = self.parent.driving_block
                    print("Infringement!", d_start, d_end)
                    print("driving_block total = ", self.parent.driving_block, "mins")
                    LPB = block - 270
                    inf_time = dt.end - LPB
                    inf_time = self.TC.mins_to_hrs(inf_time)
                    print("inf time", inf_time)
                self.set_blocks(child)



    def set_blocks(self, child):
        length = len(self.parent.break_list)
        if child.index < length - 2:        # ?Not right needs diff values for diff data
            break_block = child.duration + self.break_curr
        else:
            break_block = self.break_curr
        if break_block >= 45:
            self.parent.driving_block = 0
            self.break_curr = 0
            print("Driving block zeroed")
            self.pass_on(child)
        else:
            self.pass_on(child)


    def pass_on(self, child):
        # pass on current item's internal state
        child.set_state(self.break_curr)
