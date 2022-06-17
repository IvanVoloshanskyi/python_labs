import re
from datetime import datetime

date_format = '%d/%b/%Y:%H:%M:%S'
date_start = datetime.strptime('08/Mar/2004:07:11:37', date_format)
date_end = datetime.strptime('10/Mar/2004:11:41:52', date_format)
file1 = open("access_log", 'r')
lines = file1.readlines()
pattern = r'(\S+)\s+[-]+\s+[-]+\s+[\[](\S+)\s(\S+)]\s["](\S+)\s(\S+)\s+(\S+)["]\s([2]\d+)\s(\d+)'
unique_set = set()

for line in lines:
    x = re.match(pattern, line)
    if x:
        if date_start < datetime.strptime(x.groups()[1], '%d/%b/%Y:%H:%M:%S') < date_end:
            unique_set.add(x)
        elif datetime.strptime(x.groups()[1], '%d/%b/%Y:%H:%M:%S') > date_end:
            break
for i in unique_set:
    print(i.group(1) + " " + i.group(5) + " " * 5 + "Status ->" + " " + i.group(7))

