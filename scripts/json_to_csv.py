import csv, json
from os.path import dirname, abspath
path = dirname(abspath(__file__))
with open(path + "/../data.json") as jsonfile:
    content = json.load(jsonfile)
    with open(path + "/../data.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=content[0].keys(), delimiter=",", quotechar='"', lineterminator="\n")
        writer.writeheader()
        writer.writerows(content)