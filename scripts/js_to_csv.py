import csv, json
from os.path import dirname, abspath
path = dirname(abspath(__file__))
with open(path + "/../data.js") as jsfile:
    js_content = jsfile.read()
    prefix, suffix = "var tsubomi_data = ", ";"
    assert js_content.startswith(prefix) and js_content.endswith(suffix), "Failed\nInvalid data.js content"
    json_content = js_content[len(prefix):-len(suffix)]
    entries = json.loads(json_content)
    for entry in entries:
        entry["hasruby"] = int(entry.get("hasruby", False))
    with open(path + "/../data.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=entries[0].keys(), delimiter=",", quotechar='"', lineterminator="\n")
        writer.writeheader()
        writer.writerows(entries)
    with open(path + "/../data.json", "w") as jsfile:
        jsfile.write(json_content)