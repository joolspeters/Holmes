
import csv

# keywords = ['MSE', 'lars', 'earth', 'jamie', 'geotech' 'embankment']
keywords = ['MSE', 'embankment']

output = []

### open CSV and extract non empty cells to list:
with open('Copy of Highgate-Job Cost Analysis JTD.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        for j, cell in enumerate(row):
            if cell:
                output += [cell]

phase = ""
captured = []

### iterate through list and extract relevant entries
for i, line in enumerate(output):
    if "Phase Number" in line:
        phase = line.split(": ")[1]
    # if phase == "041 Bridge Structural Developed Design" or phase == "051 Bridge Structural Detailed Design":
    if any(key in line for key in keywords):
        captured += [[output[i-3], output[i-2], output[i-1], output[i]]]

### output relevant entries to CSV            
# print(captured)
with open('out.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    for item in captured:
        writer.writerow(item)
