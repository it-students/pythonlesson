from itertools import count
import sys

for c in count(1):
    if c > 11:
        sys.exit()
    print(c)
