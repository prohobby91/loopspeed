# loopspeed

`loopspeed` is a lightweight Python package that provides **manual** and **automatic** loop‑speed control.  
It helps developers maintain consistent loop timing by adjusting delays based on:

- Loop execution time  
- CPU frequency  
- CPU load  
- Optional smoothing for stable automatic scaling  

This is useful for games, simulations, robotics, real‑time systems, and any application that needs predictable loop timing.

---

## Features

- ✔ Manual loop‑speed control (fixed loops per second)  
- ✔ Automatic adaptive loop‑speed control  
- ✔ CPU‑aware timing using `psutil`  
- ✔ Smooth scaling to prevent jitter  
- ✔ Simple API  
- ✔ Pure Python, cross‑platform  

---

## Installation

Install from PyPI:

```bash
pip install loopspeed


# Manual Loop Speed Control----------------------------------------------------------------------------------------------------------------------------------------------

from loopspeed import LoopSpeedController

controller = LoopSpeedController(target_lps=20)  # 20 loops per second (Adjust target_lps=20 Adjust the Value "20" for example 20 loops per second currently set)

try:
    while True:
        controller.start() #Set at the start of the loop

        # Your loop work here
        print("Manual loop running...")

        controller.end() #Set at the end of the loop

except KeyboardInterrupt:
    print("Stopped.")


# Auto Loop (Adjust Loop Speed)------------------------------------------------------------------------------------------------------------------------------------------

from loopspeed import AutoScaler

auto = AutoScaler(min_lps=10, max_lps=60, smoothing=0.1) #Adjust Minimum and Maximum Loop speeds min_lps = (Adjust minimum Loops per second), max_lps = (Adjust maximum Loops per second)

try:
    while True:
        auto.start() # Set at the start of the Loop

        # Your loop work here
        print("Auto loop running...")

        current_lps, loop_time, cpu = auto.end() # Getting the Current Loops per second, Loop Time and The Current CPU at the end of the Loop
        print(f"LPS={current_lps:.2f}, Loop={loop_time:.4f}s, CPU={cpu}%")

except KeyboardInterrupt:
    print("Stopped.")
