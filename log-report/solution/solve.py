import json
import re
from collections import Counter

log_path = "/app/access.log"
report_path = "/app/report.json"

paths = Counter()
ips = set()
total = 0

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += 1
        ips.add(line.split()[0])
        m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
        if m:
            paths[m.group(1)] += 1

top_path, top_path_count = paths.most_common(1)[0]

with open(report_path, "w", encoding="utf-8") as out:
    json.dump(
        {
            "total_requests": total,
            "unique_clients": len(ips),
            "top_path": top_path,
            "top_path_count": top_path_count,
        },
        out,
    )