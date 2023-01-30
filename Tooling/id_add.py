import csv

with open('/home/fallenour/Projects/Django/test/path/to/file/<csv-file-name-here>.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
            print(row[0])
            row[]
            line_count+=1