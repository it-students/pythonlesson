import re

zen = """Although never is
often better  than
*right* now.
If the implementation
is hard to explain,
it may be a good
idea. Namespaces
are one honlimg
great idea -- let's
do more of those!"""

m = re.findall("^If", zen,re.MULTILINE)
print(m)