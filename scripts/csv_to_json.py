import csv, json
from os.path import dirname, abspath
path = dirname(abspath(__file__))
with open(path + "/../data.csv") as csvfile:
    with open(path + "/../data.json", "w") as jsonfile:
        reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
        entries = list(reader)
        for entry in entries:
            entry["hasruby"] = entry.get("hasruby", "0") == "1"
        json.dump(entries, jsonfile, ensure_ascii=False, indent=4)