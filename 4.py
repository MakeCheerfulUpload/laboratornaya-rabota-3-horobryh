import re

s = 'baab        bffba a a  a      a'
words = re.sub('\bb\w*b\b', '', s)
print(words)
