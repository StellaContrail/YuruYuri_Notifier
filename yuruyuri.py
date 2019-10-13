import urllib.request
import json
import datetime

title = "ゆるゆり"
count = 0

year = datetime.date.today().year

for i in range(1, 5):
    url = "http://api.moemoe.tokyo/anime/v1/master/" + str(year) + "/" + str(i)
    try:
        with urllib.request.urlopen(url) as res:
            html = res.read().decode("utf-8")
            if html != "":
                items = json.loads(html)
    except urllib.error.URLError as e:
        if (e.reason == "Not Found"):
            exit
        else:
            print("Unexpected Error :", e.reason)

for item in items:
    if title in item["title"]:
        count = count + 1

if count > 0:
    print("見つかりました")
else:
    print("見つかりませんでした...")