import hashlib
import re

regex = re.compile("^000000.*")

found = False
i = 1
while not found:
    hashe = hashlib.md5("ckczppom{}".format(i).encode("utf-8")).hexdigest()
    if regex.match(hashe):
        print(hashe)
        print(i)
        found = True
    i += 1