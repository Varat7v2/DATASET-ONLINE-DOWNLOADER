import os, sys

CLASSNAME_IN_KEYWORD = False
MINOR_KEYWORD_EXISTS = True

### FOR NEW PROJECT CREATE NEW DIRECOTORY TO STORE IMAGES
myPROJECT = 'emotion'
PROJECT_NAME = '{}_detection'.format(myPROJECT)

NUMBER_OF_CLASSES = 1
# Name classes to classify
CLASS_1 = 'emotion'
# CLASS_2 = 'female'
# CLASS3_NAME = 'sadness'
# CLASS4_NAME = 'surprise'
# CLASS5_NAME = 'anger'
# CLASS6_NAME = 'fear'

CLASSES = list()
MAJOR_KEYWORD_CLASSES = list()
MINOR_KEYWORD_CLASSES = list()
KEYWORDS_CLASSES = list()
for num in range(NUMBER_OF_CLASSES):
	CLASSES.append('CLASS_{}'.format(num+1))
	MAJOR_KEYWORD_CLASSES.append('MAJOR_KEYWORD_CLASS{}'.format(num+1))
	MINOR_KEYWORD_CLASSES.append('MINOR_KEYWORD_CLASS{}'.format(num+1))
	KEYWORDS_CLASSES.append('KEYWORDS_CLASS{}'.format(num+1))

MAJOR_KEYWORD_PATH = list()
MINOR_KEYWORD_PATH = list()
CLASS_KEYWORD_PATH = list()
for major_key, minor_key, class_key, iclass in zip(MAJOR_KEYWORD_CLASSES, MINOR_KEYWORD_CLASSES, KEYWORDS_CLASSES, CLASSES):
	major_key = 'keywords/{}/{}_major_keywords.txt'.format(PROJECT_NAME, eval(iclass))
	minor_key = 'keywords/{}/{}_minor_keywords.txt'.format(PROJECT_NAME, eval(iclass))
	class_key = 'keywords/{}/{}_keywords.csv'.format(PROJECT_NAME, eval(iclass))

	MAJOR_KEYWORD_PATH.append(major_key)
	MINOR_KEYWORD_PATH.append(minor_key)
	CLASS_KEYWORD_PATH.append(class_key)

# print(MAJOR_KEYWORD_PATH)
# print(MINOR_KEYWORD_PATH)
# print(CLASS_KEYWORD_PATH)

DATASET_VERSION = '{}_dataset'.format(myPROJECT)

# Maximum no. of images to download
MAX_NUMBER = 2000
SEARCH_ENGINES = {"Google", "Bing"}
BROWSER_DRIVER = "chromedriver_85"