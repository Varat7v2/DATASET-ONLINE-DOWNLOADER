import glob
import os, sys
import pandas as pd
from sklearn.utils import shuffle
import argparse
import csv
import cv2

import downloader_config as myconfig

from tqdm import tqdm

def main():
	### Downloading images from Google / Baidu / Bing
	# Under class-name-list try putting DISPARATE AND VARYING TOPIC/TITLE OF CLASS-IMAGES for googling/Binging/Baiduing

	data_version = myconfig.DATASET_VERSION
	max_number = myconfig.MAX_NUMBER

	class1 = list()
	class2 = list()
	class_dict = dict()

	for filename in myconfig.CLASS_KEYWORD_PATH:
		mykeywords = list()
		class_name = filename.split('/')[-1].split('_')[0]
		with open(filename, 'r') as csvfile:
			csvreader = csv.reader(csvfile)
			fields = next(csvreader)
			for row in csvreader:
				mykeywords.append(row[0])
		class_dict[class_name] = mykeywords
	
	# print(class_dict)
	# sys.exit(0)

	print('Downloading Images for classes')
	for key, value in class_dict.items():
		for keyword in value:
			for search in myconfig.SEARCH_ENGINES:
				os.system('python image_downloader.py {} --engine {} --max-number {} --output "data/{}/{}/{}"'
					.format(keyword, search, myconfig.MAX_NUMBER, data_version, key, keyword))

	print("Creating CSV file of imagepaths ... ")
	root, dirs, files = next(os.walk('data/{}'.format(myconfig.DATASET_VERSION)))
	mylist = list()

	for d in dirs:
		subdir = next(os.walk(os.path.join(root,d)))[1]
		for s in subdir:
			for file in glob.glob(os.path.join(root, d, s) + '/*'):
				print(file)
				mylist.append(file)

	# converting to dataframe shuffling
	df = shuffle(pd.DataFrame(mylist, columns=['filename']))
	df.reset_index(inplace=True, drop=True)

	# save to csv file
	df.to_csv('data/{}.csv'.format(myconfig.PROJECT_NAME), index=False)

if __name__ == '__main__':
	main()