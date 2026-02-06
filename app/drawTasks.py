from drawBaseImg import makeBaseCalender
from drawMonthly import draw_calender
import os


def makeBase():
    try:
        draw_calender(2026, 2)
    except FileNotFoundError:
        makeBaseCalender()
        draw_calender(2026, 2)
