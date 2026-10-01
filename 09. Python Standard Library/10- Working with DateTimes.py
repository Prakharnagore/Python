# import datetime
from datetime import datetime
import time

dt = datetime(2026, 9, 26, 10, 0, 0)
print(dt)  # 2026-09-26 10:00:00

dt = datetime.now()
print(dt)  # 2026-09-26 10:00:00

dt = datetime.strptime("2026/09/26", "%Y/%m/%d")
print(dt)  # 2026-09-26 00:00:00

dt = datetime.fromtimestamp(time.time())
print(dt)  # 2026-09-26 10:00:00

print(f"{dt.year}/{dt.month}/{dt.day}")  # 2026/9/26
dt = dt.strftime("%Y/%m/%d")
print(dt)  # 2026/09/26


dt1 = datetime(2026, 1, 1)
dt2 = datetime.now()
print(dt2 > dt1)  # True
print(dt2 < dt1)  # False
print(dt2 == dt1)  # False
print(dt2 != dt1)  # True
