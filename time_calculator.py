def add_time(start, duration, day=0):

    # Start time variables
    start_time = start.split(':')

    start_hour = int(start_time[0])
    start_minute = int(start_time[1][0:2])
    # Convert start_hour to 24-hour format
    if start_time[1][-2:] == 'PM':
        start_hour += 12

    # Duration time variables
    duration_time = duration.split(':')

    duration_hour = int(duration_time[0])
    duration_minute = int(duration_time[1])

    # Sum the start and duration times
    total_hour = start_hour + duration_hour
    total_minute = start_minute + duration_minute

    # if total_minute >= 60, add 1 hour to total_hour and subtract 60 minutes to total_minute
    if total_minute >= 60:
        while total_minute >= 60:
            total_hour += 1
            total_minute -= 60

    # if total_hour >= 24, subtract 24 hours from total_hour and add +1 to daysPassed
    daysPassed = 0
    if total_hour >= 24:
        while total_hour >= 24:
            total_hour -= 24
            daysPassed += 1

    """ 
    If the result will be the next day, 
     it should show (next day) after the time.
    If the result will be more than one day later,
     it should show (n days later) after the time,
     where "n" is the number of days later.
     """
    if (daysPassed == 1):
        daysPassedTxt = " (next day)"
    elif (daysPassed > 1):
        daysPassedTxt = " ({0} days later)".format(daysPassed)
    else:
        daysPassedTxt = ""

    # Hour/Minute result variable
    result = ""

    # Convert total_hour to 12-hour format
    if total_hour > 12:
        total_hour -= 12
        result = str(total_hour) + ":" + str(total_minute).zfill(2) + " PM"
    elif total_hour == 12:
        result = str(total_hour) + ":" + str(total_minute).zfill(2) + " PM"
    elif total_hour == 0:
        total_hour = "12"
        result = str(total_hour) + ":" + str(total_minute).zfill(2) + " AM"
    else:
        result = str(total_hour) + ":" + str(total_minute).zfill(2) + " AM"

    # calculate the day of the week
    if (day != 0):

        # make day lower case and first letter uppercase
        day = day.lower().capitalize()

        daysOfWeek = ["Monday", "Tuesday", "Wednesday",
                      "Thursday", "Friday", "Saturday", "Sunday"]

        finalDay = daysOfWeek[(daysOfWeek.index(day) + daysPassed) % 7]

        result += ", " + finalDay

    # Add days pasted to result
    result += daysPassedTxt

    return result
