from datetime import timedelta, datetime
import time

today = datetime.today()


# 1)Substract days
def getDaysAgo(days: int) -> None:
    daysAgo = today - timedelta(days=days)

    print(daysAgo)


getDaysAgo(5)


# 2)Yesterday, today, tomorrow
def getThreeDaysAround() -> None:
    yesterday, tomorrow = today - timedelta(days=1), today + timedelta(days=1)

    print(f"Yesterday: {yesterday}\nToday:{today}\nTomorrow:{tomorrow}")


getThreeDaysAround()


# 3)Drop microseconds
def dropMicroseconds(dt) -> None:
    print(dt.replace(microsecond=0))


dropMicroseconds(today)


# 4)Calc difference in seconds
def getDiffInSeconds(first: datetime, second: datetime) -> None:
    firstSeconds = time.mktime(first.timetuple())
    secondSeconds = time.mktime(second.timetuple())
    print(secondSeconds - firstSeconds)


getDiffInSeconds(today, today + timedelta(days=2))
