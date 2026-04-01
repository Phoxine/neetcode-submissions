"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals_list = [(interval.start, interval.end) for interval in intervals]
        intervals_list.sort()
        prev_end = None
        for start, end in intervals_list:
            if prev_end and start < prev_end:
                return False
            prev_end = end
        return True