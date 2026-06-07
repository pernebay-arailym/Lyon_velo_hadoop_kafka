#!/usr/bin/env python
#!/usr/bin/env python

import sys
import json

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        obj = json.loads(line)

        # extract hour from timestamp
        hour = obj["last_update"] // 3600

        # emit: hour \t 1 (count station activity)
        print("{}\t{}".format(hour, 1))

    except Exception:
        # NEVER silently fail in real debugging
        continue