import sys
import base64

if len(sys.argv):
    print(f"Requires filepath. e.g. {sys.argv[0]} ./somefile.png")
    exit(1)

if not sys.argv[1].lower().endswith("png"):
    print(f"Only png is supported")
    exit(1)

with open(sys.argv[1], "rb") as f:
    content = f.read()
    print(f"data:image/jpeg;base64,{base64.b64encode(content)}")
