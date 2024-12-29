import csv, json
from os.path import dirname, abspath, isfile
from io import StringIO
path = dirname(abspath(__file__))
with open(path + "/../data.json") as jsonfile:
    json_content = jsonfile.read()
    data = json.loads(json_content)
    with StringIO(newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys(), delimiter=",", quotechar='"', lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)
        csvfile.seek(0)
        csv_content_from_json = csvfile.read()
with open(path + "/../data.csv") as csvfile:
    csv_content = csvfile.read()
    csvfile.seek(0)
    with StringIO() as jsonfile:
        reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
        json.dump(list(reader), jsonfile, ensure_ascii=False, indent=4)
        jsonfile.seek(0)
        json_content_from_csv = jsonfile.read()

assert csv_content_from_json == csv_content, "Failed\nCSV content is different from one generated from JSON content"
assert json_content_from_csv == json_content, "Failed\nJSON content is different from one generated from CSV content"

for entry in data:
    if entry.get("screenshot", "") != "":
        assert isfile(path + "/../img/" + entry["screenshot"]), "Failed\nScreenshot file does not exist"
    if entry.get("highlight", "") != "":
        assert isfile(path + "/../img/" + entry["highlight"]), "Failed\nHighlight file does not exist"

print("Passed")