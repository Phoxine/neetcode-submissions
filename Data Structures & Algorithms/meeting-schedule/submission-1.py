"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        intervals.sort(key=lambda interval: interval.start)
        prev_end = None
        for interval in intervals:
            if prev_end and interval.start < prev_end:
                return False
            prev_end = interval.end
        return True