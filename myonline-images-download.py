import glob
import os, sys
import pandas as pd
from sklearn.utils import shuffle
import argparse
import csv

from tqdm import tqdm

def main(argv):
	parser = argparse.ArgumentParser(description="myOnline Image Downloader")
	parser.add_argument("--max-number", "-n", type=int, default=100,
	                    help="Max number of images download for the keywords.")
	args = parser.parse_args(args=argv)

	### Downloading images from Google / Baidu / Bing
	# Under class-name-list try putting DISPARATE AND VARYING TOPIC/TITLE OF CLASS-IMAGES for googling/Binging/Baiduing
	keywords_class1 = 'keywords_class1.csv'
	keywords_class2 = 'keywords_class2.csv'

	data_version = 'data_v2'

	males = list()
	females = list()

	for iclass, filename in zip([males, females], [keywords_class1, keywords_class2]):
		with open(filename, 'r') as csvfile:
			csvreader = csv.reader(csvfile)
			fields = next(csvreader)
			for rows in csvreader:
				for row in rows:
					iclass.append(row)
					
	print('Class1 keywords length: ', len(males))
	print('Class2 keywords length: ', len(females))

	class_dict = {'male':males, 'female':females}
	engine = {"Google", "Bing"}

	print('Downloading Images for class=fire')
	for key,value in class_dict.items():
		for keyword in value:
			for search in engine:
				os.system('python image_downloader.py {} --engine {} --max-number {} --output "data/{}/{}/{}"'
					.format(keyword, search, args.max_number, data_version, key, keyword))

	print("Creating CSV file of imagepaths ... ")
	### For creating csv file for all the imagepaths
	main_path = 'data'

	root, dirs, files = next(os.walk(main_path))
	mylist = list()

	for d in dirs:
		subdir = next(os.walk(os.path.join(root,d)))[1]
		for s in subdir:
			for file in glob.glob(os.path.join(root, d, s) + '/*'):
				mylist.append(file)

	# converting to dataframe shuffling
	df = shuffle(pd.DataFrame(mylist, columns=['filename']))
	df.reset_index(inplace=True, drop=True)

	# save to csv file
	df.to_csv('data/gender_detection.csv', index=False)

if __name__ == '__main__':
	main(sys.argv[1:])