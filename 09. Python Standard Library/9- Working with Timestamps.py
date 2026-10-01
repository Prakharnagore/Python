import time

# 1727308800.0 - return unix timestamp since 1970-01-01 00:00:00
print(time.time())


def send_emails():
    for i in range(1000000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)
