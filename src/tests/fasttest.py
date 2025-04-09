import re

item_lower  = 'сплит-система'
words_in_item = re.findall(r'\b[\w-]+\b', item_lower)
print(words_in_item)