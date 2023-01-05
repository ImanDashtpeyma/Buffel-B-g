
from datetime import datetime
# Check If Employee Is Free Or Not
# ─── Function Argument ──────────────────────────────────────────────────────────
# meeting_date =  DateTime Object
# date_starting = DateTime Object
# date_ending =  DateTime Object
#Format : '%Y-%m-%d %I:%M:%S'
# Example : 2015-01-01 07:00:00
# ─── Return Output ──────────────────────────────────────────────────────────────
# True = is busy
# False = is free


def is_busy(meeting_date, date_starting, date_ending):
    a = date_starting
    b = meeting_date
    c = date_ending
    d = date_starting

    delta1 = b - a
    delta2 = c - b
    delta3 = d - a
    if delta1 >= delta3 and delta2 >= delta3:
        return True
    else:
        return False
