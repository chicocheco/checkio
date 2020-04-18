"""

-    First 100 (one hundred) minutes in one day are priced at 1 coin per minute;
-    After 100 minutes in one day, each minute costs 2 coins per minute;
-    All calls are rounded up to the nearest minute. For example 59 sec ≈ 1 min, 61 sec ≈ 2 min;
-    Calls count on the day when they began. For example if a call was started 2014-01-01 23:59:59, then it counted to 2014-01-01;

First day -- 181s≈4m -- 4 coins;
Second day -- 600s=10m -- 10 coins;
Third day -- 6009s≈101m + 200s≈4m -- 100 + 5 * 2 = 110 coins;
Total -- 124 coins.

"""
import math
from collections import defaultdict


def total_cost(calls):
    total = 0
    calls_dict = defaultdict(list)
    for call in calls:
        calls_dict[call[5:10]].append(math.ceil(int(call[20:]) / 60))
    for key, value in calls_dict.items():
        if sum(value) > 100:
            total += 100 + (sum(value) - 100) * 2
        else:
            total += sum(value)
    return total


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"

    assert total_cost(
        ["2051-09-09 12:00:00 7200", "2051-09-10 12:00:00 7200", "2051-09-12 12:00:00 7200", "2051-09-14 12:00:00 7200",
         "2051-09-15 12:00:00 7200", "2051-09-18 12:00:00 7200", "2051-09-23 12:00:00 7200", "2051-09-25 12:00:00 7200",
         "2051-09-28 12:00:00 7200", "2051-10-01 12:00:00 7200", "2051-10-02 12:00:00 7200", "2051-10-04 12:00:00 7200",
         "2051-10-05 12:00:00 7200", "2051-10-06 12:00:00 7200", "2051-10-07 12:00:00 7200", "2051-10-08 12:00:00 7200",
         "2051-10-09 12:00:00 7200", "2051-10-10 12:00:00 7200", "2051-10-11 12:00:00 7200", "2051-10-12 12:00:00 7200",
         "2051-10-13 12:00:00 7200", "2051-10-14 12:00:00 7200", "2051-10-15 12:00:00 7200", "2051-10-16 12:00:00 7200",
         "2051-10-17 12:00:00 7200", "2051-10-18 12:00:00 7200", "2051-10-19 12:00:00 7200", "2051-10-20 12:00:00 7200",
         "2051-10-21 12:00:00 7200", "2051-10-22 12:00:00 7200"]) == 4200
