import csv, json
from io import StringIO
from os.path import dirname, abspath
path = dirname(abspath(__file__))
with open(path + "/../data.csv") as csvfile:
    with StringIO() as jsonfile:
        reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
        entries = list(reader)
        for entry in entries:
            entry["hasruby"] = entry.get("hasruby", "0") == "1"
        json.dump(entries, jsonfile, ensure_ascii=False, indent=4)
        jsonfile.seek(0)
        json_content_from_csv = jsonfile.read()
    with open(path + "/../data.json", "w") as jsonfile:
        jsonfile.write(json_content_from_csv)
    with open(path + "/../data.js", "w") as jsonfile:
        jsonfile.write(f"var tsubomi_data = {json_content_from_csv};")