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

if myconfig.MINOR_KEYWORD_EXISTS:
	for Kmajor, Kminor, keyword_file in zip(myconfig.MAJOR_KEYWORD_PATH, myconfig.MINOR_KEYWORD_PATH, myconfig.CLASS_KEYWORD_PATH):
		class_name = Kmajor.split('/')[-1].split('_')[0]
		fields = list()
		major_keywords = list()
		myfields = list()
		myfinalRows = list()

		with open(Kmajor, 'r') as csvfile:
			csvreader = csv.reader(csvfile)
			fields = next(csvreader)
			for rows in csvreader:
				if len(rows) != 0:
					major_name = '-'.join([row for row in rows[0].split(' ')]).lower()
					# if myconfig.CLASSNAME_IN_KEYWORD:
					# 	if class_name in major_name.split('-'):
					# 		major_name = major_name.split('-')
					# 		major_name = major_name[:major_name.index(class_name)]
					# 		major_name = '-'.join([row for row in major_name])
					major_keywords.append(major_name)
		print('Total no. of keywords for "{}" class = {}'.format(class_name, str(csvreader.line_num-1)))
		# print(major_keywords)
		# sys.exit(0)

		with open(Kminor, 'r') as csvfile:
			csvreader = csv.reader(csvfile)
			fields = next(csvreader)
			for rows in csvreader:
				if (len(rows) != 0):
					minor_key = '-'.join([row for row in rows[0].split(' ')]).lower()
					for major_key in major_keywords:
						myfinalRows.append(['{}-{}'.format(major_key, minor_key)])

		print(myfinalRows)
		with open(keyword_file, 'w') as csvfile:
		    csvwriter = csv.writer(csvfile) 
		    csvwriter.writerow(['keywords']) 	# To name the columns
		    csvwriter.writerows(myfinalRows)
else:
	for Kmajor, keyword_file in zip(myconfig.MAJOR_KEYWORD_PATH, myconfig.CLASS_KEYWORD_PATH):
		class_name = Kmajor.split('/')[-1].split('_')[0]
		fields = list()
		major_keywords = list()
		myfields = list()
		myfinalRows = list()

		with open(Kmajor, 'r') as csvfile:
			csvreader = csv.reader(csvfile)
			fields = next(csvreader)
			for rows in csvreader:
				if len(rows) != 0:
					major_name = '-'.join([row for row in rows[0].split(' ')]).lower()
					myfinalRows.append([major_name])
		print('Total no. of keywords for "{}" class = {}'.format(class_name, str(csvreader.line_num-1)))
		print(myfinalRows)
		with open(keyword_file, 'w') as csvfile:
		    csvwriter = csv.writer(csvfile) 
		    csvwriter.writerow(['keywords']) 	# To name the columns
		    csvwriter.writerows(myfinalRows)

print('Successfully created keywords csv files for each classes!')