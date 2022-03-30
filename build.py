import sys
import base64
import json
import os

with open("./config.json", "r") as f:
    config = json.loads(f.read())

with open(config["template"], "r") as f:
    template = json.loads(f.read())

for card in config["cards"]:

    with open(card["image"], "rb") as f:
        content = f.read()
        image_url = f"data:image/png;base64,{base64.b64encode(content)}"

    template["body"][0]["items"][0]["columns"][0]["items"][0]["url"] = image_url

    with open(card["output"], "w") as f:
        f.write(json.dumps(template, indent=2))

