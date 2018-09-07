"""
The sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its
 zenith, which means that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180 degrees.

6:00 - 0
12:00 - 90
18:00 - 180

12 hours / 180 degrees = 0.066666667
180/12=15
that means that in one hour the angle changes by 15 degrees
15/60=0.25
that means that every minute it changes by 0.25 degrees
12 hours is 12*60= 720 minutes
720*0.25=180

done in 40 minutes
"""


def sun_angle(time):
    amount_hours = int(time[0:2])
    hours_in_minutes = amount_hours * 60
    minutes_left = int(time[3:5])
    total_minutes = hours_in_minutes + minutes_left

    if 360 <= total_minutes <= 1080:
        minutes_in_sun = total_minutes - 360
        angle = round(minutes_in_sun * 0.25, 2)
        return angle
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    # print("Example:")
    # print(sun_angle("07:00"))
    # print(sun_angle("01:23"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
