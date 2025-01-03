import unittest
from pomodoro_timer.timer import PomodoroTimer


class TestPomodoroTimer(unittest.TestCase):
    def setUp(self):
        self.timer = PomodoroTimer(work_min=1, short_break_min=5, long_break_min=20)

    def test_reset_timer(self):
        time_text, title_text, marks = self.timer.reset_timer()
        self.assertEqual(time_text, "00:00")
        self.assertEqual(title_text, "Timer")
        self.assertEqual(marks, "")

    def test_get_next_timer(self):
        duration, label, color = self.timer.get_next_timer()
        self.assertEqual(duration, 60)  # 1 minute work
        self.assertEqual(label, "Work")
        self.assertEqual(color, "GREEN")

    def test_format_time(self):
        self.assertEqual(self.timer.format_time(90), "01:30")
        self.assertEqual(self.timer.format_time(59), "00:59")


if __name__ == '__main__':
    unittest.main()
