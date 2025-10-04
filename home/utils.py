# home/utils.py

from datetime import datetime, time

def is_restaurant_open():
    """
    Returns True if the restaurant is currently open,
    False otherwise.
    """

    # Get current day and time
    now = datetime.now()
    current_time = now.time()
    current_day = now.strftime('%A')  # e.g., 'Monday', 'Saturday'

    # Example hours (you can customize these)
    opening_hours = {
        'Monday': (time(9, 0), time(22, 0)),      # 9:00 AM - 10:00 PM
        'Tuesday': (time(9, 0), time(22, 0)),
        'Wednesday': (time(9, 0), time(22, 0)),
        'Thursday': (time(9, 0), time(22, 0)),
        'Friday': (time(9, 0), time(23, 0)),      # open late on Fridays
        'Saturday': (time(10, 0), time(23, 0)),   # 10:00 AM - 11:00 PM
        'Sunday': (time(10, 0), time(21, 0)),     # 10:00 AM - 9:00 PM
    }

    # Get today's opening hours
    if current_day not in opening_hours:
        return False  # closed if day not defined

    open_time, close_time = opening_hours[current_day]

    # Check if current time is within range
    is_open = open_time <= current_time <= close_time
    return is_restaurant_open