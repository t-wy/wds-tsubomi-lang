import csv, json
from os.path import dirname, abspath
path = dirname(abspath(__file__))
with open(path + "/../data.csv") as csvfile:
    with open(path + "/../data.json", "w") as jsonfile:
        reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
        json.dump(list(reader), jsonfile, ensure_ascii=False, indent=4)