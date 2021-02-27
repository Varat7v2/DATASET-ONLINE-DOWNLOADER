import csv
from tqdm import tqdm
import os, sys

import dataset_downloader_config as myconfig

# CREATING NECESSARY FOLDERS
if not os.path.exists('data'):
    os.makedirs('data')

if not os.path.exists('data/{}'.format(myconfig.DATASET_VERSION)):
    os.makedirs('data/{}'.format(myconfig.DATASET_VERSION))

# if not os.path.exists(os.path.join('keywords', myconfig.PROJECT_NAME)):
#     os.makedirs(os.path.join('keywords', myconfig.PROJECT_NAME))

file1_major = '{}'.format(myconfig.MAJOR_KEYWORD_CLASS1)
file2_major = '{}'.format(myconfig.MAJOR_KEYWORD_CLASS2)

file1_minor = open('{}'.format(myconfig.MINOR_KEYWORD_CLASS1), 'r')
file2_minor = open('{}'.format(myconfig.MINOR_KEYWORD_CLASS2), 'r')
temp_class1 = [keyword.strip('\n') for keyword in file1_minor.readlines()]
temp_class2 = [keyword.strip('\n') for keyword in file2_minor.readlines()]
file1_minor.close()
file2_minor.close()

for fmajor, temp_classes, class_name  in zip([file1_major, file2_major], 
											 [temp_class1, temp_class2], 
											 [myconfig.CLASS1_NAME, myconfig.CLASS2_NAME]):

	class_name = fmajor.split('/')[-1].split('-')[0]
	fields = list()
	major_filenames = list()
	myfields = list()
	myfinalRows = list()

	with open(fmajor, 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		fields = next(csvreader)
		for rows in csvreader:
			if len(rows) != 0:
				major_name = '-'.join([row for row in rows[0].split(' ')]).lower()
				if myconfig.CLASSNAME_IN_KEYWORD:
					if class_name in major_name.split('-'):
						major_name = major_name.split('-')
						major_name = major_name[:major_name.index(class_name)]
						major_name = '-'.join([row for row in major_name])
				major_filenames.append(major_name)
		print('Total no. of major_filenames for {} class = {}'.format(class_name, str(csvreader.line_num)))

	if myconfig.MINOR_KEYWORD_EXISTS:
		for temp_class in temp_classes:
			# print(temp_class)
			keyword_file = 'keywords/{}/keywords_class_{}.csv'.format(myconfig.PROJECT_NAME, class_name)
			for row in major_filenames:
				myfinalRows.append(['{}-{}'.format(row, temp_class)])
		# print(myfinalRows)
	else:
		keyword_file = 'keywords/{}/keywords_class_{}.csv'.format(myconfig.PROJECT_NAME, class_name)
		for row in major_filenames:
			myfinalRows.append([row])

	with open(keyword_file, 'w') as csvfile:
	    csvwriter = csv.writer(csvfile) 
	    # csvwriter.writerow(myfields) 	# To name the columns
	    csvwriter.writerows(myfinalRows)

print('Successfully created keywords csv files for each classes!')