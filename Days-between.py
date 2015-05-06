from datetime import datetime
​
def days_diff(date1, date2):
    return abs((datetime(*date1)-datetime(*date2)).days)
