import csv
from tqdm import tqdm
import os, sys

filename = 'nationality_list.csv'

fields = list()
rows = list()

file1 = open('male-keywords.txt', 'r')
file2 = open('female-keywords.txt', 'r')
temp_class1 = [keyword.strip('\n') for keyword in file1.readlines()]
temp_class2 = [keyword.strip('\n') for keyword in file2.readlines()]
file1.close()
file2.close()

with open(filename, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	fields = next(csvreader)
	for row in csvreader:
		rows.append(row)

	print('Total no. of rows: %d' %(csvreader.line_num))

# # printing field names
# print('Field names are: ' + ','.join(field for field in fields))
# print(rows[:5])

for class_num, temp_class in tqdm(enumerate([temp_class1, temp_class2])):
	myfields = list()
	myfinalRows = list()
	keyword_file = 'keywords_class{}.csv'.format(class_num+1)

	for row in rows:
		myrows = list()
		for subclass in temp_class:
			myrows.append('{}-{}'.format(row[0], subclass))
		myfinalRows.append(myrows)

	with open(keyword_file, 'w') as csvfile: 
	    csvwriter = csv.writer(csvfile) 
	    # csvwriter.writerow(myfields)
	    csvwriter.writerows(myfinalRows)