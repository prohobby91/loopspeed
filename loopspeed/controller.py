#---------------------------------------------------------------------------------------
# Name:        Controller (LoopSpeedPlugin)
# Purpose:     Controlling Speed of Loop (File 1)
# Format:      Python .py
# Author:      ProHobby
#
# Created:     28/06/2026
# Copyright:   (c) ProHobby 2026
# Licence:     Hobbyist
#---------------------------------------------------------------------------------------


import time
import psutil


class LoopSpeedController:
    def __init__(self, target_lps: float):
        self.target_time = 1.0 / target_lps

    def get_cpu_speed(self) -> float:
        freq = psutil.cpu_freq().current
        return freq * 1_000_000  # Hz

    def start(self):
        self._start = time.time()

    def end(self):
        end = time.time()
        loop_time = end - self._start

        cpu_speed = self.get_cpu_speed()

        # Example heuristic: CPU-based minimum loop time
        estimated_cycles = 50_000
        cpu_time = estimated_cycles / cpu_speed

        corrected_time = max(loop_time, cpu_time)

        delay = self.target_time - corrected_time
        if delay > 0:
            time.sleep(delay)

        return corrected_time