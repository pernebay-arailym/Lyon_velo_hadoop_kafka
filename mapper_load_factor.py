import sys
import json

for line in sys.stdin:
    try:
        data = json.loads(line)

        station_id = data.get("number")
        timestamp = data.get("last_update")
        available_bikes = data.get("available_bikes")
        available_bike_stands = data.get("available_bike_stands")
        bike_stands = data.get("bike_stands")
        status = data.get("status")

        # Avoid division by zero
        total = available_bikes + available_bike_stands
        if total > 0:
            load_factor = available_bikes / total
        else:
            load_factor = 0

        # Validation
        if status == "OPEN" and 0 <= available_bikes <= bike_stands:
            status_valide = 1
        else:
            status_valide = 0

        print(f"{station_id}\t{timestamp}\t{load_factor:.3f}\t{status_valide}")

    except:
        continue