import sys
import json

for line in sys.stdin:
    print("RAW:", line)  # debug
    try:
        data = json.loads(line)
        print("PARSED:", data)
    except Exception as e:
        print("ERROR:", e)
