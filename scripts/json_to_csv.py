import csv, json
from os.path import dirname, abspath
path = dirname(abspath(__file__))
with open(path + "/../data.json") as jsonfile:
    entries = json.load(jsonfile)
    for entry in entries:
        entry["hasruby"] = int(entry.get("hasruby", False))
    with open(path + "/../data.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=entries[0].keys(), delimiter=",", quotechar='"', lineterminator="\n")
        writer.writeheader()
        writer.writerows(entries)