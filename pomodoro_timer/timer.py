# timer.py

import math


class PomodoroTimer:
    def __init__(self, work_min, short_break_min, long_break_min):
        self.work_sec = work_min * 60
        self.short_break_sec = short_break_min * 60
        self.long_break_sec = long_break_min * 60
        self.reps = 0

    def reset_timer(self):
        """Reset timer state."""
        self.reps = 0
        return "00:00", "Timer", ""

    def get_next_timer(self):
        """Return the next timer duration and label."""
        self.reps += 1
        if self.reps % 8 == 0:
            return self.long_break_sec, "Break", "RED"
        elif self.reps % 2 == 0:
            return self.short_break_sec, "Break", "PINK"
        else:
            return self.work_sec, "Work", "GREEN"

    @staticmethod
    def format_time(seconds):
        """Format time in MM:SS."""
        minutes = math.floor(seconds / 60)
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"
