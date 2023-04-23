"""
This is timer for the time measurement

call start() for the start of the measurement
call finish() to get the result
"""

import time

is_run = False

def start() -> None:
    """call for the start of the timer"""
    global start_time
    global is_run
    is_run = True
    start_time = time.time()

def finish() -> float:
    """call for the end of the timer"""
    global is_run
    if is_run:
        end_time = time.time()
        is_run = False
        return end_time - start_time
    
    return -1
