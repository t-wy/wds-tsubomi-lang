import json
from os.path import dirname, abspath
path = dirname(abspath(__file__))
with open(path + "/../data.json") as jsonfile:
    data = json.load(jsonfile)
containers = {}
for entry in data:
    if entry.get("phrase", "") == "":
        continue
    containers.setdefault(entry["phrase"], []).append(entry)

import random
cnt = 1
while True:
    print(f"第 {cnt} 問")
    phrase = random.choice(list(containers.keys()))
    question = random.choice(containers[phrase])
    print(f"問題：{question['phrase']}")
    answers = [
        answer
    for answer in [
        question.get("pronunciation", ""),
        question.get("english", ""),
        question.get("orilang", ""),
    ] if answer != ""]
    print(f"答え：{'；'.join(answers)}")
    cnt += 1
    input("== 続けるには Enter キーを押してください ==")