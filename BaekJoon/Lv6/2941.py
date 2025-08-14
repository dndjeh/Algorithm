import re

text = input()

regex = r'dz=|c=|c-|d-|lj|nj|s=|z='

find_list = re.findall(regex,text)

string =''

for i in find_list:
    string += i

sum = len(re.findall(regex,text)) + (len(text)- len(string))
print(sum)