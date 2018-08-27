import re
string = open('concepts+soundex.txt').read()
new_str = re.sub('[a-z]', ' ', string)
open('b1.txt', 'w').write(new_str)
