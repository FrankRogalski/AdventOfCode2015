import hashlib
import re

regex = re.compile("^00000.*")

found = False
i = 1
while not found:
    hashe = hashlib.md5("ckczppom{}".format(i).encode("utf-8")).hexdigest()
    if regex.match(hashe):
        print(i)
        found = True
    i += 1