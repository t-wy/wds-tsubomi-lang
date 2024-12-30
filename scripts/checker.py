import csv, json
from os.path import dirname, abspath, isfile
from io import StringIO
path = dirname(abspath(__file__))
with open(path + "/../data.json") as jsonfile:
    json_content = jsonfile.read()
    entries = json.loads(json_content)
    for entry in entries:
        entry["hasruby"] = int(entry.get("hasruby", False))
    with StringIO(newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=entries[0].keys(), delimiter=",", quotechar='"', lineterminator="\n")
        writer.writeheader()
        writer.writerows(entries)
        csvfile.seek(0)
        csv_content_from_json = csvfile.read()
with open(path + "/../data.csv") as csvfile:
    csv_content = csvfile.read()
    csvfile.seek(0)
    with StringIO() as jsonfile:
        reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
        entries = list(reader)
        for entry in entries:
            entry["hasruby"] = entry.get("hasruby", "0") == "1"
        json.dump(entries, jsonfile, ensure_ascii=False, indent=4)
        jsonfile.seek(0)
        json_content_from_csv = jsonfile.read()

assert csv_content_from_json == csv_content, "Failed\nCSV content is different from one generated from JSON content"
assert json_content_from_csv == json_content, "Failed\nJSON content is different from one generated from CSV content"

imgpaths = []
for entry in entries:
    if entry.get("screenshot", "") != "":
        imgpaths.append(path + "/../img/" + entry["screenshot"])
    if entry.get("highlight", "") != "":
        imgpaths.append(path + "/../img/" + entry["highlight"])
non_existing_imgpaths = [imgpath for imgpath in imgpaths if not isfile(imgpath)]
if len(non_existing_imgpaths) > 0:
    for imgpath in non_existing_imgpaths:
        print(f"Failed\nHighlight file ({imgpath}) does not exist")
    assert False

print("Passed")