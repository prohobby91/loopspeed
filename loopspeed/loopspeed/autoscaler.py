#---------------------------------------------------------------------------------------
# Name:        AutoScaler (LoopSpeedPlugin)
# Purpose:     Controlling Speed of Loop (File 2)
# Format:      Python .py
# Author:      ProHobby
#
# Created:     28/06/2026
# Copyright:   (c) ProHobby 2026
# Licence:     Hobbyist
#---------------------------------------------------------------------------------------


import time
import psutil


class AutoScaler:
    def __init__(self, min_lps=5, max_lps=60, smoothing=0.1):
        self.min_lps = min_lps
        self.max_lps = max_lps
        self.smoothing = smoothing
        self.current_lps = max_lps
        self.target_time = 1.0 / self.current_lps

    def start(self):
        self._start = time.time()

    def end(self):
        end = time.time()
        loop_time = end - self._start

        cpu_percent = psutil.cpu_percent(interval=0)

        # Auto-adjust LPS based on CPU load
        load_factor = cpu_percent / 100.0
        new_lps = self.max_lps - (load_factor * (self.max_lps - self.min_lps))

        # Smooth transitions
        self.current_lps = (
            self.current_lps * (1 - self.smoothing) +
            new_lps * self.smoothing
        )

        self.target_time = 1.0 / self.current_lps

        delay = self.target_time - loop_time
        if delay > 0:
            time.sleep(delay)

        return self.current_lps, loop_time, cpu_percent