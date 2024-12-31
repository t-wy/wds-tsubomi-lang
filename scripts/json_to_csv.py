import csv, json
from os.path import dirname, abspath
path = dirname(abspath(__file__))
with open(path + "/../data.json") as jsonfile:
    json_content = jsonfile.read()
    entries = json.loads(json_content)
    for entry in entries:
        entry["hasruby"] = int(entry.get("hasruby", False))
    with open(path + "/../data.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=entries[0].keys(), delimiter=",", quotechar='"', lineterminator="\n")
        writer.writeheader()
        writer.writerows(entries)
    with open(path + "/../data.js", "w") as jsonfile:
        jsonfile.write(f"var tsubomi_data = {json_content};")