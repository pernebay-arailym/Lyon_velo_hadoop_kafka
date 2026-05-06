import sys
from collections import defaultdict
import statistics

data_by_station = defaultdict(list)

for line in sys.stdin:
    try:
        station_id, timestamp, load_factor, status_valide = line.strip().split("\t")

        load_factor = float(load_factor)
        status_valide = int(status_valide)

        data_by_station[station_id].append((load_factor, status_valide))

    except:
        continue


for station_id, values in data_by_station.items():
    total_samples = len(values)

    valid_values = [v[0] for v in values if v[1] == 1]
    nb_valid = len(valid_values)

    if nb_valid > 0:
        avg_load = sum(valid_values) / nb_valid
        std_load = statistics.pstdev(valid_values) if nb_valid > 1 else 0
    else:
        avg_load = 0
        std_load = 0

    print(f"{station_id}\t{avg_load:.3f}\t{std_load:.3f}\t{nb_valid}/{total_samples}")