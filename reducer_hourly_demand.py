import sys

current_hour = None
current_sum = 0

for line in sys.stdin:
    hour, count = line.strip().split("\t")
    count = int(count)

    if current_hour == hour:
        current_sum += count
    else:
        if current_hour is not None:
            print("{}\t{}".format(current_hour, current_sum))
        current_hour = hour
        current_sum = count

# last record
if current_hour is not None:
    print("{}\t{}".format(current_hour, current_sum))