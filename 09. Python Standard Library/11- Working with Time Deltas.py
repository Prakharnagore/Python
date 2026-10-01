from datetime import datetime, timedelta

dt1 = datetime(2026, 1, 1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)  # 328 days, 10:00:00
print(duration.days)
print(duration.seconds)
print(duration.total_seconds())

d3 = datetime("2026-01-01") + timedelta(1)  # timedelta(days=1, seconds=1000)
d4 = d3 + timedelta(days=1, seconds=1000)
print(d3)  # 2026-01-02 00:00:00
print(d4)  # 2026-01-03 00:00:00
d4 = d3 - dt1
print(d4)  # 329 days, 10:00:00
