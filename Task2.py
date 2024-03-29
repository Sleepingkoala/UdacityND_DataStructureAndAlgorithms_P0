"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
records = {}
for call in calls:
    if call[0] in records:
        records[call[0]]+= int(call[3])
    else:
        records[call[0]] = int(call[3])
        
    if call[1] in records:
        records[call[1]]+= int(call[3])
    else:
        records[call[1]] = int(call[3]) # no int() will leads to failure
        
[max_time,max_time_telephone] = max(zip(records.values(),records.keys())) 
print(max_time_telephone,"spent the longest time,",max_time,"seconds, on the phone during September 2016.")

